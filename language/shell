

 []中 -a  为&&

[]中 -o 为||



-eq           //等于

-ne           //不等于

-gt            //大于 （greater ）

-lt            //小于  （less）

-ge            //大于等于

-le            //小于等于



4 array=(${stringpath//=/})
 5 length=${#array[@]}
 6 proc_check_sh_path=""
 7 for (( index =1; index< $length; index++))
 8 do
 9     echo ${array[$index]}
10     $proc_check_sh_path += ${array[$index]}
11     $proc_check_sh_path +=" "
12 done
13 
14 echo $proc_check_sh_path



CORE_PROG=(aclog daemonguard fluxlogd fluxctrld monitor mysqld singress actrace boa authd)





 2 stringpath=`cat /ac/etc/config/daemon.ini|grep "fluxlog/country_stats" |grep enable_check|se   d  's/\r//'`
 3 check_path=`echo ${stringpath##*=}`
 4 
 5 str=${check_path// / };
 6 arr=($str);
 7 #遍历数组
 8 for each in ${arr[*]}
 9 do
10      echo $each
11      result=$result$each
12 done
13 echo $result
14 
15 test=`check_path`

