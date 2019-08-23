#  linux新的API signalfd、timerfd、eventfd使用说明



## 三种fd加入的内核的版本号

signalfd:2.6.22

timerfd: 2.6.25

eventfd: 2.6.22

##三种fd的意义：

signalfd：传统的处理信号的方式是注册信号处理函数；由于信号是异步发生的，要解决数据的并发访问，可重入问题。signalfd可以将信号抽象为一个文件描述符，当有信号发生时可以对其read，这样可以将信号的监听放到select、poll、epoll等监听队列中。

timerfd：可以实现定时器的功能，将定时器抽象为文件描述符，当定时器到期时可以对其read，这样也可以放到监听队列的主循环中。

eventfd：实现了线程之间事件通知的方式，eventfd的缓冲区大小是sizeof(uint64_t)；向其write可以递增这个计数器，read操作可以读取，并进行清零；eventfd也可以放到监听队列中，当计数器不是0时，有可读事件发生，可以进行读取。



# 设置线程名

```
#include<stdio.h>
#include<stdlib.h>
#include <sys/prctl.h>
prctl(PR_SET_NAME,"THREAD1");
```

```
top -Hp pid  查看
```

