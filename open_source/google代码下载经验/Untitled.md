

1、通过shadowsock翻墙

2、设置git代理

```shell
git config --global http.proxy 'socks5://127.0.0.1:1080'

git config --global https.proxy 'socks5://127.0.0.1:1080'

# 设置代理
git config --global https.proxy http://127.0.0.1:30000
git config --global https.proxy https://127.0.0.1:30000

# 取消代理
git config --global --unset http.proxy

git config --global --unset https.proxy

查看
git config --global --get http.proxy
git config --global --get https.proxy
```



3、通过下载depot_tools

```shell
git clone https://chromium.googlesource.com/chromium/tools/depot_tools
```

4、设置环境depot_tools的环境变量

5、下载代码



在linux中  

安装shadowsock

1、安装python

2、安装sslocal

```shell
  ubunut中
  sudo su root
  apt install python-pip
  apt install python-setuptools m2crypto
  pip install shadowsocks
  
  centos中
  yum install python-setuptools && easy_install pip
  pip install shadowsocks
  
  如果系统无法使用epel_release的源
  使用源码安装pip
  
  1、下载源码 https://files.pythonhosted.org/packages/93/ab/f86b61bef7ab14909bd7ec3cd2178feb0a1c86d451bc9bccd5a1aedcde5f/pip-19.1.1.tar.gz
  2、通过 Python setup.py install 安装
  3、通过  pip install shadowsocks安装
  4、使用sslocal配置本地代理
  
```

3、把源代码上传到linux中

4、设置git代理

5、重新下载代码

6、在linux中编译源码



1564737785097

决策大屏电视墙

51018100001120984872