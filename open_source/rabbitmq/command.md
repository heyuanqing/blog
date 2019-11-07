# 启动命令

./rabbitmq-server -detached

或者

sudo rabbitmqctl start_app

此时如果rabbitmq-server stop会无法停止，报节点已经启动

需用   rabbitmqctl  stop_app 停止erlang上的node

启动：

rabbitmq-server start 

如果报错：

- connected to epmd (port 4369) on 10-205-202-35
- epmd reports: node 'rabbit' not running at all
    no other nodes on 10-205-202-35
- suggestion: start the node

到服务路径下

./rabbitmq-server

 

查看是否启动成功

## rabbitmq-server status



基本原理：

* 当发送消息时，交换机下所有的队列都会接受到
* 发送消息时，可以给每个消息带上key