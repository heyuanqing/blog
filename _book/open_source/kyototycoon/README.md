#安装步骤：

- 安装kyoto cabinet
- 安装leveldb
- 安装kyoto tycoon
    - 编译脚本

        `./configure --prefix=/usr/local/kyototycoon LDFLAGS='-I /usr/local/kyototycoon/include' CPPFLAGS='-I /usr/local/kyototycoon/include -L /usr/local/kyototycoon/lib -L /usr/local/lua/lib' --with-kc="/usr/local/kyototycoon/leveldb" --with-lua="/usr/local/lua"`

#启动脚本

    `/usr/local/bin/ktserver -dmn -cmd /data/kyoto -port 1914 -auxport 1916 -sec -msec -ca /data/kyoto/ssl/ca-cert.pem -pk /data/kyoto/ssl/server-key.pem -cert /data/kyoto/ssl/server-cert.pem -rpk /data/kyoto/ssl/server-key.pem -rcert /data/kyoto/ssl/server-cert.pem -log /data/kyoto/ktserver-log -pid /data/kyoto/ktserver.pid -ulog /data/kyoto/0001-ulog -mhost 192.168.3.230 -mport 1914 -sid 3230 -plsv /usr/local/libexec/ktplugservmemc.so -plex host=192.168.3.230#port=1911 -rts /data/kyoto/0001.rts /data/kyoto/casket-0001.kch`