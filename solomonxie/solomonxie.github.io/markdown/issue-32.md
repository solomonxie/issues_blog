# WEB APP DESIGN 网络应用设计
> 记录网络应用、网站建设等相关笔记。


# Markdown中插入数学公式
以下方法：
- Google Charts API（根据url地址返回公式图片）
- [Forkosh](http://www.forkosh.com/mathtex.html)（根据url地址返回公式图片）
- [Codecogs](https://latex.codecogs.com/)  （根据url地址返回公式图片）
- MathJax 引擎（引入js文件渲染markdown中LaTex公式）

## Google Charts API 制作数学公式图
都知道Markdown中插入公式不易，需要平台自己提供LaTex渲染引擎。
如果是自己的平台倒还好说，很简单引入一个js文件即可。
但是Github的README和issues等都默认是不支持LaTex的，也不能插入外部js文件。
所以在Github中显示正常的公式唯一的方法就是引用公式的图片。
目前最流行的是Google Chart API和Forkosh服务器，但是forkosh服务器连接不畅，除非自己架服务器搭建forkosh平台，否则就只能选google了。

[参考文章。](https://www.jianshu.com/p/888c5eaebabd)

用法如下：

```
![](http://chart.googleapis.com/chart?cht=tx&chl= 在此插入Latex公式)
```
注意：公式虽然是LaTex语法，但是特殊符号必须经过url编码才行，否则Github不显示。
例：
```
https://chart.apis.google.com/chart?cht=tx&chf=bg,s,FFFF00&chl=%0D%0A4x_0%5CDelta%28x%29%2B3%5CDelta%28x%29%2B2%5CDelta%28x%5E2%29%3E0%0D%0A
```
![formula](https://chart.apis.google.com/chart?cht=tx&chf=bg,s,FFFF00&chl=%0D%0A4x_0%5CDelta%28x%29%2B3%5CDelta%28x%29%2B2%5CDelta%28x%5E2%29%3E0%0D%0A)


## Codecogs 制作数学公式
相比Google来说，Codecogs采用了一样的url引用方式，一样的语法，且也必须是url编码。但是Codecogs提供了一个网页编辑器，可以直接在上面可视化编辑公式，然后直接拷贝图片链接即可，所见即所得，要快捷的多了。
当然如果在意服务器稳定性还是想用Google的话，那还可以把图片链接前面直接改成Google api的地址即可。

![image](https://user-images.githubusercontent.com/14041622/37030346-9e91bc2e-2175-11e8-997a-234be6a543c6.png)

生成好图片后，直接右键点击生成的图片获取链接即可。


# Wordpress
> Wordpress实在是太好用，就连鄙视PHP的人也不能说Wordpress不好。作为纯傻瓜式Web应用框架来说，Wordpress实在是让我这个小白从零开始做了一套完整的企业前后台网站。不能不在这里记录一些经验以供使用。

## Wordpress初始配置
> 一般是通过ssh连接远程服务器，在命令行里操作。

### 安装LNMP环境 （Linux+Nginx+Mysql+PHP)

```
#安装环境
sudo apt-get install php5-fpm nginx mysql-server php5-mysql
# 启动Nginx服务
service nginx start
```

### 安装Wordpress
```
# 下载wordpress
wget http://wordpress.org/latest.zip
# 解压wordpress
apt-get install unzip
unzip latest.zip
# 设置权限
chmod 777 -R /var/www/html/网站文件夹名
```

### 设置Mysql
```
# 登录mysql并设置密码
mysql -u root -p
##--创建数据库--
create database 数据库名;

```


# Github Pages建立静态网站
Github Pages对于建立静态网站来说真的是超级方便，概念方便，配置方便。
只要你不超出HTML+Javascript+CSS的范围，一切都好说。
如果为了漂亮，可以使用Bootstrap等各种技术加强页面显示，只要是静态的，一切都好说。

## 个人主页vs项目主页

[参考：单个GitHub帐号下添加多个GitHub Pages的相关问题](http://chitanda.me/2015/11/03/multiple-git-pages-in-one-github-account/)

Github Pages有两种建站方案，一种叫个人主页，一种叫项目主页:
- 个人主页：这种是你可以用自己的用户名为域名访问，如我的`solomonxie.github.io`。这是最简单的方法，网页放在master分支就可以显示。但是这种方法会有比较多限制：
    - 放网页的repo必须命名为`user.github.io`这种形式，user必须与自己的用户名完全相同。
    - 一个用户只能有一个这种域名。
- 项目主页：这一种是，你可以使用任意repo，但是域名就不是`user.github.io`这么简单的形式了。而是`user.github.io/repo`这种形式。
同时，你必须要把网页放在这个repo的`gh-pages`分支里，才能显示出来。

注意一般即使上传好了网页，也不会及时显示出来，有时可能会等几个小时Github才会显示最新的页面。


## 自定义域名的配置
一般`solomonxie.github.io`这种域名虽然已经很简单了，但还是挂着github的名字且有点长，始终摆脱不了供应商的影子。如果做为个人网站的话，这一点的确会影响些形象和印象的独立性。
所以有必要把这个域名映射到自己申请的外部域名上去。

以下为域名映射的操作步骤：
- 申请域名（略）
- 在存放网页的分支里(看是个人主页还是项目主页而定)，建立一个文件，名为`CNAME`，内容极其简单，只有一行，即你申请的域名，如：`solomonxiexie.com`。然后Github会根据这个域名设置，一直替你监听这个域名的访问，然后自动帮你做所有的映射工作。
- 然后回到你申请域名的服务商那里，找到域名的配置修改页面，修改域名的指向：修改A类域名，然后指向Github的IP地址。这个ip需要自己ping一下才知道。


# Jekyll 动态地建立静态博客网站
> 提前声明：Jekyll并不简单。它的学习曲线几乎相当于Wordpress，思路也比较相似。之所以把Jekyll从Github pages的介绍中独立出来，就是为了把简单的和复杂的区分开来，这样思路会比较清晰。

其实Jekyll是博客型网站的一种**新思路**。它彻底摒弃了`数据库`这种东西。
因为你需要的只是定期更新一些Markdown格式的文章，然后让它显示成网页，并放在一起成为网站而已。没必要大动干戈的设计数据库什么的。

简单的说，Jekyll是一个基于Ruby语言的静态博客网站制作工具，它可以把Markdown转换成HTML网页。

不过对于一个HTML网页来说，它得有标题、样式、日期什么的，甚至一些根据文章的不同而动态改变的内容等。这些都不是把Markdown转换成HTML而已。你需要在写Markdown文章时，就在最上方标明一些设定。这些都是需要学习的

> 另注：Jekyll虽然经常和Github Pages搭配，但其实是完全独立的产品。可以在任何地方使用。

## 安装Jekyll

安装Jekyll需要用Ruby的包管理器gem下载，像Python的pip一样：
```sh
$ gem install jekyll
```

用Jekyll创建一个网站（自动生成名为test_blog的文件夹和一个完整的Demo网站）：
```sh
$ jekyll new test_blog
```
目录里面内容如下：
![image](https://user-images.githubusercontent.com/14041622/41506105-dcfb6dbe-7249-11e8-8ab0-7f24eaedf69d.png)
这里面是完整的一个网站，可以直接运行浏览。
然后你就可以根据自己的主页、其它网页什么的，在这个基础上修改了。


本机运行网站：
```sh
$ cd test_blog
$ jekyll serve
```
然后jekyll会将网站映射到本机的一个端口，你可以打开命令行里提示的url链接察看网站效果。

![image](https://user-images.githubusercontent.com/14041622/41506042-66022d84-7248-11e8-9254-34f109bc4781.png)


### Jekyll new时发送错误：`Bundler: ruby: No such file or directory`
我的Mac机上从来没做过任何Ruby项目，也不懂gem使用方法。全部原始配置后，使用`gem install jekyll`没问题，但是在`jekyll new ..`时，就发送这个错误：
```
Bundler: ruby: No such file or directory -- /usr/local/lib/ruby/gems/2.5.0/gems/bundler-1.16.1/exe/bundle (LoadError)
```
发生错误后，项目文件夹是生成了，但是不完整，也不能执行。

问题在于本机的gem和bundler都不是很新，需要更新一下。
参考：https://github.com/rubygems/rubygems/issues/2180#issuecomment-369423426

更新如下：
```sh
# Install latest version of Rubygems
gem update --system

# Install latest version of bundler system-wide
gem install bundler
```
更新时间会很长，等全部安装好后，就可以正常的使用jekyll了。


## 制作网站
`Jekyll new`命令新建一个网站结构后，文件夹里面有很多文件。这些文件结构都是什么作用，是我们必须要学习的。

### Jekyll文件夹结构
- `_config.yml`文件：这是你第一个需要修改的东西。全网站的通用设置都保存在这里，比如网站主题，名称，介绍，域名，Github用户名等。`.yml`是像`.ini`一样的配置文件类型。
- `_site`文件夹：这个存放你的完整静态网站的文件夹，但是这是不需要你去碰的文件夹，它是Jekyll根据你的设置和模板之类的内容，自动生成的静态网站。
- `_layout`文件夹：是存放各种网页模板的地方，主页什么样子，列表页什么样子，博客内容页面什么样子，这些分别的页面模板都是放在这里的。
- `_includes`文件夹：存放所有重复使用的、比较固定的页面模块。比如每个网页都一样的页头、页脚，导航栏，侧边栏等等。这里面的HTML文件，都不是完整的HTML网页，都只是模块，可能只是一个`<div>`标签。
- `_posts`文件夹：存放所有的Markdown格式文件。你所有的Markdown博客内容，都放在这里。文件命名也是有规定的，比如必须是`data-title.markdown`这种。


### `Front-Matter`文件头信息
文件头信息在这里被叫做`front-matter`，它是写在每个Markdown文件头部的信息。主要是指明这篇文章标题、日期、使用的模板、样式、标签、分类等，这样Jekyll就可以根据这些设置把markdown文件转换成你想要的最终HTML网页了。
![image](https://user-images.githubusercontent.com/14041622/41506335-74900244-724e-11e8-8784-e699b4ebb8e9.png)


头信息的常用参数如下：
- `layout`: 指明模板名称，即指定使用`_layout`文件夹中哪个HTML网页做为模板。
- `title`: 这篇文章的标题。
- `data`: 这篇文章的日期。
- `categories`: 这篇文章的分类。