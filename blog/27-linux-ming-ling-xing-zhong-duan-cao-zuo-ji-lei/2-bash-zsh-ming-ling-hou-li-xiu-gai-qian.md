# ❖ Bash/ZSH 命令后里修改前缀 (隐藏用户@主机，添加Git分支名称)

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

