# 编译找不到头文件的解决办法

1. 编译时通过设置如下环境变量去添加编译时查找头文件和库的路径
   ```shell
   #头文件已经验证，没有问题
   export C_INCLUDE_PATH=$C_INCLUDE_PATH:/usr/local/gperftools-2.7/include
   export CPLUS_INCLUDE_PATH=$CPLUS_INCLUDE_PATH:/usr/local/gperftools-2.7/include
   
   #这样使用有问题，暂时未发现哪里使用错误了
   #shared
   export LD_LIBRARY_PATH=/usr/local/protobuf-3.9.1/lib:/usr/local/gperftools-2.7/lib:$LD_LIBRARY_PATH
   #static
   export LIBRARY_PATH=$LIBRARY_PATH	
   ```
2. 通过编译的时候添加 -L 添加动态库的查找路径 -I 添加头文件的查找路径 静态库 直接把整个路径加库一起添加到后面 -l连接动态库
   ```shell
   g++ test.cpp  
   -I /usr/local/xxx/include
   -L /usr/local/xxx/lib
   -lpthread 
   /usr/local/xxx/lib/libtest.a
   ```


# 运行时找不到库问题件的问题

   * 直接把库文件拷贝到 /usr/lib或者/usr/lib64目录中
   * 把库文件所在的路径添仿照 /etc/ld.so.conf.d/的conf 写一个conf文件 ，然后执行ldconfig 更新系统的.so路径是我缓存。