alter USER 'root'@'localhost' identified with mysql_native_password by 'zxcvbnm,./';
select * from user;
update user set host = '%' where user = 'root';
grant all privileges  on *.* to 'root'@'%' identified by 'zxcvbnm,./';


ALTER USER 'root'@'localhost' IDENTIFIED BY "Zxcvbnm,./1@";