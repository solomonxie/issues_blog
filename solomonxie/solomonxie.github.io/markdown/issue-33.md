# OS：Linux/MacOS/Win 操作杂疑症状
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
