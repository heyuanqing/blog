# 丢包的可能情况

* 发送的频率过快
* 接受端不能及时处理导致接收端缓存区满而出现丢包现象
* 发送的数据包过大
* 局域网内不丢包，公网上丢包。这个问题我也是通过切割小包并sleep发送解决的。如果流量太大，这个办法也不灵了。
## 具体问题具体分析
1. 发送的频率过快
   很多人会不理解发送速度过快为什么会产生丢包，原因就是UDP的SendTo不会造成线程阻塞，也就是说，UDP的SentTo不会像TCP中的SendTo那样，直到数据完全发送才会return回调用函数，它不保证当执行下一条语句时数据是否被发送。（SendTo方法是异步的）这样，如果要发送的数据过多或者过大，那么在缓冲区满的那个瞬间要发送的报文就很有可能被丢失。至于对“过快”的解释，作者这样说：“A few packets a second are not an issue; hundreds or thousands may be an issue.”（一秒钟几个数据包不算什么，但是一秒钟成百上千的数据包就不好办了）。可以通过平滑发送端的发送速度来解决这个问题
   
2. 接受端不能及时处理导致接收端缓存区满而出现丢包现象
   
   首先要保证程序执行后马上开始监听（如果数据包不确定什么时候发过来的话），其次，要在收到一个数据包后最短的时间内重新回到监听状态，其间要尽量避免复杂的操作（比较好的解决办法是使用多线程回调机制）。
   
3. 发送的数据包过大

   至于报文过大的问题，可以通过控制报文大小来解决，使得每个报文的长度小于MTU。以太网的MTU通常是1500 bytes，其他一些诸如拨号连接的网络MTU值为1280 bytes，如果使用speaking这样很难得到MTU的网络，那么最好将报文长度控制在1280 bytes以下。

4. 发送方丢包

   发送方丢包：内部缓冲区（internal buffers）已满，并且发送速度过快（即发送两个报文之间的间隔过短）；  接收方丢包：Socket未开始监听；  虽然UDP的报文长度最大可以达到64 kb，但是当报文过大时，稳定性会大大减弱。这是因为当报文过大时会被分割，使得每个分割块（翻译可能有误差，原文是fragmentation）的长度小于MTU，然后分别发送，并在接收方重新组合（reassemble），但是如果其中一个报文丢失，那么其他已收到的报文都无法返回给程序，也就无法得到完整的数据了。

## 解决思路
1. 从发送端解决(推荐)

  适用条件: ①发送端是可以控制的.②微秒数量级的延迟可以接受.

  解决方法:发送时使用usleep(1)延迟1微秒发送,即发送频率不要过快,延迟1微妙发送,可以很好的解决这个问题.

2. 从接收端解决方法一
    适用条件:①无法控制发送端发送数据的频率
    解决方法: 用recvfrom函数收到数据之后尽快返回,进行下一次recvfrom,可以通过多线程+队列来解决.收到数据之后将数据放入队列中,另起一个线程去处理收到的数据.

3. 从接收端解决方法二

    适用条件:①使用方法2依然出现大规模丢包的情况,需要进一步优化

    解决方法:使用setsockopt修改接收端的缓冲区大小,

  ```
int rcv_size = 1024*1024; //1M
int optlen=sizeof(rcv_size);
int err=setsockopt(sock,SOL_SOCKET,SO_RCVBUF,(char *)&rcv_size,optlen);//设置好缓冲区大小
  ```
  设置完毕可以通过来查看当前sock的缓冲区大小
`setsockopt(sock,SOL_SOCKET,SO_RCVBUF,(char *)&rcv_size,(socklen_t *)&optlen);`

  但是,会发现查到的大小并不是1M而是256kb,后来发现原来是linux系统默认缓冲区大小为128kb,设置最大是这个的2倍

  所以需要通过修改系统默认缓冲区大小来解决

  使用root账户在命令行下输入: 
```
vi /etc/sysctl.conf
添加一行记录(1049576=1024*1024=1M)
net.core.rmem_max=1048576
保存之后输入
/sbin/sysctl -p
```
  使修改的配置生效

  此时可以通过 来看配置是否生效.
  `sysctl -a|grep rmem_max`
  生效之后可以再次运行程序来getsockopt看缓冲区是否变大了,是否还会出现丢包现象了

   ## 排查思路

1. 查看udp丢包，cat /proc/net/snmp | grep Udp（比netstat –su效果好）

2. 查看网卡丢包(ifconfig 或者ethtool –S eth1)

3. Netstat –alupt 查看队列里现存的包数，如果过多说明有问题。

4. 查看socket队列长度，cat /proc/sys/net/core/rmem_default (wmem_default是写队列长度)

