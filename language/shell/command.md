

linux删除文件后的部分恢复方式

- lsof |grep path/file_name
- 查找该文件对应的fd(/proc/pid/fd)
- cat /proc/pid/fd/xxx > file_name

