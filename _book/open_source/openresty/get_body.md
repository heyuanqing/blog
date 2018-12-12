#获取body

##配置

```
http {
    server {
        listen    80;
        location /test {
            content_by_lua_block {
                local data = ngx.req.get_body_data()
                ngx.say("hello ", data)
            }
        }
    }
}

```

##测试

```
➜  ~  curl 127.0.0.1/test -d jack
hello nil
```

##说明
大家可以看到 data 部分获取为空，如果你熟悉其他 web 开发框架，估计立刻就觉得 OpenResty 弱爆了。查阅一下官方 wiki 我们很快知道，原来我们还需要添加指令 lua_need_request_body 。究其原因，主要是 Nginx 诞生之初主要是为了解决负载均衡情况，而这种情况，是不需要读取 body 就可以决定负载策略的，所以这个点对于 API Server 和 Web Application 开发的同学有点怪。

参考下面的例子

```
http {
    server {
        listen    80;

        # 默认读取 body
        lua_need_request_body on;

        location /test {
            content_by_lua_block {
                local data = ngx.req.get_body_data()
                ngx.say("hello ", data)
            }
        }
    }
}
```

再次测试，符合我们的预期：

```
~ curl 127.0.0.1/test -d jack
hello jack
```

如果你只是某个接口需要读取body(并非全局行为)，那么这时候就可以显示调用
ngx.req.read_body()接口，参考下面示例

```
http {
    server {
        listen    80;

        location /test {
            content_by_lua_block {
                ngx.req.read_body()
                local data = ngx.req.get_body_data()
                ngx.say("hello ", data)
            }
        }
    }
}
```

##body偶尔读取不到
ngx.req.get_body_data()读取请求，会偶尔出现读取不到直接返回nil的情况。

如果请求提尚未被读取，请先调用ngx.req.read_body(或打开lua_need_request_body选项强制本模块读取请求体，此方法不推荐)。

如果请求体已经被存入临时文件，请使用ngx.req.get_body_file函数代替。

如果需要强制在内存中保存请求体，请设置client_body_buffer_size和client_max_body_size为同样大小。

参考代码：

```
http {
    server {
        listen    80;

        # 强制请求 body 到临时文件中（仅仅为了演示）
        client_body_in_file_only on;

        location /test {
            content_by_lua_block {
                function getFile(file_name)
                    local f = assert(io.open(file_name, 'r'))
                    local string = f:read("*all")
                    f:close()
                    return string
                end

                ngx.req.read_body()
                local data = ngx.req.get_body_data()
                if nil == data then
                    local file_name = ngx.req.get_body_file()
                    ngx.say(">> temp file: ", file_name)
                    if file_name then
                        data = getFile(file_name)
                    end
                end

                ngx.say("hello ", data)
            }
        }
    }
}
```

测试结果：

```
 ~  curl 127.0.0.1/test -d jack
>> temp file: /Users/rain/Downloads/nginx/client_body_temp/0000000018
hello jack
```

由于nginx是为了解决负载均衡场景而衍生的，所以它默认是不读取body的行为，会对
API server和web Application场景造成一些影响，根据需求正确读取、丢弃body对Openresty开发至关重要的。

