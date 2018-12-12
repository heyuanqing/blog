
Markdown 基本语法
#一、标题
一个#是一级，两个#是二级，依次类推。支持六级标题
示例：

```
#一级标题
##二级标题
###三级标题
####四级标题
#####五级标题
######六级标题
```

效果：
#一级标题
##二级标题
###三级标题
####四级标题
#####五级标题
######六级标题

#二、字体
**加粗** 

用两个引号包起来

*倾斜*

用一个引号包起来

***斜体加粗***

用三个引号包起来

~~删除线~~

用两个~包起来

示例：
```
**加粗**
*倾斜*
***斜体加粗***
~~删除线~~
```

效果：

**加粗**

*倾斜*

***斜体加粗***

~~删除线~~

#三、引用
在引用的文字前加>

示例：
```
>这是引用的内容
>>这是引用的内容
>>>>>>>>>>这是引用的内容

```

效果:
>这是引用的内容
>>这是引用的内容
>>>>>>>>>>这是引用的内容

#四、分割线
三个或者三个以上的-或者*都可以

示例：

```
---
----
***
*****
```

效果：
---
----
***
*****

#五：图片
语法：
```
![图片alt](图片地址 "图片title")
图片alt就是显示在图片下面的文字，相当于对图片内容的解释。
图片title是图片的标题，当鼠标移到图片上时显示的内容。title可加可不加
```

示例：

```
![blockchain](https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/
u=702257389,1274025419&fm=27&gp=0.jpg "区块链")
```

效果：

![图片](../../image/markdown/123.jpg "图片测试")

#六、超链接
语法：
```
[超链接名](超链接地址 "超链接title")
title可加可不加
```

示例：
```
[百度](http://www.baidu.com "百度链接")
```

效果：

[百度](http://www.baidu.com "百度链接")

#七、列表


* ###无序列表

语法：

用-+*任何一种都可以
```
- 列表内容
+ 列表内容
* 列表内容
注意：- + * 跟内容之间都要有一个空格
```

效果：

- 列表内容
+ 列表内容
* 列表内容

- ###有序列表

语法：数字加点

示例：

```
1.列表内容
2.列表内容
3.列表内容
注意：序号跟内容之间要有空格
```

效果：

1.列表内容
2.列表内容
3.列表内容

- 列表嵌套
 
上一级和下一级间敲一个空格即可

示例：

```
- 一级无序列表内容   
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容
 

- 一级无序列表内容 
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容

 1.一级无序列表内容   
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容
 

2. 一级无序列表内容 
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容
```
效果：

- 一级无序列表内容   
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容
 

- 一级无序列表内容 
 - 二级无序列表内容
 - 二级无序列表内容
 - 二级无序列表内容

#八、表格

语法：

```
表头|表头|表头
---|:--:|---:
内容|内容|内容
内容|内容|内容

第二行分割表头和内容。
- 有一个就行，为了对齐，多加了几个
文字默认居左
-两边加：表示文字居中
-右边加：表示文字居右
注：原生的语法两边都要用 | 包起来。此处省略
```

示例：
```
姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟
```

效果：

姓名|技能|排行
--|:--:|--:
刘备|哭|大哥
关羽|打|二哥
张飞|骂|三弟

#九、代码块

单行用``
多行用 ``````

示例：
```
`代码内容`
(```)
    代码块
    代码块
    代码块
(```)
```

效果：

`代码内容`

```
    代码块
    代码块
    代码块
```

#十、流程图

示例：

```
```flow
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```
```
效果：

```flow
st=>start: 开始
op=>operation: My Operation
cond=>condition: Yes or No?
e=>end
st->op->cond
cond(yes)->e
cond(no)->op
&```