# Machine Learning diary 机器学习日记
> By having a wild thought on start a career on Artificial intelligence, started today to do a tiny research on how to study AI. It turns out it consist of a shit black hole of knowledges, which means I have to study all of those things, not mention even some basic terms are causing a headache to me, such like Machine Learning, Deep Learning, Data Mining, Big Data, Classification etc etc. Thus I tend to write down some notes and random thoughts here helping me to organise it better. Saying, a tiny pen is better than a great brain.

## Prerequisites
### Math

- [x] Linear Algebra (Finished Basics)
PCA, SVD, Eigen Decomposition, LU Decomposition, QR Decomposition, Norms, Projection, Symmetric Matrix, Orthogonal Matrix, Matrix Operations, Vector Space, 
- [ ] Differential Calculus
- [ ] Integral Calculus
- [ ] Multivariable Calculus
微分和积分、偏微分、向量值函数、方向梯度、海森、雅可比、拉普拉斯、拉格朗日分布
- [ ] Statistics & Probability
组合、概率规则和公理、贝叶斯定理、随机变量、方差和期望、条件和联合分布、标准分布（伯努利、二项式、多项式、均匀和高斯）、 矩母函数 （Moment Generating Functions）、最大似然估计（MLE）、先验和后验、最大后验估计（MAP）和抽样方法。

### Computer Science
- [ ] Data Structures
- [ ] Algorithm & Optimization
这对理解我们的机器学习算法的计算效率和可扩展性以及利用我们的数据集中稀疏性很重要。需要的知识有数据结构（二叉树、散列、堆、栈等）、动态规划、随机和子线性算法、图论、梯度/随机下降和原始对偶方法。


### Programming (Python)
- [x] Jupyter Notebook
- [ ] matplotlib
- [ ] Numpy
- [ ] scikit-learn
- [ ] pandas

