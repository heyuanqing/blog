# 基于go开发，并遵从Apache2.0

Docker 是沙箱机制 他们之间是不会相互影响

优点：简化程序
避免选择恐惧症： 可以打包  web 后台 数据库 大数据应用 Hadoop集群 消息队列
节省开支：基于docker部署 就是云应用

Docker引擎：
一种服务器：是一种称为守护进程并长时间运行的程序
REST API用于指定程序可以用来和守护进程的接口通行
CLI  界面化得操作

系统架构：
C/S模式：
镜像
容器

安装：
要求： 1、必须是64位 
		2、内核必须>=3.10

# 内核版本升级  
## 安装包下载

在redhat6.5系统上用以下三种类内核包升级：

| 内核包类型           | 升级结果 |
| -------------------- | -------- |
| Kernel-lt-版本号.rpm | 成功     |
| Kernel-版本号.rpm    | 失败     |
| Kernel-ml-版本号.rpm | 失败     |

## #方法一

```shell
yum install yum-plugin-downloadonly
yum install --downloadonly  --downloaddir=/tmp/rpm kernel-ml-aufs kernel-ml-aufs-devel
从/tmp/rpm找到 kernel-ml-aufs-3.10.5-3.el6.x86_64.rpm ， kernel-ml-aufs-devel-3.10.5-3.el6.x86_64.rpm
```
### 方法二

* 登录[http://rpm.pbone.net](http://rpm.pbone.net/)

* 如果是上面的页面 点击Advanced RPM Search进入如下页面

* 选择你要升级的系统 redhat6 

  ​     分别下载：kernel-lt*.rpm 和kernel-lt-devel*.rpm

  ​     这里会出现多个版本的，连个包要选择一样的版本。

*  下载内核4.4.196的地址：
ftp://ftp.pbone.net/mirror/elrepo.org/kernel/el6/x86_64/RPMS/kernel-lt-devel-4.4.196-1.el6.elrepo.x86_64.rpm
ftp://ftp.pbone.net/mirror/elrepo.org/kernel/el6/x86_64/RPMS/kernel-lt-4.4.196-1.el6.elrepo.x86_64.rpm



## 升级内核
```shell
rpm –ivh kernel-lt-devel-4.4.196-1.el6.elrepo.x86_64.rpm
rpm –ivh kernel-lt-4.4.196-1.el6.elrepo.x86_64.rpm

```
## 修改默认启动内核版本
```shell
vim	/etc/grub.conf
	把default=1 改为default=0
```
## 关闭selinux
```shell
vim /etc/selinux/config
	把SELINUX的值改为disabled
```
## 重启系统

# docker 离线安装

```shell
下载docker版本https://download.docker.com/linux/static/stable/x86_64/

tar zxvf docker*.tgz -C ./
chmod +x  docker/* 
cp docker/* /usr/bin	

```

# 手动启动docker

```shell
dockerd &	
```

## docker 镜像

* 镜像的制作
  * 基于自己的系统

  ```shell
tar -cvpf /home/buildrpm.tar --directory=/ --exclude=proc --exclude=sys --exclude=dev --exclude=run /
  ```

--exclude 排除文件夹不打包

cat buildrpm.tar | docker import - buildrpm容器名字
从tar打包的tar文件 必须通过上面的命令导入到docker中
如果基于容器保存的数据，按照迁移的方式

[root@localhost redhat]# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
buildrpm            latest              47c169c5bc3f        28 minutes ago      652MB

  进入到容器中
  [root@localhost redhat]# docker run -it buildrpm:latest /bin/bash
  [root@aa94f53416ce /]# 

  


  ```

  

  * 基于现有的容器在添加新的

    * 通过docker search 和docker pull拉取

    * 或者在 [https://hub.docker.com](https://hub.docker.com/) 找对应的版本然后再拉取

      

* 镜像管理

  ```shell
  查看
  [root@localhost ~]# docker images
  REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
  buildrpm            latest              035286939ef7        5 minutes ago       652MB
  <none>              <none>              22896f1c4630        7 minutes ago       652MB
  centos              7.5.1804            1beb324dcf47        5 hours ago         200MB
  nginx               1.10                0346349a1a64        2 years ago         182MB
  删除
  [root@localhost ~]# docker rmi 22896f1c4630
  Error response from daemon: conflict: unable to delete 22896f1c4630 (must be forced) - image is being used by stopped container be035ee33dd2
  [root@localhost ~]# docker rmi -f 22896f1c4630
  Deleted: sha256:22896f1c46307fd6fc3af95c7f4a5fa6ba9bb80b38b759933176d9c62354251d
  [root@localhost ~]# 
  ```

* 关闭selinux

# dcoker使用

```shell
启动
docker run -it buildrpm:latest /bin/bash	

修改容器
在容器中修改完后，不要退出
在另外的窗口执行
[root@localhost ~]# docker ps -a
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS                      PORTS               NAMES
be035ee33dd2        buildrpm            "/bin/bash"         54 seconds ago      Exited (0) 44 seconds ago                       priceless_turing
096672f00c5c        47c169c5bc3f        "/bin/bash"         3 minutes ago       Exited (0) 54 seconds ago                       adoring_keller
[root@localhost ~]# docker commit be035ee33dd2（ps中的be035ee33dd2） buildrpm（IMAGE）
sha256:035286939ef738366695673b62a08bc48a2b328a7d103d3323243f20ff915d2c

备份  
[root@localhost ~]# docker images
REPOSITORY          TAG                 IMAGE ID            CREATED              SIZE
buildrpm            latest              035286939ef7        About a minute ago   652MB
<none>              <none>              22896f1c4630        3 minutes ago        652MB
centos              7.5.1804            1beb324dcf47        5 hours ago          200MB
nginx               1.10                0346349a1a64        2 years ago          182MB
[root@localhost ~]# docker save -o name.tar buildrpm:latest

导入
docker load -i name.tar
```

# 问题处理

问题1

```
root@hd-slave1:~# dockerd 
WARN[0000] could not change group /var/run/docker.sock to docker: group docker not found 
INFO[0000] libcontainerd: new containerd process, pid: 27014 
WARN[0000] containerd: low RLIMIT_NOFILE changing to max  current=1024 max=4096
WARN[0001] failed to rename /var/lib/docker/tmp for background deletion: %!s(<nil>). Deleting synchronously 
INFO[0001] [graphdriver] using prior storage driver: aufs 
INFO[0001] Graph migration to content-addressability took 0.00 seconds 
WARN[0001] Your kernel does not support cgroup memory limit 
WARN[0001] Unable to find cpu cgroup in mounts          
WARN[0001] Unable to find blkio cgroup in mounts        
WARN[0001] Unable to find cpuset cgroup in mounts       
WARN[0001] mountpoint for pids not found     Error starting daemon: Devices cgroup isn't mounted  
```

处理方式

```
vim /etc/fstab
#在最后一行增加以下配置信息：
none        /sys/fs/cgroup        cgroup        defaults    0    0
并重启
```

