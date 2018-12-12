#获取uri参数

首先看一下官方 API 文档，获取一个 uri 有两个方法：ngx.req.get_uri_args、ngx.req.get_post_args，二者主要的区别是参数来源有区别。
参考下面例子：

```
server {
   listen    80;
   server_name  localhost;

   location /print_param {
       content_by_lua_block {
           local arg = ngx.req.get_uri_args()
           for k,v in pairs(arg) do
               ngx.say("[GET ] key:", k, " v:", v)
           end

           ngx.req.read_body() -- 解析 body 参数之前一定要先读取 body
           local arg = ngx.req.get_post_args()
           for k,v in pairs(arg) do
               ngx.say("[POST] key:", k, " v:", v)
           end
       }
   }
}

```

##测试结果：

```
[root@localhost sbin]# curl '127.0.0.1/print_param?a=1&b=2' -d 'c=3&d=4%26'
[GET ] key:b v:2
[GET ] key:a v:1
[POST] key:d v:4&
[POST] key:c v:3
说明：%26是&
```

#传递请求的uri参数

参看下面例子：
```
   location /test {
       content_by_lua_block {
           local res = ngx.location.capture(
                    '/print_param',
                    {
                       method = ngx.HTTP_POST,
                       args = ngx.encode_args({a = 1, b = '2&'}),
                       body = ngx.encode_args({c = 3, d = '4&'})
                   }
                )
           ngx.say(res.body)
       }
   }
```

输出结果：

```
➜  ~  curl '127.0.0.1/test'
[GET]  key:b v:2&
[GET]  key:a v:1
[POST] key:d v:4&
[POST] key:c v:3
```

与我们预期是一样的。
如果这里不调用ngx.encode_args ，可能就会比较丑了，看下面例子：

```local res = ngx.location.capture('/print_param',
         {
            method = ngx.HTTP_POST,
            args = 'a=1&b=2%26',  -- 注意这里的 %26 ,代表的是 & 字符
            body = 'c=3&d=4%26'
        }
     )
ngx.say(res.body)
```

PS：对于 ngx.location.capture 这里有个小技巧，args 参数可以接受字符串或Lua 表的，这样我们的代码就更加简洁直观。

```local res = ngx.location.capture('/print_param',
         {
            method = ngx.HTTP_POST,
            args = {a = 1, b = '2&'},
            body = 'c=3&d=4%26'
        }
     )
ngx.say(res.body)
```