![image](https://user-images.githubusercontent.com/14041622/40230373-d8bd1028-5ac9-11e8-8a93-c00171b7576f.png)



## Differ all the basic terms for starters

- `Artificial intelligence`, is a superior area of all those below. But an AI could be human programmed to say something or recognise something, like coding line by line. 
- `Machine Learning`, could be so much better than human coded apps to do something. It lets machine itself to learn things and recognise things. So AI could whether has ML or not. 
- `Deep Learning`, a deeper science based logic for Machine Learning. Seems have something to do with neural something.
- `Data Mining`, machine learning is based of a shit load of data. Like a human learning something needs to encounter many things until he gets it. So Data mining is organising wild informations and provides to Machine learning.
- `Big Data`, means a load of informations, and the skill of Big data means how to handle with the data and how we can get some decisions from it.


Seems Kaggle and Ali Tianchi is a very good start for a beginner like me, and also it will be a good profile tag for a career starter who's without a solid CS background.


### `Data mining` or `web crawling` is not necessary for Machine Learning.  

For instance web crawler is only getting **EXTERNAL** data. But lots of company themselves have already had big data set, like clients' information, patiences' informatin. Only thing they want you to do is how to analyse the data.


# TL;DR. Archive Link: [Before starting Machine Learning](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-368832279)



# Examples of some categories of ML

## Unsupervised Learning examples
Only received data without any label or instruction, and you ask it to give you the answer.
- Customer. You give a whole book of customer contact list to it, and ask it to tell you what is each customer's salary?
- Language. So you're in a totally strange country and know nothing to their language, and there's no dictionary or any book as reference to your own language, then how do you understand them?
And that is what Unsupervised Learning is gonna do to solve.

## Reinforcement Learning examples
It will receive only SOME info, not by you but by itself, with some practice. 
- A toddler touch hot cup. Reinforcement learning is similar to Child Learning. A kid has curiosity to a hot cup and once he touches it he feels pain. So next time he remembers if he sees some white smoke come from the cup, he doesn't touch it.
- Playing game. You let the computer to play a game without telling it what's the move, and it starts to try every possible move, practise and practise, it remembers every 'fault move' it made and avoid it happens next time. 

## Supervised Learning examples
You feed it info with labels, right or wrong, then give a new data let it decide it's right or wrong.
- Spam and Ham emails. You give ton's of emails with classification label on each of it, let it learn , and let it predict a new email is a spam or ham.



# Baseline model
![image](https://user-images.githubusercontent.com/14041622/35781501-c8d5d338-0a25-11e8-8596-c08f1c2b8bc5.png)
![image](https://user-images.githubusercontent.com/14041622/35781530-5531a9e2-0a26-11e8-966a-13bfb7dd8e1f.png)
![image](https://user-images.githubusercontent.com/14041622/35781565-c369271e-0a26-11e8-9255-a632459342dc.png)
![image](https://user-images.githubusercontent.com/14041622/35781569-cab7ed2a-0a26-11e8-98b3-d5710bef570f.png)



# Types of learning (ML) - Note on Andrew Ng's course

### `Supervised learning`
feeding algorithm data with right answers, so it can predict more accurately.

To be more terminology, it’s also called `REGRESSION`: Predict continues value output.
 
### `CLASSIFICATION`
Depends on each result of the features comparison. A classification could have infinite features for comparing.

### `FEATURES`
A simple question for the data, like is it red or blue? Is its size ranged in large or small? It always falls into a simple output, 0 or 1, or 2,3,4 etc.

### `REGRESSION` problem VS. `CLASSIFICATION` problem?
?

### `UNSUPERVISED LEARNING`
giving an unsupervised algorithm a bunch of data without any label, for instance it don’t know it’s right answer or wrong, but let the machine itself to decide what’s the pattern in it. Simple one is, a CLUSTERING ALGORITHM can help to seperate data set to different clusters, group them, label them.

![image](https://user-images.githubusercontent.com/14041622/35790466-88869ea4-0a7d-11e8-93ed-15e4bf99067f.png)
￼

## Example of `Clustering Algorithm`
`Google News page`, it recognises all similar news and gather to a story board.

![image](https://user-images.githubusercontent.com/14041622/35790473-9150e8be-0a7d-11e8-8880-9035928ba6c2.png)

Other examples like genes, marketing, social networks etc., also could be having high demands on `CLUSTERING ALGORITHM`, aka `UNSUPERVISED LEARNING ALGORITHM`.


### `Octave`
a programming language, an alternative to Matlab. Aiming to build a Machine Learning prototype in a few lines of code. Highly recommended by Andrew Ng.



# `Octave`学习
> Matlab实在太贵，所以Andrew Ng推荐的完全开源免费的Octave却是个好的替代物。

关于为什么要用Octave，而不是用别的Matlab代替品如Freemat, Spider等，[这篇AskUbuntu](https://askubuntu.com/questions/80164/comparison-of-octave-spyder-freemat-and-scilab-as-alternatives-to-matlab)里有非常详尽的解答。

简而言之：Octave是Matlab毫无疑问的最好代替品，语法相似性达95%以上，功能完善，且社区、文档非常详尽。反之其它代替品，则要不就语法相似度低、要不就功能不全、要不就几乎没有文档学习参考。

## Octave 安装 （命令行中运行）
安装GNU官网的说明，[参考自己的平台安装方式](https://www.gnu.org/software/octave/download.html)。Mac上直接`brew install octave`即可。
![image](https://user-images.githubusercontent.com/14041622/36629461-f45176fa-1990-11e8-8c1a-0557abbdbd64.png)
可以看到，octave需要非常多的依赖包。我装了大概一个多小时吧。完成后，就可以通过命令行输入`octave`直接进入了：
![image](https://user-images.githubusercontent.com/14041622/36629588-7995b7a8-1992-11e8-829e-29c4925f4a52.png)


## Octave 安装 （包括GUI界面）
参考[官网页面](https://wiki.octave.org/Octave_for_macOS)。
Mac版的[GUI版Ocatave下载地址](https://sourceforge.net/projects/octave/files/Octave%20MacOSX%20Binary/2016-07-11-binary-octave-4.0.3/octave_gui_403_appleblas.dmg/download)，下载好后是大概300M的dmg文件。
然后打开后，完成初始提示，就可以看到主页面了：
![image](https://user-images.githubusercontent.com/14041622/36629809-52e0e962-1996-11e8-89cc-1027aff43f96.png)

## Octave绘图
命令行中的Octave也是能绘图的，只要用`plot(...)`函数就行。它会弹出一个小窗口，显示图形。效果如下：

![screencast 2018-02-25 01-03-33](https://user-images.githubusercontent.com/14041622/36632960-3fd7726e-19c8-11e8-8be4-12768b1ca0a5.gif)

## 关于Mac上Octave GUI客户端运行缓慢问题
需要注意的一点是，Mac上的Octave极其缓慢，程序经常自动停止运转，一个一根线的绘图更是要等很久。所以没有耐心的又想用Octave的，还是在命令行里用吧。


# 为什么要用IPython/Jupyter?  [TL;DR.](https://github.com/solomonxie/solomonxie.github.io/issues/24#issuecomment-363699464)


# Jupyter Notebook 绘图
> 苦于Matlab实在太贵， Octave又不能做笔记展示，所以考虑Jupyter用来做简单绘图，来辅助学习线性代数。

Jupyter 的魔法命令里有一个`%matplotlib inline`，可以直接在jupyter里面绘制出静态图形。但是需要先安装`mataplotlib`的package，简单一句`pip install matplotlib`搞定。
注意：最好还是在virtualenv里安装调试，这样也不需要`sudo pip install`也不会搞乱系统。
参考[这篇机器学习的jupyter笔记](http://nbviewer.jupyter.org/github/zlotus/notes-linear-algebra/blob/master/ReadMe.ipynb?flush_cache=true)，直接复制了某一段出图的代码，在jupyter里运行，哒哒！出图了！
![image](https://user-images.githubusercontent.com/14041622/36630706-99a3d03a-19a5-11e8-8b2d-33ecdcf4382f.png)


（在virtualenv里面安装各种包实在是太爽了，完全没障碍，不需要任何配置，不需要重启jupyter，完美运行）

#### 注意：Jupyter出的是静态图，如果用Matplotlib绘制动态图（动画）就不能用Jupyter了。


# Jupyter 绘制公式
在markdown模式下，用`$$`前后包括起来，然后在中间写上公式的表达式即可出现，如下图：
![image](https://user-images.githubusercontent.com/14041622/36630735-28bfc012-19a6-11e8-8536-bb64f8e5e2bb.png)

[这里是LaTex的公式符号对照表](http://blog.csdn.net/qq_39232265/article/details/78868487)。


# 命令行中Python利用`matplotlib`库绘制图形
一直好奇命令行里怎么显示图形，然后安装好matplotlib后看到原来是这样，效果如下：
![screencast 2018-02-25 00-50-55](https://user-images.githubusercontent.com/14041622/36632787-2640e486-19c6-11e8-9ce7-c948efe3a1d6.gif)



# 什么是`matplotlib`
说白了就是Python用来画图的库，画数学图。鼎鼎大名，功能强大。说成是Matlab替代品其实也行。

参考[中文文档](http://old.sebug.net/paper/books/scipydoc/matplotlib_intro.html)。
> matplotlib 是**python最著名的绘图库**，它提供了一整套和matlab相似的命令API，十分适合交互式地进行制图。而且也可以方便地将它作为绘图控件，嵌入GUI应用程序中。
它的文档相当完备，并且[Gallery页面](https://matplotlib.org/gallery.html#lines_bars_and_markers) 中有**上百幅缩略图**，打开之后都有源程序。因此如果你需要绘制某种类型的图，只需要在这个页面中浏览/复制/粘贴一下，基本上都能搞定。

[上百幅官方绘图参考](https://matplotlib.org/gallery.html#lines_bars_and_markers)。
![snip20180225_62](https://user-images.githubusercontent.com/14041622/36639038-0faea3c0-1a3e-11e8-9485-2ceb7c9b939b.png)





# ML 机器学习Python基础库安装
> 强烈建议在Virtualenv虚拟环境下安装所有的包，这样既不会和什么Anaconda冲突，又不会发生装不上、装错了、误删除等乌七八糟的事情。

建议进入Python3的虚拟环境：
```shell
$ source ~/VIRTUALENV-PATH/venv3/bin/activate
(venv3)$ python -V
# Python 3.6.5
```

## `Numpy安装`
```shell
$ pip3 install numpy
```
很简单就完成了：
![image](https://user-images.githubusercontent.com/14041622/39862919-b43bc058-5477-11e8-970f-33c93fa3dd94.png)

