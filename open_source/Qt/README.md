#问题一
描述：no Qt platform plugin could be initalized
解决办法：
复制Qt安装目录中的整个platform目录到执行文件目录
eg:E:\Qt\Qt5.11.0\5.11.0\msvc2017_64\plugins\platforms

#问题二
描述：QImage load失败
解决办法：复制Qt安装目录中的整个imageformats目录到执行文件目录
E:\Qt\Qt5.11.0\5.11.0\msvc2017_64\plugins\imageformats
