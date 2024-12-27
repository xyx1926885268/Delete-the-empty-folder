# 空文件夹删除器

# 介绍

还在为空文件夹太多一个一个删除费时间而烦恼吗？快来试试这款应用吧！

# 打包方法

1. 使用 Nuitka 打包为可执行文件
2. 运行以下命令打包为可执行文件：

```python
python -m nuitka --lto=no --onefile --standalone --windows-icon-from-ico=tool.ico  .\空文件夹扫描器.py
```

# 软件架构

基于python3.10.16（python3.x皆可）以及os,threading和datetime库编写

# 安装教程

1.  安装python3.x，运行 空文件夹删除器.py 文件
2.  输入想扫描的文件夹（如：D:\）,如何按回车键执行
3.  或者直接下载空文件夹删除器.exe双击运行

# 参与贡献

1.  [little_while](https://gitee.com/little_while)
1.  [xyx1926885268](https://github.com/xyx1926885268)
