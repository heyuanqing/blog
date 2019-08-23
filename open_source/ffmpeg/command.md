推流命令：

```shell
ffmpeg -stream_loop -1 -re  -i np_1.ts   -acodec copy -vcodec libx264 -f mpegts udp://172.21.23.75:3000
 ffmpeg.exe  -stream_loop -1  -re  -i /c/Users/910200/Desktop/test.ts -acodec copy -vcodec libx264 -f mpegts udp://172.21.23.75:30000

展厅环境：http://172.21.23.75:8877/live/H266
-c copy
```



