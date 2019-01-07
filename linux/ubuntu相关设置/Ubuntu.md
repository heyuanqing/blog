# root ssh登录问题

**ubuntu默认不让root通过ssh登录**

安装ssh：

```shell
sudo apt install ssh 
```

修改root登录权限：

```shell
把
#LoginGraceTime 2m
#PermitRootLogin prohibit-password
#StrictModes yes

改为
#LoginGraceTime 2m
#PermitRootLogin prohibit-password
PermitRootLogin yes
#StrictModes yes
```

# root界面登录设置

默认安装Ubuntu18.04都是不允许以root用户进行登录的，想要以root用户进行登录需要进行一些操作，主要是以下几个步骤： 
第一步：以普通用户登录系统，创建root用户的密码 
在终端输入命令：sudo passwd root 
然后输入你要设置的密码，这样就完成了设置root用户密码的步骤

第二步：修改文件/usr/share/lightdm/lightdm.conf.d/50-unity-greeter.conf文件，增加两行： 

```shell
greeter-show-manual-login=true 
all-guest=false 
```

第三步：进入/etc/pam.d目录，修改gdm-autologin和gdm-password文件 
vi gdm-autologin 
注释掉auth required pam_succeed_if.so user != root quiet_success这一行，保存 
vi gdm-password 
注释掉 auth required pam_succeed_if.so user != root quiet_success这一行，保存

第四步：修改/root/.profile文件 
vi /root/.profile 
将文件末尾的mesg n || true这一行修改成tty -s&&mesg n || true， 保存

第五步：重启系统，输入root用户名和密码，登录系统。



# 分辨率设定为1920*1080

1、查看显示器名称

```
xrandr
```

![](E:\node\book\blog\image\linux\ubuntu\1.png)

```shell
xrandr --newmode "1920x1080_60.00" 173.00 1920 2048 2248 2576 1080 1083 1088 1120 -hsync +vsync
xrandr --addmode  Virtual1 "1920x1080_60.00" #这里的Virtual1要和上面的Virtual1相同
```

# 设置字体大小

1、安装gnome-tweaks桌面配置工具。

```shell
sudo apt  install    gnome-tweaks
```

2、**alt+f2** 在运行窗口输入 **gnome-tweaks** 命令，然后回车，然后进行设置