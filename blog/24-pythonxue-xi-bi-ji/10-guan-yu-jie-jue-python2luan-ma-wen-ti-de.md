# ❖ 关于解决Python2乱码问题的终极解决方案 (TL;DR)

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
