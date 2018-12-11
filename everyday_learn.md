20181211

1、实时预览：安装 MarkdownLivePreview
2、修改配置项：打开setting：Preferences → Package Settings → MarkdownLivePreview → Setting
将左边default设置代码复制到右边User栏，将markdown_live_preview_on_open: false,把false改为true，保存。 
git的命令： git config --global user.name "he9282@126.com"

git config --global user.password "1990610abc"

git remote set-url origin git@github.com:heyuanqing/blog.git

设置ssh 

git config --list

git push -u origin master

git remote add origin https://github.com/heyuanqing/blog.git

kt  /usr/local/bin/ktserver -dmn -cmd /data/kyoto -port 1914 -auxport 1916 -sec -msec -ca /data/kyoto/ssl/ca-cert.pem -pk /data/kyoto/ssl/server-key.pem -cert /data/kyoto/ssl/server-cert.pem -rpk /data/kyoto/ssl/server-key.pem -rcert /data/kyoto/ssl/server-cert.pem -log /data/kyoto/ktserver-log -pid /data/kyoto/ktserver.pid -ulog /data/kyoto/0001-ulog -mhost 192.168.3.230 -mport 1914 -sid 3230 -plsv /usr/local/libexec/ktplugservmemc.so -plex host=192.168.3.230#port=1911 -rts /data/kyoto/0001.rts /data/kyoto/casket-0001.kch

./configure --prefix=/usr/local/kyototycoon LDFLAGS='-I /usr/local/kyototycoon/include' CPPFLAGS='-I /usr/local/kyototycoon/include -L /usr/local/kyototycoon/lib -L /usr/local/lua/lib' --with-kc="/usr/local/kyototycoon/leveldb" --with-lua="/usr/local/lua"



nginx 11 个处理阶段

nginx实际把请求处理流程划分为了11个阶段，这样划分的原因是将请求的执行逻辑细分，各阶段按照处理时机定义了清晰的执行语义，开发者可以很容易分辨自己需要开发的模块应该定义在什么阶段，其定义在http/ngx_http_core_module.h中有定义：


NGX_HTTP_POST_READ_PHASE:
接收完请求头之后的第一个阶段，它位于uri重写之前，实际上很少有模块会注册在该阶段，默认的情况下，该阶段被跳过

NGX_HTTP_SERVER_REWRITE_PHASE:
server级别的uri重写阶段，也就是该阶段执行处于server块内，location块外的重写指令，在读取请求头的过程中nginx会根据host及端口找到对应的虚拟主机配置

NGX_HTTP_FIND_CONFIG_PHASE:
寻找location配置阶段，该阶段使用重写之后的uri来查找对应的location，值得注意的是该阶段可能会被执行多次，因为也可能有location级别的重写指令

NGX_HTTP_REWRITE_PHASE:

location级别的uri重写阶段，该阶段执行location基本的重写指令，也可能会被执行多次

NGX_HTTP_POST_REWRITE_PHASE:
location级别重写的后一阶段，用来检查上阶段是否有uri重写，并根据结果跳转到合适的阶段

NGX_HTTP_PREACCESS_PHASE:
访问权限控制的前一阶段，该阶段在权限控制阶段之前，一般也用于访问控制，比如限制访问频率，链接数等

NGX_HTTP_ACCESS_PHASE:
访问权限控制阶段，比如基于ip黑白名单的权限控制，基于用户名密码的权限控制等

NGX_HTTP_POST_ACCESS_PHASE:
问权限控制的后一阶段，该阶段根据权限控制阶段的执行结果进行相应处理

NGX_HTTP_TRY_FILES_PHASE:
try_files指令的处理阶段，如果没有配置try_files指令，则该阶段被跳过

NGX_HTTP_CONTENT_PHASE:
内容生成阶段，该阶段产生响应，并发送到客户端

NGX_HTTP_LOG_PHASE:
日志记录阶段，该阶段记录访问日志

2. nginx lua 8个处理阶段

init_by_lua           | http
set_by_lua            |server, server if, location, location if
rewrite_by_lua        | http, server, location, location if
access_by_lua         | http, server, location, location if
content_by_lua        | location, location if
header_filter_by_lua  | http, server, location, location if
body_filter_by_lua    | http, server, location, location if
log_by_lua            | http, server, location, location if
{
    set_by_lua: 流程分支处理判断变量初始化
    rewrite_by_lua: 转发、重定向、缓存等功能(例如特定请求代理到外网)
    access_by_lua: IP准入、接口权限等情况集中处理(例如配合iptable完成简单防火墙)
    content_by_lua: 内容生成
    header_filter_by_lua: 应答HTTP过滤处理(例如添加头部信息)
    body_filter_by_lua: 应答BODY过滤处理(例如完成应答内容统一成大写)
    log_by_lua: 会话完成后本地异步完成日志记录(日志可以记录在本地，还可以同步到其他机器)
}


