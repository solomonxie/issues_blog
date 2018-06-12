# Linux 命令行终端操作积累
## 积累终端命令行相关经验，包括Shell中的bash,zsh，终端中的Terminal, Mac Terminal.app,iTerm等

注意：这里说linux，linux之类的，其实在mac中也ok。只不过说起来和搜索起来方便而已。





## 命令行添加文字颜色
> 不是终端的颜色主题，只加了颜色主题但是文字还是同样颜色，其实没什么用。主要就是要类似于语法高亮的功能，要不然命令行里源源不断的一页一页的字冒出来实在不好读。

### 方案一：直接添加Terminal的配置文件
Mac中和Linux是一样的，直接在本用户的根目录添加一个`.bash_profile`文件写入配置，打开颜色开关即可。
```shell
$ vi ~/.bash_profile
export CLICOLOR=1
```
但是效果不佳，开关顶多加上了`ls`文件夹的颜色，没什么大用。如图：
![image](https://user-images.githubusercontent.com/14041622/35258738-783302ae-003c-11e8-9443-f65288c59c7c.png)
所以就需要再进一步找一个靠谱的解决方案。


## Bash shell / Zsh 里修改前缀 (隐藏用户@主机，添加Git分支名称)
> 每次在命令行里进入有git的文件夹，都没什么显示，不像网上其他人截屏出来的样子，就好奇怎么弄的。下面分bash和zsh两种方式分别来说。
`注：`这里都是使用的Mac Terminal.app做实验，Mac的iTerm或Linux上的终端没有做实验，但是操作不会有太大差异。

### 1. Bash的修改方法
其实特简单，还是在`~/.bash_profile`文件中添加：
```shell
$ vim ~/.bash_profile

# Shows Git branch name in prompt.
parse_git_branch() {
  git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/ (\1)/'
}
export PS1="\u@\h \W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "
# Or hide User @ Name (still with git branch name)
# export PS1="\W\[\033[32m\]\$(parse_git_branch)\[\033[00m\] $ "
```
效果如下：
![image](https://user-images.githubusercontent.com/14041622/35312980-08149de4-00f9-11e8-8eee-cf6f955f6957.png)

### 2. Zsh的修改方法
类似于Bash，在`~/.zshrc`这个文件中修改，打开后，随便找个位置（最好靠上面一点方便查看）加上一行`DEFAULT_USER=$USER `即可。如果为zsh安装了`Oh my zsh`这个工具（一般玩zsh第一步就是安装它），这里就不需要单独处理像Bash一样手动编程添加Git名称了，因为会自动出现。进入zsh后，可以看到效果如下：
![image](https://user-images.githubusercontent.com/14041622/35313348-c698b510-00fa-11e8-86ad-b6c81ddd8d8c.png)

当然，我这里的Git分支还配上了图标和颜色等，这都需要给终端（这里是Mac Terminal.app)安装相应配色方案，我用的是著名的`Solarized Dark`配色方案。具体配色和字体问题（字体用来支持图标，因为那些图标的本质是文字），需要专开一篇来说。

## Zsh中将全路径缩短为当前文件夹名
有时候经常嫌一层一层目录实在太长太占地方，而且截屏时也不方便把全路径显示出来。所以需要隐藏起来会比较方便，需要看全路径的话一句`pwd`就显示了。
默认全路径显示：
![image](https://user-images.githubusercontent.com/14041622/36319855-3ce060c4-137f-11e8-9a8c-f5a348663074.png)

修改后效果：
![snip20180217_106](https://user-images.githubusercontent.com/14041622/36319878-52602c72-137f-11e8-915e-b7dcc1f18db0.png)

Zsh中，配置文件`~/.zshrc`里面可以配置`DEFAULT_USER=$USER`来隐藏用户名和主机名，下面还有一句`prompt_context() {}`设定一般来说是可以写入函数来隐藏全路径并只显示当前文件夹的。
但是配置了agnoster配色主题后，怎么修改好像都没用，参考[这篇文章](http://bugcode.net/2016/05/03/zsh-iTerm2%E6%8A%98%E8%85%BE%E8%AE%B0%E5%BD%95/)，得知，只要到agnoster配色主题的配置文件中改一个字即可：
找到文件：一般是在这个位置`~/.oh-my-zsh/themes/agnoster.zsh-theme`，打开后找到`prompt_dir() {}`这个函数，然后将`prompt_segment blue black '%~'`最后面的~改为c即可：`prompt_segment blue black '%c'`。
![image](https://user-images.githubusercontent.com/14041622/36319801-1340a8b4-137f-11e8-8054-bc8ab90d0812.png)



## 安装并配置zsh
> `zsh`原称为**Z Shell**。也是一种shell，兼容最常用的bash这种shell的命令和操作，并且有很多增强，超强的订制性。查来查去，bash虽然很标准，但是自己日常的话还是不要太偏执，力求简单方便的工具更好，所以就玩弄起了zsh。超漂亮又简单,也很好上手。

Mac原生就安装了zsh，linux的话需要安装一下，简单如`sudo apt-get install zsh`这样就安装好了。
可以先通过`cat /etc/shells`查看自己有哪些shell，一般都会有很多种。
使用方法很简单，直接在命令行里输入`zsh`就开始使用了。不过要变成每次打开终端默认使用zsh，则需要改配置。
### 安装`Oh My Zsh`
原本zsh就是很强大，但是配置超难，直到**Oh my zsh**工具出现，一切zsh的配置都变简单了。所以这是用zsh的必备工具，安装只需一句话：
```shell
sudo  curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh 
```
屏幕显示这个图，就算安装好了：
![image](https://user-images.githubusercontent.com/14041622/35263685-c564c77a-0054-11e8-9152-81b2071c28f5.png)
然后再打开终端，感觉一切都变了：直接进入zsh，命令行前一大串的用户名主机等都被隐藏了，进入git文件夹时前面也都加上了`git (master)`这样的带颜色分支字样，按Tab自动补全时也不用区分大小写了(太棒了)。。。如下图
![image](https://user-images.githubusercontent.com/14041622/35263813-3cbde8a6-0055-11e8-9437-da2506352be4.png)

有一点需要注意，安装完oh my zsh后，机子(Mac)上的Terminal会变成默认打开就进入zsh。如果不习惯的话，可以改回默认先。Mac的Terminal在设置里将`shell open with`改成`/bin/bash`就好了：
![image](https://user-images.githubusercontent.com/14041622/35265450-16b0e4a0-005b-11e8-9839-5a15c4eba114.png)


## Mac终端配色方案 Color schemes

要想配置出这种好看的方案，标配就是：`zsh` + `Meslo字体` + `Soloarized Dark显示方案` + `Agnoster配色方案`。网上有很多文章介绍，不过这里也简单总结个cheatsheet方便以后用。
注：之前已经写了zsh和基本工具`oh my zsh`的安装方法了。后面都是在此基础上。
![image](https://user-images.githubusercontent.com/14041622/35314446-2b49018a-0101-11e8-94bd-2f0d06322cbe.png)

### 1. 安装Solarized显示方案 (仅用于本地客户端应用)
显示方案主要负责修饰命令行前缀，隐藏user@host，识别git文件夹，添加图标，命令高亮等。
去`Solarized`官网下载一个[zip压缩包](http://ethanschoonover.com/solarized/files/solarized.zip)。压缩包中包含了这种颜色方案应用在各种各样平台、终端、软件的配置文件。找到自己用的终端文件夹。如我用的是Mac Terminal，那么就在`osx-terminal.app-colors-solarized`这个文件夹，将里面的`Solarized Dark ansi.terminal`文件导入到终端。如下图：
![image](https://user-images.githubusercontent.com/14041622/35315201-f8f593ec-0105-11e8-9a9b-1b67b9385cbd.png)
![image](https://user-images.githubusercontent.com/14041622/35315223-171b34b2-0106-11e8-9c7d-4c0e3f4a3895.png)
在终端的配置里导入配色方案后，就出现了`Solarized Dark`选项，将其设为默认，重新打开终端，就出现基本的配色方案了。

### 2. 安装字体 （仅用于本地客户端应用）
Solarized配色包需要`Meslo LG M Regular for Powerline`这种字体才能显示各种特殊字符（图标），下载好ttf字体文件并安装。下载链接在这里[https://github.com/powerline/fonts/raw/master/Meslo%20Slashed/Meslo%20LG%20M%20Regular%20for%20Powerline.ttf](https://github.com/powerline/fonts/raw/master/Meslo%20Slashed/Meslo%20LG%20M%20Regular%20for%20Powerline.ttf)
装好以后，可以在终端中输入这个来测试是否成功：
```echo "\ue0b0 \u00b1 \ue0a0 \u27a6 \u2718 \u26a1 \u2699"```
如果能正常显示所有图标，则安装成功。
然后打开终端的偏好设置，在当前`Solarized`的配色方案下，找到字体选项，选择`Meslo LG M Regular for Powerline`字体，成功。
![image](https://user-images.githubusercontent.com/14041622/35315371-0582e28a-0107-11e8-8336-b2d2c7e8c75b.png)

### 3. 设定Agnoster配色主题
不同于如Solarized显示方案，配色主题单纯负责颜色问题。
这个需要在Zsh配置文件`~/.zshrc`中配置，由于`agnoster`是Oh My Zsh工具自带，所以无需安装额外文件直接修改选项。
找到`~/.zshrc`文件，将`ZSH_THEME`变量改成`agnoster`，保存并重新打开终端即可。如下图：
![image](https://user-images.githubusercontent.com/14041622/35315665-9ef20526-0108-11e8-9726-c4d38fbd37c7.png)

最后，我在Mac终端上显示效果如下：
![image](https://user-images.githubusercontent.com/14041622/35315432-55a881c0-0107-11e8-93ed-0a179044f1aa.png)
好像颜色哪里差了点，是因为它原生在iTerm终端才能发挥完全效果。效果如下：
![image](https://user-images.githubusercontent.com/14041622/35315453-74bad900-0107-11e8-858a-eeb45c980857.png)

iTerm的配置方法和Terminal.app非常相似，自己在偏好设置中采用类似的操作即可。
关于其它Oh My Zsh自带的色彩主题，可以到这里看效果：
[https://github.com/robbyrussell/oh-my-zsh/wiki/Themes](https://github.com/robbyrussell/oh-my-zsh/wiki/Themes)


## 终端里添加快捷路径
> 一般要一路cd进入五层以上的目录，是真的有点头疼。所以研究了下有没有设置快捷路径的方法

1. 方法一：设置系统变量
通过在`~/.bash_profile`或`~/.zshrc`里面设置`export DIR="/path/path/path"'这种来设置变量，然后引用是通过`$var`来引用。
但是每次都加`$`确实有点不爽，好像也没达到什么特别快捷的方法。
2. 方法二：alias
直接设置`alias topath="cd /path/path/path"`这种来设置别名，每次在终端直接输入类似topath，回车即可。这种方式是可取的。
为了保证可管理性，建议所有的alias别名都放到`~/.bash_profile`这种用户自定义的终端配置文件里，方便以后备份移植。


# Zsh 常用插件
> zsh有了各种插件后才真是如虎添翼，各种命令高亮，自动补全，命令参数辅助等。

## zsh插件安装方法
各种插件的安装方法各异，有的直接将插件文件夹拷贝到`~/.oh-my-zsh/custom/plugins`目录中，然后在`~/.zshrc`中的`plugins`数组中加入插件名即可；有的则需要配合别的工具并在`~/.zshrc`中加入别的命令。以下是几个常用的。
安装时经常会看到一些`$ZSH_xx`变量，这些都是zsh或oh my zsh设置的各种变量，便于插件运用。我们安装插件时也可以用这些变量安装，如插件保存的位置一般为`$ZSH_CUSTOM/plugins/插件文件夹名/`。



## `Oh my zsh自带插件`
自带插件在安装时就已经存在了，默认是只开启了git一个插件。其它的话也很简单，只需要在`~/.zshrc`文件中添加引用即可。打开文件找到`plugins`数组，然后把插件名加入数组即算开启。
如下图：
![image](https://user-images.githubusercontent.com/14041622/35327373-6c0bd3fe-0134-11e8-832c-3a7bab28e17f.png)

目前已经有的自带插件在官网Github中可以看到，[https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins](https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins)。
凡是这里有的，都可以立刻生效。



## Zsh命令自动补全插件 [zsh-autosuggestions](https://github.com/zsh-users/zsh-autosuggestions)
这里利用Oh my zsh的方法安装。直接一句话命令行里下载并移动到oh my zsh目录中：
```shell
git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
```
然后在`~/.zshrc`文件中找到plugins数组，加入`zsh-autosuggestions`名字，重新打开终端即可。



## Zsh命令语法高亮插件 [zsh-syntax-highlighting](https://github.com/zsh-users/zsh-syntax-highlighting)
将插件下载到oh my zsh的插件目录下的该新建插件同名文件夹中
```shell
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
```
编辑`~/.zshrc`文件将然后将插件引用命令写入该文件最后一行（必须）
```
# Note the source command must be at the end of .zshrc
source "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh"
```
保存重新打开即可看到高亮的命令行了。


## Zsh自动跳转目录插件 [autojump](https://github.com/wting/autojump)

安装方法：
```shell
brew install autojump

# 未完待续...
```


### 终端里用Sublime Text或其他应用程序打开文件
Mac下的Sublime Text的位置是`/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl`
所以我们直接用alias别名引用它就好了。
Bash的话在`~/.bash_profile`里，zsh的话在`~/.zshrc`里，直接加入这句话：
```
alias subl="/Applications/Sublime\ Text.app/Contents/SharedSupport/bin/subl"
```
然后就可以直接命令行里打开编辑器了：
```
subl ~/readme.txt
```
执行后会弹出Sublime Text编辑器，并打开readme.txt文件。

**同理，换成其它编辑器，或在其它系统里，也是这样修改流程**



## ffmpeg 超强视频处理程序
> 开源视频处理几乎必用的一个程序，功能强大。

## Installation

```
# for Ubuntu 14.04 (no need to install on 15.04)
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install ffmpeg -y
```

## 以最低CPU优先率执行命令

```
nice -19 ffmpeg 各种参数
```

## .webm to .mp4

```
nice -19 ffmpeg -i input.webm -c:v libx264 -crf 20 -c:a aac -strict experimental out.mp4
```

## Split Video

```
# 不转码截取片段（）
nice -19 ffmpeg -i "input.mp4" -ss 00:03:25 -to 00:05:42 -c copy "output.mp4"
```

## 调整音频与视频匹配不上的问题

### 方法1

```
nice -19 ffmpeg -i "input.mp4" -itsoffset 2.0 -i "input.mp4" -vcodec copy -acodec copy -map 0:0 -map 1:1 "output.mp4"
```

### 方法2: 一开始就分开截取音频视频 然后再合并

```
# ...
```

ffmpeg的参数顺序很重要, 不同的顺序造成截然不同的结果

## 切割视频

```
# 从指定开始点到指定结束点
ffmpeg -i 文件名 -ss 01:00:00 -t 00:06:00  -vcodec copy -acodec copy 输出文件名
ffmpeg -i 文件名 -ss 00:01:00 -to 00:02:00 -c copy 输出文件名
# 从指定开始点到指定时长
ffmpeg -ss 00:01:00 -i 文件名 -to 00:02:00 -c copy 输出文件名
# 调整音频匹配不上的问题 #方法1
ffmpeg -i "test.mp4" -itsoffset 2.0 -i "test.mp4" -vcodec copy -acodec copy -map 0:0 -map 1:1 "new.mp4"

# 调整音频匹配不上的问题 #方法2: 一开始就分开截取音频视频 然后再合并
# 
```


## cd命令常用技巧
- `cd ~`  进入用户主目录，`cd 空格`也行；
- `cd -`  返回进前一个所在目录；
- `cd ..`  返回上级目录；
- `cd ../..`  返回上两级目录；
- `cd !$`  把上个命令的参数作为cd参数使用


## rm 删除文件和文件夹
- `rm 文件名`删除文件
- `rm -rf 文件夹` 删除文件夹及其内所有文件


# 修改终端默认的shell
之前说过了，一般终端的默认Shell只要在终端应用如Terminal.app,iTerm2等的系统设置里直接改就好了。
但是如果我们要用ssh登录服务器就不能这么设置了，需要用到`chsh`这个命令。很简单
如果不懂的话，直接 `man chsh`就可以看到很简单的描述--改变登录shell。
首先要查到当前机器有哪些以安装的shell，`cat /etc/shells`。
![image](https://user-images.githubusercontent.com/14041622/35557228-749dbabe-05df-11e8-94a5-1311fcb87c62.png)
我的默认有这些，可以看到zsh位于`/bin/zsh`，那么如果想要将zsh改为默认，就直接在终端里输入：
```
chsh -s /bin/zsh
```
即可达到修改默认终端的效果。如果是ssh连接服务器的话，需要重连才能看到效果。


## Mac在终端上的快捷键
> 一开始是为了找翻屏（上下滚动）的快捷键，Windows和Linux上一般PageUp, PageDown即可，Macbook上没有这两个键，所以还挺难找的。后来查了一系列其它的终端快捷键，如下：

- `Cmd+Up` 向上滚动
- `Cmd+Dn` 向下滚动
- `Fn+Left` 和`Ctrl+A`一样，移到命令行最左端
- `Fn+Right` 和 `Ctrl+E`一样，移动的命令行最右端
- `Ctrl+U` 删除当前命令行
- `Ctrl+K` 删除当前光标后的所有内容


## Bash里读取Json数据
查看Stackovervlow, 发现[答案](https://stackoverflow.com/questions/1955505/parsing-json-with-unix-tools)，既可以使用`sed+awk`来自己写解析读取json，也可以通过引用python方法来更方便的解析。推荐python方法，如下：
```bash
echo '{"hostname":"test","domainname":"example.com"}' | python -c 'import json,sys;obj=json.load(sys.stdin);print obj[0]["hostname"]'
```
由于*nix都原生带有python，所以这么执行是没问题的。而且一般也不用考虑到执行速度问题。


# Bash键盘快捷键
[参考菜鸟教程](http://www.runoob.com/w3cnote/bash-shortcut.html)


快捷键 | 快捷键说明
-- | --
OOOOO | OOOOO
CTRL-A | 将光标移到行首（在命令行下）
CTRL-B | 退格 (非破坏性的)，这个只是将光标位置往回移动一个位置。
CTRL-C | 中断，终结一个前台作业。
CTRL-D | “EOF” (文件结尾：end of file)。它用于表示标准输入（stdin）的结束。在控制台或xterm 窗口输入文本时，CTRL-D 删除在光标下的字符。从一个shell中退出 (类似于exit)。如果没有字符存在，CTRL-D 则会登出该会话。在一个xterm窗口中，则会产生关闭此窗口的效果。
CTRL-E | 将光标移动到行尾（在命令行下）
CTRL-F | 将光标向前移动一个字符（在命令行下）
CTRL-G | BEL。在一些老式打印机终端上，这会引发一个响铃。在xterm终端上可能是哔的一声。
CTRL-H | 擦除(Rubout)(破坏性的退格)。在光标往回移动的时候，同时擦除光标前的一个字符。
CTRL-I | 水平制表符。
CTRL-J | 新行(换行[line feed]并到行首)。在脚本中，也可能表示为八进制形式(‘/012′)或十六进制形式(‘/x0a’)。
CTRL-K | 垂直制表符(Vertical tab)。在控制台或 xterm 窗口输入文本时，CTRL-K会删除从光标所在处到行尾的所有字符。在脚本中，也可能表示为八进制形式(‘/013′)或十六进制形式(‘/x0b’)。
CTRL-L | 跳纸，换页(Formfeed)，清屏。清空终端屏幕。在终端上，这个命令的作用和clear命令一样。但当这个命令发送到打印机时，Ctrl-L会直接跳到纸张(Paper sheet)的末尾。
CTRL-M | 回车(Carriage return)。
CTRL-N | 擦除从history缓冲区召回的一行文本（在命令行下）。如果当前输入是历史记录中选择的时候，这个是从这个历史记录开始，每按一次，是更接近的一条命令。
CTRL-O | 产生一个新行（在命令行下）。
CTRL-P | 从history缓冲区召回上一次的命令（在命令行下）。此快捷键召回的顺序是由近及远的召回，即按一次，召回的是前一次的命令，再按一次，是召回上一次之前的命令，这和CTRL-N都是以当前的输入为起点，但是两个命令操作刚好相反，CTRL-N是从起点开始由远及近（如果起点是历史命令的话）。
CTRL-Q | Resume (XON)。恢复/解冻，这个命令是恢复终端的stdin用的，可参见CTRL-S。
CTRL-R | 回溯搜索(Backwards search)history缓冲区内的文本（在命令行下）。注意：按下之后，提示符会变成(reverse-i-search)”:输入的搜索内容出现在单引号内，同时冒号后面出现最近最匹配的历史命令。
CTRL-S | Suspend(XOFF)，挂起。这个是冻结终端的stdin。要恢复可以按CTRL-Q。
CTRL-T | 交换光标位置与光标的前一个位置的字符内容（在命令行下）。比如：echo $var;，假设光标在a上，那么，按下C-T之后，v和a将会交换位置：echo $avr;。
CTRL-U | 擦除从光标位置开始到行首的所有字符内容。在某些设置下，CTRL-U会不以光标位置为参考而删除整行的输入。
CTRL-V | 在输入文本的时候，按下C-V之后，可以插入控制字符。比如：echo -e '/x0a’;和echo <CTRL-V><CTRL-J>;这两种效果一样。这点功能在文本编辑器内非常有效。
CTRL-W | 当在控制台或一个xterm窗口敲入文本时, CTRL-W 会删除从在光标处往后（回）的第一个空白符之间的内容。在某些设置里, CTRL-W 删除光标往后（回）到第一个非文字和数字之间的字符。
CTRL-X | 在某些文字处理程序中，这个控制字符将会剪切高亮的文本并且将它复制到剪贴板中。
CTRL-Y | 将之前已经清除的文本粘贴回来（主要针对CTRL-U或CTRL-W）。
CTRL-Z | 暂停一个前台的作业；在某些文本处理程序中也作为替换操作；在MSDOS文件系统中作为EOF（End-of-file)字符。
CTRL-/ | 退出。和CTRL-C差不多，也可能dump一个”core”文件到你的工作目录下(这个文件可能对你没用)。
CTRL-/ | 撤消操作，Undo。
CTRL-_ | 撤消操作。
CTRL-xx | 在行首和光标两个位置间进行切换，此处是两个”x”字符。
ALT-B | 光标往回跳一个词，词以非字母为界(跳动到当前光标所在词的开头)。
ALT-F | 光标往前跳一个词(移动到光标所在词的末尾)。
ALT-D | 删除光标所在位置到光标所在词的结尾位置的所有内容(如果光标是在词开头，则删除整个词)。
ALT-BASKSPACE | 删除光标所在位置到词开头的所有内容。
ALT-C | 将光标所在位置的字母转为大写(如果光标在一个词的起始位置或之前，则词首字母大写)。
ALT-U | 将光标所在位置到词尾的所有字母转为大写。
ALT-L | 将光标位置到词尾的所有字母转为小写。
ALT-R | 取消所有变更，并将当前行恢复到在历史记录中的原始状态(前提是当前命令是从历史记录中来的，如果是手动输入，则会清空行)。
ALT-T | 当光标两侧都存在词的时候，交换光标两侧词的位置。如：abc <ALT-T>bcd -> bcd abc
ALT-. | 使用前一次命令的最后一个词(命令本身也是一个词，参见后一篇的Bang命令中的词指示符概念)。
ALT-_ | 同ALT-.。
ALT-数值 | 这个数值可以是正或者是负，这个键单独没有作用，必须后面再接其他内容，如果后面是字符，则表示重复次数。如：[ALT-10,k]则光标位置会插入10个k字符(负值在这种情况下无效)；如果后面接的是命令，则数字会影响后面命令的执行结果，如：[ALT--10,CTRL-D]则向CTRL-D默认方向相反(负数)的方向执行10次操作。
ALT-< | 移动到历史记录中的第一行命令。
ALT-> | 移动到历史的最后一行，即当前正在输入的行(没有输入的情况下为空)。
ALT-P | 从当前行开始向前搜索，有必要则向”上”移动，移动时，使用非增量搜索查找用户提供的字符串。
ALT-N | 从当前行开始向后搜索，如果有必要向”下”移动，移动时，使用非增量搜索查找用户提供的字符串。
ALT-CTRL-Y | 在标志点上插入前一个命令的第一个参数(一般是前一行的第二个词)。如果有参数n，则插入前一个命令的第n个词(前一行的词编号从0开始，见历史扩展)。负的参数将插入冲前一个命令的结尾开始的第n个词。参数n通过M-No.的方式传递，如：[ALT-0,ALT-CTRL-Y]插入前一个命令的第0个词(命令本身)。
ALT-Y | 轮询到删除环，并复制新的顶端文本。只能在yank[CTRL-Y]或者yank-pop[M-Y]之后使用这个命令。
ALT-? | 列出能够补全标志点前的条目。
ALT-* | 把能够补全[ALT-?]命令能生成的所有文本条目插入到标志点前。
ALT-/ | 试图对标志点前的文本进行文件名补全。[CTRL-X,/]把标志点前的文本当成文件名并列出可以补全的条目。
ALT-~ | 把标志点前的文本当成用户名并试图进行补全。[CTRL-X,~]列出可以作为用户名补全标志点前的条目。
ALT-$ | 把标志点前的文本当成Shell变量并试图进行补全。[CTRL-X,$]列出可以作为变量补全标志点前的条目。
ALT-@ | 把标志点前的文本当成主机名并试图进行补全。[CTRL-X,@]列出可以作为主机补全标志点前的条目。
ALT-! | 把标志点前的文本当成命令名并试图进行补全。进行命令名补全时会依次使用别名、保留字、Shell函数、shell内部命令，最后是可执行文件名。[CTRL-X,!]把标志点前的文本当成命令名并列出可补全的条目。
ALT-TAB | 把标志点前的文本与历史记录中的文本进行比较以寻找匹配的并试图进行补全。
ALT-{ | 进行文件名补全，把可以补全的条目列表放在大括号之间，让shell可以使用。











# Linux 创建多级目录 | 多层次文件夹
- `mkdir <folder>` 创建单层文件夹, 比如`mkdir ./src`。不能创建多层，不能重复创建
- `mkdir -p <path>` 创建多层次文件夹，可以重复创建同一个文件夹。如`mkdir -p ./src/s/e/w/asdf`


# 读取和写入剪切板数据
目前剪切板的操作原生支持还不是很完善，windows/mac/linux的工具都不一样，而且如果不是自己写脚本的话很难原生支持剪切板里的图片读取和写入。

## Mac 自带`pbcopy`和`pbpaste`
```shell
# 写入剪切板
$ echo 'hihihi' | pbcopy
#或
$ pbcopy < echo 'hello'

# 读取剪切板
$ pbpaste
# 保存剪切板内容到文件
$ pbpaste > ~/test.txt
```

# Mac处理剪切板图像
目前没有原生支持剪切板的文字之外的类型。所以必须要下载第三方应用。
## [`pngpaste`](https://github.com/jcsalterego/pngpaste) 最简单的剪切板图像转文件工具
mac上直接`brew install pngpaste`，完成后一句`pngpaste path-to-img.png`即可在指定位置生成图片文件。没有特别option选项，仅此一句。
经过测试，能支持截图软件、浏览器、mac图片预览等的右键点击copy得来的常用图像。
官方的图像类型支持说明：
Supported input formats are `PNG, PDF, GIF, TIF, JPEG`.
Supported output formats are `PNG, GIF, JPEG, TIFF`.
Output formats are determined by the provided filename extension, falling back to PNG.
It's unclear if EXIF data in JPEG sources are preserved. There's an issue with pasting into JPEG format from a GIF source.
但是：
- 不支持直接在文件上`ctrl+c`这样拷贝来的图片
- 不支持gif，实测

## `xclip`
原本是在linux常用的剪切板操控工具，后来可能流行起来在mac也支持了。但是mac上安装要麻烦点，必须要先安装依赖工具：`X11`即`XQuartz`，200M的安装文件，装完了还要重启mac电脑才行。不过为了剪切板的事，忍了。[安装地址在这](https://www.xquartz.org/)。下载好dmg文件安装就行了。
安装好后，用`brew install xclip`即可轻松装好。
但是！！！
装好才发现，xclip并没有和系统剪切板沟通，而只是在自己程序里的一些缓存。而且而且而且！每次在命令行里用xclip，还都会在桌面启动`XQuartz`这个app，还不会自动关闭。实在太不爽了这种设置。
另外，所有这些x开头的剪切板程序，都是建立在`X Windows`基础上的，即刚刚安装的XQuartz。[wiki这里有一个列表](https://en.wikipedia.org/wiki/X_Window_selection#Programs)，所有xsel、xclip等等都是这样的。。。
难道mac和linux的小小剪切板就这么难操作吗？


## 查看本地存储空间情况

### `$ df -h`就可以查看本地各处的存储情况了。下图是我的树莓派存储：
![image](https://user-images.githubusercontent.com/14041622/35480902-b5b50f3a-0453-11e8-892e-d1f9be0ee8d6.png)



# `scp`命令在服务器上传下载文件

```shell
#Copy a local file to a remote host:
scp path/to/local_file remote_host:path/to/remote_file

#Copy a file from a remote host to a local folder:
scp remote_host:path/to/remote_file path/to/local_dir

#Recursively copy the contents of a directory from a remote host to a local directory:
scp -r remote_host:path/to/remote_dir path/to/local_dir
```


# 命令行里打印日期
```shell
# 注意是反引号 因为是要执行date命令
echo `date`   

# 一个好用的技巧，快捷键commit
alias gc = "git add . && git commit -m \"`date`\" "
```


# Linux 定时任务 `crontab`
运行`crontab -e`后会自动跳进程序，在最底下一行写入执行命令，必须要按照格式写。
格式是`* * * * * 命令`，其中前五个星号分别代表着第几分钟、第几小时、每月第几日、哪个月、星期几。要按照顺序替换*为一个数字，如果保持*，则表示任意。
*还可以加运算符：
[参考文章](https://segmentfault.com/a/1190000007478002)

[在线Cron表达式生成工具。](http://xiongyingqi.com/cron-online/)

```
*:任何时间
/:每隔多久
-:连续时间
,:不连续的时间
```
[参考视频](https://www.youtube.com/watch?v=QZJ1drMQz1A)


```shell
# 每2分钟执行
*/2 * * * * echo "hello" >> ~/test.txt

# 每天执行
** 
```

## 动态修改Crontab
我们可以用Python或Shell脚本动态修改crontab：
```sh
# 先导出crontab设置
$ crontab > ./tasks.txt

# 输入新的crontab设置到文件中 (也可以直接修改txt文件)
$ echo '# some new command' >> ./tasks.txt

# 导入(覆盖)到crontab中
$ crontab ./tasks.txt
```

## `Crontab创建任务时报错：crontab: no crontab - using an empty one crontab: "/usr/bin/vi" exited with status 1`
![image](https://user-images.githubusercontent.com/14041622/39955127-aabdd0b2-55fc-11e8-9d13-d6b043df0708.png)

这个错误主要是没有在bash或zsh中指定文本编辑器的问题。
直接到`~/.bash_profile`或`~/.zshrc`文件中添加指定编辑器的语句即可：
```shell
export EDITOR=vim
```
退出后，重启Bash或者Zsh即可。


# Linux 设计系统时区和时间

把程序运行在树莓派上时，获取的时间默认是美国的，这样记录日志之类的东西也都是美国时间会容易混淆。所以需要在命令行里修改系统时区。

### 改时区
我们在`/usr/share/zoneinfo`这个文件夹里可以看到各种各样的国家和时区，找到自己的时区后拷贝到`/etc/localtime`即可改变时区

```shell
# 中国是ROC
sudo cp /usr/share/zoneinfo/ROC /etc/localtime

# 验证
date
```

### 改时间
一般其实不需要改时间，联网的话默认是从网上获取的。
如果要改，[参考这篇文章](https://www.garron.me/en/linux/set-time-date-timezone-ntp-linux-shell-gnome-command-line.html)


# `tail`命令实时监控某文件变化
> 一般我们在程序生成log日志时，会想到用`cat`去查看内容。但是要想在程序运行过程中实时查看内容的变化，cat就不够好了，总不能手动一遍一遍去查吧。`tail`命令就可以解决这个问题，它让你像看直播看文件内容。

![screencast 2018-02-16 23-18-15](https://user-images.githubusercontent.com/14041622/36314429-d0ef2634-136f-11e8-8a14-bcbd04594dfd.gif)

目前，






# `tmux`的超绝便利
> 上面提到服务器的任务不间断运行，就是利用了tmux的特性。就是说，一般ssh是断开就会停止所有之前连接ssh期间运行的所有processes，而tmux的核心业务不在于把屏幕分成几块好看，而是它能保存session！而且还能多端实时直播session！

了解tmux的安装和使用已经理解，这个[短视频](https://www.youtube.com/watch?v=BHhA_ZKjyxo)足矣！如果想试试tmux的session共享，让别的机器或别人像直播一样看你在命令行里打字、操作，也用tmux一句话即可，参考[这个视频](https://www.youtube.com/watch?v=norO25P7xHg)。

我万万没想到，将vim打造成IDE、将脚本不间断运行、让任务运行状态多处可观看的tmux，是这么简单。
一句`sudo apt-get install tmux`就安装好，一句`tmux`就开启，一句`tmux new -s <session-name>`就可以创建和保存session。超绝！

[常用操作快捷键参考。](https://gist.github.com/ryerh/14b7c24dfd623ef8edc7#%E5%90%8C%E6%AD%A5%E7%AA%97%E6%A0%BC)

## Tmux常用命令参考

```shell
#启动新会话：
tmux [new -s 会话名 -n 窗口名]

#恢复会话：
tmux at [-t 会话名]

#列出所有会话：
tmux ls

#关闭会话：
tmux kill-session -t 会话名

#关闭所有会话：
tmux ls | grep : | cut -d. -f1 | awk '{print substr($1, 0, length($1)-1)}' | xargs kill
```

## Tmux 常用内部命令
> 所谓`内部命令`，就是进入Tmux后的指令。在按下`前缀键`后的命令，一般前缀键为`Ctrl+b`.

```vim
#会话
:new<回车>  启动新会话
s           列出所有会话
$           重命名当前会话

#窗口
c  创建新窗口
w  列出所有窗口
n  后一个窗口
p  前一个窗口
f  查找窗口
,  重命名当前窗口
&  关闭当前窗口

#窗格（分割窗口）
%  垂直分割
"  水平分割
o  交换窗格
x  关闭窗格
⍽  左边这个符号代表空格键 - 切换布局
q 显示每个窗格是第几个，当数字出现的时候按数字几就选中第几个窗格
{ 与上一个窗格交换位置
} 与下一个窗格交换位置
z 切换窗格最大化/最小化

#调整窗口排序
swap-window -s 3 -t 1  交换 3 号和 1 号窗口
swap-window -t 1       交换当前和 1 号窗口
move-window -t 1       移动当前窗口到 1 号

#同步窗格 
#这么做可以切换到想要的窗口，输入 Tmux 前缀和一个冒号呼出命令提示行，然后输入：
:setw synchronize-panes

#调整窗格尺寸
#如果你不喜欢默认布局，可以重调窗格的尺寸。虽然这很容易实现，但一般不需要这么干。这几个命令用来调整窗格：
PREFIX : resize-pane -D          当前窗格向下扩大 1 格
PREFIX : resize-pane -U          当前窗格向上扩大 1 格
PREFIX : resize-pane -L          当前窗格向左扩大 1 格
PREFIX : resize-pane -R          当前窗格向右扩大 1 格
PREFIX : resize-pane -D 20       当前窗格向下扩大 20 格
PREFIX : resize-pane -t 2 -L 20  编号为 2 的窗格向左扩大 20 格
```

## Tmux无法持久保存session问题
它虽然好用，但是缺点是关机的话session就全都消失了。要解决这点，需要安装单独的插件。
这个时候你就需要`Tmux-Resurrect`插件来了，[地址在这](https://github.com/tmux-plugins/tmux-resurrect)。
插件说明里很清楚的写了，tmux一旦关机，就会失去一切的设置。所以还必须用插件来解决。
安装方法：

## Tmux安装[插件管理器TPM](https://github.com/tmux-plugins/tpm)
和vim一样的思路，需要先安装tmux专属的插件管理器，一般都是用这个：`tmux plugin manager`，即tpm。注意：文档里面都会提到`prefix + ...`，其中`prefix`指的是tmux的命令前缀，默认是`ctrl+b`。

按照[官网](https://github.com/tmux-plugins/tpm)的做法，很简单就安装上了，输入下面命令：
```shell
# 把管理器文件安装到`~/.tmux/plugins/tpm`之下 此前这些目录是不存在的
git clone https://github.com/tmux-plugins/tpm ~/.tmux/plugins/tpm

# 新建配置文件
touch ~/.tmux.conf
vim ~/.tmux.conf

# 将下面内容复制到`~/.tmux.conf`
# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'
# Other examples:
# set -g @plugin 'github_username/plugin_name'
# set -g @plugin 'git@github.com/user/plugin'
# set -g @plugin 'git@bitbucket.com/user/plugin'
# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm' 

# 在tmux运行的时候，找到任意窗口输入下面这个完成安装管理器：
tmux source ~/.tmux.conf
```

## tmux安装插件
在tpm管理器基础上，我们直接到`~/.tmux.conf`文件里的`List of plugins`部分，写入插件名称，然后按`Ctrl+b`，再按`Ctrl+I`，这里面是大写的i。然后程序就会自动下载安装好插件了。

### 安装[`tmux-resurrect`](https://github.com/tmux-plugins/tmux-resurrect)插件
由于tmux不能持久保存session的特性，我们需要安装这个插件来将session的设置完全保存到本地，然后重启后也能够快速恢复窗口等设置的内容。
首先在`~/.tmux.conf`文件的`List of plugins`部分加入这句话：
```
set -g @plugin 'tmux-plugins/tmux-resurrect'
```
保存好后，在tmux的任意窗口按`ctrl+b`及大写的`I`，即可完成下载安装。

#### 用法
- `prefix + Ctrl-s` - 保存session
- `prefix + Ctrl-r` - 恢复session

## Tmux中的vim等软件颜色丢失
这是因为tmux默认TERM没有用256color，那么每次运行tmux时指定color即可,`TERM=screen-256color-bce tmux`，或者更简单一点，在`~/.bash.profile`或者`~/.zshrc`中设置别名：
```
alias tmux="TERM=screen-256color-bce tmux"
```
然后在`~/.tmux.conf`文件中加入这句话：
```
set -g default-terminal "xterm-256color"
```

## Tmux中鼠标滚屏不能用
tmux中鼠标滚屏默认是关闭的，且不是很容易像开关一样开启支持。
看过了一些stackoverflow尝试了一些解决方案，发现没有一个管用。如果比这个还麻烦，暂时我就觉得没有必要再折腾了，直接用原生的屏幕滚动浏览快捷键即可：
`Prefix + [`，然后直接用上下箭头，或者PnUp和PnDown即可

## `Tmux的配置文件`
配置文件默认位于`~/.tmux.conf`.
日常使用中，前缀键`Ctrl+b`和切换窗口键`Ctrl+o`等等，实在太麻烦了。所以改快捷键有时候是很必要的。
[参考这篇文档。](https://gist.github.com/ryerh/14b7c24dfd623ef8edc7#配置文件tmuxconf)

我的配置如下：
```vim
# 基础设置
#set -g default-terminal "screen-256color"
set -g default-terminal "xterm-256color"     # recover colorful terminal
set -g display-time 3000
set -g escape-time 0
set -g history-limit 65535
set -g base-index 1
set -g pane-base-index 1


# 前缀绑定 (Ctrl+a)
#set -g prefix ^a
#unbind ^b
#bind a send-prefix

# 启用鼠标(Tmux v2.1)
set -g mouse on

# 选中窗口
bind-key k select-pane -U
bind-key j select-pane -D
bind-key h select-pane -L
bind-key l select-pane -R

# copy-mode 将快捷键设置为 vi 模式
setw -g mode-keys vi

#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Tmux Plugin Manager(Tmux v2.1)
#== TMUX PLUGIN MANAGER ==#
# Tmux Resurrect
set -g @plugin 'tmux-plugins/tmux-resurrect'

# List of plugins
set -g @plugin 'tmux-plugins/tpm'
set -g @plugin 'tmux-plugins/tmux-sensible'

# Initialize TMUX plugin manager (keep this line at the very bottom of tmux.conf)
run '~/.tmux/plugins/tpm/tpm'
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
```


# 使服务器上的任务不间断运行
> 通过ssh登录服务器运行一个python脚本，想让它24小时不间断运行。可是一旦我退出ssh，整个程序就断了。这是由于ssh的session特性——它本身就是一个session，连接上开启session，断开ssh连接则关闭session，关闭时所有你在这个session里运行的东西都会被中断。

### 关于ssh关闭连接就关闭运行程序的问题，[在这里可以看到一些解决方案](https://askubuntu.com/questions/8653/how-to-keep-processes-running-after-ending-ssh-session)。

## 解决方案一：`tmux`

很幸运，在学习怎么把vim分屏浏览时知道了tmux，然后看视频时学到：原来ssh是这样的特性，断开就会停止所有之前连接ssh期间运行的所有processes，而tmux的核心业务不在于把屏幕分成几块好看，而是它能保存session！而且还能多端实时直播session！

### 解决方案二：`nohup`
网上一般说到不间断任务，一般也都会先提到这个，可以说是常规方案。

### 解决方案三：`screen`或`byobu`
这据说是现在更常用的方法，[参考文章](https://www.howtogeek.com/howto/ubuntu/keep-your-ssh-session-running-when-you-disconnect/)。

### 解决方案四：`disown`
据说的最简单方案：在命令后加`&`或者用`ctrl+z`把任务转到后台，然后用`disown -a`将任务解除与当前session的关联（意思就是当前session关闭也不影响它）


# Linux 标准输出(stdout)和标准错误(stderr)的重定向
> 以前经常会听到这些词，还有标准输入之类，完全不明所以。直到最近需要让python脚本里的print内容打印到日志文件里，才开始研究这到底是什么。


原来，`标准输出(stdout)`指的就是在命令行里，每次你输入指令后，终端上打印出来的那些话，那些反馈。`标准错误(stderr)`跟标准输出差不多，只不过是程序出错时反馈的内容。`标准输入(stdin)`就是程序指示让你输入用户名密码之类的这种，这里不多谈输入。

问题是，我们很常用的会让一些脚本自己在后台24/7运行，这种时候脚本的输出内容到屏幕上（标准输出）也没什么意义，我们看不到也保存不了。所以最好让它把反馈的内容全部直接写如一个文件里，我们叫日志文件，其实就是个txt。然后我们自己可以查看日志来看到底发生了什么。


#### 这种把显示到屏幕的程序反馈，变成存到文件里的动作，我们叫做`输出重定向(stdout redirection)`

在命令行里，我们可以用符号直接把程序输出`转向`到某个文件或某个程序，如下：
```shell
$ git push > log.txt
```
然后，理论上我们平常`git push`后的反馈就会保存到`log.txt`这个文件里了，且屏幕上不会显示任何东西。
但其实这个还是有问题的，因为事后我们发现有一些存到了log.txt，还有一些话漏网显示到了屏幕上，没存进去文档里。
其实原来这些显示到屏幕上的反馈有些是`stdout`有些是`stderr`，我们用`>`或`>>`符号重定向，只是默认重定向`stdout`，没有重定向`stderr`，所以会有漏网之鱼。对此，我们需要了解下这个符号的设定，和怎么把`stderr`也包括进来，一起重定向过去。

## 重定向符号和语句
稍微会一点点linux命令的，都会用到`cmd > file`这样的语句，把命令反馈的输出到一个文件里。当然还有`cmd >> file`，这是把内容追加到文件里，而不是重新擦写一遍。`>`这个符号可以念`redirect to`。
实际上，重定向有很多种设置和配合，让你可以分别重定向标准输出和标准错误，或者一起重定向，然后还可以选择是只输出到文件里还是同时输出大显示屏上和文件里。
这里我们就要了解一下设置重定向的基本语法了，如下：

- `>`   以擦写的模式重定向至... 
- `>>` 以追加的模式重定向至...
- `1`  代表`stdout`标准输出
- `2` 代表`stderr`标准错误

所以，`cmd > file`实际上是缩略了的写法，理解起来，应该是`cmd &1> file`，也就是只把标准输出转出去。
那么同理，只把标准错误转出去，就应该是`cmd &2> file`。
其中，`&`符号没任何实际意义，只是以至区分，代表后面的符号是要设置重定向用的，而不是某个文件的名字。

## `2>&1`
每次查重定向问题时，我们总会看到这句话，一般人很难理解这到底是在干嘛。我一开始以为是2要大于1什么的，真是笑话。
其实这是个重定向的设置，设置让2重定向到1，也就是让`stderr`标准错误重定向到`stdout`标准输出，然后两个并在一起再重定向。其中`&`没什么意思只是区分开来1是代表`stdout`而不是代表一个文件名。
用起来的格式是：`cmd > file 2>&1`。
为什么设置要放在后面呢?
具体暂时还不知道，只知道是这么用，放在前面还不行只能放在后面。

比如：
```shell
$ git push > log.txt 2>&1
```
那么这时候，屏幕上就真的不会显示任何东西了，标准输出、标准错误，全部都会存到log.txt文件里了。

## 常用重定向及解释

#### 参考文章：[stackoverflow回答](https://askubuntu.com/questions/420981/how-do-i-save-terminal-output-to-a-file)

![image](https://user-images.githubusercontent.com/14041622/36338289-cdaec1d4-13e5-11e8-98e0-1181c1510bf8.png)

- `command > output.txt`

The standard output stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, it gets overwritten.

- `command >> output.txt`

The standard output stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

- `command 2> output.txt`

The standard error stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, it gets overwritten.

- `command 2>> output.txt`

The standard error stream will be redirected to the file only, it will not be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

- `command &> output.txt`

Both the standard output and standard error stream will be redirected to the file only, nothing will be visible in the terminal. If the file already exists, it gets overwritten.

- `command &>> output.txt`

Both the standard output and standard error stream will be redirected to the file only, nothing will be visible in the terminal. If the file already exists, the new data will get appended to the end of the file..

- `command | tee output.txt`

The standard output stream will be copied to the file, it will still be visible in the terminal. If the file already exists, it gets overwritten.

- `command | tee -a output.txt`

The standard output stream will be copied to the file, it will still be visible in the terminal. If the file already exists, the new data will get appended to the end of the file.

- `(*)`

Bash has no shorthand syntax that allows piping only StdErr to a second command, which would be needed here in combination with tee again to complete the table. If you really need something like that, please look at "How to pipe stderr, and not stdout?" on Stack Overflow for some ways how this can be done e.g. by swapping streams or using process substitution.

- `command |& tee output.txt`

Both the standard output and standard error streams will be copied to the file while still being visible in the terminal. If the file already exists, it gets overwritten.

- `command |& tee -a output.txt`

Both the standard output and standard error streams will be copied to the file while still being visible in the terminal. If the file already exists, the new data will get appended to the end of the file.



# Linux生成随机数
`echo $RANDOM`即可生成一个5位数的随机数。


# 进入`docker`的世界
> 最近学习Machine Learning发现好多人都用docker，之前一直听说但是感觉和自己无关。但是现在发现原来docker是个这么方便的东西，可以跨平台（不分什么版本的linux，甚至mac和windows也行）运行。所以这里开一篇来记录学习感谢。


# Linux查看文件及文件夹大小
```sh
# 查看某目录或文件的大小(目录的话默认显示里面所有文件的大小)
$ du <file-or-folder>

# 只查看某文件夹自身的总大小("-d  0"代表max depth为0)
$ du -d 0 <folder>

# 指定size单位查看（如k, M, G等）
$ du -d 0 -h <folder>
```


# Linux说明书/手册 `man page`
> 实际上不需要各种cheatsheet，Linux上自带就有手册，`man page`。

`man page`其实就是Manual Page的意思，使用方法是`man 命令`，然后就会显示某个命令的所有官方说明和用法。这个是基础中的基础。
![image](https://user-images.githubusercontent.com/14041622/36626847-13f5c8f6-1975-11e8-904a-18d37b87fbe5.png)


但是苦于Man Page和历史上所有的说明书一样，实在是太官方太枯燥了，所以我们可以看到一些衍生品：

## `TLDR`
`TL;DR`的意思是Too long; Dont' read. 这个词在写文章时代表接下来要出现一个很长的内容了，但是在Linux中其实代表着相反的意思：把大长篇的说明简化为两三句话，直入重点展示命令的用法。
![image](https://user-images.githubusercontent.com/14041622/36626831-d16d75ba-1974-11e8-88e5-8965920b57e2.png)

`tldr`是Linux命令行工具，[官网在此](https://github.com/tldr-pages/tldr/)。安装方式如下：
```
# Mac
brew install tldr

# Linux
sudo pip install tldr
```
注意：各种设备、平台上的安装方法都不同，请到官网看详情。

## [`bropage`](http://bropages.org/)
相当与`tldr`的社区版，即社区可以贡献每种命令的使用事例，然后通过投票方式排名。所以bropage每次执行都是需要联网查询的。
![image](https://user-images.githubusercontent.com/14041622/36626839-e8cbca22-1974-11e8-808a-544fc4662987.png)

用法是：`bro 命令`


# Mac homebrew医生 `brew doctor`

用来检测当前环境问题。


# Linux查看本机`Public IP`地址
用不着什么命令行工具，直接用`curl`访问一些ip检测的网页就ok了。
比如：
```
curl ipinfo.io/ip
```
或者更常用的httpbin：`curl httpbin.org/ip`


# 用SSH免密码登录服务器或树莓派

[参考文章。](http://blog.csdn.net/permike/article/details/52386868)

1. 首先在本机器生成密钥对 key pair:
输入`ssh-keygen`，然后一路回车。这样就成功的在`~/.ssh/`下创建了`id_rsa`私钥和`id_rsa.pub`公钥，且没有passphrase密码。
2. 连接到服务器。一般也是通过SSH连接，因为没配置好ssh呢，所以先用户密码登录。
3. 将本地的`id_rsa.pub`公钥内容复制到服务器的`~/.ssh/authorized_keys`文件中，这个文件支持多个公钥设置，每一行写一个：
```shell
echo "刚刚复制的本机公钥内容" >> ~/.ssh/authorized_keys
``` 
4. 一般来说，到了这里，就可以直接通过ssh登录服务器了。
5. 有的服务器的ssh默认设置，没有允许别人通过密钥登录等等，所以需要在设置文件里修改下：
```shell
vim /etc/ssh/sshd_config

#然后找到以下几样内容，改成一样的：
# 开启密钥登录功能
RSAAuthentication yes
PubkeyAuthentication yes

#  root 用户也可以通过 SSH 登录
PermitRootLogin yes

# 禁用密码登录
PasswordAuthentication no

# 编辑完后，保存退出，然后重启ssh
service sshd restart
```


# Linux更改服务器的默认Shell
因为老登录服务器和树莓派什么的，默认bash实在太难看，tab补全也不好用，所以希望一连接就直接用zsh。
方法很简单：更改`/etc/passwd`这个文件。
看样子那个文件是保存密码似的，其实真不是，就一堆明文的各用户配置，其实也看不懂每行什么意思，如下：
![image](https://user-images.githubusercontent.com/14041622/36644332-7e27217e-1a93-11e8-8734-7bb0f7058bfb.png)
因为是系统文件，所以需要root权限，这时用`sudo vim /etc/passwd`打开文件进行编辑，找到自己当前的用户名那一行，把最后的`/bin/bash`改成`/bin/zsh`即可。保存退出，重新登录连接服务器，哒哒！完成。



# Linux用`sudo apt-get install`安装时报错`Could not get lock /var/lib/dpkg/lock` 
之前因为`sudo apt-get install`安装什么东西，然后按键终止掉了安装，结果就一直被锁住。
[解决方案参考文章。](https://askubuntu.com/questions/15433/unable-to-lock-the-administration-directory-var-lib-dpkg-is-another-process)

1. 删除文件锁：`sudo rm /var/lib/dpkg/lock`
2. 然后虽然没有被锁住了，但是还报错误`E: dpkg was interrupted, you must manually run 'sudo dpkg --configure -a' to correct the problem.`
于是按照系统提示的解决方法输入命令，如下：
```shell
sudo dpkg --configure -a
```
3.这时虽然可以启动安装程序了，但是运行到最后往往还是会报这个错误：
```
Errors were encountered while processing:
 cups
 ssl-cert
 sudo
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
尝试了网上无数种apt-get purge, clean, -f install等等等等，都不行。
于是看到了[一篇中文文章](https://www.cnblogs.com/anpengapple/p/5098960.html)两句话解决：
```shell
sudo mv /var/lib/dpkg/info/ /var/lib/dpkg/info_backup/
sudo mkdir /var/lib/dpkg/info/
```
意思是，主要出错原因在于`/var/lib/dpkg/info/`文件夹，把它备份或删掉就好了，然后再创建一个同名文件夹。
之后`sudo apt-get upgrade`升级试试，一切完好！


# 树莓派挂载U盘
[参考文章](https://segmentfault.com/a/1190000014173634)

```shell
# 检查设备名字
sudo fdisk -l

# 设定映射目录
sudo mkdir /mnt/udisk
# 将指定设备映射到刚刚创建到目录
sudo mount -o uid=pi,gid=pi /dev/sda1 /mnt/udisk/

# 开机自动执行
sudo vim /etc/rc.local
# 将下面这句加到文件内容中(rc.local最后的exit 0之前都行)
mount -o uid=pi,gid=pi /dev/sda1 /mnt/udisk/

# 弹出优盘方法
sudo umount /mnt/udisk

# 如果提示device is busy
ps -ef | grep /mnt/udisk
sudo kill -9 xxx
```



# `Exiftool` 命令行操作图片元信息(Megadata)
> Exiftool 是命令行操作exif最强大的工具。

[官方网址。](https://www.sno.phy.queensu.ca/~phil/exiftool/)

[参考：图片EXIF信息查看与Exiftool使用](https://www.jianshu.com/p/d76457799de1)

安装：
```shell
# Mac上安装
$ brew install exiftool

# 或Linux上安装
$ sudo apt-get install exiftool

# 查看图片全部exif信息
$ exiftool 图片位置

# 查看图片某个tag信息
$ exiftool -tag
```

## 语法
每种格式的图片都有自己不同的一堆Tags，比如时间、日期、地理位置等，jpg和png都很不一样。
所以到官网参考每种图片的不同tags，才能确定自己要怎么改这个信息。

[ExifTool Tag Names](https://www.sno.phy.queensu.ca/~phil/exiftool/TagNames/index.html)

注意，引用tag时，要用小写。

基本语法是一样的：
- 设置某tag的值：`-tag=VALUE` 
- 增减某tag值(如果是数字的话)：`-tag+=VALUE` 或`-tag-=VALUE`
- 清空: `-tag=`

```sh
$ exiftool -artist=solomon
```

但是有一点一定要注意：每种tag所接受的值的格式是很严格的：
- 日期
- 时长

## 常用操作
```sh
$ exiftool photo.jpg #查看所有信息
$ exiftool -a -u -g1 photo.jpg #查看所有元信息，包括重复和未知标签，并按小组排列
$ exiftool -s -ImageSize -ExposureTime photo.jpg #查看图片尺寸
$ exiftool -common dir  #查看dir目录文件信息（不仅仅是图片）
$ exiftool -l  c.jpg d.jpg  #从两个图像文件打印所有信息。
$ exiftool -l -canon c.jpg d.jpg  #从两个图像文件打印标准的佳能信息。
```

更改创建和修改时间
```sh
$ exiftool -gps:all= photo.jpg  #有些相机会记录拍照时的GPS定位信息。如果你不希望别人看到使用该命令删除gps信息
$ exiftool -all= photo.jpg  #删除所有信息
$ exiftool -all= --exif:all photo.jpg  #删除EXIF以外的所有信息
```

写入标签
```sh
$ exiftool -artist=标签名称 photo.jpg            #写入艺术家标签
$ exiftool -artist=标签名称 a.jpg b.jpg c.jpg   #写多个文件
$ exiftool -artist=标签名称  /exiftoolTest      #写在一个目录的所有文件 exiftoolTest为文件夹
```

其它：
```sh
$ exiftool -Comment ='这是一个新的评论'dst.jpg
    向JPG图片写入新评论（取代任何现有评论）。
$ exiftool -comment = -o newdir -ext jpg。
    删除当前目录中所有JPG图像的评论，
    将修改后的图像写入新目录。
$ exiftool -keywords = EXIF -keywords =编辑器dst.jpg
    用两个新的关键字（“EXIF”和。）替换现有的关键字列表
    “编辑”）。
$ exiftool -Keywords + =单词-o newfile.jpg src.jpg
    将源图像复制到新文件，然后添加关键字（“单词”）
    当前关键字列表。            
$ exiftool -credit- = xxx dir
    从一个目录中的所有文件中删除信用信息，信用值是“xxx”。
$ exiftool -all = dst.jpg
    从图像中删除所有元信息。注意：你不应该
    对RAW图像（DNG除外）进行处理，因为它是专有的RAW图像
    格式通常包含制造注释中的信息
    转换图像所必需的。
$ exiftool -all = -comment ='寂寞'dst.jpg
    删除图像中的所有元信息并添加评论
    （注意顺序很重要：“-comment ='lonely'-all =”
    也会删除新评论。）
$ exiftool -all = --jfif：全部dst.jpg
    从图像中删除除JFIF组以外的所有元信息。
$ exiftool -Photoshop：全部= dst.jpg
    从图像中删除Photoshop元信息（注意
    Photoshop信息还包括IPTC）。
$ exiftool -r -XMP-crss：all = DIR
    递归删除a中的图像中的所有XMP-crss信息
    目录。
$ exiftool'-ThumbnailImage <= thumb.jpg'dst.jpg
    从指定的文件中设置缩略图（注意：引号是
    以防止外壳重定向）。
$ exiftool'-JpgFromRaw <=％d％f_JFR.JPG'-ext NEF -r。
    递归地写入以“_JFR.JPG”结尾的文件名的JPEG图像
    添加到扩展名为“.NEF”的类似文件的JpgFromRaw标记中
    当前目录。 （这是“-JpgFromRaw”的倒数
    上面的“READING EXAMPLES”部分的命令）。
$ exiftool -DateTimeOriginal - ='0：0：0 1：30：0'dir
    调整目录“dir”中所有图像的原始日期/时间
    减去1小时30分钟。 （这相当于
    “-DateTimeOriginal- = 1.5”。请参阅Image :: ExifTool :: Shift.pl
    细节。）
$ exiftool -createdate + = 3 -modifydate + = 3 a.jpg b.jpg
    向两个CreateDate和ModifyDate时间戳添加3个小时
    图片。
$ exiftool -AllDates + = 1：30 -if'$ make eq“Canon”'dir
    移动DateTimeOriginal，CreateDate和ModifyDate的值
    将所有佳能影像转换1小时30分钟
    目录。 （AllDates标签作为这些的快捷方式提供
    三个标签，允许他们通过一个标签访问。）
$ exiftool -xmp：city = Kingston image1.jpg image2.nef
    将标签写入两个图像的XMP组。 （没有“xmp：”
    自从“City”存在以后，该标签将被写入IPTC组
    在这两种情况下，IPTC默认是首选。）
$ exiftool -LightSource - ='未知（0）'dst.tiff
    只有在值为0时才删除“LightSource”标签。
$ exiftool -whitebalance- = auto -WhiteBalance = tung dst.jpg
    只有之前为“自动”时，才将“WhiteBalance”设置为“Tungsten”。
$ exiftool -comment- = -comment ='新评论'a.jpg
    只有当图片还没有时才写新评论。
$ exiftool -o％d％f.xmp目录
    为“dir”中的所有图像创建XMP元信息数据文件。
$ exiftool -o test.xmp -owner = Phil -title ='XMP File'
    仅从命令中定义的标签创建XMP数据文件
    线。
```

## 常用标签名(Tags)
> 因为编辑exif信息需要知道图片里内置的各种标签名才能修改，所以下面为标签名参考。

![screenshot-www sno phy queensu ca-2018 04 21-12-29-03](https://user-images.githubusercontent.com/14041622/39080383-a9b40cc0-455f-11e8-9baf-6ac0b12cf350.png)



# `Pandoc文件转化工具`

[参考 Pandoc Demos](https://pandoc.org/demos.html)
[官方收集的各种模板： User contributed templates](https://github.com/jgm/pandoc/wiki/User-contributed-templates)

![image](https://user-images.githubusercontent.com/14041622/39826697-1239deaa-53e8-11e8-8511-a6d30bbd53af.png)

## 常用转换

```shell
# Markdown to Microsoft word .docx
$ pandoc FILENAME --to docx -o FILENAME.docx
```

## Markdown转HTML
一般来说，简单一句就够了：
```shell
$ pandoc in.md -o out.html
```

但是，页面丑爆了！所以我们必须加上模板来渲染出漂亮的页面，比如Github风格的markdown页面。
但是这就有一些些复杂了。

这里我们采用`GitHub Pandoc HTML5 Template`模板，地址在此：
https://github.com/tajmone/pandoc-goodies/tree/master/templates/html5/github

需要把这个目录中所有文件复制到`~/.pandoc/templates/`文件夹下:
![image](https://user-images.githubusercontent.com/14041622/40443379-ac41e270-5ef8-11e8-90d9-567fc3b9f072.png)

如果本地没有这个文件夹，就自己创建一个。复制好之后，就可以直接引用名字来生成渲染过的markdown网页了:
```shell
$ pandoc --template=Github.html5 in.md -o out.html
```



# Linux 常用命令101集合

## `mv`

### 移动多文件
[参考。](https://askubuntu.com/questions/214560/how-to-move-multiple-files-at-once-to-a-specific-destination-directory)
```shell
# 移动指定的多文件 (最后一个即终点)
mv file1 file2 file3 DESTINATION

# 根据查找结果移动多文件
mv  `ls|grep IDENTIFIER` DESTINATION
# or
mv *.doc /path/to/dest/folder/
```

### 重命名文件、文件夹
```shell
# 重命名文件夹
mv old_folder_name new_folder_name

# 重命名文件
mv old_file_name new_file_name
```


# Mac上ZSH每次打开都会显示`You have new mail`
查了下才知道，原来不是我的邮箱，而是另一种新建，一种叫`mail`的命令保存的信件。
它的创建应该是和创建的`crontab`任务有关系。

输入`mail`命令，一条一条看完，就不会再显示了。

![image](https://user-images.githubusercontent.com/14041622/40096487-a943a842-5903-11e8-9732-aaeca20046db.png)



# 让命令行终端使用Vi模式
> 命令行里输入长命令时，真是个pain。不能跳词，不能用鼠标，只能按左右键一个字母一个字母移动，实在是挺费劲的。

[参考文章。](https://dougblack.io/words/zsh-vi-mode.html)

实际上非常非常简单，完全无需额外下载什么插件，都是内置功能。
如果Bash终端的话，只要在`~/.bash_profile`或`~/.bashrc`中加入这个命令：
```vim
set -o vi
```

如果是Zsh，则在`~/.zshrc`中加入：
```vim
bindkey -v
export KEYTIMEOUT=1
```

[参考视频：TFW You Learn There's a Vim Mode in Bash...](https://www.youtube.com/watch?v=GqoJQft5R2E)

具体使用：

我使用的iTerm2+Zsh终端，已经进入了vi模式。但是屏幕上没有任何显示当前是`Normal`模式还是`Insert`模式。所以经常不知道自己在什么模式，还是有点不习惯。
使用上，完全和vi相同。



# Linux 文件搜索检索

## `Find`查找文件
`find`命令可以在指定目录及里面所有子文件夹的文件里搜索。不光可以按文件名搜索，还可以结合`grep`根据内容搜索。

```shell
# 根据文件名搜索
find 路径 -name '*.jpg'

# 根据文件名搜索 并且只显示内容中包括关键字的结果
$ find 路径 -name '*.txt' | xargs grep '关键字'

# 查找所有含有某关键字的文件：
$ find 路径 * | xargs grep '关键字'
```


# Linux发送邮件的命令行应用
先说明下：不管是什么邮件客户端，都是可以直接发邮件的。但是，因为默认的话，发件人是很随便地设置成你本机地名字。并且**100%**会被邮箱当成垃圾邮件处理。如果你去垃圾箱里找，还是可以看到的。这就是为什么，我们还是需要配置它，让它登录某个邮箱来使用它的身份发邮件了，比如gmail邮箱或阿里云邮箱。（国内的163和qq邮箱都已经屏蔽第三方客户端登录了）

> 另注：为什么如今这么电子技术这么发达的年代，命令行邮件终端相关的应用和文章还这么少几乎都是很多年前的？我想是因为：python等都已经能很好很方便支持发邮件了，没必要折腾命令行版本。
事实上，试过就知道：为什么这些客户端会被抛弃了。。。请看下面我入的坑：

## ~`Mail`和`Sendmail`~
> 注：Mail的配置相当麻烦，网上找文章也寥寥无几，有也都是十几年前的东西。所以建议放弃，使用更先进的客户端。

## `Mutt`
> Mutt是Linux邮箱客户端榜上有名的利器了。

先不说什么界面操作之类的，因为我们用命令行的邮箱客户端都是用来自动化的，不想用什么界面。

[参考：Linux使用mutt发送邮件](http://blog.51cto.com/wzlinux/2043647)

### 安装
其中`mutt`是软件本身，`msmtp`是用来帮助发件的工具。
```shell
# Linux
$ sudo apt-get install mutt msmtp

# 或Mac
$ brew install mutt msmtp
```

### 配置
你需要配置两个文件，一个是`~/.muttrc`用来配置Mutt本身，一个是`~/.msmtprc`用来配置发件人的，需要写入密码一类的。

[参考：Linux下使用mutt,msmtp发信](http://coolnull.com/82.html)

配置`~/.msmtprc`:
```shell
account     Aliyun
host        smtp.aliyun.com
from        jason@aliyun.com
auth        login
user        jason@aliyun.com
password    abcde123123123
account default : Aliyun
logfile ~/.msmtp.log
```
然后必须修改`~/.msmtprc`文件的权限，否则程序无法读取，发邮件时会报错。修改如下：
```shell
chmod 600 ~/.msmtprc
```

配置`~/.muttrc`：
```shell
set sendmail="/usr/bin/msmtp"
set use_from=yes
set realname="Jason"
set from="Jason@aliyun.com"
set envelope_from=yes
set editor="vim -nw"
```
注意：第一条`set sendmail`中的位置不一定是这样的，在Mac和Linux上都会不同，所以需要用`which msmtp`来找到它的真实位置，再填进去。

关于配置的解释可以看这里：
![image](https://user-images.githubusercontent.com/14041622/40438772-8415e3da-5eeb-11e8-8733-83b6aadab2b4.png)


### 发送邮件命令格式
注意：收件人的地址前一定要明确指定参数名`--`，如下所示。否则无法正确发送附件。

```shell
# 常用格式如下 -s   “标题”  -c    抄送  -a  附件
$ echo “HELLO WORLD” | mutt -s “TITLE” -- RECIPIENT@gmail.com

# 发送HTML格式漂亮的邮件
$ mutt -- RECIPIENT@gmail.com -e 'set content_type="text/html"' -s "TITLE" < out.html

# 发送给多人，抄送，添加附件
$ echo "hello" | mutt -s "TITLE" aaa@gmail.com, bbb@gmail.com -c ccc@gmail.com -a /home/pi/pic.jpg address="RECIPIENT@gmail.com"

# 发送邮件时设置邮件的文本类型为：html格式，邮件的等级为:重要
$ echo $content | mutt  -s "${subject}" -e 'set content_type="text/html"' -e 'send-hook . "my_hdr  X-Priority: 1"' $address
```

语法：
![image](https://user-images.githubusercontent.com/14041622/40440006-455fbfa4-5eef-11e8-93b2-3b405e0215fb.png)

参数：
![image](https://user-images.githubusercontent.com/14041622/40440013-4b1cc57c-5eef-11e8-943b-d2bb7e762fe5.png)


### Mutt发送HTML漂亮富文本邮件
默认语法是：
```shell
$ mutt -- RECIPIENT@gmail.com -e 'set content_type="text/html"' -s "TITLE" < out.html
```
但是，值得注意的是，语法虽然简单，可一旦你本机的`mutt`版本不对，邮件将无法显示出正确的格式，而只是无尽的html源代码。
通过`mutt -v`可以看到，发送出显示正常的邮件的mutt版本是在树莓派上安装的`Mutt 1.5.23 (2014-03-12)`。而不成功的是在Mac上的`Mutt 1.9.5 (2018-04-13)`，反而是最新的版本！


## 邮箱配置
- [阿里云邮箱](https://help.aliyun.com/knowledge_detail/36576.html)
![image](https://user-images.githubusercontent.com/14041622/40422684-b1df8542-5ec2-11e8-96e1-8e8ad4045a98.png)
- 163邮箱
![image](https://user-images.githubusercontent.com/14041622/40435788-12ad41ea-5ee4-11e8-838d-4969e6224c92.png)
- 新浪邮箱
```
- 新浪@sina.com邮箱，
接收服务器地址为：pop.sina.com或pop3.sina.com，
发送服务器地址为：smtp.sina.com

- 新浪@sina.cn邮箱，
接收服务器地址为：pop.sina.cn或pop3.sina.cn，
发送服务器地址为：smtp.sina.cn

- 端口号设置：
POP协议：pop端口：110、smtp端口：25 
IMAP协议：IMAP 端口：143、smtp端口：25

- 加密设置：
pop是995、imap的是993
smtp是587或465，如465不能正常使用，
可以更换587试试，但不同的国家有可能只支持
一个端口(并非所有客户端都支持加密码) 。
```






# Ubuntu和树莓派更新源方法

两步搞定：
```shell
$ sudo vim /etc/apt/sources.list

# 然后把源的一条一条的地址复制进去 保存即可

# 更新索引清单
$ sudo apt-get update

# 更新依赖关系
sudo apt-get upgrade -y
```

## 树莓派的中国源
```
deb http://mirrors.aliyun.com/raspbian/raspbian/ jessie main non-free contrib rpi
deb-src http://mirrors.aliyun.com/raspbian/raspbian/ jessie main non-free contrib rpi
```

## Ubuntu的中国源
```
#sohu shangdong
deb http://mirrors.sohu.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.sohu.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.sohu.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.sohu.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.sohu.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.sohu.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.sohu.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.sohu.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.sohu.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.sohu.com/ubuntu/ trusty-backports main restricted universe multiverse

#163 guangdong
deb http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty-security main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty-updates main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty-proposed main restricted universe multiverse
deb-src http://mirrors.163.com/ubuntu/ trusty-backports main restricted universe multiverse

#aliyun
deb-src http://archive.ubuntu.com/ubuntu xenial main restricted
deb http://mirrors.aliyun.com/ubuntu/ xenial main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-updates main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates universe
deb http://mirrors.aliyun.com/ubuntu/ xenial multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-updates multiverse
deb http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted
deb-src http://mirrors.aliyun.com/ubuntu/ xenial-security main restricted multiverse universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security universe
deb http://mirrors.aliyun.com/ubuntu/ xenial-security multiverse


#tsinghua.edu
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security main restricted
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security universe
deb http://mirrors.tuna.tsinghua.edu.cn/ubuntu/ xenial-security multiverse

#neu.edu
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial main restricted #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial restricted multiverse universe #Added by software-properties
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-updates main restricted multiverse universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial multiverse
deb http://mirror.neu.edu.cn/ubuntu/ xenial-updates multiverse
deb http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-backports main restricted universe multiverse
deb http://archive.canonical.com/ubuntu xenial partner
deb-src http://archive.canonical.com/ubuntu xenial partner
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted
deb-src http://mirror.neu.edu.cn/ubuntu/ xenial-security main restricted multiverse universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security universe
deb http://mirror.neu.edu.cn/ubuntu/ xenial-security multiverse
```


# ImageMagick转换PDF
`ImageMagick`是Linux上超强大、功能超丰富的图片处理的命令行工具。
而`ImageMagick`在做PDF相关的工作时，是基于`Ghostscript`进行处理的。所以两个都要安装。

首先确保本机已经安装ImageMagick与Ghostscript, 以Mac为例：
```sh
brew install ghostscript imagemagick
```

安装好后，命令行里就可以调用ImageMagick的一系列命令了。

常用命令有：
```sh
#JPG图片转为PNG图片
$ convert image.jpg image.png

#将图片缩放为50%大小
$ convert image.png -resize 50% image2.png

#将图片缩放为指定长宽
$ convert image.png -resize 640x480 image2.png

#横向合并图片
$ convert image1.png image2.png image3.png +append image123.png
```

## PDF转图片

用`imagemagick`将pdf转成图片（不是提取图片）的命令是：
```sh
$ convert sample.pdf sample.jpg
```

命令非常简单，速度也极快。但是在PDF转图片的过程中，如果不加任何设置直接`convert xx.pdf xx.png`这样的转换，效果可是**非常之差**，如下图：

![image](https://user-images.githubusercontent.com/14041622/40873821-1fdacbf4-669a-11e8-94bb-d256c69ad744.png)

注意：一般如果设置输出为png的话，程序会提出警告：
convert: profile 'icc': 'RGB ': RGB color space not permitted on grayscale PNG sample-default-convert.png' @ warning/png.c/MagickPNGWarningHandler/1744.
这是因为程序没有很好支持`PNG`格式图片的问题。虽然报错，但是png文件也能正常生成。如果不喜欢的话，就改成`JPG`格式输出好了。

### `清晰度设置`
`convert`命令将PDF转图片的最大难度在于清晰度问题。网上有很多种解决方案，各有优缺。

以下为一些尝试的总结：

```sh
# 默认转换：图片大小几乎与pdf相同
$ convert sample.pdf sample.jpg

# resize设置：无论resize 100还是3000，都没有清晰化
$ convert -resize 3000 sample.pdf sample.jpg

# quality设置：完全没有作用
$ convert -quality 100% sample.pdf sample.jpg

# verbose+density+quality+flatten+sharpen转换：也就大概还原了80%的清晰度
$ convert -verbose -density 150 -trim -quality 100 -flatten -sharpen 0x1.0 sample.pdf sample.jpg

# density 300转换：100%还原，但是文件增大10倍
$ convert -density 300 -trim -quality 100 sample.pdf sample.jpg

# geometry 转换：100%还原，文件增大7倍
$ convert -geometry 1600x1600 -density 200x200 -quality 100 sample.pdf sample.jpg
```

总结：经过各种考察，中外网友对`convert`转换图片的清晰度设置，也全都在猜的阶段。而且设置都太固定，并不能稳定保证所有的PDF都转换成一样的清晰度。
所以问题需要转换另一个思路去解决：
直接提取PDF中的原画，这样就100%是原画质了。
而且一般对于扫描书籍的PDF来说，全页只有一个图片，所以用`pdfimages`就比较好解决。

这个需要另一个命令行工具`pdfimages`来做到了。
请参考另一篇相关笔记。




# 利用命令行工具`pdfimages`来提取PDF中的图片
`pdfimages`是一个非常简便好用的PDF图片提取工具，很简单的一个命令就可以提取出PDF指定页面里的所有图片。但是，

注意：
`pdfimages`只能`提取`PDF中的图片，和`imagemagick`的`生成`图片有本质上的不同！也就是说，如果PDF中的内容不是图片的话，那么就提取不出来。

安装：
`pdfimage`是`poppler-utils`工具的一个子集，所以需要安装`poppler-utils`或`poppler`才能使用。Mac上，直接homebrew：
```sh
$ brew install poppler
```

安装好后就可以用`pdfimages`命令了，用法如下：
```sh
# 提取出来的图片保存为默认的. ppm格式文件 (图片文件巨大，会比pdf文件大23倍左右）
$ pdfimages sample.pdf img_name

# 设定提取的图片保存为png格式 (图片大小是3倍左右）
$ pdfimages -png sample.pdf img_name

# 提取某一页的图片 (last one page)
$ pdfimages -l 3 sample.pdf img_name

# 提取前几页的图片(first number of pages)
$ pdfimages -f 2 sample.pdf img_name
```

提取的图片，会按照指定的位置和名字生成如`img_name-000.jpg, img_name-001.jpg, img_name-002.jpg`这样的文件，每一个图片都对应着PDF中原始的图片。

如果没有图片，则不输出。


# 利用命令行工具`pdftk`对PDF进行合并分割
`pdftk`是非常好用的PDF页面操作工具，能够切割、合并、提取指定页面等。

[参考：PDF 合并和分割工具--PDFtk](https://blog.seisman.info/pdftk/)
[参考官网：PDFtk server:  the pdf tool kit](https://www.pdflabs.com/tools/pdftk-server/)

常用包括的功能如下：
- 合并 PDF；
- 分割 PDF 页面；
- 旋转 PDF 页面；
- PDF 带密码访问；
- PDF 填加密码；
- 用 X/FDF 填写 PDF 表格；
- 从 PDF 表格中生成 PDF Data Stencils；
- 加背景水印或前景印章；
- 报告 PDF Metrics，书签和元数据；
- 增加 / 更新 PDF 书签或元数据；
- 给 PDF 页面或文档加附件；
- 解压 PDF 附件；
- 分解 PDF 文档为多个单页；
- 解压缩和重压缩页面流；
- 修复受损的 PDF 文档；

## 安装
Linux上安装：
```sh
$ sudo apt-get install pdftk
```
Mac上安装：因为它对Homebrew支持还不算特别好，需要这样指定文件位置来安装：
```sh
$ brew install https://raw.githubusercontent.com/turforlag/homebrew-cervezas/master/pdftk.rb
```

## 常用命令

```sh
#提取第1至3，第5，第6至10页，并合并为一个pdf文件
$ pdftk input.pdf cat 1-3 5 6-10 output output.pdf

#合并(concatenate) 前面所有的pdf为output.pdf
$ pdftk file1.pdf file2.pdf ... cat output output.pdf

#拆分PDF的每一页为一个新文件 并按照指定格式设定文件名
$ pdftk input.pdf burst output out_%d.pdf

#按照通配符，合并大量PDF文件
$ pdftk *.pdf cat output combined.pdf

#去除第 13 页,其余的保存为新PDF
$ pdftk in.pdf cat 1-12 14-end output out1.pdf

#扫描一本书，odd.pdf 为书的全部奇数页，even.pdf 为书的全部偶数页，下面的命令可以将两个 pdf 合并成页码正常的书
$ pdftk A=odd.pdf B=even.pdf shuffle A B output collated.pdf

#按180°旋转所有页面
$ pdftk input.pdf cat 1-endsouth output output.pdf

#按顺时针90°旋转第三页，其他页不变
$ pdftk input.pdf cat 1-2 3east 4-end output output.pdf

#输入密码转换成无密码PDF
pdftk secured.pdf input_pw foopass output unsecured.pdf

```


# wget 常用命令

[参考：wget命令](http://www.cnblogs.com/peida/archive/2013/03/18/2965369.html)

```sh
# 下载多个链接 --input-file
$ wget -i List.txt

# 下载到指定目录 --directory-prefix
$ wget <url> -P ./folder

# 强制按照url的层级结构，创建多层目录 --force-directories
$ wget <url> -x

# 不覆盖已有文件 --no-clobber
$ wget <url> -nc 

# 输出log下载日志 小写o，--output-file
$ wget <url> -o logname

# 保存文件为指定的名字 大写O， --output-document
$ wget <url> -O filename

# 限速下载
$ wget <url> --limit-rate 300k

# 每次下载都等待3秒
$ wget <url> --wait 3

# 每次下载随机等待0~2秒之间
$ wget <url> --random-wait

# 每次重新连接retry时等待1秒
$ wget <url> --waitretry 1

# 响应超时为5秒 --timeout
$ wget <url> -T 5

# 打印调试输出 --debug
$ wget <url> -d
# 不输出信息 --quiet
$ wget <url> -q
```


# 用pdftohtml将PDF转成HTML
`pdftohtml`同样是超强命令行工具集`poppler`的一个子集，和`pdfimages`等优秀的子集一样。用好了是非常便利的。

需要理解的是，`pdftohtml`对`扫描版PDF`是没什么用对。它的主要功能是把pdf中元素全部提取出来，然后按照布局生成HTML。但是扫描版的相当于是一张图片，没有任何元素信息。

Mac上，直接homebrew：
```sh
$ brew install poppler
```
安装好`poppler`工具集后，就可以用`pdftohtml`命令了。

常用命令：
```sh
# 默认输出 (生成多个互相嵌套的html文件，以及多个图片
$ pdftohtml sample.pdf sample.html

# 生成"复杂"排版，其实就是更精确排版的意思 --complex
$ pdftohtml -c sample.pdf sample.html

# 指定第一页至最后一页区间：first-last
$ pdftohtml -f 1 -l 2 sample.pdf sample.html
```

效果：
效果还好，即使是中文的，排版也没有偏离很远。
程序会自动生成很多很多很多的html和图片文件，全都在一个文件夹里面不分类。



# Llinux 重复上一条命令

[参考：History（历史）命令用法 15 例](https://linux.cn/article-1143-1.html)

一般有这几种方法：
- 按方向键`⬆`
- 按 `!!`和回车
- 输入`!-1` 和回车
- 按 `Ctrl+P`或`Ctrl+N`上下滚动


# Linux的cp, mv, rm等显示当前操作或进度的方法

## mv
```sh
# -v参数verbose
$ mv -v ./src/* /tmp
```

## rm
```sh
# -v 和-r参数 注意文件列表太多的话会不执行
$ rm -vr <from> <to>
```

## cp
```sh
# -v 和-r参数 verbose & recursive
$ cp -vr <from> <to>

# 使用rsync命令代替
$ rsync -avP <FROM> <TO>
```


# rsync 强大的远程、本地文件夹同步工具

一般Mac、Ubuntu等主流*nix系统，都原生搭配了这个命令，非常好用。但是命令比较复杂，需要学习。

[参考：rsync中文Man Page](http://man.linuxde.net/rsync)

注意事项：
- 目录名后有或没有`/`是很不同的。
`./source`代表整个文件夹，`./source/`代表这个文件夹下的所有文件。
- 不是所有参数都能混合在一起用的，经常会互相冲突


## 本地同步
以下为常用的同步语句：
```sh
# 正常copy，同cp命令
$ rsync -r ./src/ .target/

# 完全同步 --recursive --delete 注意这两个是固定搭配
# 如果source中没有的，target目录中有的会被删除
$ rsync -r --delete ./src/ ./target/
```


## 远程同步

```sh
# 本地文件夹同步到远程 (通过SSH方式)
$ rsync -r  ~/local/ pi@192.168.1.123:/home/pi/remote

# 远程文件夹同步到本地 (SSH)
$ rsync -r pi@192.168.1.123:/home/pi/remote ~/local/
```