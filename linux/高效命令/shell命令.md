```shell
du -al ../  |grep "\.h"|awk '{print $2}'|xargs -i  cp -r {} ./include/{}
for i in `du -al ./packager`; { if [ -f $i ];then a=${i/packager/packager_back}; cp /home/heyuanqing/DASH/Packager/packager_src/packager_src/src/$i $a ;fi;}

find ./ -name  *unittest* -type f |xargs rm -rf

du -al / --max-depth=1 
```

