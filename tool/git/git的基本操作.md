# 设置ss
git config --global http.proxy 'socks5://127.0.0.1:1080'
git config --global https.proxy 'socks5://127.0.0.1:1080'

# 设置代理
git config --global https.proxy http://127.0.0.1:1080
git config --global https.proxy https://127.0.0.1:1080

# 取消代理
git config --global --unset http.proxy
git config --global --unset https.proxy



# 初始化一个本地仓库

1. git 初始化一个本地repository

   `git init`

2. git 设置配置

- 配置用户名

  `git config --global user.name "用户名"`

- 配置密码

  `git config --global user.password "密码"`

- 设置远程库url

  ```shell
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

- 强行同步

  `git pull -p`

# 问题
No refs in common and none specified; doing nothing.
找不到对应的分支

执行 `git push origin master`

# 回滚的操作 

* 一个人提交时

  ```shell
  # 查找要回滚的时间点
  $ git reflog
  f76c4cd (HEAD -> master, origin/master, origin/HEAD) HEAD@{0}: commit: 整理之前和现的记录
  59bc6b2 HEAD@{1}: clone: from git@github.com:Snail-code/Everyday-Learning-Experience.git
  #本地回退到指定版本
  git reset --hard 59bc6b2
  #强制推送到远程端
  git push -f 
  ```

* 多人提交时

  ```
  1、先拉分支
  2、回退到自己的要回退的版本
  3、合并刚刚拉的分支到主版本中
  ```

  # 分支的切换合并

* 本地创建切换主分支 

  ```shell
  git branch <分支名> 在当前分支的基础上创建分支
  git branch -d <分支名> 删除当前分支
  git checkout <分支名> 切换分支
  git checkout -b <分支名> 创建并切换分支
  git branch  查看本次分支
  ```

* 远程分支

  ```shell
  git push origin --delete <分支名> 删除远程分支
  git push --set-upstream origin dev 第一次设置推送到远程分支
  git push 推送到当前分支
  ```

* 合并冲突

  ```shell
  git checkout master
  git pull origin master 
  git merge dev
  如果有冲突
  git mergetool
  解决后
     
  git commit -m ""
  git push origin master  
  ```

* 创建开发分支 `git checkout -b dev`

* 创建自己的开发分支 `git checkout -h hyq`

* 在自己的开发分支上开发

# 分支更新操作

在dev分支中

` git pull origin master`

会把master覆盖到dev中

直接git push 可以提交到远程仓库

