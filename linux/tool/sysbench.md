## [sysbench的安装详解](https://www.cnblogs.com/JiangLe/p/7059136.html)

sysbench是一个压力测试工具、可以用它来测试cpu、mem、disk、thread、mysql、postgr、oracle；然而作为一个mysql dba 我当然是用它来压测mysql啦！

 

**一、从哪里可以下载到sysbench**：

　　sysbench的源码可以在github上面下载的到，sysbench的主页

```
https://github.com/akopytov/sysbench
```

 

**二、sysbench的一些安装依赖**：

```
yum -y install  make automake libtool pkgconfig libaio-devel vim-common
```

　　在我的机器上已经安装上了mysql相关的所有包，如果你机器上还没有安装过这些，那你还要安装上mysql的开发包，由于系统自带mariadb

　　这个mysql分支，所以在安装mysql-devel时应该是安装mariadb-devel

 

**三、安装sysbench**：

　　1　　进入到sysbench源码目录

```
/home/peter/Desktop/sysbench-master
```

　　2　　执行autogen.sh用它来生成configure这个文件

```
./autogen.sh
```

　　3　　执行configure && make && make install 来完成sysbench的安装

```
./configure --prefix=/usr/local/sysbench/ --with-mysql --with-mysql-includes=/usr/local/mysql/include --with-mysql-libs=/usr/local/mysql/lib
make
make install
```

　　我这里之所以要这样写是因为我的mysql安装在/usr/local/；而不是默认的rpm的安装位置

 

**四、测试是否安装成功**：

```
[root@workstudio bin]# /usr/local/sysbench/bin/sysbench --version
sysbench 1.1.0
```

　　到目前为止sysbench的安装就算是完成了！

**五、sysbench的帮助内容如下**：

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
 1 Usage:
 2   sysbench [options]... [testname] [command]
 3 
 4 Commands implemented by most tests: prepare run cleanup help
 5 
 6 General options:
 7   --threads=N                     number of threads to use [1]
 8   --events=N                      limit for total number of events [0]
 9   --time=N                        limit for total execution time in seconds [10]
