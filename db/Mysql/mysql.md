1. mysql远程连接权限问题

   > 通过修改user表的数据可以解决这个问题

* 修改user表中用户的密码

  ```sql
  alter USER 'root'@'localhost' identified with mysql_native_password by 'zxcvbnm,./'
  ```

* 修改user表用户连接ip

  ```sql
  select * from user;
  update user set host = '%' where user = 'root'; # % 代表所有的ip
  grant all privileges  on *.* to 'root'@'%' identified by 'zxcvbnm,./';
  ```

* 刷新数据让数据生效

  ```sql
  FLUSH PRIVILEGES ;
  ```

