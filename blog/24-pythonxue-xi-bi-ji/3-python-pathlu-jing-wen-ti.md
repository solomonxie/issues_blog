# ❖ Python path路径问题

> 看似是个小问题，但是在python里实际上是个非常容易被混淆的东西。

## `路径解析`
路径解析就是你拿出一个包含路径文字的str字符串，然后把它的每一部分都拆分解析出来，包括文件名，扩展名，文件夹名和文件夹路径等。

### 文件名
```py
>>> s = '/Users/me/movie/abc.mp4'
>>> os.path.basename(s)
'abc.mp4'
```


### 文件名（不含扩展名）
```py
>>> s = '/Users/me/movie/abc.mp4'
>>> os.path.basename(os.path.splitext(s)[0])
'abc'
```

### 目录名
```py
>>> s = '/Users/me/movie/'
>>> os.path.basename(os.path.realpath(s))
'movie'
```
为什么要这么写？看看下面实验就知道：
![image](https://user-images.githubusercontent.com/14041622/40163558-b548fa8e-59e9-11e8-8c07-41462fefc9a5.png)

## 获取系统相关路径

获取当前系统用户文件夹(Home Directory)：
```py
# 也就是解析命令行里`~`指向的地址
path = os.path.expanduser("~")

# 延伸：
path = os.path.expanduser('~/.tmux')
```

## 获取当前脚本相关路径
获取当前脚本的所有相关位置。

[参考文章](https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory-with-python)。

需要`import os`和`import sys`
- 当前工作区: `os.getcwd()`，注意，这不是脚本的位置，而是命令行中的工作区位置。
比如当你在`~/A/`执行`~/B/`文件夹中的一个python代码，那么返回的是`~/A/`，因为命令行中的工作区在`~/A/`.
- 当前文件名：`sys.argv[0]`或`__file__`，注意，两个变量都不稳定。__file__这个默认变量在一些环境下是没有被定义的，sys.argv[0]有时是完整路径有时只是一个文件名，所以，慎用。最好都配合os.path的各种方法运用。
所以正确方法是：`os.path.basename(sys.argv[0])`
- 当前文件完整路径：`os.path.realpath(sys.argv[0])`
- 当前文件所在文件夹：`os.path.dirname(os.path.realpath(sys.argv[0]))`
- 当前脚本完整路径：`os.path.split(os.path.realpath(__file__))[0]`
- 当前脚本父级目录：`os.path.dirname( os.path.split(os.path.realpath(__file__))[0] )`
- 当前脚本的父父级目录：`os.path.dirname( os.path.dirname(....) )`