10   --warmup-time=N                 execute events for this many seconds with statistics disabled before the actual benchmark run with statistics enabled [0]
11   --forced-shutdown=STRING        number of seconds to wait after the --time limit before forcing shutdown, or 'off' to disable [off]
12   --thread-stack-size=SIZE        size of stack per thread [64K]
13   --thread-init-timeout=N         wait time in seconds for worker threads to initialize [30]
14   --rate=N                        average transactions rate. 0 for unlimited rate [0]
15   --report-interval=N             periodically report intermediate statistics with a specified interval in seconds. 0 disables intermediate reports [0]
16   --report-checkpoints=[LIST,...] dump full statistics and reset all counters at specified points in time. The argument is a list of comma-separated values representing the amount of time in seconds elapsed from start of test when report checkpoint(s) must be performed. Report checkpoints are off by default. []
17   --debug[=on|off]                print more debugging info [off]
18   --validate[=on|off]             perform validation checks where possible [off]
19   --help[=on|off]                 print help and exit [off]
20   --version[=on|off]              print version and exit [off]
21   --config-file=FILENAME          File containing command line options
22   --luajit-cmd=STRING             perform LuaJIT control command. This option is equivalent to 'luajit -j'. See LuaJIT documentation for more information
23   --tx-rate=N                     deprecated alias for --rate [0]
24   --max-requests=N                deprecated alias for --events [0]
25   --max-time=N                    deprecated alias for --time [0]
26   --num-threads=N                 deprecated alias for --threads [1]
27 
28 Pseudo-Random Numbers Generator options:
29   --rand-type=STRING random numbers distribution {uniform,gaussian,special,pareto} [special]
30   --rand-spec-iter=N number of iterations used for numbers generation [12]
31   --rand-spec-pct=N  percentage of values to be treated as 'special' (for special distribution) [1]
32   --rand-spec-res=N  percentage of 'special' values to use (for special distribution) [75]
33   --rand-seed=N      seed for random number generator. When 0, the current time is used as a RNG seed. [0]
34   --rand-pareto-h=N  parameter h for pareto distribution [0.2]
35 
36 Log options:
37   --verbosity=N verbosity level {5 - debug, 0 - only critical messages} [3]
38 
39   --percentile=N       percentile to calculate in latency statistics (1-100). Use the special value of 0 to disable percentile calculations [95]
40   --histogram[=on|off] print latency histogram in report [off]
41 
42 General database options:
43 
44   --db-driver=STRING  specifies database driver to use ('help' to get list of available drivers)
45   --db-ps-mode=STRING prepared statements usage mode {auto, disable} [auto]
46   --db-debug[=on|off] print database-specific debug information [off]
47 
48 
49 Compiled-in database drivers:
50   mysql - MySQL driver
51 
52 mysql options:
53   --mysql-host=[LIST,...]          MySQL server host [localhost]
54   --mysql-port=[LIST,...]          MySQL server port [3306]
55   --mysql-socket=[LIST,...]        MySQL socket
56   --mysql-user=STRING              MySQL user [sbtest]
57   --mysql-password=STRING          MySQL password []
58   --mysql-db=STRING                MySQL database name [sbtest]
59   --mysql-ssl[=on|off]             use SSL connections, if available in the client library [off]
60   --mysql-ssl-cipher=STRING        use specific cipher for SSL connections []
61   --mysql-compression[=on|off]     use compression, if available in the client library [off]
62   --mysql-debug[=on|off]           trace all client library calls [off]
63   --mysql-ignore-errors=[LIST,...] list of errors to ignore, or "all" [1213,1020,1205]
64   --mysql-dry-run[=on|off]         Dry run, pretend that all MySQL client API calls are successful without executing them [off]
65 
66 Compiled-in tests:
67   fileio - File I/O test
68   cpu - CPU performance test
69   memory - Memory functions speed test
70   threads - Threads subsystem performance test
71   mutex - Mutex performance test
72 
73 See 'sysbench <testname> help' for a list of options for each test.
```

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

 

**六、sysbench对数据库进行压力测试的过程**：

　　1　　prepare 阶段 这个阶段是用来做准备的、比较说建立好测试用的表、并向表中填充数据。

　　2　　run       阶段 这个阶段是才是去跑压力测试的SQL

　　3　　cleanup 阶段 这个阶段是去清除数据的、也就是prepare阶段初始化好的表要都drop掉

 

**七、sysbench 中的测试类型大致可以分成内置的，lua脚本自定义的测试：**

　　1、内置：

　　　　fileio 、cpu 、memory 、threads 、 mutex 

　　2、lua脚本自定义型：

　　　　sysbench 自身内涵了一些测试脚本放在了安装目录下的：

```
[peter@cstudio sysbench]$ ll share/sysbench
总用量 60
-rwxr-xr-x. 1 root root  1452 10月 17 15:18 bulk_insert.lua
-rw-r--r--. 1 root root 13918 10月 17 15:18 oltp_common.lua
-rwxr-xr-x. 1 root root  1290 10月 17 15:18 oltp_delete.lua
-rwxr-xr-x. 1 root root  2415 10月 17 15:18 oltp_insert.lua
-rwxr-xr-x. 1 root root  1265 10月 17 15:18 oltp_point_select.lua
-rwxr-xr-x. 1 root root  1649 10月 17 15:18 oltp_read_only.lua
-rwxr-xr-x. 1 root root  1824 10月 17 15:18 oltp_read_write.lua
-rwxr-xr-x. 1 root root  1118 10月 17 15:18 oltp_update_index.lua
-rwxr-xr-x. 1 root root  1127 10月 17 15:18 oltp_update_non_index.lua
-rwxr-xr-x. 1 root root  1440 10月 17 15:18 oltp_write_only.lua
-rwxr-xr-x. 1 root root  1919 10月 17 15:18 select_random_points.lua
-rwxr-xr-x. 1 root root  2118 10月 17 15:18 select_random_ranges.lua
drwxr-xr-x. 4 root root    46 10月 17 15:18 tests
```

 

八、通过sysbench自带的lua脚本对mysql进行测试：

　　1、第一步 prepare  

```
sysbench --mysql-host=localhost --mysql-port=3306 --mysql-user=sbtest \
    --mysql-password=123456 --mysql-db=tempdb oltp_insert prepare
```

　　2、第二步 run

```
sysbench --mysql-host=localhost --mysql-port=3306 --mysql-user=sbtest     --mysql-password=123456 --mysql-db=tempdb oltp_insert run                                                              
sysbench 1.1.0 (using bundled LuaJIT 2.1.0-beta3)

Running the test with following options:
Number of threads: 1
Initializing random number generator from current time


Initializing worker threads...

Threads started!

SQL statistics:
    queries performed:
        read:                            0
        write:                           22545
        other:                           0
        total:                           22545
    transactions:                        22545  (2254.37 per sec.)
    queries:                             22545  (2254.37 per sec.)
    ignored errors:                      0      (0.00 per sec.)
    reconnects:                          0      (0.00 per sec.)

Throughput:
    events/s (eps):                      2254.3691
    time elapsed:                        10.0006s
    total number of events:              22545

Latency (ms):
         min:                                  0.31
         avg:                                  0.44
         max:                                 10.47
         95th percentile:                      0.67
         sum:                               9918.59

Threads fairness:
    events (avg/stddev):           22545.0000/0.00
    execution time (avg/stddev):   9.9186/0.00
```

　　3、第三步 cleanup

```
sysbench --mysql-host=localhost --mysql-port=3306 --mysql-user=sbtest     --mysql-password=123456 --mysql-db=tempdb oltp_insert cleanup                                                   
sysbench 1.1.0 (using bundled LuaJIT 2.1.0-beta3)

Dropping table 'sbtest1'...
```