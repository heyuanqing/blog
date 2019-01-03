1、	数据结构（哈希表和红黑二叉树，图）

2、	网路编程（epoll）

3、	Socket的状态模式

4、	设计模式

5、	Rtsp rtmp flv ts hls

6、	C++基础（多态）

7、	Tcp底层的实现

8、	Linux文件机制

9、	Linux内存机制

10、	知识的体系化

11、	C++特点总结

流行的开源框架： grpc thrift 

协成库 libgo libco

服务框架：alc 

序列化：protobuf

负载均衡 ： robin conhash 

Rpc框架：在我们看来，RPC框架绝不仅仅是封装一下网络通讯就可以了的，要想应对数以百计的不同服务、数千万用户、百亿级PV的业务量挑战，RPC框架还必须在高可用、负载均衡、过载保护、通信协议向后兼容、优雅降级、超时处理、无序启动几个维度都做到足够完善才行。

Cgi：

Rpc: rest_rpc thrift  Avro   

Netty：java封装的网络传输库

Rtsp rtmp rtp rtcp flv hls  sdp  h264 h265 ffmpeg webrtc ts mp4 http 采集播放
设计模式  算法 yuv nginx  opencv opengl 内容的处理和显示



系统的相关知识：
大的方向	详细问题	答案	内核优化的策略
内存	内存使用情况		
	内存泄漏		
	内存占用		
	内存管理		
	内存查看		
Cpu	Cpu的整体使用情况		
	程序占用cpu情况		
	Cpu占用高的查找方法		
	Cpu占用高的优化		
	Cpu使用的一些概念		
磁盘	磁盘IO问题		
	磁盘的使用情况		
	磁盘满问题		
	磁盘管理		
网络	网络IO		
	网络丢包		
	网络管理		
	网络配置		
	网络状态		
	并发		
			
			
C++基础：
类的内存模型	
虚函数考点	
Class和struct	
联合体	
封装，继承，多态	
友员	
Static	
Const	
模板	
指针 引用	
指针步长	

TCP	TCP的状态图
	TCP的底层算法
	开发注意的问题
UDP	Udp的特性
	包长
	组播
	Udp的问题
	
http	http1.0
	http2.0
	Websocket
	状态码
	自己解析的话，解析过程

技术热情：
书名	
	
	
	
	
开源的框架（redis）	


专业知识：
大的模块	问题	
Ffmpeg	模块的及其功能	
	函数	
Libx264	码率的控制	
	各个帧的作用和由来	
Ts		
Flv		
Rtmp		
Rtsp		
Rtp/rtcp		
Hls		
储存协议		


RTP Payload Format for the Opus Speech and Audio Codec  rfc7587  https://tools.ietf.org/html/rfc7587
A More Loss-Tolerant RTP Payload Format for MP3 Audio    rfc5219  https://tools.ietf.org/html/rfc3119
RTP Payload Format for H.265/HEVC Video
                   draft-ietf-payload-rtp-h265-14.txt                      rfc         https://tools.ietf.org/html/draft-ietf-payload-rtp-h265-15
vp8                                                                                                     https://tools.ietf.org/html/draft-ietf-payload-vp8-17
vp9                                                                                                     
rtmp                                                                                                    https://tools.ietf.org/html/rfc7425