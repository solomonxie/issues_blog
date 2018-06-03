# Git Workflow
> 主要记录Git从零开始学习的一些常用流程和指令 

## Online Courses
- [ ] [GitHub Training & Guides (Youtube)](https://www.youtube.com/user/GitHubGuides/videos)



# Git Workflow 1: Beginner's flow
> 最简单的Git工作流--即给初学者的工作流，尽量避免多分支，现在master分支上把常用指令学明白，然后再开启分支合流模式。

## 第一步 建立仓库 (Init | Clone)
一般会提到`git init`这个指令，在本地某个文件夹执行它就会把这个文件夹建立成一个git项目。但是我们初学者一般不是这个流程，我们需要建立一个github的repo，并将本地和它联通，反而简单很多。
首先直接到github首页新建一个repo，建好了以后直接点clone按钮复制.git结尾的链接。在本地用`git clone`命令克隆到本地生成一个文件夹项目。如果本地已经做了一些文件，那就把文件复制进这个文件夹就好了。
命令如下：
```
$ git clone 项目克隆网址 本地路径
```
然后进入文件夹开始项目即可。

## 第二步 本地提交 (commit)
先不涉及远程repo仓库，git需要在本地完成提交，常规三步如下：
```git
# 查看本地文件变动状态
$ git status
# 添加变动文件到预备区
$ git add --all
# 完成提交
$ git commit -m "变动描述"
```
然后本地的准备就完成了，随时可以连接远程仓库。

## 第三步 远程提交 (push)
一般情况下，远程仓库都是我们自己的，拥有所有权限，所以暂不涉及向其他人的仓库提交（pull request)一类概念。
所以只需推送到远程自己的仓库，一句话`git push`即可。
然后如果在安装git后设置过通用的用户名和邮箱，这里就只会要求你输入密码，然后就可以上传本地提交到远程repo仓库里了。
就这么简单。前三步基本流程如下图：
![image](https://user-images.githubusercontent.com/14041622/35376835-c56c8fca-01e7-11e8-9e7c-bdcce610a390.png)

## 第四步 远程抓取 (pull)
有的时候会用别的机器（比如公司）提交一些变化到远程，然后回家后想把变化同步到本地。
如果远程也是自己的repo拥有完全权限，那么直接`git pull`即可完成一切同步。


# 初次运行Git的配置
> Linux和Mac的git安装都很方便很多是自带的，Windows则强烈推荐安装Git Bash整个终端，包括了git本身以及所有常用的linux指令。

初始配置不是必要的。
因为主要是配置通用的用户名和邮箱，方便每个项目登录github并上传用的。简单就是两句话设置好：
```git
$ git config --global user.name "John Doe"
$ git config --global user.email johndoe@example.com
```
这两句话就会分别设置好当前电脑用户的通用github（或其他服务商）登录名和邮箱，密码不在这里写是要在用的时候才在命令行里输入。

其实我要将的不是这两句话，网上很多人说过。只是要讲其实用`git config`命令的作用，只是把内容帮你加到`~/.gitconfig`这个文件里而已。虽然效果一样，但是便于日后管理所有git的配置内容，强烈建议不用命令输入，而是直接到这个文件里面改。参考下图：

这个是默认状态下的配置文件：
![image](https://user-images.githubusercontent.com/14041622/35375662-d31c1f1e-01e2-11e8-9f13-3dc06d4fb553.png)

这个是利用`git config`命令后的文件：
![image](https://user-images.githubusercontent.com/14041622/35375761-3536ff7a-01e3-11e8-9bd8-cae9f52e6e47.png)

所以为了日后方便管理，还是直接改文件的好。
另外，详细初始配置，如默认编辑器是vim还是emacs，differ用哪个编辑器显示等细节，参考git官方文档。[起步 - 初次运行 Git 前的配置](https://git-scm.com/book/zh/v1/%E8%B5%B7%E6%AD%A5-%E5%88%9D%E6%AC%A1%E8%BF%90%E8%A1%8C-Git-%E5%89%8D%E7%9A%84%E9%85%8D%E7%BD%AE)


# .gitignore文件
> 整个项目里面肯定会有这个文件的，用来屏蔽一些文件的记录和上传。比如一些临时文件夹和涉及隐私的文件，就不需要传到github上了。

## 语法
简单说起来就是：
- 直接写一个名字（文件名或文件夹名），它就是被屏蔽的;
- 在名字前加上`!`就是不被屏蔽的，用于屏蔽整个文件夹时却不屏蔽其中的某个文件;
- `#`是注释符号;
- 名字里的`*`会代替名字里不限量的字，如`*.gif`, `test*.html`;
- 直接写文件夹名，只会屏蔽直属于该文件夹的所有文件，但不会屏蔽其子文件夹;
- 文件夹名后加`/`，就会屏蔽其中所有文件和文件夹，包括子文件夹

引用一个[网上文章](https://www.jianshu.com/p/ea6341224e89)的例子：
```gitignore
# 忽略 .a 文件
*.a
# 但否定忽略 lib.a, 尽管已经在前面忽略了 .a 文件
!lib.a
# 仅在当前目录下忽略 TODO 文件， 但不包括子目录下的 subdir/TODO
/TODO
# 忽略 build/ 文件夹下的所有文件
build/
# 忽略 doc/notes.txt, 不包括 doc/server/arch.txt
doc/*.txt
# 忽略所有的 .pdf 文件 在 doc/ directory 下的
doc/**/*.pdf
```
再加一篇网上文章：[彻底理解.gitignore](http://ybin.cc/git/gitignore-syntax/)


## 提交错误 error: There was a problem with the editor 'vi'.
在Mac上，可能之前重装vim变动了一些设置，所以才会有这个错误，导致git不能提交。
![image](https://user-images.githubusercontent.com/14041622/35610332-d81089b6-069b-11e8-949d-7a1e3e951532.png)
查了后解决方案很简单，直接输入：
```shell
git config --global core.editor $(which vim)
```


# Git为每个repo设置不同的用户名
之前讲过在电脑本地文件夹中`~/.gitconfig`文件即可设置本机的通用用户名，用来登录远程。
但我常会把公开代码上传到github，私密代码上传到Bitbucket，所以需要不同的登录名等。
Git其实可以为每个repo设置单独的用户名用来登录远端，像global的用法一样，可以命令行里设置也可以直接在文件里写：
```
$ git config user.name "John Doe"
$ git config user.email johndoe@example.com
```
手动改写文件的话，就位于repo目录中的`.git/config`这个文件。
设置的格式和`~/.gitconfig`完全一样，具体参考git初始配置那篇。


# Git误删文件恢复的方法
Stackoverflow的这个回答相当不错，我也很快找回了文件。[参考链接](https://www.quora.com/How-can-I-recover-a-file-I-deleted-in-my-local-repo-from-the-remote-repo-in-Git)
具体说起来是这样的，
```
# If the deletion has not been committed, 
# the command below will restore the deleted file in the working tree.
git checkout -- <file>

# You can get a list of all the deleted files in the working tree using the command below.
git ls-files --deleted

If the deletion has been committed, find the commit where it happened, then recover the file from this commit.
git rev-list -n 1 HEAD -- <file>
git checkout <commit>^ -- <file>
```


# 阿里云Code (Git托管）的初始设置
最近在考虑有的时候想托管一些国内方便的内容比如当cdn使用，还有码云什么的，比较了下易用性和容量，仅有的几个托管商里也就阿里云最合适，也最接近github。
[链接](https://code.aliyun.com/)
其它都是正常操作，唯一遇到的问题是git push的时候总是无法完成用户认真，在git里面设置了user.name和email等都不行。
原来阿里云code的登录密码是单独设置的，不能直接用自己的账号密码去登录，
必须要在阿里云Code的管理后台里面找到密码设置，然后选择忘记密码（修改密码没用，因为没有原始密码，只能点忘记密码）。

发邮件确认后，设置密码，就可以登录了。
所以这里git push时，用户名是阿里云的账号email， 密码是Code的单独密码。
参考[官方文档](https://help.aliyun.com/document_detail/60018.html#h1-u4E2Au4EBAu8BBEu7F6E)。

但是！这时候还不能做push等远程操作。如图：
![image](https://user-images.githubusercontent.com/14041622/35901838-b313ff80-0c13-11e8-8b36-962eb84710f8.png)

repo页面里面，一不小心漏过了一条提示：
![image](https://user-images.githubusercontent.com/14041622/35901276-d3f91594-0c10-11e8-9ba4-e24ad1183b27.png)

按照提示，在Profile->sshkeys页面里面，把本地电脑里`~/.ssh/id_rsa.pub`这个公钥文件内容粘贴到里面，添加密钥：
![image](https://user-images.githubusercontent.com/14041622/35901705-f563cefc-0c12-11e8-919a-ab410baad71a.png)

阿里云还需要设置每个参与人员的权限。在控制台里可以找到，如下图：
![image](https://user-images.githubusercontent.com/14041622/35900541-7342081c-0c0d-11e8-8b1f-bf464c446d4c.png)

但是不管我怎么尝试，都添加不了members，项目中都members总是为0。

最后结果还是不能push。


# Github 存储容量标准
官方解释的非常清楚，[在这里](https://help.github.com/articles/what-is-my-disk-quota/)，包括各种访问方式、大文件处理方式、repo存储空间提示等等的情况。
说白了，Github几乎没有任何容量限制，但是你不怀好意地把github当网盘用，频繁访问、不断传大文档等，是会收到通知的。


# Git文件历史追踪问题
> 有很多时候，git追踪某一个文件的变化历史和轨迹，是非常重要的，不管是代码还是文档。这里主要说文档。但是我们的笔记、文档，总是喜欢改名和转移目录之类行踪不定，那么一旦有这些改动，git还能追踪吗？

## 文件改名 `rename`
> git仓库实际上对文件改名这个问题是比较忌讳的，应当说是尽量避免的。因为如果不用特殊处理，改名之后git只会认为你删了这个文件，又新建了另一个文件。

如果你在系统里面手动把一个文档`1.txt`改成了`2.txt`，那么这时候输入`git status`只会看到`1.txt`被删除，新增加文件`2.txt`。
同样的，命令行里用`mv 1.md 2.md`改名，也是同样的效果。
要保持这个文件历史记录不断的话，`正确做法`是：
```
git mv 1.txt 2.txt
```
这样再用`git status`查看就会看到，识别为`renamed:   1.txt -> 2.txt `。它的历史记录就没有断。

## 文件移动
> 有时候会把文件移动到另一个文件夹或者某个子文件夹，但是git却认为你是删了一个而新建了另一个。

这是因为和改名一样，只要是在git命令之外移动的，git就识别不到。
所以，这里也要用`git mv`命令来移动。
```
git mv 1.txt ./src/1.txt
```
这个时候在查看git状态就会发现，显示为`renamed:   1.txt -> src/1.txt`

## 文件覆盖
> 这个问题逻辑要复杂点：有时候我们需要批量抓取网上的一些资源到这个目录里面，有些是重复的内容一样的，有些却是新的，还有些是网上删除了的，那么我们想要网上抓取的和本地的同步，应当怎么办呢？

虽然这个方法不严谨，但是非常简单有效：只要这些东西体积不是很大，那么就可以完全删除本地现有的文件，然后再把新抓取的保存到本地。
这个时候就是考验git的追踪识别能力了。
经过一系列试验发现：
- 首先不能用`git rm`删除文件，如果用了它那么不管怎么做，它都会知道你删除了文件，而我们要做的是让它误以为没有删除。
- 如果文件位置和名字没变，内容也没变，那么只要你没有add或commit，即使新生成的文件的创建日期和修改日期都变化了，`git status`也不会显示任何变动。
- 如果文件位置和名字没变，内容变化了，只要没add或commit，那么`git status`只会告诉你`modified 某文件`。
- 如果文件位置或名字变了，那么，**git完全不知道**。会认为你删除了老的，建了新的。像上面重命名的问题一样。这时候如果你还想要保持这个文件的追踪历史，要不你就尽量避免改名字，要不就想把法用`git mv`命令告知git，但是这个逻辑比较麻烦，尤其是涉及文件比较多的时候。所以我一般选择避免改名字，或干脆就断了追踪。


# Git缓冲区理解：`index`，`add`和`reset`，`staged`和`unstaged`
> 在git里面，有一个叫`index`的区域，你把东西加到那里叫`add`， 把东西再从哪里撤回来叫`reset`；已经在里面的我们形容它是`staged`，还没有加进去的我们形容它是`unstaged`。

其实`index区`就是一个纯粹的缓冲区，也叫`staging area`，是正式提交之前给我们的一个缓冲，还有犹豫的余地。因为一旦正式commit提交了，你所有还没解决的愚蠢的傻事都会公开，即使能覆盖能撤销，但还是掩藏不了历史。

自己做的话无所谓其实，但是如果是团队合作的话，每次commit都是一次公开。
其实形容的话，就相当于老板让你做个项目，你肯定不可能做了一点东西就跑到老板办公室去送一趟文件，应该会先把做好的放在桌子的上那个小文件架上。然后那个文件架就叫`index`。

[参考：Git 基础 - 撤消操作](https://git-scm.com/book/zh/v1/Git-%E5%9F%BA%E7%A1%80-%E6%92%A4%E6%B6%88%E6%93%8D%E4%BD%9C)

## Git 撤销add
```sh
# 指定文件
$ git reset HEAD file.txt

# 全部撤销
$ git reset HEAD .
```

## Git撤销修改
```sh
# 指定文件
$ git checkout -- file.txt

# 全部撤销
$ git checkout -- .
```

## Git 撤销commit
**一旦commit，就不能撤销！会永远留在历史里面。**

## Git 修改commit
一般流程如下：
```sh
$ git commit -m '首次提交'

$ git add forgotten_file
$ git commit --amend
```


![image](https://user-images.githubusercontent.com/14041622/36060082-b951bb6a-0e7c-11e8-9a66-b69e1ebe0091.png)

![image](https://user-images.githubusercontent.com/14041622/36060761-9f2ead34-0e8a-11e8-857c-2ade28a723af.png)



# Git的merge理解
> 一般来说，`merge`是新手的噩梦 。所以为了还有学习的动力，我前期几乎放弃，只是一心只用最简单的功能，等像现在这样慢慢理解了基本东西了，了解基本知识局限性了遇到很多问题了，才是好机会来加强理解这一层。

当我们谈到merge的时候，实际上是有很多种不同的情况的。比如有这几种情况的merge，分别是：`local merge`,`sync merge`和`fork merge`。（这都是我自己起的名字）

Merge本身并不难理解，无非是从这边融合到那边，不同的只是起点终点的方向罢了。
Merge的难点在于`merge conflict`，就是融合的时候有冲突怎么办？


# Git入门之形象化理解checkout
> `git checkout`实际上其实是个平行宇宙时光机，可以带你穿梭到任意一个平行宇宙中，还可以带你穿梭回过去的任意一个时间点。在过去的那个点上，你可以各种观察、修改、删除等，而不对原本时间点产生任何影响。

每一个branch分支，都是一个平行的宇宙，你可以用checkout在两个宇宙之间穿梭。
每一个commit提交，都是现在时间轴上的一个时间点，你可以用checkout回到过去的任何一个时间上。

顺着时光机的思路，你现在身处的时间点，在git里叫`HEAD`，而当你回到过去时，你的时间点就叫做`detached HEAD`，因为你已经是"detached reality"脱离现实了。

再来让它容易记一点，我们可以叫`checkout`为一个`Jumper`！
它可以跳来跳去，跳到任何地方。你可以用它来跳到别的分支，还可以跳到过去的任何点，总之git里面的它都可以跳过去。所以每次我们用`git checkout`时，我们可以心里念`git 跳到`，这样就好理解多了！

> 如果是`git checkout 时间点`，那么这就是一个回到过去的跳跃；
   如果是`git checkout 宇宙名`，那么这就是一个平行宇宙的跨越。

其中`时间点`，就是每次commit的sha值，可以在`git log`中看到；
`宇宙名`，指的就是每个branch的名字，可以在`git branch`中看到。

## 那么如果我checkout跳到过去，还改变了些东西，会发生什么？
> 可以肯定的是，不会发生时空扭曲或祖母悖论。

现在我试一试用`git checkout 时间点`, git返回了如下信息：
![image](https://user-images.githubusercontent.com/14041622/36060959-2bb994be-0e8e-11e8-8217-54b317a8c2f0.png)
意思就是告知我，现在已经和`现实分离`，随便玩。“现实”就是`HEAD`，所以`现实分离`状态就是`detached HEAD`。不管怎么样都可以，add, rm, commit等等。
但是，如果做了些实验发现挺好的，想保留，那么就要新建立一个分支来保持这些变动。然后呢，再让这个分支去和主流合并，这之后就是正常merge流程了。

那么回到过去，修修改改后，想保存并建立分支需要用如下命令：
```shell
git checkout -b <new-branch-name>
```
实际上它是把两个单独的命令合到一起，一个是`git branch <name>`建立新分支并保存当前的改变，和另一个`git checkout <name>`跳转到该分支，这样一步到位还是挺方便的。

### 返回到现在进行时
当跳跃到过去到某个点时，它是绝对的`detached Head`状态。
在各种时间跳跃后，简单一句`git checkout master`就可以跳回到现在进行时了。当然，也可以是`git checkout 某分支名`跳跃到任何一个平行宇宙的现在进行时。

## Git checkout 的妙用：撤销更改
`git checkout 某文件名`则可以让某个自己不满意的文件，回到最近一个时间点，即最近一个commit提交。


# Git的diff理解与学习
> `git diff`和系统的`diff`命令是不同的，`git diff`是用作对比两个文件的差别，但是它是对这个文件和它在时光轴上的某个点上的自己做对比。当然`git diff`也可以用作--------

明白这点，就好理解多了。
先看这幅图：
![image](https://user-images.githubusercontent.com/14041622/36060761-9f2ead34-0e8a-11e8-857c-2ade28a723af.png)

`git diff`可以用当前工作区的某文件，来进行：@1 它和自己保存在缓冲区的复制品对比，@2 它和过去每一个commit时光点上的自己对比。
当然，对比开始后，显示结果就和系统`diff`显示的大同小异了。
```shell
# 当前工作区与缓冲区的对比
git diff [指定对比的文件，或不指定也行]

#  缓冲区与过去commits对比
git diff --staged [指定对比的文件，或不指定也行]
```

## 本次commit与上次commit的diff
[参考文章。](https://stackoverflow.com/questions/9903541/finding-diff-between-current-and-last-versions)
最简单写法：
```python
git diff HEAD^ HEAD
# or
git diff @~..@
# or
git show
# or with GUI display
git difftool HEAD^ HEAD
```



# Git的Reachability理解
> 根据现有commits和branches的树形结构，有很多节点是无法访问到的，


# Git `pull`遇到错误 `refusing to merge unrelated histories`

```shell
git checkout master
git merge origin/master --allow-unrelated-histories
```


# Git 在当前目录之外的地方执行命令

```shell
# Clone a repos
git clone <URL> <PATH>

# Run git command at another folder
git -C <PATH> <COMMAND>
```




# Git 添加remote远端仓库对应

[参考文档](https://help.github.com/categories/managing-remotes/)
```shell
git remote add origin https://github.com/user/repo.git

# Branch master set up to track remote branch master from origin.
git branch -u origin/master
```


# Git push 遇到 `failed to push some refs to` 错误
> 一直在让脚本自动push本地仓库，仓库中的一些文件是从网上更新下来的，每次到push这一步都会产生错误，好像意思是remote有更新但是本地还没更新之前就push是不行的。但是所有remote更新都是本地push上去的，本地应该是一直保持在最新才对。。。不知道为什么

![image](https://user-images.githubusercontent.com/14041622/36249328-427cfe44-1275-11e8-8c8a-662774748e71.png)

[参考stackoverflow回答](https://stackoverflow.com/questions/24114676/git-error-failed-to-push-some-refs-to)

在每次commit本地更新后，在push前用`git pull --rebase origin master`解决了。



# 如何让git记住密码
全局的话：
```shell
git config --global credential.helper cache
```
只是当前repo的话：
```shell
git config credential.helper cache
```
这两句话的做的工作是一样的，就是在`~/.gitconfig`全局配置文件或者`.git/config`当局配置文件中加入这段话：
```
[credential]
        helper = cache
```
所以直接找到配置文件加入这两句话也是一样的。

上面三种配置都完成后，git push的时候就会记住密码，下次不用再输入了。

不过有个问题是，最好在全局配置user.name 和user.email，不然的话还是需要每次都让你输入用户名密码。





# 如何用SSH与Github连接（push等）
为了让服务器自动push本地仓库，试过了`git config credential.helper cache`这样让它缓存用户名。
但是这个不稳定，每过一段时间github又会要求你再手动输入密码。
如果想让脚本自动推送，最可靠的还是用ssh访问github。
可是一般都知道，ssh要访问哪里，本地还是需要输入一个密码来解锁ssh的private key的，说白了就跟不用ssh连接直接输入密码没区别了嘛！
网上解决方案一般都是用什么openssl之类的，重新生成一个没有密码的ssh key。太麻烦，
发现其实ssh自带生成密钥的工具就能够设置不带密码的key。

方法：
直接输入`ssh-keygen`命令，就会提示输入`key pair`密钥对的地址和名称，不输的话就默认为`~/.ssh/id_rsa`这个文件作为私用密钥，同目录的`id_rsa.pub`作为公用密钥。
然后会提示输入密码，这时只要什么都不输直接回车，就可以创建好一个不用输`passphrase`的ssh key了。
然后到github的个人设置页里，找到ssh处，把`id_rsa.pub`的内容完全拷贝进去保存即可。
这时候，随意的`git push`之类与远程仓库连接都不需要输什么密码了。

问题：
目前只有默认名的`~/.ssh/id_rsa`这个管用，自己起名字的ssh key现在还不能用。


# Git与python的Virtualenv冲突
如果在git仓库中使用了virtualenv，那么每当使用`git add .`或者`git commit`都会遇到错误，使得不能继续。问题就在于virtualenv对它的冲突。
目前简单的解决办法就是在`.gitignore`中把所有virtualenv相关的文件都屏蔽，一般包括`.Python`,`lib`,`include`,`bin`。


# Git通过proxy代理访问
假设本地的代理端口为1087，那么命令行设置：
```
git config --global http.proxy http://127.0.0.1:1087
```
或者直接在`~/.gitconfig`中添加：
```
[http]
    proxy = http://127.0.0.1:1087
```


# 用SSH连接github项目时报错`ssh_exchange_identification: Connection closed by remote host`
一直在正常通过ssh连接github的repo，在哪里都没有改动的情况下突然`git push`不管用，一直报这个错误，就连`git clone`一个ssh地址都不行。
还以为github把我屏蔽。
考虑了网上很多本地ssh连接的问题，都没用，而且思路也不对。
索性ssh连接到我在新加坡租用的服务器，在服务器里尝试ssh连接github。
结果还是不行！
所以不是Github屏蔽了我的IP，也不是我本地的ssh设置问题，因为服务器的ip地址和ssh等都不一样还是遇到了这个问题。
网上还有说路由器的加速插件问题，这个也通过用服务器连接和切换wifi的方式否定掉了。
结果我心里只有一个结论：那就是Github本身的问题了。
结果没过几分钟，
所有端都可以正常连接了。
也许真的是github突然遇到什么问题导致所有地方都不能访问。

第二天更新：
结果真的第二天就收到这个新闻：Github昨天晚上遭遇史上最大DDOS攻击。但是不包括我吧，我顶多每分钟10次连接，而且还是用的绑定的ssh key和oauth码。。。
![image](https://user-images.githubusercontent.com/14041622/36930989-e39b3772-1ee7-11e8-93ae-5c0b83817d44.png)




# Git 连接远程仓库
如果本地已经有了一个repo，想要与远程服务器如Github上的repo建立连接，然后push和pull等，就需要用`git remote`命令操作建立连接。

[参考：阮一峰 Git远程操作详解](http://www.ruanyifeng.com/blog/2014/06/git_remote.html)
[参考：Git Basics - Working with Remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes)

```shell
# 检查现有远程连接，如果没有，则显示空
git remote -v

# 添加远程连接, URL可以是远程repo的http或ssh地址 (先设定为origin)
git remote add origin URL

# 或者修改现有远程URL (这里先设定为origin)
git remote set-url origin URL

# 先与远程同步
git pull origin master

# 提交到远程
git push origin master
```

这个时候还不能直接`git push`，因为没有设置默认`push`到远程的`origin master`分支，需要设置默认分支。

[参考：Git push与pull的默认行为](https://segmentfault.com/a/1190000002783245)

```shell
git config push.default simple
```

然后就可以安心的`git push`直接推送到远程的`origin master`了。

更多参考：
[Github Help: Adding a remote](https://help.github.com/articles/adding-a-remote/)
[Github Help: Changing a remote's URL](https://help.github.com/articles/changing-a-remote-s-url/)


# Git branch 分支

## 新建分支
```sh
$ git checkout <new-branch-name>

# 以上一句话等同于以下两句话：
$ git branch <new-branch-name>
$ git checkout <new-branch-name>
```

## 不同分支的修改状况
- 如果在一个分支进行修改，而没有`add`和`commit`，那么即使另一个分支，文件也一样是改变了的。
- 如果修改后commit了，那么切换分支时，则会体现出不同。




# Git merge 合并分支

## 本地分支操作
```sh
# 先切换到主分支（或即将被覆盖的分支）
$ git checkout master

# 将某个指定分支覆盖到当前分支
$ git merge <branch-name>

# 删除之前的分支 (已经没用了)
$ git branch -d <branch-name>
```

## 远程分支操作
本地不管怎么push，如果不指定push的分支的话，远程是没有变化的。
```sh
# 把本地分支更新到远程分支
$ git push origin <branch-name>

# 删除远程分支：语法非常奇怪 但就是这么操作的
$ git push origin <local-branch-name>:<remote-branch-name>
# 如 $ git push origin :dev
```