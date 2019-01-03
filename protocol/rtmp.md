3.1 RTMP(Real Time Messaging Protocol)实时消息传送协议
是Adobe Systems公司为Flash播放器和服务器之间音频、视频和数据传输开发的开放协议。

它有三种变种：
1)工作在TCP之上的明文协议，使用端口1935；
2)RTMPT封装在HTTP请求之中，可穿越防火墙；
3)RTMPS类似RTMPT，但使用的是HTTPS连接；
  RTMP协议(Real Time Messaging Protocol)是被Flash用于对象,视频,音频的传输.这个协议建立在TCP协议或者轮询HTTP协议之上.
  RTMP协议就像一个用来装数据包的容器,这些数据既可以是AMF格式的数据,也可以是FLV中的视/音频数据.
  一个单一的连接可以通过不同的通道传输多路网络流.这些通道中的包都是按照固定大小的包传输的.