5. 查看网卡队列长度， ethtool -g eth1 

6. 查看cpu负载情况，top，vmstat 1（或者mpstat –P ALL 1）

7. 如果是arp缓存导致的丢包，查看arp缓存队列长度，/proc/sys/net/ipv4/neigh/eth1/unres_qlen

8. sysctl命令使用

9. 看换从区大小

  ```shell
  1. TCP收发缓冲区默认值 
  [root@qljt core]# cat /proc/sys/net/ipv4/tcp_rmem 
  4096 87380 4161536（TCP接收缓冲区min，default，max）
  cat /proc/sys/net/ipv4/tcp_wmem
  4096 16384 4161536（TCP发送缓冲区min，default，max）
  2. UDP收发缓冲区默认值
  [root@qljt core]# cat /proc/sys/net/core/rmem_default
  1048576（UDP接收缓冲区的默认值1M）
  [root@qljt core]# cat /proc/sys/net/core/wmem_default
  1048576（UDP发送缓冲区的默认值1M）
  3. TCP或UDP收发缓冲区最大值
  [root@qljt core]# cat /proc/sys/net/core/rmem_max 
  8388608（TCP或UDP接收缓冲区的最大值8M）
  [root@qljt core]# cat /proc/sys/net/core/wmem_max
  8388608（TCP或UDP发送缓冲区的最大值8M）
  可以通过setsockopt()和getsockopt()函数设置和获取相应缓冲区的大小
  ```

### 修改和获取网卡队列大小的方式
```c++
struct ifreq ifr;
memset(&ifr, 0, sizeof(ifr));
strncpy(ifr.ifr_name, "eth0", sizeof(ifr.ifr_name));
ifr.ifr_qlen = 10000;
if (-1 == ioctl(sock_, SIOCSIFTXQLEN, &ifr))
  PLOG(ERROR) << "failed to set dev eth0 queue length";
if (-1 == ioctl(sock_, SIOCGIFTXQLEN, &ifr))
  PLOG(ERROR) << "failed to get dev eth0 queue length";
LOG(KEY) << "Dev eth0 queue length " << ifr.ifr_qlen;


struct ifreq ifr;

memset(&ifr, 0, sizeof(ifr));
strncpy(ifr.ifr_name, "eth0", sizeof(ifr.ifr_name));

if (-1 == ioctl(sock_, SIOCGIFTXQLEN, &ifr))
    PLOG(ERROR) << "failed to get dev eth0 queue length";
LOG(KEY) << "Dev eth0 queue length " << ifr.ifr_qlen;
```

### udp最大MTU分析

UDP允许传输的最大长度理论上2^16 - udp head - iphead（ 65507 字节 = 65535 - 20 - 8）

但是实际上UDP数据报的数据区最大长度为1472字节。分析如下：

首先,我们知道,TCP/IP通常被认为是一个四层协议系统,包括链路层,网络层,运输层,应用层. 

UDP属于运输层,下面我们由下至上一步一步来看:    
以太网(Ethernet)数据帧的长度必须在46-1500字节之间,这是由以太网的物理特性决定的。这个1500字节被称为链路层的MTU(最大传输单元)。
但这并不是指链路层的长度被限制在1500字节,其实这这个MTU指的是链路层的数据区。 并不包括链路层的首部和尾部的18个字节。 所以,事实上,这个1500字节就是网络层IP数据报的长度限制。 因为IP数据报的首部为20字节,所以IP数据报的数据区长度最大为1480字节.    
而这个1480字节就是用来放TCP传来的TCP报文段或UDP传来的UDP数据报的。 又因为UDP数据报的首部8字节,所以UDP数据报的数据区最大长度为1472字节。这个1472字节就是我们可以使用的字节数。

超过1500字节怎么办？

这也就是说IP数据报大于1500字节,大于MTU.这个时候发送方IP层就需要分片(fragmentation).    
把数据报分成若干片,使每一片都小于MTU.而接收方IP层则需要进行数据报的重组.    
这样就会多做许多事情,而更严重的是,由于UDP的特性,当某一片数据传送中丢失时,接收方便    
无法重组数据报.将导致丢弃整个UDP数据报。    

因此,在普通的局域网环境下，我建议将UDP的数据控制在1472字节以下为好. 

进行Internet编程时则不同,因为Internet上的路由器可能会将MTU设为不同的值.    
如果我们假定MTU为1500来发送数据的,而途经的某个网络的MTU值小于1500字节,那么系统将会使用一系列的机    
制来调整MTU值,使数据报能够顺利到达目的地,这样就会做许多不必要的操作。鉴于Internet上的标准MTU值为576字节,

所以我建议在进行Internet的UDP编程时. 最好将UDP的数据长度控件在548字节(576-8-20)以内.
