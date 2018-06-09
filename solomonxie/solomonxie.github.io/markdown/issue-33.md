# OS Ops 操作杂疑症状
> Linux、Windows、Mac等操作系统日常操作实在需要解决的问题太多了，在这里记录点滴再合适不过了


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


# 总是在Windows与Linux之间抉择，又总是在Linux各发行版之间抉择
@ 24 Nov 2015

## 1
这样做有什么意义呢？
看了恩多的comments，又查了恩多的介绍文章，Linux这好那好，各个发行版又各种神奇。
自从用电脑这么多年来，就没停止过对Linux的幻想。
每次鼓足了勇气，备份好了所有Windows数据，安装了个LInux版本，然而不超过一个月总是会有一样的结果：
哎呦不行，还是得换回来。
我之前还做了个list，想追根到底的讲清楚，到底自己依赖哪些必要的Windows产品？
然并卵……
直到今天，又在备份所有Windows数据准备进军Linux时候，才恍然大悟：
我只有一台电脑，根本就脱离不开Windows嘛！
有人以为是MS Office的垄断性普及让人脱离不开，或者说大家都是为了Office而装Windows，这是不错的。
但远不止。
试想在Linux里有百度云、360云、微盘这么多高效自动备份工具吗？Linux里面能轻松给Android手机和iPhone刷系统吗？Linux能安然地打开虾米、酷狗听音乐吗？Linux能一键各种迅雷BT下载、磁性下载吗？Linux能那么轻松的在各种软件之间交互吗？
不知道是我的思维已经被限制了还是怎么的，最起码我觉得，现在想在中国过个正常日子，没个Windows处理日常，真的是说不过去。
网上各种在Linux中建立替代方案的，其实说白了就是舍近求远，只是为了折腾而折腾，怎么替代能比原作好？
Windows中这么多年经验的技术积累，方方面面都有数不胜数的程序员在作出贡献，已经是一个非常成熟的系统了。
的确，作为编程平台或者是服务器之类，Windows各种被鄙视。
但是我觉得自己被骗的地方是，这些观点都没错。可是——
当这些观点揉合在一起，给你提出的那个建议，就出了问题了，不知道害了多少人。
也就是说，除了上了点层次的程序员有能力买好几台电脑的，其实好多人也就一台电脑。
只有这一台电脑的人，在网上各种问我能不能把系统换成Linux啊，好不好啊？然后这些有多台电脑的人就会各种夸Linux强。然后有一台电脑的人就陷入这种万劫不复的深坑了，就像我一样。

所以说，我写这篇看起来像是抱怨的东西，其实就是为了提醒自己这种循环掉坑别再犯了：
**我就一台电脑！踏踏实实的在Windows下装个Linux虚拟机就完事了，别整什么双系统，也别整什么Linux下的Windows替代方案了！**  

其实想想也是，Windows各种处理正常事物，然后新人就当好新人，安安全全的在虚拟机里研究Linux，然后在虚拟机里编程就不错了。等到一定境界，或者找到相应工作，或者升职加薪，再来一台电脑。然后再踏踏实实玩Linux。这样一来逼格也高了，老板突然让你改个Excel也不会慌了。


## 2
今天试了一下Virtualbox虚拟机安装Ubuntu14，感觉还不错啊~~
虽然速度没那么爽（因为内存只给配了700M,而且还是32bit的）
适应了一切命令行操作以后，好像一切都没那么难以接受了。
安装了Mysql和Python的几个IDE，比如Sublime, IDLE, Vim。
感觉上也还行，比较能接受。
但是，心里还是有一种感觉就是，这体验，也没比Windows好到哪去啊？
真要上手认真编程，会好吗？
还有待观察。。。。

对了，Virtualbox很不错啊，一切都好简单好轻松。比起付费的臃肿的VMware不知道好多少！

另外，今天装系统时，顺便把Windows10降回了Win7，速度简直飞跃一般！
还是踏踏实实的用Win7这个确实稳定的系统吧。



# Windows安装SSH服务器

## FreeSSHD (不推荐）
这个应该是搜索关键字时给出的第一个建议吧。
但是其实这个软件并不好用，配置不是那么先进，bug也多。

经常遇到各种`Permision Denied`的情况。


## Bitvise SSH
重点推荐。

配置全面，也有简单模式，条理清晰，而且软件比较新。连接情况也有动态log显示给你看。

[安装参考：在win8.1上用Bitvise SSH Server 6.24(原名winsshd)搭建SSH2服务器](https://blog.csdn.net/gsls200808/article/details/45127781)

主要步骤就是：
- 官网下载exe安装文件并安装（选Personal个人免费版）
- 配置页面选择`Open easy settings`
- 设置port端口（注意22虽是ssh默认接口但是经常被占用）
![image](https://user-images.githubusercontent.com/14041622/41194162-e48212e6-6c49-11e8-9d73-d7c70fb962f2.png)
- 切换到Windows account选项卡，取消真实windows用户账户
![image](https://user-images.githubusercontent.com/14041622/41194165-f2be5a4a-6c49-11e8-9ce1-3382ab3b390d.png)
- 切换到Virtual account虚拟账户选项卡，建立虚拟登录用户账户
![image](https://user-images.githubusercontent.com/14041622/41194173-08fd4e4c-6c4a-11e8-8b96-2db23397f62e.png)
- 输入用户名，或者导入PublicKey公钥。方法是把你自己客户端电脑上的`~/.ssh/id_rsa.pub`文件复制到这个服务器上，然后点击import导入，成为这个虚拟账户的publickey。这样就可以免密码登录了。
![image](https://user-images.githubusercontent.com/14041622/41194175-0bf2cf82-6c4a-11e8-9fa8-77389a819648.png)
![image](https://user-images.githubusercontent.com/14041622/41194176-0de2e3d6-6c4a-11e8-8533-45753d9c0f58.png)
![image](https://user-images.githubusercontent.com/14041622/41194177-0fe65438-6c4a-11e8-88dc-808f2f1fb371.png)
![image](https://user-images.githubusercontent.com/14041622/41194179-12b01e2e-6c4a-11e8-9f98-8bd16c889ce1.png)
- 回到主界面，Start开启服务

这时候就可以开始连接了。

到自己的Linux或Mac上命令行里，输入：
```sh
# 根据自己的IP、用户名和port端口来输入
$ ssh admin@192.168.1.111 -p 26
```

关于Shell：
主页面设定里，还有可以设定Shell的地方，默认是BitviseShell。不是很好用，命令很少。
可以自己尝试一下别的shell。