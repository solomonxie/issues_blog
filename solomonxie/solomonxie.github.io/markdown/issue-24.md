# Python学习笔记
## 这种方式记笔记可能会很轻松，开篇试试吧


# Get System Arguments 获取系统参数

```python
import sys

# 输出文件名
print sys.argv[0]

# 输出第一个参数
sys.argv[1]
```


# Define a class 定义类

```
class Person:
    self.name = ''
    self.id = 0
    self.father = 1
    self.mother = 2 

    def __init__(self, name):
        self.name = name
	self.born()
    
    def born(self):
        self.id = self.father + self.mother

me = Person('Solomon')
print(me.id)
```


# FLask 初接触
> Flask是基于Python的Web后台服务器框架，相对于Django来讲属于非常灵巧的轻量级框架。目前市面上应用程度很广，值得学习一下。

## Installation

- Windows Git Bash

```
pip install virtualenv
mkdir /d/workspace/myFlask
cd /d/workspace/myFlask

virtualenv --no-site-packages venv
source venv/Scripts/activate
# Now is already in virtual enviroment

pip install Flask
```

- Windows CMD

```
# 其他都一样 只有运行不同
venv\Scripts\activate
```

## Deployment

```
touch hello.py
mkdir static
mkdir templates
```

## Hello World

在hello.py中输入以下内容并保存(最简单Flask)

```
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

    if __name__ == '__main__':
        app.run(debug=True)
```

## 运行

```
python hello.py
```

## 渲染模板

在`template`文件夹中新建模板users.html，并随便写几句话，在hello.py中加入如下语句：

```
#记住在前面需要引用渲染函数
from flask import render_template

@app.route('/users/')
def show_users():
    return render_template('users.html') 
```




# python path路径问题
> 看似是个小问题，但是在python里实际上是个非常容易被混淆的东西。


## 获取文件名
```py
>>> s = '/Users/me/movie/abc.mp4'
>>> os.path.basename(s)
'abc.mp4'
```


## 获取文件名（不包含扩展名）
```py
>>> s = '/Users/me/movie/abc.mp4'
>>> os.path.basename(os.path.splitext(s)[0])
'abc'
```

