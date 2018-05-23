# OS Ops 操作杂疑症状
> Linux等操作系统日常操作实在需要解决的问题太多了，在这里记录点滴再合适不过了。
其它Unix类（包括Mac中与此相关都）也都在这里。
与命令行学习有区分，这里只是针对Linux系统而言，即使有一些命令的运用但也只是针对某发行版或某种只在Linux上才会出现的问题


## Ubuntu循环登陆问题（包括各种基于Ubuntu的系统）

网上各种说权限问题等，实际上绝大多数问题，都是由误装、误删软件引起的。
而这其中，绝大多数是搜狗拼音或其他输入法相关的操作引起的。
重新安装fctix各种输入法即可， 瞬间解决。

```
sudo apt-get install fcitx-pinyin fcitx-sunpinyin fcitx-googlepinyin fcitx-anthy fcitx-mozc -y
```


## Ubuntu用dpkg安装搜狗拼音官方deb包导致问题

在搜狗拼音for linux官网上，下载deb包后正常`dpkg -i xx.deb`后，
基本上都会出现安装错误，尤其是elementaryOS等ubuntu based系统
这个时候非常尴尬，安装包无法删掉， 而且导致连apt-get大多数功能都无法用。
网上居多方法都没用。
才找到简单的方法：在试过正常删除后，删掉`sogoupinyin`相关一切文件就ok了

```
sudo rm -rf /var/lib/dpkg/info/sogou*
sudo apt-get -f install
sudo apt-get update
```


## Ubuntu中无法激活中文输入法问题

```shell
# 新建`.xprofile`文件并编辑
sudo vim /home/.xprofile
# 然后输入并保存
export LC_ALL=zh_CN.utf8 
export XMODIFIERS=@im=fcitx 
export QT_IM_MODULE=xim 
export GTK_IM_MODULE=xim 
fcitx -d
```


## 查看本地存储空间情况

### `$ df -h`就可以查看本地各处的存储情况了。下图是我的树莓派存储：
![image](https://user-images.githubusercontent.com/14041622/35480902-b5b50f3a-0453-11e8-892e-d1f9be0ee8d6.png)



# A quick note of Keyboard symbols

- `` ` ``, **Backticks** or **Back quote**
- `~`, **Tilde** sounds like "Till da"
- `!`, **Exclaimation mark**
- `^`, **Caret**
- `*`, **Asterisk**
[More Details](https://user-images.githubusercontent.com/14041622/35766438-ab7f0fa6-0913-11e8-84a0-3f064dd87102.png)



# Mac 打字时连续按两下就会打出`.`句号的问题
这个功能是默认的，实际上很耽误事，尤其在编程时连续打4个空格时。
取消很简单，如下图：

![Add period with double-space](https://user-images.githubusercontent.com/14041622/35217554-abf43b1c-ffa6-11e7-9194-008c83bff8df.png)



# Mac: Automator自动化学习
> Mac上想要实现各种自动化，光靠Python是不够的，还需要很多系统底层的支持。其实如果不是企业级应用，而是小工具的话，反而直接使用Automator要快得很多。只要功能实现了就好嘛

## Automator特点
- 几乎没有什么官方文档和全面的教程，最好的方式是自己一个一个试，或看看别人的事例。
- 单纯的Automator是没有Conditional条件控制的，也就是没法if-then-else这样的流程控制，只能单线发展。如果需要条件控制、循环等，就只能用applescript写了。
- 基于Automator单线流程，每个item命令都只接受上一个item的输出作为自己的输入，然后把自己的输出作为下一个item的输入。没有选择接受什么样的内容和输出哪些内容的权利。
- Automator没有界面设计（不像VB），最多是一些自带的输入框、确认框等。
- 如果是创建的Application应用，那么就会生成.app的程序，可以像其他所有独立程序一样单独运行和设立快捷键。
- Workflow等文件，只能保存到`~/Library/Services/`中，不能选择位置。

## 将shell script输出弹出为系统通知
![image](https://user-images.githubusercontent.com/14041622/36493790-627f613c-176b-11e8-9e24-f917d90eaf01.png)

## 获取剪切板文字，保存到变量，并弹出通知显示
![image](https://user-images.githubusercontent.com/14041622/36493996-d972e444-176b-11e8-96f0-e236b61d202e.png)



# Mac为某app应用设置icon图标
> 适用于所有Mac app，包括Automator做出来的。

[参考文章](https://apple.stackexchange.com/questions/369/can-i-change-the-application-icon-of-an-automator-script)

就是右键点某个app的`get info`，然后在它的icon上点一下，再`ctrl+c`复制，然后再到目标app的`get info`中的图标上点一下，再用`ctrl+v`粘贴，完成！


# Applescript 学习
> 之前说到了Automator的局限性，仅限于单一流程简单操作，完全没有条件控制、循环和错误控制等。所以如果希望加入一些控制，那就要掌握applescript。这也是一个很有意思的领域，稍有编程基础的话大概看几眼就能掌握，就算不懂的话大概一天之内就能学明白。

## Applescript特点
- 语法偏原生英语，简单好理解
- 支持对象、函数、条件控制、循环、错误控制等
- 能够操作大量系统底层API，可以运用自如
- 可以直接在Sublime Text里面编辑和运行（需要安装插件）
- 可以直接生成.app应用程序

## 常用语句
### 显示对话框
```applescript
tell current application
    display dialog "Hello World."
end tell
```

### 设置变量
```applescript
set str to "MacOS"
tell current application
    display dialog "Hello " & str
end tell
```

### 清空回收站
```applescript
tell application "Finder"
    empty the trash
end tell
```

### 显示通知框
```applescript
display notification "All graphics have been converted." with title "My Graphic Processing Script" subtitle "Processing is complete." sound name "Frog"
```

### 朗读文字
```applescript
say "Sheet sheel bore"

say "Just what do you think you're doing Dave?" using "Alex" speaking rate 140 pitch 42 modulation 60
```

### 显示剪切板文字
```applescript
display dialog (the clipboard)
```

### 运行shell脚本
```applescript
do shell script "ls -la"
```


# 从Terminal终端运行Applescript脚本
Mac上原生安装了`osascript`这个命令行工具，可以直接运行一句applescript脚本，或者执行一个脚本文件。

- 运行一句脚本：
```shell
osascript -e 'display dialog "hello world" '
```
- 运行脚本文件：
```shell
osascript PATH-TO-SCRIPT.scpt
```