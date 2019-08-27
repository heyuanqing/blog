# pkg-config 

1. 配置命令的查找*.pc的路径

   通过设置环境变量PKG_CONFIG_PATH来实现
2. 查看库的头文件和依赖关系

```shell
[root@localhost grpc]# pkg-config --cflags --libs  libcares 
-I/usr/local/cares/include  -L/usr/local/cares/lib -lcares
```
3. 在编译中使用示例
   ` gcc program.c $(pkg-config --cflags --libs gnomeui)`