## 获取目录名
```py
>>> s = '/Users/me/movie/'
>>> os.path.basename(os.path.realpath(s))
'movie'
```
为什么要这么写？看看下面实验就知道：
![image](https://user-images.githubusercontent.com/14041622/40163558-b548fa8e-59e9-11e8-8c07-41462fefc9a5.png)

## 获取当前脚本的路径
[参考文章](https://stackoverflow.com/questions/4934806/how-can-i-find-scripts-directory-with-python)。

需要`import os`和`import sys`
- 当前工作区: `os.getcwd()`，注意，这不是脚本的位置，而是命令行中的工作区位置。
比如当你在`~/A/`执行`~/B/`文件夹中的一个python代码，那么返回的是`~/A/`，因为命令行中的工作区在`~/A/`.
- 当前文件名：`sys.argv[0]`或`__file__`，注意，两个变量都不稳定。__file__这个默认变量在一些环境下是没有被定义的，sys.argv[0]有时是完整路径有时只是一个文件名，所以，慎用。最好都配合os.path的各种方法运用。
所以正确方法是：`os.path.basename(sys.argv[0])`
- 当前文件完整路径：`os.path.realpath(sys.argv[0])`
- 当前文件所在文件夹：`os.path.dirname(os.path.realpath(sys.argv[0]))`


# python调用命令行
参考[这篇文章](https://www.jianshu.com/p/5d999a668e79)

```python
import os

#只返回结果
os.system(command)

#或者，返回结果与终端显示信息
with os.popen(command, mode) as f: 
    print(f.read())

```


# Python代码之美
> 有时特别想摘抄一些别人漂亮的代码书写。在这里贴上吧。

### [`gh-issues-import.py`](https://github.com/IQAndreas/github-issues-import/blob/master/gh-issues-import.py)
代码整齐和常量名全大写
![image](https://user-images.githubusercontent.com/14041622/35791554-9d0f75d4-0a83-11e8-8110-cfd227a4f198.png)
分隔有序，不用注释也可以清晰表面之间分别
![image](https://user-images.githubusercontent.com/14041622/35791749-7734bc38-0a84-11e8-9143-5db51fa864c4.png)
简单函数和复杂函数的断行方式
![image](https://user-images.githubusercontent.com/14041622/35791839-dab7cb1a-0a84-11e8-9601-d6e18c8b6871.png)



# Python 读取JSON数据

```python
import json

him = json.loads( '{"title": "Jason", "content": "hello"}' )

print( him['title'] )
```
Out:
```
Jason
```


# ~Python2中文简易解决方案~ （暂废除）
翻了翻几年前研究Python中文编码的问题，原来如此复杂。。。。一时间全忘了。
为了避开这个理论上的难题，我直接开启了实验出真知的模式，试验出一个简单的方法。
简单来说如下：
1. 首先页头要有`# -*- coding: utf-8 -*-`的声明
2. 整个py文件中，只要任何一处设计字符串，都要认真处理
3. 所有获得的字符串，都要先进行`"字符串".decode('utf-8)`解码为某种原始编码。
4. 所有要发出的或写入文件的，都必须要进行`"字符串".encode('utf-8')`编码为统一码。


# 为什么要用IPython/Jupyter? 
> python里面调试确实有点烦恼，尤其是在vim里，想要尝试一些简单的编码问题，实在是有点麻烦，不想到命令行模式一行一行执行，也不想再新建一个文件测试一个简单的功能。

而且就是不管这些，测试一个简单的功能如学习语法、测试编码、测试新学习的包等，在IDE里面测试，看不到每个部分的output效果（除非自己手动去命令行里复制或截屏），在命令行里测试，则没法轻松撤销前面的代码。。。。
所以这时候才想到好像前阵子看到youtube视频里别人用IPython，是那种又能轻松编辑又能为每部分显示output效果，还能在旁做markdown笔记的东西。
出于这个想法，搜到了这篇[知乎回答](https://www.zhihu.com/question/51467397)，看到了不少有意思的东西，感觉又展开了一个崭新的领域，python的视界豁然开朗。
[这篇文章](https://zhuanlan.zhihu.com/p/33654849)极好的解释了IPython的入门用法，相当酷！我怎么竟然这么久都不知道这种东西的存在？

### IPython和Jupyter的区别？
据说一开始IPython是作为`IPython shell`的存在，后来Jupyter融合了它，又把自己和IPython上独立出来，做成了网页版的`Jupyter Notebook`这样的东西。Jupyter强大的特性，加上和各种数据研究库的紧密结合，真让人不能忽视它的存在了。
IPython的安装方法，简单地`pip install ipython`即可。
但是，想到IPython本身一个shell，让我想起了我自己用的shell是`zsh`，让我把zsh切换到别的shell里面去，还真有点不喜欢。。这可能是个stylish issue吧。
所以，应该直接了当的安装jupyter，其中也会自动安装上`IPython shell`，作为其运行的Kernel。

## 错误的安装Jupyter
~只安装Jupyter本身的话，很简单：`python -m pip install jupyter`。不过根据官方文档，强烈建议安装Jupyter的`Anaconda`发行版，像大礼包一样的自动安装`python+Jupyter Notebook+一系列数据研究库`。因为本来就是要研究机器学习等一系列数据研究的，所以Anaconda正合适。这个我觉得再好不过了，所以直接跳到[`Anaconda`页面](https://www.anaconda.com/download)去看安装方法。然后看到，Anaconda安装方法是不能简单`apt-get`或`brew`或`pip install`的，500M左右的大小，需要下载后启动图形安装工具或shell脚本安装（`.sh`文件本身就500M，而且安装分为Python 3和Python 2的两种方式。~

然后就会发现：**Anaconda谁装谁后悔！**
Anaconda体积庞大，软件管理看起来一体化简单，实际上在处理一些Bug和自定义设置的情况下非常不好定位。我在Mac上初次安装Anaconda大礼包后，连简单的`jupyter notebooke`这样的命令都执行不了，详尽了办法最后才用直接指定路径的方式运行。这只是一开始，之后还有notebook里各种找不到外部安装的python package的情况。
所以还是别图便宜，手动安装一步一步来吧。一键安装很多时候都没那么好。
试了下手动安装的方法，`pip install jupyter`，或者官方的`python -m pip install jupyter`，都会发生`jupyter: command not found`找不到命令。参考了数十篇网络上中英文文章，都没有解决。常说的直接引用`~/.local/bin`这个位置的 jupyter也不行（没有）。
终于，意识到这些方法都是错误的思路。

## 正确的安装Jupyter Notebook
不管官网怎么推荐Anaconda，网络上各种简单解说，总之Anaconda或`pip install jupyter`都很容易引发巨大的问题。由于jupyter的性质：它是调用python内核的东西，用系统python还是用自己的python，这都是很敏感很麻烦的问题。用系统的python很容易识别不到或者被别的程序修改导致bug，用自己的python会导致别的地方安装的package在jupyter里识别不了。
所以：
参考了[这篇的思路](https://zhuanlan.zhihu.com/p/27542582)，正确的方法是在virtualenv虚拟环境下，绝对安全封闭的环境下用`pip`安装jupyter。这样的话，第一，不需要`sudo pip`这样敏感的东西去安装jupyter这么复杂的工具；第二，也保证了jupyter不会搞乱其它东西。
然后，二话不说，在已有virtualenv的情况下，在某个文件夹里建立虚拟环境，并启动虚拟环境。然后简单一句`pip install jupyter`，完成安装。
安装完成后`jupyter notebook`，完美运行！
```shell
# for Python2
$ pip install jupyter

# for Python3
$ pip3 install jupyter
```
这样的话，即使以后要在jupyter里各种安装插件、各种配置新kernel等，都不用害怕了，因为再怎么玩弄，也出不去这个圈。
话说回来，实际上你也没什么需要在全系统配置jupyter的必要，在某个文件夹玩就足够足够的了。
何必呢？

## 启动Jupyter
用命令行启动很简单，在某个工作目录，输入：
```
$ jupyter notebook
```
这样就能以这个目录打开一个`http://localhost:8889/tree`的网页，一切都在这个网页里操作。

## 正确的启动Jupyter
正确的方式，实际上是在Virtualenv虚拟环境下启动，可以随意安装各种包，适配各种Python版本环境：
```shell
# 启动Virtualenv
$ source ~/PATH-TO-VENV/activate 

# 启动Jupyter
(venv)$ jupyter notebook
```

## 添加Python3 Kernel
[参考：Jupyter增加内核](http://www.cnblogs.com/Jeffiy/p/4861528.html)

默认的只有Python2 Kernel，所以只能建立Python2的笔记。
要添加也很简单。
**强烈建议在Python3的Virtualenv虚拟环境下实现！！！**
```shell
# 启动Virtualenv
$ source ~/PATH-TO-VENV/activate 

# 在Python3的虚拟环境下安装Kernel
(venv3)$ pip3 install ipykernel

# 将Kernel添加进Jupyter笔记选项中
(venv3)$ python -m ipykernel install
```
启动Jupyter notebook后，就会看到Kernel里面多了Python3了：
![image](https://user-images.githubusercontent.com/14041622/39862292-f1c80168-5475-11e8-9d50-576620dd6d6f.png)

### 终端里找不到`jupyter`命令
总是报`command not found jupyter`错误，说没有这个命令。一开始还以为是zsh的问题，可是切换到bash也一样。
照着网上攻略在`.zshrc`里改也没用，在`.bash_profile`里改也没用。
然后发现，在Mac自带的Terminal.app中就可以正常打开，不需要改任何配置。
这才知道原来是iTerm2无法识别。于是在Terminal.app中用`which`命令查看jupyter命令的所在处，看到它位于`/Users/我的用户名/anaconda2/bin/jupyter`这个地方。
于是直接在`~/.zshrc`中加入alias：
```shell
$ alias jupyter="/Users/我的用户名/anaconda2/bin/jupyter"
```
重启iTerm2，好用！

但是，iTerm2中的bash还是不能访问，用同样的方法也不行。暂时没找到解决方法。



# Python `requests`库抓取网页出现乱码
> 练习抓取网页时遇到的，如果是简书等这些标准网站，正常抓取是没问题的。但是很多网页竟然怎么抓取都是所有中文都乱码。弄的我还以为是python代码本身的encoding问题。最后才追溯到原来是出现在源头requests库里面。

参考这两篇文章，[requests官方文档](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)， 和，[代码分析Python requests库中文编码问题](http://xiaorui.cc/2016/02/19/%E4%BB%A3%E7%A0%81%E5%88%86%E6%9E%90python-requests%E5%BA%93%E4%B8%AD%E6%96%87%E7%BC%96%E7%A0%81%E9%97%AE%E9%A2%98/)，非常有参考性。

第二篇文章中看到，很多网页实际上并不都是`utf-8`的编码格式，还有很多是`ISO-8859-1`格式，如下图：
![image](https://user-images.githubusercontent.com/14041622/35913040-5fb39cc6-0c39-11e8-9cee-8dc8e7961918.png)
但是，其实不是网页本身的问题！我们查看网页本身的`headers`发现，他们的`charset`值是`utf-8`，但是为什么用`r.encoding()`得到的却是`ISO-8859-1`呢？文章中指出原来是requests的bug，而且常年不解决。所以就需要我们自己来想办法。
我们不能手动去检查每一个网页的编码啊，那样太麻烦了。
官方文档中出现了这么一小句话，非常重要，亲测有效：
![image](https://user-images.githubusercontent.com/14041622/35913251-0508ce9e-0c3a-11e8-8f76-188c026436ca.png)
虽然这句话不是为了处理网页的，但是`二进制`！沿着这个思路，又在官网看怎么将网页获取为二进制模式的：
![image](https://user-images.githubusercontent.com/14041622/35913331-3c097b96-0c3a-11e8-8bed-5a872e457116.png)
就是使用`r.content`获取。



# 关于解决Python2乱码问题的终极解决方案 (TL;DR)
![image](https://user-images.githubusercontent.com/14041622/35929949-a242afbe-0c6b-11e8-8848-508c4e8124d1.png)

> 有个特别好玩的现象，当我们为了python编码头疼的时候，几乎搜索到所有的文章都会先发一通牢骚。然后在无可奈何地写解决思路（是解决思路不是方案）。这个问题真不是新手问题，即使是十几年python老手也经常头疼。中国外国都一样。看看这个python专家在[PyCon大会上用半个多小时讲解乱码的视频](https://www.youtube.com/watch?time_continue=1040&v=sgHbC6udIqc)就了解了，他自己都给自己的来回encoding, decoding, encoding, decoding说晕了，台下举手他都拒绝回答，可想而知这个问题复杂性。

我认为，几乎每个pythoner，都会有一段人生浪费在了编码上。可以说这个问题，是如果你不彻彻底底解决，就永远会崩溃的地步。翻看我曾经写的数篇文章就知道了：
- [对Python 2.x的通宵抱怨](https://github.com/solomonxie/solomonxie.github.io/issues/9)
- [Python中文字符的理解：str()、repr()、print ](https://github.com/solomonxie/solomonxie.github.io/issues/10)
- [Python里中文编码的理解：unicode、utf-8、gbk](https://github.com/solomonxie/solomonxie.github.io/issues/20)

牢骚结束，下面是我又一次用了两个整天才测试整理书写完成的ipython notebook笔记。`ipynb`格式的笔记源文件在这里，当然有可能会链接失效，有喜欢ipython的live coding笔记的且想要用这个笔记测试编码的，请联系我。

### 首先，需要先要了解python的`print大法`
如果python的print的特性都没有了解的话，希望你不要贸然尝试用print去调试测试乱码编码的问题。
这里的print厉害到让你不高兴的地步——它不管你塞过来的是什么格式什么编码，字符串数组对象什么的的都一口气全打印出来。
感觉好像很好，但其实是我们仔细研究编码问题的最大阻碍。
因为你塞给print一个unicode它能打出中文，塞一个utf-8或iso8895给它，也一样给你打印出原文。这样以来，你看着它出现原文后，就欣喜若狂产生了一种胜利的错觉。
所以我想在这里最先说清楚它：
#### 不要轻易在研究乱码的时候用print测试目标！
也不是说这种时候一点都不能用，而是说你可以print别的什么东西，但是如果想看清某个变量本质的话，千万不要用。
这个时候要用`print repr(字符串)` ,或者最好是在命令行或ipython里面测试，像这样：
![image](https://user-images.githubusercontent.com/14041622/35959122-2d49108a-0cdf-11e8-8a92-66872afc4782.png)

看出区别了吗？明确了这点，再来继续研究编码问题。

### 简单来说，先要记住，在Python2里字符串只有两大阵营：

## `unicode`和`str`

如果`type(字符串)`显示结果是`str`，其实指的是`bytes`字节码。
而其它各种我们所说的`utf-8`，`gb2312`等等也都是Unicode的不同实现方式。
这里不要去考虑那么复杂，只要先记住这两大阵营就行。

## `encoding`和`decoding`

绝对要记住的：
从`unicode`转换到`str`，这个叫`encoding`，编码。
从`str`转换到`unicode`，这个叫`decoding`，解码。
![image](https://user-images.githubusercontent.com/14041622/35937299-c7e99858-0c80-11e8-8c0d-aedfb723a2c1.png)
(图片引用自知乎相关某答案。)

来回记住这个问题，才能进入下一步！

然后来看个案例。
![image](https://user-images.githubusercontent.com/14041622/35928287-ca30e972-0c67-11e8-96d1-7d3a05e26e43.png)

> 通过上面两种格式的对比我们看到，str和unicode的各种区别。

那么，既然变量里面会出现两种不同的格式，如果我们把两种格式的字符串连在一起操作会发生什么呢？
如下：
![image](https://user-images.githubusercontent.com/14041622/35928324-dddbf200-0c67-11e8-96db-31061e6848eb.png)

### 看！著名的编码错误`UnicodeDecodeError: 'ascii' codec can't decode`就这样出现了！

以上是我们用`显性`字符串来比较两种格式字符串的区别。

但是，我们经常性处理python编码问题，都不是在这种`显性`的字符串上出现的，不是从网上爬取的就是从本地文件读取的，意思就是文件内容庞大，编码格式很难猜到是什么。
所以这里我们将问题再拆分为两部分讨论：本地文件和网络资源。

## 本地文件编码测试
首先在本地建立一个有中文的以`utf-8`格式保存的文本文件（实际上无论.txt还是.md等都无所谓，内容是一样的）。
内容只有'你好'。

### 然后我们来读取一下：
![image](https://user-images.githubusercontent.com/14041622/35928363-f0ffdb44-0c67-11e8-9b37-1cf8ebcb5ec0.png)

> 上面看到，从文件读取出来的，就是str格式的字符串。
那么如果要把str转化为unicode，就要解码，也就是decoding.

![image](https://user-images.githubusercontent.com/14041622/35928391-017b7d0c-0c68-11e8-8a73-eed6d071fc56.png)

### 这种时候实际上是最迷糊也最容易造成之后错误的，就是分不清该编码还是该解码。

> 所以上面提到，必须要记住这两个区别。
那么如果现在我搞反了怎么办？就会再次出现下面错误：

![image](https://user-images.githubusercontent.com/14041622/35928408-10b50180-0c68-11e8-8a41-9d4d97a3be66.png)

### 话说回来，我们该怎么统一他们呢？
> 为了避免两种格式的字符串在一起乱搞，统一他们是必须的。但是以哪一种为统一的呢，unicode还是bytes?

网上各种文章统一口径，要求代码中出现所有的变量都统一为unicode。
可是我在实践和测试中都越来越发现：这种做法真的不那么可靠，甚至我怀疑有可能我们碰到那么多的问题，都是由它搅乱引起的。

#### 下面我们来看看做常用的环境下字符串都是什么格式

![image](https://user-images.githubusercontent.com/14041622/35928691-b8c8ea1c-0c68-11e8-952d-97c8c205ae79.png)

> 这样就明白了：除了r.text返回的内容外，其它几乎都是使用str格式，也就是bytes字节码码。所以我们只要转化requests相关的内容就行！

实际上，requests返回的response中, 除了用`.text`获取内容，我们还可以用`.content`获取同样的内容，只不过是bytes格式。

那就正和我们意，不用再去转化每一个地方的字符串，而只要盯紧这一个地方就足够了。

### 为什么我们不能把所有字符串变量统一为unicode呢？

先提醒下，变成unicode的过程，叫`decoding`。不要记错。
像`.text`经常把`ISO8859`等猜不到也检测不到编码(机率很低)的字符串扔过来，如果遇到的话，是很麻烦的。
`decoding`有两种方法：
```
unicode(b'你好‘）
b'你好'.decode('utf-8')
```

这里因为不知道来源的编码，所以必须用`unicode()`来解码，而不能用`.decode('utf-8')`，因为显然你不能乱写解码名称，如果来源果真是（很大几率是）`ISO8859`等方式，那么错误的解码肯定会产生乱码，或者直接程序报错。切记！

所以这里只能用`unicode()`解码。如下例：

![image](https://user-images.githubusercontent.com/14041622/35928475-387899f2-0c68-11e8-9821-3f31939c7742.png)

##  结论：一定记住，全文都统一用`str`格式字符串
### 只要盯紧requests、json等这种经常处理外来资源的库就好了。
只要控制好外来源的字符串，统一为`str`，其它一切都好说！

> 实际上，我发现遇到的绝大多数编码问题，实际上不是python原生方法导致的，而是这些外来库所引起的！因为每个模块都会有自己的一套处理编码的方式，你还真不知道它是采用哪个。就像JSON的dumps()一样埋着大坑等着我们。所以真正应该盯紧的就是这些库了。


下面是一个从获取网络资源（含中文且被requests认为编码是ISO8850的网页）到本地操作且存储到本地文件的完整测试。
```python
import requests

r = requests.get('http://pycoders-weekly-chinese.readthedocs.io/en/latest/issue5/unipain.html')

# write a webpage to local file
with open('test.html', 'w') as f:
    f.write( r.content )

# read from a local html file
with open('test.html', 'r') as f:
    ss = f.read()
```
大功告成！效果如下：

![image](https://user-images.githubusercontent.com/14041622/35929410-69cf7e42-0c6a-11e8-915d-f020a729bbb4.png)

### 再也不用纠结、检查每一个变量、写一大堆嵌套转化方法了！注意，只要盯紧各种外来模块和库的文字处理就够了。

> 另外，关于JSON的乱码问题，又是一个新的较长篇章。我会单分一篇，请到我的专栏里找。


# Python2操作JSON出现乱码的解决方案
> 其实刚刚写过一整篇Python编码问题的解决方案，由于JSON又是一种特殊案例（与库相关，与语言本身无关）所以就单独提出来说。


## 我们来看一个从网上获取json并又存到本地文件的例子
```python
import requests,json

r = requests.get('https://api.github.com/repos/solomonxie/\
solomonxie.github.io/issues/25/comments')

# 获取到我的github中某条issue的所有评论，形式为<JSON格式的字符串>
comments = json.loads( r.content )

# 取某一条评论查看内容（中文）
cc = comments[0]['body'][0:10] # 取出的内容是'## 配置：先从配置'
```
然后来测试下变量cc：
![image](https://user-images.githubusercontent.com/14041622/35958210-88aad5ee-0cda-11e8-8192-08a8da696a31.png)

### 好，到这里先停一下！
JSON的读取到目前为止，都是正常的：JSON Object对象给出的值都是unicode，没有被莫名转义，也没有报错误。
> 但是，unicode格式，意味着它和str格式不兼容！
这时，害羞的大姑娘Unicode刚出炉，你不能在这个时候让它和Str操作在一起！
报错也往往就在这种疏于防备的时候！

比如你看：

![image](https://user-images.githubusercontent.com/14041622/35958360-59681c8c-0cdb-11e8-9a83-c825e4a9eb8b.png)

上面打印了三条Unicode和Str的结合，
前两条分别是以Str格式的结合，以Unicode格式的结合。
但是第三条，把两个不同格式的字符串结合，就出错了。

对不起，这里不是Javascript，变量不可以任意交合。Python对变量和编码都是极其谨慎的。

所以明白了这点，我们再继续。

### 上面获得了JSON Object对象，那么再来试试将`JSON对象`整体存到文本文件中。
如果要存到本地文件，那么就必须把Object对象转换为Str格式的字符串。
json库自带.dumps()函数可以进行转化。
但是这里问题出现了！我们来小试一下：
![image](https://user-images.githubusercontent.com/14041622/35958250-b7b04900-0cda-11e8-860b-bc1494274be5.png)
> 竟然连`print大法`都不能把`json.dumps()`返回的内容正确打印出来。经过各种测试和查看官网对于此函数的文档，发现：

### 原来`json.dumps()`是默认所有非ascii码强制转化为代号（而非汉字）的，于`repr()`效果等同！
[官方文档](https://docs.python.org/2/library/json.html#encoders-and-decoders)里有说明，`json.dumps()`里面有个`ensure_ascii`参数，默认为True。
意思就是默认把所有非ascii字码用`\`强制转化。所以，为了关闭这个功能，我们必须把它设为`False`.
下面是个小测试：
![image](https://user-images.githubusercontent.com/14041622/35958259-c42808e4-0cda-11e8-87ca-dc16e0816567.png)

### 这样一来JSON在Python里的编码问题就解决了：须用`json.dumps(obj,  ensure_ascii=False)`来转化为字符串

下面是完整的代码测试：
```python
# @网络资源到本地存储真实测试
import requests,json

r = requests.get('https://api.github.com/repos/solomonxie/solomonxie.github.io/issues/25/comments')

# 获取到我的github中某条issue的所有评论，形式为<JSON格式的字符串>
comments = json.loads( r.content )

outgoing = json.dumps( comments, ensure_ascii=False )

with open('test.txt', 'w') as f:
    f.write(outgoing.encode('utf-8'))
with open('test.txt', 'r') as f:
    read = f.read()
    
print read[0:20], type(read)
```
来看结果：
![image](https://user-images.githubusercontent.com/14041622/35958296-f90e1260-0cda-11e8-8aed-2a320a9ac6f1.png)

## 大功告成！


# 更多Python2编码的小细节

## 数组`.join()`合并
数组中必须所有的元素都是字符串，且都是统一的编码才能合并，否则报错。统一后，如果全是unicode，那么返回的字符串就是unicode；如果元素全是str，那么返回的就是str。
![image](https://user-images.githubusercontent.com/14041622/35965010-6c01a23c-0cf4-11e8-81ce-9340217d9553.png)




# python将某个目录打包为`zip`文件
比较古老的方法是用`zipfile`库创建zip包，但是要写各种循环迭代需要很多行代码。
还有另一种[python自带库`shutil`](http://python.usyiyi.cn/translate/python_278/library/shutil.html),可以一句话打包为zip文件。
```
import shutil
shutil.make_archive(base_name, format, root_dir, base_dir)
```
很快就打包好了！
唯一注意的是，怎样把它安装自己想象的结构打包。
- base_name，是加上完整路径（不能缩写）的文件或文件夹名
- format一般是zip，其它tar之类也行
- root_dir是要压缩的目录或文件
- base_dir是压缩包里的文件层级。如你写`a/b/c`，这样所有文件都会塞到最底层的c文件夹中。



# Python 日期和时间
```
from datetime import date
d = str(date.today())
print(d)
```



# Python调试工具`pdb` —— Python Debuger
[参考文章1](https://zhuanlan.zhihu.com/p/25942045)，[参考文章2](https://docs.python.org/2/library/pdb.html)

- 启动方法一：`python -m pdb PATH-TO-SCRIPT.py`
- 启动方法二：代码中写入`import pdb;pdb.set_trace()`，即插入了一个断点。

## 常用命令
```shell
# 退出循环
until

# 下一步
next 或 n

# 深入性下一步（进入每次调用的函数里面）
step 或 s

# 移动到上一层／下一层函数
up 或 u
down 或 d

# 执行直至当前函数结束
return 或 r
```


# 用requests报错`requests.exceptions.SSLError`
![image](https://user-images.githubusercontent.com/14041622/35994940-df8d7214-0d4c-11e8-95fa-b4824ddde4d8.png)
明明没有改代码，突然就报这种错误。
调查发现，原来是被服务器拒了。可能是今天来回调试，多次访问同一个地址，就被屏蔽了。
但是，同样是没有设置请求Headers的客户端postman和insomnia就还能正常访问，不知道为什么。
后来知道了，原来是服务器拒绝给我传送数据，因为访问量太大了！
Github的API是比较好的，它会在response中返回一个当前访问剩余量和下次能再次开始访问的时间。所以搞明白这个就知道，不是自己代码的事，而是访问量的事了。解决方法就是request访问时加上auth认证，这样就会从默认的每小时60次访问增加到每小时5000次。基本上够用了。


# Python操作Git库 `GitPython`
[参考文章](http://note.qidong.name/2018/01/gitpython/)
[参考文章](http://www.cnblogs.com/baiyangcao/p/gitpython.html)
[复杂点的参考](https://my.oschina.net/hopeMan/blog/141221)

试了一圈发现，git库的用法设置非常符合原生git命令，只不过之间加了个`.`而已。
比如原本命令行里是`git add .`，这里就是`repo.git.add('.')`，
原本是`git commit -m "信息"`，这里就是`repo.git.commit(m='信息')`
可以说减少了很多学习时间，基本上我很多都是没参考文档自己猜出来的也能用。

```
sudo pip install gitpython
```
库安装好后可以直接在python中用了。

### 创建、识别、克隆仓库
文件夹地址可以是全路径，也可以是`.`当前文件夹、`../`上级文件夹等用法。
```
# 在文件夹里新建一个仓库，如果已存在git仓库也不报错不覆盖没问题
repo = git.Repo.init(path='文件夹地址')

# 选择已有仓库
repo = git.Repo( '仓库地址' )

# 克隆仓库
repo = git.Repo.clone_from(url='git@github.com:USER/REPO.git', to_path='../new')
```
### 常用语句：
```python
# 查看repo状态
print repo.git.status()   # 返回通常的status几句信息
print repo.is_dirty()    # 返回是否有改动（包括未add和未commit的）

# 添加文件 可以是单个文件名，也可以是`[ ]`数组，还可以是`.`代表全部
print repo.git.add( '文件名' )

# commit提交
print repo.git.commit( m='提交信息' )
```

### 远程交互操作
```python
# 创建remote：
remote = repo.create_remote(name='gitlab', url='git@gitlab.com:USER/REPO.git')

# 远程交互：
remote = repo.remote()
remote.fetch()
remote.pull()
remote.push()
```

### 实验效果
```python
 # 原意是返回工作区是否改变的状态
# 但是测试发现，工作区有变动它返回False，没变动却返回True
print repo.is_dirty()
```

### 生成tar压缩包
```python
# 压缩到 tar 文件
with open('repo.tar', 'wb') as fp:
    repo.archive(fp)
```


# `pip 常用操作`
注意：
- 安装过程中尽管很多包需要sudo权限，但是，尽量不要sudo！最好的是在virtualenv下操作
- 一些常见问题，升级pip到10.0就解决了

```shell
## 安装pip
$ curl https://bootstrap.pypa.io/get-pip.py >> get-pip.py
$ python get-pip.py

## 安装包
pip install <package name>

## 删除包
pip uninstall <package name>

## 升级某个包
pip install --upgrade <package name>

## 安装某个版本的包
pip install django==1.9

## 升级自己
pip install --upgrade pip

## 显示模块包的安装路径
pip show <package name>

## 查看已经过期的软件（不是最新版）
pip list --outdated

## 列出已安装的包 (二者皆可)
pip list
pip freeze

## 导出已安装包到requirements.txt
pip freeze > requirements.txt

## 批量安装包
pip install -r requirements.txt

## 搜索包
pip search

## 查询可升级的包
pip list -o
```


# Python 删除某文件夹
[参考文章](https://askubuntu.com/questions/555318/delete-all-files-except-files-with-the-extension-pdf-in-a-directory/555326)
- os.remove() will remove a file
- os.rmdir() will remove an empty directory
- [shutil.rmtree()](https://docs.python.org/3/library/shutil.html#shutil.rmtree) will delete a directory and all its contents

```python
# 删除某个目录及里面所有内容，第二个参数为True时忽略所有错误中断
shutil.rmtree('<path>', True)
```





# Python2 异常捕获
常用配置是这样的：
```
try:
    do_something()
except BaseException as e:
    print 'Failed to do something: ' + str(e)
```



# Python 睡眠
[参考文章](https://www.pythoncentral.io/pythons-time-sleep-pause-wait-sleep-stop-your-code/)

```python
import time
 
# Wait for 5 seconds
time.sleep(5)
 
# Wait for 300 milliseconds
# .3 can also be used
time.sleep(.300)
```


# Jupyter Notebook IPython无法识别Module问题
因为Jupyter notebook的python不是系统里的python， 而是运行在`/Users/solomonxie/anaconda2/bin/python`这里的。同时还有其他很多位置、kernel等等问题非常复杂，网上目前还很难找到比较简单的解决方案。
唯一看到的是[这篇文章](https://jakevdp.github.io/blog/2017/12/05/installing-python-packages-from-jupyter/)，讲到很不一样的思路，即用conda还是pip来安装module的分别。


# Python集合的操作
> 有时候在对比两个数组，如果运用上集合的话就会相当精妙。

### 基本操作
[参考文章](http://blog.csdn.net/business122/article/details/7541486)
```python
s = set([3,5,9,10])
t = set([1,2,3,4,5,6,7,8,9,10])

# 基本运算
a = t | s          # t 和 s的并集  
b = t & s          # t 和 s的交集  
c = t – s          # 求差集（项在t中，但不在s中）  
d = t ^ s          # 对称差集（项在t或s中，但不会同时出现在二者中） 

# 基本操作：  
t.add('x')            # 添加一项  
s.update([10,37,42])  # 添加多项  
t.remove('H')     #删除一项
```
以下来自[官方参考](https://docs.python.org/2/library/sets.html)：

![image](https://user-images.githubusercontent.com/14041622/36139421-626ac50e-10d8-11e8-8f40-eb63c095956e.png)

![image](https://user-images.githubusercontent.com/14041622/36139390-467c0b3c-10d8-11e8-95e4-072b164ac9c3.png)



# Python Logging 日志记录入门
> `Python Logging`原来真的远比我想象的要复杂很多很多，学习路线堪比git。但是又绕不过去，alternatives又少，所以必须要予以重视，踏踏实实认认真真的来好好学学才行。

学习Logging的目的：
简单脚本还好，print足够。
但是稍微复杂点，哪怕是三四个文件加起来两三百行代码，调试也开始变复杂起来了。
再加上如果是后台长期运行的那种脚本，运行信息的调查更是复杂起来。
一开始我还在各种查`crontab`的日志查看，或者是`python后台运行查看`，或者是`python stdout的获取`等等，全都找错了方向。
真正的解决方案在于正确的logging。
记录好了的话，我不需要去找python的控制台输出`stdout`，也不需要找`crontab`的日志，只需要查看log文件即可。
下面是python的logging学习记录。

### 最简单的日志输出（无文件记录）
```python
import logging
 
logging.error("出现了错误")
logging.info("打印信息")
logging.warning("警告信息")
```

## 首先，忘掉logging.info()! 忘掉logging.basicConfig()!
网上各种关于python logging的文章实在是太不体谅新手了，logging这么复杂的东西竟然想表现得很简单，还用各种简单的东西做假象。
实际上我们真正要用起来的日志，绝对是不会直接用`logging.info()`和`logging.basicConfig()`这样的，这是此模块的官方推出来迷惑人的——看似让你一键上手，快速看到结果，但是跟实际真的不搭！
所以为了后面解释起来轻松，必须先警告这点：忘记它们俩！
记住，唯一要用到`logging.`什么的，就只有`logging.getLogger()`这一次。

## 了解logging的工作流
不想上流程图一类的东西，那样反而更迷糊。
简单说吧：
`logging`模块是会自动将你自定制的logger对象`全局化`的，
也就是说，
你在自己的模块里只要定义了一次某个logger，比如叫`log`，那么只要是在同一个模块中运行的其他文件都能读取到它。
比如说，你在主文件`main.py`中自定义了一个logger，可能设置了什么输出文件、输出格式什么的，然后你在`main.py`中会引用一些别的文件或模块，比如`sub.py`，那么在这个`sub.py`中你什么都不用设置，只要用一句`logger = logging.getLogger('之前在main.py定义的日志名')`即可获得之前的一切自定义设置。

当然，被调用的文件（先称为子模块）中，用`logging.getLogger('日志名')`时，最好在日志名后加一个`.子名称`这样的，比如`main.sub`。这样输出的时候就会显示出来某条日志记录是来自于这个文件里了。当然，`.`前面的父级logger必须名字一致，是会被识别出来的！
然后，子日志还可以再子日志，甚至一个子模块可以再让所有函数各又一个子子日志，比如`main.sub.func1`这样的。logging都会根据`.`识别出来上下级关系的。

这样一说，实际上也就是class类继承的那种机制了。你按照父级名称继承，然后还可以改写自己的新设置等。

了解了这些概念以后，才能来谈代码。实际上也就好理解多了。

## 设置logger的方法
看来看去，这篇文章说得比较全面也最清楚，以下很多都参考到它的内容：[Python 101: An Intro to logging](https://www.blog.pythonlibrary.org/2012/08/02/python-101-an-intro-to-logging/)

一般想要自定义一个logger，比如让它输出信息时按照什么格式显示，输出到哪个文件，要不要输出到屏幕一类，有三种方法可以达到设置：
- 直接在python代码里设置
- 用外部的config.ini文件配置
- 用python的dict字典配置

三种达到的目的都是一样的，字典用的人很少也不方便，配置文件比较好用只是`.ini`的语法不是很方便读，且不容易做到变量的动态设置，所以一般直接在python代码里写就好。

## 常用设置语句

以下是程序主入口文件的通用写法，注意，一定要在主入口定义好logger，这样其他所有的子模块才能够继承到。
```python
#   main.py
import logging
import otherMod2   # 等下会调用到的子模块

def main():
    """
    这个文件是程序的主入口
    """

    define_logger()

    log = logging.getLogger('exampleApp')

    # 输出信息测试
    logger.info("Program started")
    result = otherMod2.add(7, 8)     # 这个是来自别的模块的方法
    logger.info("Done!")

def define_logger():
    logger = logging.getLogger("exampleApp")
    logger.setLevel(logging.INFO)

    # 设置输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
    # 设置日志文件处理器
    fh = logging.FileHandler("new_snake.log")
    fh.setFormatter(formatter)    # 为这个处理器添加格式

    # 设置屏幕stdout输出处理器
    sh  = logging.StreamHandler(stream=None)
    sh.setFormatter(formatter)
 
    # 把处理器加到logger上
    logger.addHandler(fh)
    logger.addHandler(sh)
 
if __name__ == "__main__":
    main()
```

下面是子模块中的调用方法（很简单）：
```python
# otherMod2.py
import logging
 
module_logger = logging.getLogger("exampleApp.otherMod2")

def add(x, y):
    # 这里一句`getLogger`就继承到父级的logger了
    logger = logging.getLogger("exampleApp.otherMod2.add")

    # 输出测试
    logger.info("added %s and %s to get %s" % (x, y, x+y))
    return x+y
```

注意，`主文件`中，在什么地方定义logger都可以，可以在`main()`里也可以在任何单独的函数或类里，无所谓。只要在调用子模块之前定义好了就可以了。一旦定义过，`日志名`就会被记下来，然后子模块就可以轻松继承到。


# 定期执行Python脚本
目前知道的有两种方法：python自带的`time.sleep()`定时器循环执行某段代码 和 linux系统的`crontab`命令定期执行某个脚本


- `time.sleep()`方法，这个方法是执行脚本一次，然后内在代码在`while`循环中定期迭代。这种的问题在于，一旦将程序切换到后台，或者部署在服务器上断开ssh连接时，脚本就停止了。
- `crontab`方法，是定期执行整个脚本。这个能够满足一般要求，唯一问题是它不会输出任何脚本的stdout，而是默默的执行。所以要想做这个，又能看到进程，需要用比较复杂的方法来配合执行。


# Python执行脚本将输出重定向时编码错误
> 原本以为python内部的编码问题解决了，但是用linux命令将标准输出重定向时没想到又遇到了亲切的编码问题。

![image](https://user-images.githubusercontent.com/14041622/36322055-f02f0200-1386-11e8-8071-d394cca60f68.png)

根据[文章](http://www.708luo.com/posts/2014/06/python-print-encode-error/) 和 [文章](https://mozillazg.com/2014/01/python-fix-shell-python-program-redirect-to-file-raise-unicodedecodeerror)的解释，是因为linux的重定向命令并不知道python文件的输出编码而默认使用了ascii，所以当输出有超出128的字都会报错。
解决方法很简单：

在执行python的命令前加上`env PYTHONIOENCODING=utf-8`，如：
```shell
env PYTHONIOENCODING=utf-8 python ~/hello.py >> log.txt
```

还可以分开写：
```
$ export PYTHONIOENCODING=utf8
$ python hello.py  > hello.txt
```

这里还有一些相关的[stackoverflow回答](https://stackoverflow.com/questions/3828723/why-should-we-not-use-sys-setdefaultencodingutf-8-in-a-py-script)。

## 这还是不能输出所有内容
因为linux输出重定向的道理（在刚刚写的Linux学习的篇章里有专门说明），光是编码还不行，会发现还有很多内容并没有转向到文件里，而还是显示在屏幕上了。
其实我们上面写的转向语句，只是把显示在屏幕上的`stdout`标准输出转向了日志文件，可是还有`stderr`标准错误没有转向到日志文件，所以才显示到了显示屏里。
虽然看上去很多内容看起来并不是错误，比如`git push`的正常返回，好像和`stderr`标准错误没什么关系，可是它们本质上是通过`stderr`输出到屏幕的，只是我们不知道而已。
所以这时候，
应该把标准错误合流到标准输出里，一起转向。
在命令的结尾加上`2>&1`，让2转向1，意思就是让标准错误转向至标准输出。其中`>`代表`Redirect to`，`&`没意义只是用来告诉系统后面的1是代表输出设置，而不是文件名。

用上面的例子，这里应该这样写：
```shell
env PYTHONIOENCODING=utf-8 python ~/hello.py >> log.txt 2>&1
```

然后，哒哒！屏幕上不会显示任何内容了！也就是说所有的东西都转向了log.txt文件里保存。


# Python clipboard/pasteboard image 处理剪切板图像问题
目前python对剪切板的原生支持几乎是没有，必须下载第三发模块。
目前比较流行的是跨平台最好的`pyperclip`和比较强大的`gtk`。
但是pyperclip虽然简单易用，但是只支持文字，不支持图片等。
gtk支持剪切板中的图像，但是代码较复杂，因为它原本是为了做桌面程序的库。

再深入调查，python专门处理的图像的`PIL`库以及其升华版`Pillow`库，也并不能完好支持剪切板图像的读取。Pillow只能支持windows平台上的剪切板图像读取。

看到这么麻烦，我试图转换思路：
看看能不能用外部程序如命令行等先把剪切板图片保存为本地图片然后再让python来处理。
但是，linux和mac都原生对剪切板图像的支持也不是很好，即使是第三方应用xclip、xsel等建立在x window基础上的应用也很难做到这个简单的东西。
目前在Mac平台上比较好用的相关命令行应用，只有`pngpaste`。方便好用，只是不支持gif和在文件上直接复制来的数据。

还是不够满意，于是再深度搜索和阅读大量的文章、大量的尝试，最后得到Mac上处理剪切板图像的python方案：`PyObjC`库。
`Pyobjc`库是用python实现与Mac电脑基层api连接操作的库，在操作Mac OS底层问题上十分强大。
`pyobjc`中有一个AppKit模块，而Appkit模块中有一个NSPasteboard类，有非常全面的支持剪切板操作的方法支持。
我的Mac系统是Sierra，10.12，在以前安装过xcode的基础上，直接用`pip install pyobjc`即可完成整个库的安装，非常简单。注意：为了怕库太复杂影响系统其他程序操作，所以我打开virtualenv环境，安装在项目里而不是系统里。
安装好后就可以直接在python里面编码了。以下代码改编自[这篇简书文章](https://www.jianshu.com/p/7bd4e6ed99be)：
```python
# pasteboard.py

import os
import time

# 从PyObjC库的AppKit模块引用NSPasteboard主类，和PNG、TIFF的格式类
from AppKit import NSPasteboard, NSPasteboardTypePNG, NSPasteboardTypeTIFF

def get_paste_img_file():
    """
    将剪切板数据保存到本地文件并返回文件路径
    """
    pb = NSPasteboard.generalPasteboard()  # 获取当前系统剪切板数据
    data_type = pb.types()  # 获取剪切板数据的格式类型

    # 根据剪切板数据类型进行处理
    if NSPasteboardTypePNG in data_type:          # PNG处理
        data = pb.dataForType_(NSPasteboardTypePNG)
        filename = 'HELLO_PNG.png'
        filepath = '/tmp/%s' % filename            # 保存文件的路径
        ret = data.writeToFile_atomically_(filepath, False)    # 将剪切板数据保存为文件
        if ret:   # 判断文件写入是否成功
            return filepath
    elif NSPasteboardTypeTIFF in data_type:         #TIFF处理： 一般剪切板里都是这种
        # tiff
        data = pb.dataForType_(NSPasteboardTypeTIFF)
        filename = 'HELLO_TIFF.tiff'
        filepath = '/tmp/%s' % filename
        ret = data.writeToFile_atomically_(filepath, False)
        if ret:
            return filepath
    elif NSPasteboardTypeString in data_type:
        # string todo, recognise url of png & jpg
        pass

if __name__ == '__main__':
    print get_paste_img_file()

```


# Python图片转化为Base64编码
常用github api上传文件或图片，必须要将文件转化为base64编码才能上传。所以这里总结了下：
```python
import base64

with open('PATH-TO-IMAGE', 'rb') as f:
    pic = f.read()

print base64.b64encode(pic)
```


# `pip freeze`命令显示当前环境所有安装的package
对于我们经常使用virtualenv虚拟环境来说，经常需要指明需要哪些python package倚赖包。另外由于virtualenv如果和git仓库共存的状况下，我们必须要屏蔽文件夹里所有virtualenv的内容，所以这种情况更需要有一个显示的方法指明项目需要哪些倚赖包。
很简单的一句话就搞定：
```
pip freeze > requirements.txt
```
这样的话，pip就会自动显示出当前环境下已安装的所有package包，并且利用`>`重定向，输出到一个txt文档里。
以后的话，还可以用这个txt文件达到一键安装所有倚赖：
```
pip install -r requirements.txt
```


# Python运行`matplotlib`时报错：`Python is not installed as a framework.`

[参考这篇回答](https://stackoverflow.com/questions/21784641/installation-issue-with-matplotlib-python)。
即使我的matplotlib是在virtualenv虚拟环境里安装的，它还是会在用户目录下生成一个`~/.matplotlib`目录。
然后我们在创建一个文件并填入一句话：
```
touch vim ~/.matplotlib/matplotlibrc
echo "backend: TkAgg" > ~/.matplotlib/matplotlibrc
```
![image](https://user-images.githubusercontent.com/14041622/36632771-c3775e02-19c5-11e8-9987-819cd66d3e2a.png)



# Virtualenv虚拟环境的正确使用方法
之前当真以为是每个小项目都配置一个virtualenv环境，就每个文件夹都分别用`virtualenv`命令生成一个环境，还出现了一大堆文件夹，而且每次都要`pip install`重新安装一系列东西。
再加上很多小项目都有git配置，两者冲突，所以必须在`.gitignore`文件里屏蔽virtualenv都一切文件夹。

后来发现：
virtualenv虚拟环境不是只在这一个文件夹里生效的，它是那种只要开启了，你就带着这个虚拟都帽子到哪里哪个文件夹哪个项目都生效。
所以我就想，直接配置一个单独的文件夹专门放置virtualenv环境，然后每次都开启着它然后`cd`到项目文件夹去操作就行了。
这样既不会搞乱系统python环境，又不会每次都创建环境那么麻烦，毕竟不是什么大项目嘛。
如果是大型的项目，再单独在项目其中创建一个虚拟环境就好了。绝大多数时候，我只需要一个虚拟环境代替系统的python环境就足够了。

步骤是这样的：
1. 随便建一个位置，比如`cd ~/`，然后`virtualenv venv`，创建了一个叫`venv`的文件夹并且在里面配置了虚拟python环境。
2. 配置命令行别名：`alias venv="source ~/venv/bin/activate"`，这样就能一键开启虚拟空间，带上小帽子。
3. 安装自己所有需要的包，代替系统环境：`pip install PACKAGE-1 PACKAGE-2...`，或者`pip install -r PATH/requirements.txt`从之前的备份列表中一键恢复安装。


# Python requests返回`Max retries exceeded`错误
经常在脚本访问API时接受到这个反馈，这个可以理解因为一般一个ip太频繁访问某个网址就会被服务器拒绝。
但是比如我访问Github的API，明明已经通过认证且每小时5000次访问量了，怎么会没消费掉访问量就被返回`Max retires`呢。
查了很多文章，大家只是说让requests去sleep一会儿再访问，但是这不是正确的解决方案。
最后通过这个回答，真的一键解决了：
![snip20180225_61](https://user-images.githubusercontent.com/14041622/36638698-06b33364-1a37-11e8-9f06-b4a472e10c82.png)


也就是，安装这个包就好了：`pip install pyopenssl`或`pip install -U pyopenssl`。也就是当时报错里提示的关于`SSL`的什么东西，这样就解决了。


# `crontab`和`virtualenv`搭配使用
`crontab`是linux系统下定时执行任务的命令，`virtualenv`是python虚拟环境。
那么，怎么让crontab定时执行某个python脚本时是保证在virtualenv的虚拟环境中运行的呢？
答案是：
~在crontab执行shell命令时，不是用系统默认的python如`python PATH-TO-SCRIPT.py`这样的，而是指定运行虚拟环境中的python，如`~/venv/bin/python PATH-TO-SCRIPT.py`这样的。~
参考[这篇文章](https://stackoverflow.com/questions/4150671/how-to-set-virtualenv-for-a-crontab)。


# `pip uninstall`卸载包或`pip install`时发生`Operation not permitted`错误
在Mac上，无论是pip uninstall还是`sudo pip uninstall`，都会发生这个错误。
实际上，是Mac装机自带python的固有问题，包括如果不`sudo pip`就不能用的问题，都是这里的原因。
解决方法很简单：
只要`brew reinstall python`就全解决了！
注意，重装python意味着很多之前装的packages包都会丢失，请用`pip freeze requirements.txt`备份。

当然，我目的就是为了清楚所有系统python环境下的包才重装的，结果发现重装python之后还顺便解决了之前的各种权限问题。现在不用sudo也能`pip install`和`pip uninstall`了。
删除了系统python中所有的packages后，感觉轻松了很多。
之后就可以无忧无干扰的在virtualenv下安心编程了。



# 研究Python某些库附带安装的一些packages包
> 卸载系统python的安装包时，由于需要手输几十个包的名称，发现了一些有意思的。后来知道这些包是安装Jupyter Notebook时附带安装的，看起来可以作为以后自己使用的包，以下列一些参考。

- [`bleach`](https://bleach.readthedocs.io/en/latest/) 强大的HTML净化库，可以将html标签编码为安全的url格式，也可以将url生成A标签等。
- [`gitdb2`](https://github.com/gitpython-developers/gitdb) 纯python实现的git 对象数据库
- [`MarkupSafe`](https://pypi.python.org/pypi/MarkupSafe/1.0) HTML的处理工具
- [`modulegraph`](https://pypi.python.org/pypi/modulegraph/0.16) Python modules倚赖分析
- [`mistune`](https://pypi.python.org/pypi/mistune/0.8.3) 纯python实现的Markdown渲染引擎
- [`pathlib2`](https://docs.python.org/dev/library/pathlib.html) 处理文件路径的库 升级版
- [`pathtools`](http://pythonhosted.org/pathtools/) 文件路径相关的处理库
- [`prompt-toolkit`](https://pypi.python.org/pypi/prompt_toolkit/1.0.15) 纯python实现，开发命令行软件的强大库。
- `PyGithub`简单的操作github的库。
- `python-dateutil`强大的补充系统datetime的库
- [`requests-toolbelt`](https://pypi.python.org/pypi/requests-toolbelt/0.8.0)强化requests的库
- `scandir`更快速循环读取目录文件的库，代替os.walker()
- [`Send2Trash`](https://pypi.python.org/pypi/Send2Trash/1.5.0)跨平台实现原生删除文件到回收站。
- `six`python2和3兼容的库
- `testpath`检验目录文件的库
- `watchdog`监控系统事件和文件变动
- [`webencodings` ](https://pythonhosted.org/webencodings/) 处理上古网页遗留的编码问题



# Python 批量卸载packages包
不像`pip install -r requirements.txt`可以批量安装包，卸载就没有原生方法了，需要用巧劲。
目前Stackoverflow有这么一种用法：
`pip freeze | grep pyobjc-framework | xargs pip uninstall -y`
其中`pyobjc-framework` 是搜索关键字，搜索包含这些字的包然后批量卸载。
如果不是指定某些关键字，直接`pip freeze | xargs pip uninstall -y`，那么就是卸载所有的包了。
不出所料的话，应该是执行不了的，总有哪个包的卸载会出错，然后中断进程。

如果想达到`恢复出厂设置`的感觉，那么直接类似`brew reinstall python`这样的重装python就可以了罢。不过我再重装后，虽然很多删掉了，但还是会有些遗留，需要手动清除。



# `Python List Comprehension`
指的Python单行循环:
```python
a = [n for n in alist if n>0]
```

## 进阶
如果在单行循环中，想获得某个item的序号，那么就需要用到python自带的`enumerate()`函数
```python
# Python "List Comprehension" method
old = ['zero', 'one', 'two', 'three', 'four', 'five', 'six']
new = [item for index, item in enumerate(list1) if index < 4]
print new

# Output:
['one', 'two', 'three']
```
注意：使用`enumerate()`时，必须用2个变量承接它的返回值，第一个是index序号，第二个是item本身。




# Python去除空白字符
Python里面不是trim，而是strip.
```
# 去除两边所有空白字符
string.strip()

# 去除两边指定的字符 (不分顺序)
string.strip('\r\t\n')

# 只去除左边、右边，用法同上
string.lstrip(s)
string.rstrip(s)
```


# 升级`pip`报错：`ImportError: module 'pip' has no attribute 'main'`
[参考：解决 ImportError: module 'pip' has no attribute 'main'](https://blog.csdn.net/Jiaach/article/details/80188262)

正在用pip（没有在虚拟环境中，直接在系统里操作的），提示我可以将9.9升级到10.0，然后就`sudo pip install --upgrade pip`了，结果就报这个错误，导致所有的pip操作都无法进行。找到解决方案如下：

![image](https://user-images.githubusercontent.com/14041622/39810142-823a9474-53b6-11e8-92f0-81bcd49d1798.png)


```shell
## 如果报权限错误 则加上sudo
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py;python get-pip.py
```
完成。




# `BeautifulSoup`
> BeautifulSoup是Python包里最有名的HTML parser分解工具之一。简单易用

## 安装：
```shell
pip install beautifulsoup4
``` 
注意大小写，而且不要安装`BeautifulSoup`，因为`BeautifulSoup`代表3.0，已经停止更新。

## 常用语法
[参考我之前的文章：BeautifulSoup ：一些常用功能的使用和测试](https://www.jianshu.com/p/55fc16eebea4)

```py
# 创建实例
soup = BeautifulSoup(html, 'html5lib')
```

## 选择器
根据不同的网页，选择器的使用会很不同：
- 绝大部分下使用CSS选择器`select()`就足够了
- 如果按照标签属性名查找，而属性名中有`-`等特殊字符，那么就**只能**使用`find()`选择器了。

```py
# 最佳选择器: CSS选择器（返回tag list）
results = soup.select('div[class*=hello_world] ~ div')

for tag in results:
    print(tag.string)       #print the tag's html string
    # print(tag.get_text())     #print its inner text

#单TAG精确选择器：返回单个tag. 
tag = soup.find('div', attrs={'class': 'detail-block'})
print(tag.get_text())

# 多Tag精确选择器: 返回的是text，不是tag
results = soup.find_all('div', attrs={'class': 'detail-block'})

# 多class选择器(标签含有多个Class)，重点是"class*="
results = soup.select('div[class*=hello_world] ~ div')
```

## 获取值
```py
tag = soup.find('a')

# 只获取标签的文本内容
text = tag.get_text()

# 获取标签的全部内容(如<a href='sdfj'> asdfa</a>)
s = tag.string

# 获取标签的属性
link = tag['href']
```

## 修改值
[参考：Beautiful Soup（四）--修改文档树](https://blog.csdn.net/yybmec/article/details/44426081)

```py
tag = soup.find('a', attrs={'class': 'detail-block'})

#修改属性
tag['href'] = 'https://google.com'

# 修改内容 <tag>..</tag>中间的内容
tag.string = 'New Content'

# 删除属性
del tag['class']

```

## 对象类型
在我们使用选择器搜索各类tag标签时，BeautifulSoup会根据使用的函数而返回不同类型的变量。而不同的变量的使用方法也需要注意。

- Tag类型（`<class 'bs4.element.Tag'>`）:
    - `tag.string`
    - `tag.get_text()`
    
- 可遍历字符串类型（`bs4.element.NavigableString`）:
- Comment类型（`<class 'bs4.element.Comment'>`）:

## 增删改标签
[参考：使用BeautifulSoup改变网页内容](https://blog.csdn.net/abclixu123/article/details/39754799)

```py
# 修改标签内容
tag = soup.find('title')
tag.string = 'New Title'
```


# Python 对url的操作
Python原生带有url的切割、组合、识别等包，可以很轻松引用。
[参考官方文档： urlparse](https://docs.python.org/2/library/urlparse.html)

## Url parse （解析）
![image](https://user-images.githubusercontent.com/14041622/39822297-c629a000-53dc-11e8-9c18-528416007562.png)


## Url join （组合）

![image](https://user-images.githubusercontent.com/14041622/39822351-ecaf83de-53dc-11e8-9421-208e646bd501.png)



# Virtualenv创建Python3环境

## Mac安装Python3
> 注意，一般没什么人会完全删除Python2.7而只用Python3， 所以几乎都是同时安装Python2.7和Python3.

[参考官方文档：在Mac OS X上安装Python 3](http://pythonguidecn.readthedocs.io/zh/latest/starting/install3/osx.html)

一般Ubuntu或Mac默认是Python2.7， 所以需要先安装系统的Python3环境，Virtualenv才能够通过它来创建虚拟环境。需要注意的是，不同系统和不同包管理器的安装方式不一样，注意你选择的安装方法一定不能和Python2.7冲突。
Mac的话，需要麻烦一点，
`brew install python3`是行不通的，因为会提示`Error: python 2.7.14_3 is already installed. To upgrade to 3.6.5, run `brew upgrade python.`
具体操作如下：
```shell
$ brew upgrade python

#==> Upgrading 1 outdated package, with result:
#python 2.7.14_3 -> 3.6.5
```
然后很快就安装成果，并显示如下：
![image](https://user-images.githubusercontent.com/14041622/39858130-39e72d56-5468-11e8-9c7e-2804077921bd.png)

这个时候在命令行里输入`python`，就会直接跳入python3的编程环境了。
![image](https://user-images.githubusercontent.com/14041622/39858088-151357fc-5468-11e8-9308-dba3d3c4d421.png)

然后我们通过`which`命令，得知两种版本python的位置，便于之后virtualenv的设置：
![image](https://user-images.githubusercontent.com/14041622/39858273-a0c8e938-5468-11e8-893c-b001038f23c6.png)

## 安装Python3环境的Virtualenv
这个时候已经保证了本机同时存在Python2.7和Python3，那么安装虚拟环境就简单多了：
```shell
# 创建虚拟环境
$ virtualenv -p python3 ~/FOLDER-PATH/venv3
# 或更具体的指定路径（同样适用于Python2的安装）
$ virtualenv -p /usr/local/opt/python/libexec/bin/python ~/FOLDER-PATH/venv3

# 进入虚拟环境
$ source ~/FOLDER-PATH/venv3/bin/activate

# 退出环境
deactivate
```
然后就在你自己定义路径下添加了一个`venv3`文件夹，这就是你的虚拟环境啦。
每次只需要`source ~/FOLDER-PATH/venv3/bin/activate`就可以进入Python3的虚拟环境了。
当然，为了简单，我把这么长的一句话设置成为alias，一句`venv3`就可以简单进入环境。

## Python3虚拟环境下安装包
Python3的环境下，是需要用`pip3`来安装各种包的。

## 升级至Python3后Python2的异常
Mac中升级到Python3后，原本的`python`命令行关键字被直接指定为`python3`，而原有的python2需要通过`python2.7`来进入python2.

### 原来Virtualvenv的Python2环境下无法用pip安装包
![image](https://user-images.githubusercontent.com/14041622/39987342-112e22fc-5797-11e8-9c8d-2dec0981da57.png)
错误原文如下：
```shell
$ pip install requests
Collecting requests
  Could not fetch URL https://pypi.python.org/simple/requests/: There was a problem confirming the ssl certificate: [SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:590) - skipping
  Could not find a version that satisfies the requirement requests (from versions: )
No matching distribution found for requests
```

解决方案：在这个虚拟环境下，重新安装一下pip就好了：
```shell
$ curl https://bootstrap.pypa.io/get-pip.py >> get-pip.py
$ python get-pip.py

# 必要的时候升级下pip
$ pip install --upgrade pip
```
完成，顺利安装好后就能顺利install包了。







# Python2 乱码解决方案(Anti-TLDR)

```py
# 首先把所有相关字符串变量检查一遍
print type(s1)
print type(s2)
print type(s3)

# 然后把所有"unicode"格式的字符串转换成"str"格式
s1 = str(s1)
```
完成！


# `os.walk() 文件遍历`
> 学习os.walk文件遍历，最最最重要的是了解这种遍历方法的逻辑，它的路径！！不了解的话，永远也学不会。

os.walk()是Python原生的遍历文件夹方法，但是表现出来的逻辑真的不是很好记忆。

用法：
```py
os.walk(顶级目录地址, topdown=True, onerror=None, followlinks=False) 
```
函数返回一个三元Tupple: `(目录路径(字符串), 子目录名(列表), 文件名(列表))`

![image](https://user-images.githubusercontent.com/14041622/40161575-cdfbb2f2-59e3-11e8-8efd-8db59fe88c96.png)

## 遍历路径
`os.walk()`是**逐层扫描**的，一层一层来。
比如上图中，从`Root`根目录下开始扫，
- 先扫第一层，获得`pics1.jpg`, `pic2.jpg`, 然后是一个目录`New`和目录`Old`。
- 这个时候还不深入每个子目录，现在算完成一个循环，返回一个子目录列表: `[pics1.jpg, pics2.jpg, New, Old]`
- 然后在从上面的第一个子目录开始，往下扫，如同上面的过程。
- 完成第一个目录后，再继续第二个子目录。

记住，它不会无穷尽深入每一个目录一直到底，而是逐层扫。
**扫完一层后，再跳出来需要遍历的目录深入下一层。**

## 指定深度
os.walk默认是深入到底的，遍历所有的位置。有时候我们只需要一层或两层。
抱歉，os.walk()没这个功能，只能自己写。
方法就是：声明一个`depth`变量记录当前深度，循环到一定深度后，用`break`语句退出循环。
以下为示例代码：
```py
depth = 1
for root, subdir, filenames in os.walk():
    if depth is 2:
        break
    depth += 1
```


## 示例：只看文件
```py
search_dir = '/home/me/`
for root, subdir, filenames in os.walk(search_dir):
    print(root, subdir)
    for fn in filenames:
        print(fn)
```


# Python 文件基本I/O操作

## 操作模式 Mode

- `r`
> Opens a file for reading only. The file pointer is placed at the beginning of the file. This is the default mode.

- `rb`
> Opens a file for reading only in binary format. The file pointer is placed at the beginning of the file. This is the default mode.

- `r+`
> Opens a file for both reading and writing. The file pointer will be at the beginning of the file.

- `rb+`
> Opens a file for both reading and writing in binary format. The file pointer will be at the beginning of the file.
- `w`
> Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

- `wb`
> Opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

- `w+`
> Opens a file for both writing and reading. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.

- `wb+`
> Opens a file for both writing and reading in binary format. Overwrites the existing file if the file exists. If the file does not exist, creates a new file for reading and writing.
- `a `
> Opens a file for appending. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

- `ab`
> Opens a file for appending in binary format. The file pointer is at the end of the file if the file exists. That is, the file is in the append mode. If the file does not exist, it creates a new file for writing.

- `a+`
>Opens a file for both appending and reading. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.

- `ab+`
> Opens a file for both appending and reading in binary format. The file pointer is at the end of the file if the file exists. The file opens in the append mode. If the file does not exist, it creates a new file for reading and writing.


# Python3 编码乱码问题
> 没想到从Python2升级到3，还是有编码问题-_-!

## 小技巧
在txt等文本文件读取时，如果遇到打开文件乱码，那么最简单的方法是把文件拖到Chrome浏览器里，然后在Chrome开发工具的Console里检查文件的编码格式：
```js
>>> document.charset
'UTF-16LE'
```
检查好了，然后再到python里针对其进行解码。



# Jupyter Notebook 安装插件

## 安装插件管理器 Jupyter Nbextensions Configurator
[Refer to Github page.](https://github.com/Jupyter-contrib/jupyter_nbextensions_configurator)
首先需要安装Configurator：
强烈建议在Virtualenv虚拟环境下使用pip安装：
```shell
# 安装Jupyter的配置器
$ pip install jupyter_nbextensions_configurator

# 启动配置器
$ jupyter nbextensions_configurator enable --user
```
装好后，输入`jupyter notebook`命令打开网页，就会发现多出一个栏目：
![image](https://user-images.githubusercontent.com/14041622/40265819-32308d76-5b72-11e8-824d-0bedec50cb24.png)

## 安装颜色主题 Jupyter-themes
[参考：Github jupyter-themes](https://github.com/dunovank/jupyter-themes)

安装：
```sh
$ pip install jupyterthemes
$ pip install --upgrade jupyterthemes
```

使用方法：
`Jupyter-themes`实际上是一个命令行的命令工具，切换主题的话需要用命令行来执行。安装好后，就可以用`jt`命令来执行。

以下是常用的命令：
```sh
# 查看所有颜色主题 --list
$ jt -l

# 选择主题 --theme
$ jt -t 主题名称

# 恢复默认主题 --recover
$ jt -r
```


# Python 安装Mysql模块及安装中错误的解决 (Windows)

初试爬虫之后，各种快感。然后进入到Python练习的下一阶段了——把抓取到的数据存到数据库中。
再三考虑，还是决定从MySQL开始入手。虽然评论区很多倾向于SQLite及MongoDB等新潮玩意，但是MySQL还是占有决定性的市场。为了适应以后生存，这方面必须得会，就拿它先练手吧。

> 我的开发环境是中文win7系统32位， Python 2.7, MySQL 14.4。（Linux在虚拟机里呢，熟练之前先不挑战开发环境了-_-!）
> 注意：这里是安装python的`mysql模块`，而不是mysql, 到了这一步它应该是已经安装好了的（包括`MySQL Server`和`MySQL python connector`）。

**先检查自己是不是已经安装了这个模块**
极其简单：在Python的命令行中输入`import MySQLdb`，如果没有报错，那就已经安装了。
## 最简单的安装方法

其实就是随便找个地方按下`win+R`，输入`cmd`回车——打开windows命令行，进行著名的`pip安装大法`：  

> pip install mysql-python

按理来说，这一步足够了。但是我这出现了据说在windows环境下python安装模块的痛：命令行里返回了错误：

> error: Unable to find vcvarsall.bat

然后我想到，是不是在windows用`pip`不太合适？所以还是循规蹈矩地到[Python官网下载](https://pypi.python.org/pypi/MySQL-python/1.2.5#downloads)了MySQLdb的_源文件_，即[MySQL-python-1.2.5.zip](https://pypi.python.org/packages/source/M/MySQL-python/MySQL-python-1.2.5.zip#md5=654f75b302db6ed8dc5a898c625e030c) ([md5](https://pypi.python.org/pypi?:action=show_md5&digest=654f75b302db6ed8dc5a898c625e030c))这个压缩包。
随便找个地方解压缩，然后以最快的速度在cmd命令行中进入这个目录，输入：

> python setup.py build
> python setup.py install

按理来说，到这一步就完全成功了。不过，返回的结果是一毛一样的。。。

> error: Unable to find vcvarsall.bat

然后我就知道了：其实`pip`安装，和我自己下载源码用`python setup.py build` 、 `python setup.py install`是一样的效果。
问题源头还是在`vcvarsall.bat`这个东西上。一看文件名就知道是和vc相关。
查询相关资料，说是[凡是安装和操作系统底层密切相关的Python扩展，几乎都会遇到这个错误。](http://blog.csdn.net/secretx/article/details/17472107)
经过搜索，绝大多数的回答都是：需要安装`Microsoft Visual Studio`2008或者2010版本，才能满足Python在windows系统上安装各种底层扩展的需要。
正在下载2G的VS中。。。
**不过趁着下载等待时间，我在评论区发现了更easy的方法。。。。**
![image](https://cloud.githubusercontent.com/assets/14041622/11773086/c79be226-a25f-11e5-891a-ea4c73d5e1c9.png)
打开页面，http://www.lfd.uci.edu/~gohlke/pythonlibs/ 是这个模样：
![image](https://cloud.githubusercontent.com/assets/14041622/11773088/cf7ba4a4-a25f-11e5-8e8c-9212c424267a.png)

满屏幕毫无美感的英文，连排版都没有，真有点不太好接受。不过趁着VS还没下载完，就简单读了读，发现了第二行关键词：`University of California, Irvine.`，原来是加大的作品啊，一看就是科学家制作，比较大气，耐着心读了读说明段落——好像是专门针对windows对python支持性差做的工作——把python扩展都制作成了**二进制文件**，即`.whl`文件。
## 安装二进制的Python扩展包

看起来好像是个好东西，就`ctrl+f`查找mysql，还真找到了！

> MySQL-python, a Python database API 2.0 interface for the MySQL database
> Mysqlclient is a Python 3 compatible fork of MySQL-python.
> MySQL_python-1.2.5-cp27-none-win32.whl
> MySQL_python-1.2.5-cp27-none-win_amd64.whl

选择`win32.whl`这个文件下载，才772k。
但是这个`whl`文件格式怎么安装呢？回到网页上面，发现说了是用pip安装，于是我在这个目录打开cmd命令行，输入：

哈哈，献丑了！`whl`文件的安装方法，在`pip`的官方文档里说明的很清楚([看这里](https://pip.pypa.io/en/latest/user_guide/#installing-from-wheels))
所以再来了一遍：
输入：

> pip install MySQL_python-1.2.5-cp27-none-win32.whl
> 返回：
> Processing c:\tdownload\mysql\mysql_python-1.2.5-cp27-none-win32.whl
> Installing collected packages: MySQL-python
> Successfully installed MySQL-python-1.2.5

安装成功！

到Python里面试了一下`import MySQLdb`，也正常！
于是乎，我觉得写文章的这个功夫，已经下载好的Microsoft Visual Studio也没必要了。。。。



# Python 发送邮件
> 程序人员对于`邮件自动化`的日常需求还是很高的。但是入过了Linux的命令行邮件客户端如`Sendmail`, `Mutt`, `Alpine`等坑之后，发现现代其实很少人真的在用它们实现邮件自动化，根据搜索引擎里相关文章的数量就可知一二。取而代之的是，现代都在用Python或PHP等编程语言直接实现。Python更是自带一套模块实现邮件发送。

先上示例代码，之后再详解。

注：全部代码在Python3环境下测试通过，正常使用，正常显示，无需任何外置模块。

[参考：菜鸟教程 - Python SMTP发送邮件](http://www.runoob.com/python/python-email.html)
[参考：简单三步，用 Python 发邮件](https://zhuanlan.zhihu.com/p/24180606)

## `发送HTML格式的漂亮邮件`
```py
import smtplib
from email.mime.text import MIMEText

# Settings of sender's server
host = 'smtp.aliyun.com'
sender = 'Jason@aliyun.com'
user = 'Jason@aliyun.com'
password = input('Please type your password: ')
to = ['Jason@outlook.com']

# Content of email
subject = 'Python send html email test'
with open('./test.html', 'r') as f:
    content = f.read()

# Settings of the email string
email = MIMEText(content,'html','utf-8')
email['Subject'] = subject
email['From'] = sender
email['To'] = to[0]
msg = email.as_string()

# Login the sender's server
print('Logging with server...')
smtpObj = smtplib.SMTP() 
smtpObj.connect(host, 25)
smtpObj.login(user, password)
print('Login successful.')

# Send email
smtpObj.sendmail(sender, to, msg) 
smtpObj.quit() 
print('Email has been sent')
```

## `发送带附件的邮件`
```py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Settings of sender's server
host = 'smtp.aliyun.com'
sender = 'Jason@aliyun.com'
user = 'Jason@aliyun.com'
password = input('Please type your password: ')
to = ['Jason@outlook.com']

# Make content of email
subject = 'Python send email with attachments'
with open('./test.html', 'r') as f:
    content = MIMEText(f.read(),'html','utf-8')
    content['Content-Type'] = 'text/html'
    print('Loaded content.')

# Make txt attachment
with open('./txt.md', 'r') as f:
    txt = MIMEText(f.read(),'plain','utf-8')
    txt['Content-Type'] = 'application/octet-stream'
    txt['Content-Disposition'] = 'attachment;filename="txt.md"'
    print('Loaded txt attachment file.')

# Make image attachment
with open('./pic.png', 'rb') as f:
    img = MIMEImage(f.read())
    img['Content-Type'] = 'application/octet-stream'
    img['Content-Disposition'] = 'attachment;filename="pic.png"'
    print('Loaded image attachment file.')

# Attach content & attachments to email
email = MIMEMultipart()
email.attach(content)
email.attach(txt)
email.attach(img)

# Settings of the email string
email['Subject'] = subject
email['From'] = sender
email['To'] = to[0]
msg = email.as_string()

# Login the sender's server
print('Logging with server...')
smtpObj = smtplib.SMTP() 
smtpObj.connect(host, 25)
smtpObj.login(user, password)
print('Login successful.')

# Send email
smtpObj.sendmail(sender, to, msg) 
smtpObj.quit() 
print('Email has been sent')
```


# `pipenv虚拟环境`
> 2018的PyCon把最新型最先进的Python虚拟环境`pipenv`吵得火热。看了下介绍感觉真的很好用，它在`virtualenv`的基础上包装了一些更便捷的功能，解决了很多很多`virtualenv`欠缺的事情。

[参考pipenv的前世今生：PyCon 2018 之 Python 未来的依赖管理工具 pipenv](https://juejin.im/post/5b07620a518825389f5f4bb5)
[参考：pipenv 更优雅的管理你的python开发环境](https://segmentfault.com/a/1190000012837890)
[直接参考创造者Kenneth的官方说明](https://github.com/pypa/pipenv)

简单说，`pipenv`就是把`pip`和`virtualenv`包装起来的一个便携工具。

它不会在你的项目文件夹里生成一大堆东西，只有两个文本文件：
- `Pipfile`, 简明地显示项目环境和依赖包。
- `Pipfile.lock`, 详细记录环境依赖，并且利用了hash算法保证了它完整对应关系。只在你使用`pipenv lock`命令后才出现。

### 安装
Mac安装很简单，只要用Homebrew：
```shell
$ brew install pipenv
```

Linux的话，是用pip安装：
```
$ pip install --user pipenv
```
安装好后，终端里还调取不了命令，因为它现在只是个包。
需要先找到它的真是路径，然后为了方便把它加到bash或zsh等shell里面：
```sh
# 先获取python包的位置
$ python -m site --user-base
```
比如我的显示在`/home/pi/.local`，那么pipenv就藏在`/home/pi/.local/bin`里。
所以需要打开shell的设置文件，比如bash的话就编辑`~/.bash_profile`, zsh的话就编辑`~/.zshrc`，在里面把刚才查到的包路径存进去：
```
alias pipenv="home/pi/.local/bin/pipenv"
```
注意：我没有像其他人一样整个export进去，因为不知道为什么树莓派里面的zsh使用不来这个。


## 创建虚拟环境
在某个文件夹创建一个Python3环境：
```shell
# 泛指python的版本
$ pipenv --three

# 或者，特指某个python版本
$ pipenv --python 3.5

# 或者，特指某个位置的python
$ pipenv --python <path/to/python>
```
然后就会显示如下动态，可以看出来，`pipenv`调用了`virtualenv`，从本机把Python3环境拷贝一份到某个本机位置，然后在你的项目文件夹里只创建了两个文件`Pipfile`和`Pipfile.lock`，记录了所有你这个项目需要的环境配置，内容极其简单易懂：

![image](https://user-images.githubusercontent.com/14041622/40583975-943a9c14-61cb-11e8-8248-96d13523e246.png)

### 显示当前虚拟环境的储存位置
```sh
$ pipenv --venv
```

### 运行环境
运行虚拟环境(无需进入特定shell即可按照该环境运行脚本)：
```sh
$ pipenv run python xxx.py
```

### 进入环境
进入虚拟环境：
```shell
# 进入虚拟环境
$ pipenv shell

# 退出虚拟环境
$ exit
```
其实进入`pipenv`虚拟环境，本质上就是`virtualenv`的`source ./bin/activate`动作，只是使用不一样。进入后，你会发现用`deactivate`也是能生效的。但是：

注意：进入`pipenv`环境后千万不要用`deactivate`退出，而应该用`exit`退出。否则你再进去这个环境就会产生错误：
```
Shell for UNKNOWN_VIRTUAL_ENVIRONMENT already activated. 
No action taken to avoid nested environments.
```

### 安装packages包
```shell
$ pipenv install <包名>
```

你需要知道的是，进入pipenv虚拟环境后，你还是可以用`pip install`来安装包的，也能正常使用，因为virtualenv就是这样做的。
但是，这样你就不算使用了`pipenv策略`了，如果你要在项目文件夹里的`Pipfile`记录所有项目需要的依赖环境，就应该放弃使用`pip install`而使用`pipenv install`，这样你的`Pipfile`就会精确记录所有需要的依赖。

重新安装所有packages：
有时候需要冲github上clone项目，下载好后，只需要一句话就可以完成创建环境：
```sh
# 根据Pipfile中的描述安装所有依赖
$ pipenv install

# 或者，根据Pipfile.lock中的描述安装所有依赖
$ pipenv install --ignore-pipfile

# 或者，只安装dev组的依赖
$ pipenv install --dev

# 或者，根据曾经在pip上导出requirements.txt安装依赖
$ pipenv install -r <path-to-requirements.txt>
```

### 按照树形结构显示当前环境的依赖关系：
```sh
$ pipenv graph
```
然后就会显示出如下效果：
![image](https://user-images.githubusercontent.com/14041622/40592932-210992d6-6257-11e8-8901-e4dba397f21c.png)

### 删除虚拟环境：
```sh
# 删除某个包
pipenv uninstall <包名>

# 删除整个环境
$ pipenv --rm
```

## `pipenv lock`时遇到的SSL Error
错误反馈如下：
```
Pipfile.lock not found, creating…
Locking [dev-packages] dependencies…
Locking [packages] dependencies…
usr/local/Cellar/pipenv/2018.5.18/libexec/lib/python3.6/site-packages/pipenv/vendor/requests/sessions.py", line 508, in request
    resp = self.send(prep, **send_kwargs)
  File "/usr/local/Cellar/pipenv/2018.5.18/libexec/lib/python3.6/site-packages/pipenv/vendor/requests/sessions.py", line 618, in send
    r = adapter.send(request, **kwargs)
  File "/usr/local/Cellar/pipenv/2018.5.18/libexec/lib/python3.6/site-packages/pipenv/vendor/requests/adapters.py", line 506, in send
    raise SSLError(e, request=request)
requests.exceptions.SSLError: HTTPSConnectionPool(host='pypi.org', port=443): Max retries exceeded with url: /pypi/pyobjc-framework-netfs/json (Caused by SSLError(SSLError(1, u'[SSL: TLSV1_ALERT_PROTOCOL_VERSION] tlsv1 alert protocol version (_ssl.c:590)'),))
```
[参考`pipenv`的issue解答。](https://github.com/pypa/pipenv/issues/836)

最佳解决方案是：
```sh
$ pip install pyopenssl
```
因为这种SSL Error在其他地方也常见，一般都是没有在环境里安装`pyopenssl`的问题。所以不管你在哪个环境，如果出现这个SSL问题，就先装`pyopenssl`解决。
注意：不要用`pipenv install pyopenssl`，因为你真的不想在每个环境里都重新装一遍这个，干脆把它撞到本机：`$ pip install pyopenssl`.

## 常见错误操作

### 不要在`pipenv shell`里面运行`pipenv install`
尽量不要这样做，因为没有必要。
不过也有一些特殊情况，是需要这样做的：比如我在安装`Pillow`包的时候，只有在`pipenv shell`里面才能够安装成功。

### 不要在`pipenv shell`里面运行`deactivate`



# Python正则表达式Regular Expression

```py
import re
s = '<h3>下一个你需要输入的数字是83105. </h3>'

pattern = re.compile(r'<h3>\D+(\d{5})\D*</h3>')
result = pattern.findall(s)

print(result)
#out>>>  ['83105']
```


# Python字符串替换

```py
line = line.replace(';', ':')
```


# Jupyter Notebook改变默认打开的浏览器 (未完待续)

因为有开双浏览器的习惯，不喜欢Jupyter默认打开Chrome。所以希望它默认打开Opera。

[参考：Jupyter: Os X 下修改默认打开的浏览器](https://n3xtchen.github.io/n3xtchen/data_analytics/2016/12/03/jupyter-default-browser)

以下是Mac上修改默认浏览器方法：
```sh
# 先生成一个本地配置文件，以供修改
$ jupyter notebook --generate-config

# 修改刚刚生成的配置文件(.py文件)
$ vim ~/.jupyter/jupyter_notebook_config.py

# 搜索"browser"找到配置行

```


# Jupyter Notebook 修改快捷键


## 方法一：在网页里直接设置

直接在帮助菜单里找到`edit command mode keyboard shortcuts`：

![image](https://user-images.githubusercontent.com/14041622/41332078-da2c592e-6f0e-11e8-9b98-ba878b6d69d3.png)

然后修改对应的快捷键：

![image](https://user-images.githubusercontent.com/14041622/41332092-ee6ec520-6f0e-11e8-84e0-53483251d042.png)


## 方法二：修改自定义脚本.js文件

[参考官方文档：Keyboard Shortcut Customization](https://jupyter-notebook.readthedocs.io/en/stable/examples/Notebook/Custom%20Keyboard%20Shortcuts.html)

在用户目录下会有一个`.jupyter`目录，里面留有用户自定义的js和css文件，可以实现自定义修改，像vimrc和zshrc一样。

文件位置：`~/.jupyter/custom/custom.js`

修改方法：
在`custom.js`中加入以下javascript语句添加快捷键：
```js
Jupyter.keyboard_manager.command_shortcuts.add_shortcut('r', {
    help : 'run cell',
    help_index : 'zz',
    handler : function (event) {
        IPython.notebook.execute_cell();
        return false;
    }}
);
```
