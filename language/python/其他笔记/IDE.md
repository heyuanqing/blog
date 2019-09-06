# pycharm

1、设置文件编码格式 参考 [中文编码](./1、中文编码.md)

2、安装格式化工具 autopep8

* 安装

	```python
	pip install autopep8
	```

* 配置 file->tools->External tools ->add

  ```
  program: autopep8
  Arguments:  --in-place --aggressive $FilePath$
  working directory:  $ProjectFileDir$
  ```

* 设置快捷键

  file->setting->External tools->External tools ->autopep8 右键 add keyboard shortcut