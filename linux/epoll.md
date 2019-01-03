#一、epoll简介

epoll是当前在Linux下开发大规模并发网络程序的热门选择，epoll在Linux2.6内核中正式引入，和select相似，都是IO多路复用（IO multiplexing）技术。

按照man手册的说法，epoll是为处理大批量句柄而做了改进的poll。

##linux下的几个经典的服务器模型

##1、PPC模型和TPC模型

PPC（Process Per Connection）模型和TPC（Thread Per Connection）模型的设计思想类似，就是给每一个到来的连接都分配一个独立的进程或者线程来服务。对于这两种模型，其需要耗费较大的时间和空间资源。当管理连接数较多时，进程或线程的切换开销较大。因此，这类模型能接受的最大连接数都不会高，一般都在几百个左右。

##2、select模型

对于select模型，主要有以下几个特点：

+ 最大并发数限制：由一个进程所打开的fd(文件描述符)是有限制的，由FD_SETSIZE设置，默认的值是1024/2048，因此select模型的最大并发数被限制了
+ 效率问题：每次进行select调用都会线性扫描全部的fd集合。这样的效率会呈现线性下降。
+ 内核、用户空间内存拷贝问题：select在解决将fd消息传递给用户空间时，采用了内存拷贝的方式。这样的效率不高。

##3、poll模型

对于poll模型，其解决了select最大鬓发梳的限制，但是依然莫有解决select的效率问题和内核拷贝问题。

##4、epoll模型




