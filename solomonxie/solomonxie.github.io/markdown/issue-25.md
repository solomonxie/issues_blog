# Vim成长之路
## 学vim的笔记。觉得这样历程型的笔记再好不过了。


## 配置：先从配置行号开始
> 其实对初学者来说，不需要太花哨的东西，只需要练习各种快捷键就好了。
但是没有行号是真的很头疼的，所以这是我第一步想做的。

可以直接在vim中输入命令达到效果：
`:set number`
但是这个不会保存，一退出就没有了。所以需要一个配置文件来长期维持。
这个文件就是vim最重要的配置文件了 `.vimrc`，一切的配置语句都写在这个文件里。
它的位置为_~/.vimrc_。
然后这么操作就够了：
```bash
touch ~/.vimrc
vim ~/.vimrc
```
然后在文件里随便找个空位置写上_set number_就ok了。


## 配置：设置颜色主题 
> 既然都开启了`vimrc`技能，就忍不住好奇心去看看还有什么能配置的。这里就不一一说明了，这个坑太大，配置方案太多。先讲个代表性的配色问题。以下在mac下有效。

首先, vim自带有一些基本的色彩主题，一般在`/usr/share/vim/vim74/colors/`中，如下图：
![Default Colors](https://user-images.githubusercontent.com/14041622/35219551-0c24371a-ffae-11e7-93dc-f1e59660b158.png)
这个文件夹由于权限原因，不能动。所以要到当前用户的用户文件夹来增加配置文件。一般当前用户是没有这个配置文件夹的，需要自己新建。
```shell
mkdir ~/.vim 
mkdir ~/.vim/colors
```
然后把下载好的色彩主题包中`/colors/`文件夹全部拷贝到`~/.vim/colors/`中就可以使用了。具体操作如下：
### 下载主题包

[参考：vim官方收集的各种主题包：Vim.org色彩主题集](http://www.vim.org/scripts/script_search_results.php?keywords=&script_type=color+scheme&order_by=creation_date&direction=descending&search=search)
[参考：Vim Colors - Online Preview](http://vimcolors.com/)
[下载：Vim colorschemes - one colorscheme pack to rule them all!](https://github.com/flazz/vim-colorschemes)
[下载：我比较喜欢的gruvbox主题](https://raw.githubusercontent.com/morhetz/gruvbox/master/colors/gruvbox.vim)

我这里下载了一个badwolf主题，是zip文件。解压后将主题包里`colors`文件夹内的`.vim`文件直接拷贝到`~/.vim/colors/`中即可。
然后在vim或`.vimrc`文件中输入这两句句话配置就成功了：
```vimrc
colorscheme 色彩主题名称
syntax on
```
效果如下图：
![image](https://user-images.githubusercontent.com/14041622/35219872-3d0bac90-ffaf-11e7-94a7-fe6e1531b692.png)



## Vim学习成长列表
> 参考 [Vim简明教程](http://blog.csdn.net/niushuai666/article/details/7275406)

- [x] 各种插入模式
a → 在光标后插入
o → 在当前行后插入一个新行
O → 在当前行前插入一个新行
cw → 替换从光标所在位置后到一个单词结尾的字符

- [x] 简单的移动光标
0 → 数字零，到行头
^ → 到本行第一个不是blank字符的位置（所谓blank字符就是空格，tab，换行，回车等）
$ → 到本行行尾
( ) → 跳转到当前区块的非空句首、句尾
[ or { → 跳转到目前区块开头。
] or } → 跳转到目前区块结尾。
g_ → 到本行最后一个不是blank字符的位置。
/pattern → 搜索 pattern 的字符串（陈皓注：如果搜索出多个匹配，可按n键到下一个）

- [x] 翻页
Ctrl+f和Ctrl+b  上下翻页
Ctrl+u和Ctrl+d 上下翻半页

- [x] 拷贝/粘贴
 （p/P都可以，p是表示在当前位置之后，P表示在当前位置之前）
P → 粘贴
yy → 拷贝当前行当行于 ddP

- [x] Undo/Redo
u → undo
<C-r> → redo

- [x] 打开/保存/退出/改变文件(Buffer)
:e <path/to/file> → 打开一个文件
:w → 存盘
:saveas <path/to/file> → 另存为 <path/to/file>
:x， ZZ 或 :wq → 保存并退出 (:x 表示仅在需要时保存，ZZ不需要输入冒号并回车)
:q! → 退出不保存 :qa! 强行退出所有的正在编辑的文件，就算别的文件有更改。
:bn 和 :bp → 你可以同时打开很多文件，使用这两个命令来切换下一个或上一个文件。

- [ ] 重复命令
. → (小数点) 可以重复上一次的命令
N<command> → 重复某个命令N次
2dd → 删除2行
3p → 粘贴文本3次
100idesu [ESC] → 会写下 100个`desu`
`.` → 重复上一个命令—— 100 “desu “.
`3.` → 重复 3 次 “desu”

- [x] 合并行
J 合并当前行和下一行
3J 连同当前行一共合并3行
- [ ] 行目跳转
NG → 到第 N 行 
gg → 到第一行
G → 到最后一行。
按单词移动：
w → 到下一个单词的开头。
e → 到下一个单词的结尾。

- [ ] 窗口跳转
Ctrl + w, 然后用JKHL方向键跳转
Ctrl + w 再按q, 退出当前窗口
:sp 将当前窗口分成两个




## Vim 安装插件管理器
安装插件前，一般都会用到`Vundle`这个插件包管理器。它的名字其实是`Vim bundle`的组合。
安装方法可以参考[官网](https://github.com/VundleVim/Vundle.vim)，说的很详细。简单说的话，安装方法如下：
```
git clone https://github.com/VundleVim/Vundle.vim.git ~/.vim/bundle/Vundle.vim
```
然后打开`~/.vimrc`，把下面这段话全部粘贴到文件顶部:
```
" Vundle phrases must be on the top
set nocompatible              " be iMproved, required
filetype off                  " required
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
    Plugin 'VundleVim/Vundle.vim'
call vundle#end()            " required
filetype plugin indent on    " required
```
其中`Plugin`的部分，可以删除不需要的插件。
保存后，直接在Vim界面里输入这个命令：`:PluginInstall`，或在外部运行`vim -c VundleUpdate -c quitall`。然后vim就会跳转到插件安装界面，并自动下载安装上面列出来的插件。
![image](https://user-images.githubusercontent.com/14041622/35513252-6192f5e4-053d-11e8-9c4d-f70aab0b8b54.png)
等到最下面显示`Done!`时，就安装完成了。需要整个退出Vim，再进入，就可以使用了。

## 删除插件
直接在`.vimrc`里把Plugin的那一行删除，然后在vim里运行`:PluginUpdate`即可，然后将`~/.vim/bundle/`下该插件的目录删除。


## Vim UltiSnips自动补全 （Python强依赖）
> 想要Vim像Sublime一样快速编程，就需要各种好的snippets快速生成一段预备好的代码。一般常用的插件是`UltiSnips`作为生成代码的引擎，`Vim-snippets`插件作为各种语言的常用语句包。

**注意：此插件极其依赖Python特定版本，一旦本地python版本有一丁点变动，整个vim的使用都会完全受阻！**

### 安装Snippets插件
在已有Vundle插件管理器的基础上，直接在`.vimrc`文件中加入这两个插件名：
![image](https://user-images.githubusercontent.com/14041622/35559228-243d437c-05e5-11e8-9c9f-4993bdd80282.png)
然后退出vim再进入vim，输入命令: `:PluginInstall`，等待安装完成后，重新进入vim，就可以正常使用了。

### 创建snippets
相比于sublime， 在vim中创建snippets是稍微麻烦点。主要跟随这几点：
- 找到插件目录，是位于`~/.vim/bundle/`下的`ultisnips`和`vim-snippets`。
- 不要在`vim-snippets`中预备好的各语言snippets上直接修改，因为每次更新都会被覆盖。
- 必须在`ultisnips`文件夹下创建一个`UltiSnips`文件夹，所有自定义代码都存在这里。
- 自定义的代码片段必须给每个语言创建单独文件，保存的文件名必须遵循`语言名.snippets`格式.如果是运用到所有文件上的，就叫`all.snippets`。
- 文件保存后即刻生效，无需重启vim。
- 代码片段文件里面需要遵循如下格式：
```vim
snippet  关键词 "描述" 生成模式
代码片段
endsnippet
```
其中，生成模式有很多种，一般为`b`，即只有在一行的开头输入关键词时，才会调用代码片段。其它还有b, A, w, i等模式，具体可以在vim 的`:help ultisnip`中查看文档。

举个例子，我们要为html文件做一些快捷代码，那么：
首先创建、或修改一个snippets文件：
```sh
$ vim ~/.vim/bundle/ultisnips/UltiSnips/html.snippets
```

然后添加如下格式的声明：
```vim
snippet html "create html 5 structure" b
<!DOCTYPE html>
<html>
<head><title></title></head>
<body>
</body>
</html>
endsnippet
```
保存后打开一个html文件，找个地方输入`html`然后按Tab，就会弹出预定好的html代码。
注意：由于安装了`vim-snippets`常用代码集，html文件中的很多关键词都被占用了，比如`html`。所以要避免冲突，可以直接到`~/.vim/bundle/vim-snippets/UltiSnips`中对应的文件中查看：
![image](https://user-images.githubusercontent.com/14041622/35560217-b50bba1c-05e7-11e8-8595-3109f8e68a48.png)


### snippets 高阶用法
> 上面只是输入关键词然后生成一段固定内容的方法。实际上更常用的方法是，根据给定的变量生成动态内容，或是指定需要更改的几个位置，生成内容后自动把焦点分别指向这几个位置供你修改。


## `UltiSnips插件报错：缺少的Python支持问题`
经常因为系统的Python版本变动，导致整个Vim瘫痪，起因就是这个Snippets插件。因为它完全依赖python，所以导致vim每次敲键盘都会报错。
![image](https://user-images.githubusercontent.com/14041622/39951062-fa1a1ab0-55b8-11e8-9be8-f404e66ee0ec.png)

#### Mac解决方案：
最简单的是通过升级vim解决。因为升级vim时，会重新根据当前的环境进行make编译。所以之前由于python版本的改变导致的问题，都这么解决了。
```shell
$ brew upgrade vim
```
注意：
网上找的话解决方案真的不多，如果有，也几乎都是劝你重新自己根据环境来手动make编译vim的。所以最好的方法还是upgrade vim，相当于自动重新编译了。


## 从源代码编译Vim 8.0 （当前环境：树莓派原生系统）
> 因为在安装某个vim最难安装的插件，必须要最新版本的vim才行，而通过`apt-get`是无法更新vim的，所以又必须要自己在本地编译源代码才行。所以才花了几个小时倒腾这个。我相信，非常非常非常多的人在编译vim都遇到了困难。

因为不敢在Mac自己机子上随便试，就拿树莓派练手。安装过程不光麻烦，而且耗时比较长。具体是参考[这篇文档](https://github.com/Valloric/YouCompleteMe/wiki/Building-Vim-from-source)安装，中文翻译版本在[这里](https://linux.cn/article-8094-1.html)。
简而化之，我使用的命令如下：
```shell
# 安装基础支持库
sudo apt install libncurses5-dev libgnome2-dev libgnomeui-dev \
    libgtk2.0-dev libatk1.0-dev libbonoboui2-dev \
    libcairo2-dev libx11-dev libxpm-dev libxt-dev python-dev \
    python3-dev ruby-dev lua5.1 lua5.1-dev libperl-dev git

# 删除已安装的vim和所有相关
sudo apt-get remove vim vim-runtime gvim vim-tiny vim-common vim-gui-common vim-nox

# 从vim的github上下载最新的源文件（太慢的话就直接手动去其github页面下载zip文件并解压）
cd ~
git clone https://github.com/vim/vim.git

# 初始化配置
cd vim
./configure --with-features=huge \
    --enable-multibyte \
    --enable-rubyinterp=yes \
    --enable-pythoninterp=yes \
    --with-python-config-dir=/usr/lib/python2.7/config \
    --enable-python3interp=yes \
    --with-python3-config-dir=/usr/lib/python3.5/config \
    --enable-perlinterp=yes \
    --enable-luainterp=yes \
    --enable-gui=gtk2 --enable-cscope --prefix=/usr
make VIMRUNTIMEDIR=/usr/share/vim/vim80

# 编译
cd ~/vim
sudo make install

# 设置vim为默认编辑器
sudo update-alternatives --install /usr/bin/editor editor /usr/bin/vim 1
sudo update-alternatives --set editor /usr/bin/vim
sudo update-alternatives --install /usr/bin/vi vi /usr/bin/vim 1
sudo update-alternatives --set vi /usr/bin/vim

# 检查vim版本
vim --version
```


## Vim原生补全工具 OmniComplete
用了一天倒腾自动补全插件，实在是崩溃，但凡有点名气的都对vim本身的编译有很麻烦的要求。搜索过程中才发现Vim其实是自带补全功能的，称为`OmniComplete`。
输代码的过程中，直接按`Ctrl+X`然后再按`Ctrl+O`，就会弹出vim猜测的一系列补全内容。可以在菜单里按“上下键”选择，注意是方向上下键，不是JK键。
经过测试，原生支持很多种语言。
![image](https://user-images.githubusercontent.com/14041622/35573497-42d7e634-0612-11e8-80de-75c35583f096.png)



# Vim键盘映射
> 之前一直在找方法将`Capslock`键映射为`Esc`键，这样vim中就不用每次跑很远去按Esc了。可惜MacOS最新版的系统都无法很好兼容市面上的键盘映射软件，就放弃了。
然后发现Vim其实本身就可以设置键盘映射，这样大好，原本对Key Mapping需求多的也只有Vim而已，其它地方不太需要这么乱七八糟的改键。

[参考：利器系列之 —— 编辑利器 Vim 之快捷键配置](http://blog.guorongfei.com/2015/09/03/vim-shortcut/)
[参考：VIM键位映射总结](https://blog.csdn.net/jalused/article/details/42708429)

## 递归绑定和非递归绑定
Vim 的快捷键绑定分为递归和非递归两种，比如：
```
" 非递归方式 (No-re-map) 不会把a转嫁到c
noremap a b
noremap b c

" 递归方式 (会把a转嫁到c)
map a b
map b c
```

![image](https://user-images.githubusercontent.com/14041622/40460620-3c098160-5f3a-11e8-8d4d-01a61801c0f3.png)


## 改键方法
- 方法一：直接在Vim中输入命令
`:map 原键 新键`,只是临时的改变，一般人都不怎么用。
- 方法二：在`.vimrc`中配置
打开文件后，随便找个地方加入改键命令即可。

## 特殊名称
```
<ESC> ESC键
<BS> backspace退格键
<CR> ENTER回车键
<Space> 空格键
<Shift> shift键
<Ctrl> ctrl键
<Alt> alt键
<F1>-<F12> F1到F12功能键<k0>-<k9> 小键盘数字0到9
<S-x> 大写S配合x，意味着shift+x组合键
<C-x> 大写C配合x，意味着ctrl+x组合键
<A-x> 大写A配合x，意味着alt+x组合键
```


## 常用映射

### `CapsLock`
注意：CapsLock在vim中无法被捕获，所以必须用额外的软件才可以达到。
Windows非常简单，用Autohotkey全解决。Mac可以用Karabiner。

### 括号自动补全
```vim
inoremap ( ()<Esc>i  
inoremap [ []<Esc>i  
inoremap { {}<Esc>i  
```


# `<Leader>键`
[参考。](http://learnvimscriptthehardway.stevelosh.com/chapters/06.html)

Vim的默认Leader前缀是`\`键。
说白了，就是一个快捷命令的前缀。
一般比如cc，dd之类都被占用，映射起来不方便。所以加上`前缀`后，就可以追加各种自己喜欢的快捷命令了。



## Vim注释的方法
> Vim里面注释对初学者真是比较头疼的事情。需要先$跳到行头，i插入模式，输入注释，Esc退出插入模式。如果批量就更麻烦。下面是几种常用方法。

1. 原生方法一
> `Ctrl+v`进入Block选择，向下移动选择待注释行，`Shift+i`批量插入，输入注释符，按两次Esc退出，等几秒实现批量注释。

2. `.vimrc`配置文件法
在`.vimrc`中加入如下语句：
```
" Commenting blocks of code.
autocmd FileType c,cpp,java,scala let b:comment_leader = '// '
autocmd FileType sh,ruby,python   let b:comment_leader = '# '
autocmd FileType conf,fstab       let b:comment_leader = '# '
autocmd FileType tex              let b:comment_leader = '% '
autocmd FileType mail             let b:comment_leader = '> '
autocmd FileType vim              let b:comment_leader = '" '
noremap <silent> ,cc :<C-B>silent <C-E>s/^/<C-R>=escape(b:comment_leader,'\/')<CR>/<CR>:nohlsearch<CR>
noremap <silent> ,cu :<C-B>silent <C-E>s/^\V<C-R>=escape(b:comment_leader,'\/')<CR>//e<CR>:nohlsearch<CR>
```
然后注释的快捷键是`,cc`，取消注释是`,cu`。

3. 插件法
常用插件有NerdCommenter，在`vimrc`的插件位置中加入`Plugin 'scrooloose/nerdcommenter'`，重新打开vim后输入`:PluginInstall`后安装成功。
注释的快捷键是`\cc`，反注释是`\cu`。其实和自己直接在vimrc中写没什么太大区别。
其它注释插件大同小异，就不都说了。


## Vim里Insert模式下不能按Backspace删除前面的内容
因为默认当前插入只能创建新内容，不允许改动别的东西。如果要变成Insert mode下随便编辑的模式，在`~/.vimrc`中加上：
```
set backspace=indent,eol,start
```
或者更简单的`set backspace=2`，效果一样。


# Vim中Tab变Space等相关设置
Tab和Space之争和Vim于Emacs是一样等，我是Vim和Space派。但是我和大多数人一样喜欢按Tab出Space。
在`~/.vimrc`中设置如下，重启vim就会生效：
```
set autoindent "换行时自动缩排 同时对应的还有其它两种模式 smartindent, cindent
set tabstop=4 "设定tab宽度为4个字符
set shiftwidth=4 "设定自动缩进为4个字符
set expandtab "用space替代tab的输入 取消的话 就用set noexpandtab "不用space替代tab的输入
retab "打开文件时自动转换所有tab为空格
```


# Vim快捷命令

- 上下行调换位置：`ddp`
- 前后字符调换位置：`xp`

### 删除命令
- 删至行尾：`d$`
- 删至行头：`d0`
- 此行以前所有行全部删除：`dgg`
- 此行以前所有行全部删除：`dG`
- 删除扩号之间内容：`di(` 注意，它非常只能，会识别到离自己最近的一组括号组
- 删除？号之间等内容：和引号之间一样，用`di`+符号，如单引号`di'`、双引号`di"`等。

### 删除、复制引号，括号中的内容
参考[这篇文章](http://blog.csdn.net/YHM07/article/details/44522315)。
下面的符号可以是`'   "  [  (  { `等，注意都是左半边。

以下的命令对标点内的内容操作
1. `ci`+符号：分别更改这些配对符号中的内容 
2. `di`+符号：分别删除这些配对符号中的内容 
3. `yi`+符号：分别复制这些配对符号中的内容 
4. `vi`+符号：分别选中这些配对符号中的内容 

如果把上面各条命令中的`i`改成`a`,可以连配对符号一起操作


# Vim Movement Commands

![image](https://user-images.githubusercontent.com/14041622/35904841-a4c7c586-0c1f-11e8-9ae0-374cb310541a.png)



# Vim产生的`.swp`文件
参考文章：[VIM不正常退出产生的swp文件](http://blog.csdn.net/pwiling/article/details/51830781)
常用关于swp文件的命令或`vimrc`配置：
- 查看当前目录下的所有swp文件: `vim -r`
- 恢复文件：`vim -r filename`，上次意外退出没有保存的修改，就会覆盖文件。
- 停止vim产生交换文件：在`~/.vimrc`中加入`set noswapfile`
- 定时自动保存文件：
```
set updatetime=23000 " 设置每200个字符保存一次
set updatecount=400 " 设置每4秒保存一次
" set updatecount=0 " 不保存交换文件
```
- 设置交换文件默认目录：`set directory=./tmp`


# Vim自动运行（或编译运行）文件
不像SublimeRepl需要安装插件，Vim原生支持直接运行python等代码。只要输入命令：
`:!python %`
其它语言代码类似。
输入命令后，vim界面会暂时跳出编辑页面跳到终端页面显示执行过程，期间可以按任意键返回vim编辑页面。
输过一次后，就可以用`:!!`直接重复上次的命令，不用再输一遍命令。
![screencast 2018-02-07 16-17-40](https://user-images.githubusercontent.com/14041622/35906002-00ab9e64-0c24-11e8-86c6-a72026149396.gif)



# Vim左下角总显示"recording"
这是因为不小心按到了`q`键，进入了录制宏模式。
再按以下`q`就退出了。


# Vim支持鼠标滚动界面
Mac下，Vim支持鼠标滚动光标，通过光标移动上下翻动页面。但是这样太别扭了，我们需要的是滚轮控制界面滚动，如vim中`ctrl+e`一样的效果。
简单：`~/.vimrc`中加一句`set mouse=a`即可。
不过这样设置会导致每次用鼠标选择一段文本都会自动进入visual模式，这样的话我们就没法复制到系统剪切板了。
网上说mouse后一个-好即可，如`set mouse-=a`，但是试过没用。
这时候，需要按住`Alt`键然后再用鼠标选择文本，这样一来就不会启动v模式，且可以复制到剪切板。


# Vim里批量查找替换文字
没有一般编辑器按快捷键那么方便，需要以输入一条命令的方式才能执行。
格式如下：
- 对当前行执行替换  `:s/查找内容/替换内容/g`
- 在全文执行替换  `:%s/查找内容/替换内容/g`
- 对选中行中内容进行批量替换  用v模式选中行然后`s/查找内容/替换内容/g`

大概可以看到，`s`代表执行search命令，`%`代表全文执行，`/`是相当于分隔符，`g`代表global对指定范围内所有结果进行替换，如果没有`g`那么只替换第一个找到的结果。


# Vim 的Git插件 - `Fugitive`
在vim里面操作，总是切换出去用git命令提交，一开始学习阶段还好，但是慢慢也烦了，就找到了这款最通用的插件，而且是Vundle管理器的默认搭配插件。
[参考文章](http://vimcasts.org/episodes/fugitive-vim---a-complement-to-command-line-git/)。
常用命令如下：
![image](https://user-images.githubusercontent.com/14041622/36022290-9060671a-0dc3-11e8-98c7-6b37f7160f34.png)



# Vim的NerdTree插件
> 一个项目文件多起来时，左边的文件树菜单是必要的。

[参考：常用文件树快捷键](https://yang3wei.github.io/blog/2013/01/29/nerdtree-kuai-jie-jian-ji-lu/)
[所有命令及推荐键盘映射：官方](https://github.com/scrooloose/nerdtree/blob/master/doc/NERDTree.txt)

![image](https://user-images.githubusercontent.com/14041622/40785675-c52d07fa-651b-11e8-82d7-c6520ce91e4f.png)

在vundle插件管理的方式，直接在`~/.vimrc`中的Plugin段落中加入`Plugin "scrooloose/nerdtree
"`然后重启Vim并输入`PluginInstall`，即可完成安装

然后输入`: NERDTreeToggle`即可打开文件树。当然，默认是关闭的，需要每次都输入命令打开。
还可以设置vim快捷键来映射,在vimrc中加入：
```
map <F3> :NERDTreeMirror<CR>
map <F3> :NERDTreeToggle<CR>
```


## 切换工作台和目录
```
ctrl + w + h    光标 focus 左侧树形目录
ctrl + w + l    光标 focus 右侧文件显示窗口
ctrl + w + w    光标自动在左右侧窗口切换
ctrl + w + r    移动当前窗口的布局位置

o       在已有窗口中打开文件、目录或书签，并跳到该窗口
go      在已有窗口 中打开文件、目录或书签，但不跳到该窗口
t       在新 Tab 中打开选中文件/书签，并跳到新 Tab
T       在新 Tab 中打开选中文件/书签，但不跳到新 Tab
i       split 一个新窗口打开选中文件，并跳到该窗口
gi      split 一个新窗口打开选中文件，但不跳到该窗口
s       vsplit 一个新窗口打开选中文件，并跳到该窗口
gs      vsplit 一个新 窗口打开选中文件，但不跳到该窗口
!       执行当前文件
O       递归打开选中 结点下的所有目录
m    文件操作：复制、删除、移动等
```

## 切换标签页
```
:tabnew [++opt选项] ［＋cmd］ 文件      建立对指定文件新的tab
:tabc   关闭当前的 tab
:tabo   关闭所有其他的 tab
:tabs   查看所有打开的 tab
:tabp   前一个 tab
:tabn   后一个 tab

标准模式下：
gT      前一个 tab
gt      后一个 tab
```

### 刚开始使用时候的小问题
目前问题是，不能保存所有打开文件的状态。在同一个tab中打开另一个文件时，之前文件的编辑历史都会丢失，也就是没法`u`撤销编辑。即使有相关的方法控制这些，只是作为一个文件菜单来说，这也太麻烦了。
解决方案：
文件都在新tab打开，这样就可以保持各自状态了。

## 常用键盘映射
![image](https://user-images.githubusercontent.com/14041622/40790652-1391d6b2-6528-11e8-8088-902418cf5de3.png)


## NerdTree 在 .vimrc 中的常用配置
```
autocmd vimenter * NERDTree  "自动开启Nerdtree
"let g:NERDTreeWinSize = 25 "设定 NERDTree 视窗大小
"开启/关闭nerdtree快捷键
map <C-f> :NERDTreeToggle<CR>
"let NERDTreeShowBookmarks=1  " 开启Nerdtree时自动显示Bookmarks
"打开vim时如果没有文件自动打开NERDTree
autocmd vimenter * if !argc()|NERDTree|endif
"当NERDTree为剩下的唯一窗口时自动关闭
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
"设置树的显示图标
let g:NERDTreeDirArrowExpandable = '▸'
let g:NERDTreeDirArrowCollapsible = '▾'
let NERDTreeIgnore = ['\.pyc$']  " 过滤所有.pyc文件不显示
"let g:NERDTreeShowLineNumbers=1  " 是否显示行号
let g:NERDTreeHidden=0     "不显示隐藏文件
"Making it prettier
let NERDTreeMinimalUI = 1
let NERDTreeDirArrows = 1
```

## Nerdtree隐藏某些指定文件
Vim经常产生swp缓存文件，还有一些python产生的pyc文件，Nerdtree显示出来很不好看，最好屏蔽掉。
在vimrc中配置这几句话可以达到效果：
```vim
" 不显示隐藏文件
let g:NERDTreeHidden=0
" 过滤: 所有指定文件和文件夹不显示
let NERDTreeIgnore = ['\.pyc$', '\.swp', '\.swo', '\.vscode', '__pycache__']  
```

## Nerdtree刷新
正常下Nerdtree是不会自动刷新的，文件删除了，多了都不会自动显示。
但是其实不用退出vim，
按`r`就一下子刷新了。

## NerdTree的美化
> 用多了Vim,就需要nerdtree树形菜单，用多了菜单，就像把它美化。

一般最常用的美化Nerdtree插件就是[`vim-devicons`](https://github.com/ryanoasis/vim-devicons)，详细配置方法在github官网有，主要如下：
1. 安装 `Nerd Font`字体，[网址在此](https://github.com/ryanoasis/nerd-fonts)。安装字体的方法每个电脑系统不一样。因为全部字体多到3G，所以最快到方法是到[官网首页](http://nerdfonts.com/)点击Download，下载`Droid Sans Mono Nerd`这个字体，8M左右，下载好了如果是Mac的话，就选择压缩包里的`Droid Sans Mono Nerd Font Complete.otf`，双击安装。
2. 在Terminal.app或iTerm2的系统设置里，设置字体为`Droid Sans Mono Nerd`。
3. 在`~/.vimrc`中插件管理处加入`Plugin 'ryanoasis/vim-devicons'`，重启vim然后`:PluginInstall`进行下载安装。
4. 在`~/.vimrc`中配置默认编码`set encoding=utf8`和默认字体`set guifont=DroidSansMono_Nerd_Font:h11`
完成。
然后就会变成这个样子：
![image](https://user-images.githubusercontent.com/14041622/36613461-89b90172-1914-11e8-8c6e-72882a65899a.png)

## 进一步美化： `vim-nerdtree-syntax-highlight`插件
[`vim-nerdtree-syntax-highlight`](https://github.com/tiagofumo/vim-nerdtree-syntax-highlight)插件是配合上面`vim-devicons`插件增强的。直接在vimrc中`Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'`，重启并`:PluginInstall`即可。效果如下：
![image](https://user-images.githubusercontent.com/14041622/36613881-c8500556-1915-11e8-9729-57167564c848.png)


注意：安装完`vim-devicons`后，vim速度已经有些许延迟了，再安装这个插件会感受到更明显的延迟。



### Text editors learning curves
![image](https://user-images.githubusercontent.com/14041622/36091285-3ec383bc-101e-11e8-82e6-4e1e785142fc.png)



# Vim NerdTree的美化
> 用多了Vim,就需要nerdtree树形菜单，用多了菜单，就像把它美化。

一般最常用的美化Nerdtree插件就是[`vim-devicons`](https://github.com/ryanoasis/vim-devicons)，详细配置方法在github官网有，主要如下：
1. 安装 `Nerd Font`字体，[网址在此](https://github.com/ryanoasis/nerd-fonts)。安装字体的方法每个电脑系统不一样。因为全部字体多到3G，所以最快到方法是到[官网首页](http://nerdfonts.com/)点击Download，下载`Droid Sans Mono Nerd`这个字体，8M左右，下载好了如果是Mac的话，就选择压缩包里的`Droid Sans Mono Nerd Font Complete.otf`，双击安装。
2. 在Terminal.app或iTerm2的系统设置里，设置字体为`Droid Sans Mono Nerd`。
3. 在`~/.vimrc`中插件管理处加入`Plugin 'ryanoasis/vim-devicons'`，重启vim然后`:PluginInstall`进行下载安装。
4. 在`~/.vimrc`中配置默认编码`set encoding=utf8`和默认字体`set guifont=DroidSansMono_Nerd_Font:h11`
完成。
然后就会变成这个样子：
![image](https://user-images.githubusercontent.com/14041622/36613461-89b90172-1914-11e8-8c6e-72882a65899a.png)

## 进一步美化 `vim-nerdtree-syntax-highlight`插件
[`vim-nerdtree-syntax-highlight`](https://github.com/tiagofumo/vim-nerdtree-syntax-highlight)插件是配合上面`vim-devicons`插件增强的。直接在vimrc中`Plugin 'tiagofumo/vim-nerdtree-syntax-highlight'`，重启并`:PluginInstall`即可。效果如下：
![image](https://user-images.githubusercontent.com/14041622/36613881-c8500556-1915-11e8-9729-57167564c848.png)


注意：安装完`vim-devicons`后，vim速度已经有些许延迟了，再安装这个插件会感受到更明显的延迟。


# Vim报错`Sorry, this command is disabled, the Python's site module could not be loaded.`
一般是在系统中改动了python的环境或什么，导致vim的一些插件无法使用python。
测试：在vim里面输入`:py print('hello')`。如果返回这个错误，说明vim没有找到python。
然后在vim里输入`:echo has('python')`和`:echo has('python3')`，哪个显示`0`哪个也是没有的。

![image](https://user-images.githubusercontent.com/14041622/36629273-b7315026-198e-11e8-88cd-955c5391f73c.png)

通过这个命令，`vim --version | grep python`，我们先查看下当前vim版本对python的支持：
![image](https://user-images.githubusercontent.com/14041622/36629495-5017d3ee-1991-11e8-931c-10a0dfbd2872.png)
说明我当前的vim支持python，不支持python3.
另外，直接`vim --version`可以先看到，我的vim已经用`brew install vim`更新到了vim 8.0:
![image](https://user-images.githubusercontent.com/14041622/36629502-7632045a-1991-11e8-97ee-54d1c2c08ce2.png)
所以出错原因就在于这里了。真是不应该随便`brew install vim`，之前vim是7.4。
各种查找资料后（国内解决方案很少，国外解决方案也集中在vim官方github的issues里面），找到[这个简单易懂的方案](https://github.com/editorconfig/editorconfig/wiki/FAQ#when-using-the-vim-plugin-i-got-e887-sorry-this-command-is-disabled-the-pythons-site-module-could-not-be-loaded)：
![image](https://user-images.githubusercontent.com/14041622/36629637-5deba638-1993-11e8-979f-05f4658c2978.png)
上面说了，基本大家在Mac上遇到这个问题都是brew升级vim版本后产生的。所以再用`brew uninstall vim`就可以了，如果还不行，就再uninstall后加条件:`brew reinstall vim --with-custom-python`。
再不行的话，就按照本机的python支持情况按个例解决了。
我直接`brew reinstall vim`就解决了。


# Vim 文件操作
[参考：在 Vim 中进行文件目录操作](https://harttle.land/2016/10/14/vim-file-and-directory.html)

```vim
# 新建文件/打开文件
: e [FILE-NAME]

# 新建文件 （只打开半个窗口 另半个窗口保留之前的文件）
:new [FILE-NAME]

# 退出 (如果文件更改则保存)
:x 
```

## 打开目录
```vim
:e FOLDER-PATH    " 编辑该目录
:Explore .      " 浏览该目录
:Sexplore .     " 在水平分割窗口中浏览该目录
:Vexplore .     " 在垂直分割窗口中浏览该目录
```

## 调用bash命令
```vim
# 列出文件
:!ls

# 删除文件
:!rm foo.txt
```


# Vim文本复制
> Vim的文本复制，逻辑上要比我们日常的拷贝、粘贴要复杂些。

之前看了很多文章，真是太复杂了，复制个东西搞得好像系统性的工程建设一样。其实两句话就解释明白的。
[参考这篇文章：vim的剪切板](https://segmentfault.com/a/1190000000382847)

首先输入`:reg`命令，查看Vim记录的所有剪切板内容，大概是这样的：
![image](https://user-images.githubusercontent.com/14041622/40037189-6e024c5e-583e-11e8-9566-c1650f619ef2.png)


常用命令：
```vim
:reg        #查看所有注册的剪切板内容

""            #Vim内部的默认剪切板

"+           #Vim外部的剪切板，也就是系统的剪切板, 复制粘贴到它就能和其他编辑器交互了

"3y        #把文本复制到第3个剪切板

"+y        #复制到系统板

"+p        # 从系统板粘贴
```

### 举例1（Vim内部复制粘贴）：
在Normal模式下，用`v`命令开始选择文本，然后按下`"1y`，就把已经选中的文本存到了`编号1`的剪切板。需要用的时候，就在vim中进入Normal模式，然后按下`"1p`，就粘贴出来啦。

### 举例2（Vim与系统其他程序交换复制粘贴）:
随便在网页里复制一段话，然后进入vim的Normal模式，按下`"+p`，就把刚才的文字粘贴出来了。
反过来，在Vim的Normal模式下，按`v`命令开始选择一段文本，然后按下`"+y`，就把文字复制到系统的剪切板了，随便找个文本编辑器如Sublime Text，按`Ctrl+v`，就会发现刚才复制的内容粘贴出来了。


# Vim的自动缓存文件`.swp`
Vim不会帮你自动保存当前文件，但是它会帮你创建一个缓存文件，一旦不正常退出或掉线，你能通过这个文件快速recover恢复过去。

恢复文件的命令：
```shell
# 如果是在vim内
:rec

# 如果是在vim外
vim -r FILENAME
```

[参考：VIM不正常退出产生的swp文件](https://blog.csdn.net/pwiling/article/details/51830781)

找到`~/.vimrc`加入这些内容可以设置缓存文件：
```vim
" ---- Swap files (for recovery) ----
set swapfile    "enable swap file
set updatetime=23000   "save swap file every amount of ms
set updatecount=20     "save swp file every amount of characters
set directory=/tmp    "set swp file directory. 
```


# `Vim的vim-multiple-cursors插件`

[官方Github链接。](https://github.com/terryma/vim-multiple-cursors)

这个插件是可以像Sublime Text一样快捷多选文本的插件。
![example2](https://user-images.githubusercontent.com/14041622/40489256-465b106e-5f9b-11e8-9ed2-0eae87f64102.gif)

总结：
虽然看起来很爽，其实操作起来并没有想象中的那么简单，离Sublime Text的多选便捷度差太远。
而且又要重新学习一套东西，记住一系列的命令。而且还要用到各种方向键。所以还不如用Vim原生的多选功能。真的没有必要。


# Vim 在Insert模式下粘贴速度很慢的问题

一般当我们在Insert模式下粘贴一段超大量的文本，比如1000行。那么Vim会变得奇慢无比，大概半分钟？

所以，如果我们要粘贴文本，需要用另一种方法：在Normal模式下调用系统粘贴版进行粘贴，命令如下：
```
"+p
```
这样速度就超快了，一瞬间完成。


# Vim配置状态栏 Status line
Vim里一个好看的状态栏是非常加分的。

### `vim-lightline` 简单好安装的状态栏

安装方法：
Vundle管理器的话，在`~/.vimrc`中的插件函数中加上：

然后在函数外写上：
```vim
# 把这句加到vundle函数里：
Plugin 'itchyny/lightline.vim'

# 把这两句加到函数外面任意地方：
set laststatus=2
let g:lightline = { 'colorscheme': 'powerline', }
```

![image](https://user-images.githubusercontent.com/14041622/40912076-2532cc3e-6823-11e8-9e55-17e3a73c3c09.png)

## `vim-powerline` 从入门到放弃
和其它插件一样用Vundle安装：
```vim
# 把这句加到vundle函数里：
Plugin 'Lokaltog/vim-powerline'

# 把这两句加到函数外面任意地方：
set laststatus=2
set t_Co=256
let g:Powerline_symbols= 'unicode'
set encoding=utf8
```

但是安装完了会变成这个样子：

![image](https://user-images.githubusercontent.com/14041622/40912706-eb7aa168-6824-11e8-828b-3a9a70ec4903.png)

看了很多网上文章，没什么简单有效的方法。先放一放看看有没有别的代替品吧。

## `vim-airline` 最佳状态栏
虽说是powerline的fork，但是照我看比powerline强大的多。而且配置简单，效果多样，官方文档很清洗。一步到位。

[参考：Vim-airline 官方文档](https://github.com/vim-airline/vim-airline)
[参考：vim-airline-themes-screenshots](https://github.com/vim-airline/vim-airline/wiki/Screenshots)

安装：
```vim
# 把这句加到vundle函数里：
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'

# 把这几句配置加到函数外面任意地方：
" @airline
set t_Co=256      "在windows中用xshell连接打开vim可以显示色彩
let g:airline#extensions#tabline#enabled = 1   " 是否打开tabline
"这个是安装字体后 必须设置此项" 
let g:airline_powerline_fonts = 1
set laststatus=2  "永远显示状态栏
let g:airline_theme='bubblegum' "选择主题
let g:airline#extensions#tabline#enabled=1    "Smarter tab line: 显示窗口tab和buffer
"let g:airline#extensions#tabline#left_sep = ' '  "separater
"let g:airline#extensions#tabline#left_alt_sep = '|'  "separater
"let g:airline#extensions#tabline#formatter = 'default'  "formater
let g:airline_left_sep = '▶'
let g:airline_left_alt_sep = '❯'
let g:airline_right_sep = '◀'
let g:airline_right_alt_sep = '❮'
```

默认安装好后是这样的：

![image](https://user-images.githubusercontent.com/14041622/40913065-01d7c44e-6826-11e8-803e-3a656e01ebf2.png)



# Vim Buffer缓冲区：多文件编辑方案
> Buffer听起来很高大尚，实际上的功能和Tab、window是一模一样的。只是这些东西的内在实现不一样而已了。

Buffer是Vim自带的多文件编辑方式，有了它其实你不用单装Nerdtree插件来实现多标签编辑。
这是看个人习惯吧。
虽然我已经习惯了用Nerdtree做多文件多标签编辑，但是学习一下Vim自带的buffer方式也不错。

[参考：Vim 多文件编辑：缓冲区](https://harttle.land/2015/11/17/vim-buffer.html)

注意：默认来讲，如果你修改了文件但还没保存，是不能切换buffer的。但是这样会很不方便，不像切换tab一样。我们可以在vimrc中设置来取消这个限制：
```vim
set hidden
```
但是要知道，没有保存的话，是不能关闭buffer的。

怎样开启buffer？
实际上，buffer一直在开启着。这是你每次用`:e file`切换文件，或者在Nerdtree上按`o`打开文件，都是把当前的画面切换成了新文件你没有注意到而已。
实际上背后的buffer一直都在，你只要打开过一次的，都可以切换回去。

其实在没有安装`vim-airline`状态栏之前是没有注意到的，但是airline好心的有功能在最上方显示buffer，才让我觉得其实buffer有时候可能会比tab标签更好用。

## 常用命令
```vim
" List Buffers 查看当前所有的buffer 
:ls b

" Buffer Next 下一个buffer
:bn

" Buffer Previous 上一个buffer
:bp

" Buffer Down 关闭当前buffer
:bd

" Buffer number 指定第二个buffer
:b 2


```

## 快捷键设计
如果要保证buffer的切换像tab一样方便，肯定是要设置快捷键的，要不然总输入命令太慢了。
```vim
"按Ctrl+h 向左移动一个buffer
nnoremap <C-h> :bp<CR>
"按Ctrl+l 向右移动一个buffer
nnoremap <C-l> :bn<CR>
"按Ctrl+^ 关闭当前buffer
nnoremap <C-^> :bd<CR>
```


# Vim Recording 录制动作并重复
我不是很喜欢`宏`这个词，很简单的东西把它弄复杂了。

Vim记录你的一系列动作很简单，关键字是`q`。记录并重复一系列的动作，只要这样做：
- 按`q`和`{0-9a-zA-Z}`中任意一个字，比如`q1`，开始记录动作。
- 状态栏显示：`recording @1`。
- 开始做一系列的动作，改词，删字，等等。
- 按`q`，结束当前的记录。
- 按`@1`，重现刚才记录的动作。


# Vim原生的自动补全Autocomplete

在Insert编辑模式时，输入某个词，然后：
- 按`Ctrl+x`再按`Ctrl+l`，就会显示出一个提示列表。
- 按`Ctrl+n`或`Ctrl+p`上下选择。

当然，这样按键太麻烦，我们要做键盘映射了：
```vim
" 按Ctrl+d显示自动补全
inoremap <C-d> <C-x><C-l>
```


# Homebrew更新后Vim无法打开问题

很久不使用brew安装东西，安装了一个小软件，结果Homebrew直接更新python到3.7版本，然后导致Vim完全无法打开。报错如下：
```
dyld: Library not loaded: /usr/local/opt/python/Frameworks/Python.framework/Versions/3.6/Python
  Referenced from: /usr/local/bin/vim
  Reason: image not found
[1]    38809 abort      vim
```

尝试重新安装Vim：
```sh
$ brew reinstall vim
```
但是经过长时间安装后，仍然失败：
![image](https://user-images.githubusercontent.com/14041622/42413775-d5db3968-8259-11e8-8253-8c374f90e1e3.png)


最后通过这个解决：
```sh
$ brew uninstall --ignore-dependencies perl
$ brew uninstall vim
$ brew install vim
```


# Vim Snipmate 自动补全插件

在`~/.vimrc`的Vundle插件管理函数中添加以下内容(插件本身和所依赖的插件)：
```vim
    Plugin 'MarcWeber/vim-addon-mw-utils'
    Plugin 'tomtom/tlib_vim'
    Plugin 'garbas/vim-snipmate'
    Plugin 'honza/vim-snippets' "massive common snippets
```

然后在Vim中输入命令安装插件：
```
:source %
:PluginInstall
```
完成。

## 使用方法
输入状态下，直接按<Tab>，就会自动打出相关的snippets预设片段。


## 如何自定义snippets
直接在`~/.vim/snippets/`目录下添加`*.snippets`文件即可。

注意以下几点：
- `~/.vim/snippets/`目录是位于所有插件之外的，所以不会因插件更新而被删除。
- 如果你也安装了`vim-snippets`，那么在trigger同名的时候，vim会在状态栏弹出选项让你选择使用哪个snippets。

比如针对所有python文件，那就在`~/.vim/snippets/`目录下创建一个`python.snippets`文件，内容格式如下：
```vim
snippet #!
    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
```
以上片段，只要你在python文件中输入`#!`并按下<Tab>，就会自动输出定义的那段内容。




# Vim下方总是弹出总是弹出`enter or type command to continue`或`Error E349 no identifier under cursor`

![image](https://user-images.githubusercontent.com/14041622/42730507-4c6e8e4e-8828-11e8-809c-81d4189eb523.png)


这个很恼火。搜了一圈发现，有人说是`vimrc`的配置出了问题，但是就算我把vimrc整个清空了也还是有这个问题。



# Vim中的搜索高亮

[参考：在 Vim 中优雅地查找和替换](https://harttle.land/2016/08/08/vim-search-in-file.html)




# Vim鼠标支持问题

Vim高版本默认是支持鼠标滚动的。但是在Tmux中就不可以。

这样可以通过在`~/.vimrc`中设置`set mouse=a`来达到开启鼠标支持的左右。
`a`模式为`all`，即鼠标的"完全支持模式": 在所有情况下都支持鼠标，包括鼠标定位到某行，某个单词，甚至在tmux中。

但是`set mouse=a`有一个缺点不好解决就是：鼠标选择文字的话，会默认进入Visual模式。