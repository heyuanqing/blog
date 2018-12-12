#1.git 初始化一个本地repository

        `git init`
#2.git 设置配置

- 配置用户名

    `git config --global user.name "用户名"`

- 配置密码
    
    `git config --global user.password "密码"`

-  设置远程库url

    ```
        git remote set-url origin git@github.com:heyuanqing/blog.git 
        git remote add origin https://github.com/heyuanqing/blog.git
    ```



- 配置ssh

    - 生成秘钥（如果已经有秘钥了就可以直接跳过该步骤）
    
        `ssh-keygen -t rsa 并回车3下（为什么按三下，是因为有提示你是否需要设置密码，如果设置了每次使用Git都会用到密码，一般都是直接不写为空，直接回车就好了）会在 ~/.ssh/目录下生成一个私钥 id_rsa和一个公钥id_rsa.pub`

    - 设置秘钥到git上

        - 通过 
            `cat ~/.ssh/id_rsa.pub 并复制id_rsa.pub的所有内容`

    - 登录到自己的github上 
        
        在setting->SSH and GPS kyes->New GPSG Key
        
        把刚刚复制的id_rsa.pub的内容复制过来 

        点击添加Add GPG key

- 查看git的配置

    `git config --list`

- 上传本地代码到远程仓库上

    `git push -u origin master(指定分支) `



