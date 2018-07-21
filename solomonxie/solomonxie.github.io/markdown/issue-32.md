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


# Jekyll 动态地建立静态博客网站 (Get Started)
> 提前声明：Jekyll并不简单，必须要正确的看待它。把它和PHP，JSP和Django等放在一起讨论会减少很多失落感。它的学习曲线几乎相当于Wordpress，工作流程和结构也几乎一样。

Jekyll与Wordpress最大不同的就是，没有数据库。但是体验上来说也算不上什么大差别。
彻底摒弃数据库，这算是一种Jekyll式的**新思路**。
因为你需要的只是定期更新一些Markdown格式的文章，然后让它显示成网页，并放在一起成为网站而已。没必要大动干戈的设计数据库什么的。

简单的说，Jekyll是一个基于Ruby语言的静态博客网站制作工具，它可以把Markdown转换成HTML网页。

不过对于一个HTML网页来说，它得有标题、样式、日期什么的，甚至一些根据文章的不同而动态改变的内容等。这些就不仅是把Markdown转换成HTML而已了。很多内容需要你在Markdown文件里面就写明指定。

> 另注：Jekyll虽然和Github Pages搭配免费，但其实是完全独立的产品。可以在任何地方使用，像Wordpress一样。

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



## 生成网站

渲染网站
```sh
$ cd test_blog
$ jekyll serve
```
或实时渲染网站：
```sh
$ jekyll server --watch
```
如果加上了`--watch`参数，jekyll就会实时监控你的文件，只要那个文件有变动了，比如新增了markdown文件，或修改了layout模板，它都会即时渲染生成网站，总保持更新。

运行渲染的命令后，jekyll就会把你的Markdown根据指定的模板渲染为静态网站，
同时还会把网站映射到本机的一个端口，你可以打开命令行里提示的url链接察看网站效果。

![image](https://user-images.githubusercontent.com/14041622/41506042-66022d84-7248-11e8-9254-34f109bc4781.png)


## Jekyll Workflow 工作流程
使用Jekyll，主要难就在一开始，需要设计网页样式，设置全站的规则等等。
但是一旦这些基本设置都完成了，以后更新就只需要专注的写Markdown文件即可。


## Jekyll自定义网站
`Jekyll new`命令新建一个网站结构后，文件夹里面有很多文件。这些文件结构都是什么作用，是我们必须要学习的。

### `Jekyll文件夹结构`
- `_config.yml`文件：这是你第一个需要修改的东西。全网站的通用设置都保存在这里，比如网站主题，名称，介绍，域名，Github用户名等。`.yml`是像`.ini`一样的配置文件类型。
- `_site`文件夹：这个存放你的完整静态网站的文件夹，但是这是不需要你去碰的文件夹，它是Jekyll根据你的设置和模板之类的内容，自动生成的静态网站。
- `_layout`文件夹：是存放各种网页模板的地方，主页什么样子，列表页什么样子，博客内容页面什么样子，这些分别的页面模板都是放在这里的。
- `_includes`文件夹：存放所有重复使用的、比较固定的页面模块。比如每个网页都一样的页头、页脚，导航栏，侧边栏等等。这里面的HTML文件，都不是完整的HTML网页，都只是模块，可能只是一个`<div>`标签。
- `_posts`文件夹：存放所有的Markdown格式文件。你所有的Markdown博客内容，都放在这里。文件命名也是有规定的，比如必须是`data-filename.markdown`这种。


注意：
- `_site`文件夹需要你在`.gitignore`中加入屏蔽，因为这个动态生成的东西，完全不需要在git里面进行追踪。而且放在Github Pages上的话，Github引擎也不会在你的目录里面生成这个文件夹，而是在后台直接给你生成页面。之所以会有它，主要是本地设计时候用。

### `Front-Matter 文件头信息`
文件头信息在这里被叫做`front-matter`,或`yml-header`，它是写在每个Markdown文件头部的设置信息。主要是指明这篇文章标题、日期、使用的模板、样式、标签、分类等，这样Jekyll就可以根据这些设置把markdown文件转换成你想要的最终HTML网页了。
![image](https://user-images.githubusercontent.com/14041622/41506335-74900244-724e-11e8-8784-e699b4ebb8e9.png)


头信息的常用参数如下：
- `layout`: 指明模板名称，即指定使用`_layout`文件夹中哪个HTML网页做为模板。
- `title`: 这篇文章的标题。
- `data`: 这篇文章的日期。
- `categories`: 这篇文章的分类。


## “真正的”拿到Jekyll生成的静态网站
Jekyll的最终目标和整个存在意义都是生成静态网站。
但是，
默认情况下，所谓生成出来的静态HTML页面，你也**不能**直接打开看到效果！必须要运行`jekyll serve`才行，或者把它放到Github的Repo里。
那还叫什么静态网站？！
真正的静态网站不是生成HTML就行了，而是让你双击打开HTML就能在浏览器看到效果。

避开这个有点矛盾的逻辑不说了，我们有比较方便的外部工具来做到这点。
那就是最常用的`wget`下载命令。
`wget`可以把网页或整个网站下载下来，并且能自动转换各种文件里的路径。
命令如下：
```$
$ wget -r --convert-links <URL>
```
所以当你运行`Jekyll serve`成功编译生成`_site`目录后，就可以用wget下载本地的这个网站了。


## Jekyll的体验

目前体验极其糟糕：
- 不能**真正**生成静态网站，必须开着Jekyll服务才能展示出网页
- Macbook air上运行jekyll服务器不到一会儿，CPU温度就极速增高
- 大概几十篇文章，就需要10s+的生成时间
- 各个主题安装极其不同，每个主题都需要单独学习其内在逻辑、变量、结构、生成方法，学习成本非常高
- 依赖性极高，很容易导致gem或nodejs依赖过期无效或出错
- Jekyll对配置文件的tokens（比如指定变量名）经常改变和更新，很快你写的配置文件就不管用老报错了。



# Jekyll 安装模版
实际上，Jekyll安装主题是非常反人类的——它一点也不比自己写模版简单，学习成本真是高。
安装主题不是把人家做好的template直接复制过来就能用了。
每个模版设置的变量设置名、依赖的gem包都不一样，还经常需要在本地安装所有依赖包，安装jekyll插件等。如果不懂Ruby gem的话，还真是不简单。

到了这里，一般人真的会问自己应不应该再继续下去。因为明明简单的东西，不知道是不是还值得了。

> 我相信所有坚持学习jekyll的人，都有自己非学不可的理由吧。


## 包管理器的理解
Jekyll是用Ruby语言构建的，且每个主题都会有超多的Ruby依赖包。在这里需要先理解一些基本概念才能进行下去。

- `Ruby`：是语言。这就不说了
- `Gem`：全称`RubyGems`，是Ruby的包管理器。相当于Python的pip。每一个包都叫`a gem`，在Python里叫`package`.
- `Bundler`：是管理gem管理器的管理器……相当于Python的pipenv，管理每个项目的gem包依赖。

简单说，gem主要管理整个系统的Ruby包，下载安装卸载之类。而Bundler只负责管理每个项目的Ruby包依赖。


## 一般安装方法
先讲讲一般通用的模板安装方法：
- 首先到模版的Github网页里clone下来全部文件。
- 在命令行里打开这个模版的文件夹（其实它就是一个完整的Jekyll文件夹结构）
- 首先直接运行这个主题：
```sh
$ jekyll serve
```
- 如果没有出错能直接使用最好，出错的话就走下一步。
- 输入以下命令安装模版所需的依赖环境：
```sh
$ bundle install
```
- 这样`bundle`命令就会会根据文件夹中的`Gemfile`文件下载安装所有模版所需的依赖环境。
- 静等结束之后，一般就可以`$ jekyll serve`直接运行网站了。
- 打开jekyll提示的网站，到处点一点，如果网站能正常运行，那么就可以把自己的markdown文章导入到`_posts`文件夹里了。
- 然后在每篇markdown文章的`Front Matter`里，把`theme`改成这个模版的名称，`layout`改成这个模版要求的layout等。
- 然后重新运行`jekyll serve`，开始运行服务。
- 复制命令行里提示的本地url地址(每个主题的地址都不同)，在浏览器里打开，就可以在网站上看到更新了。
- 如果出错，可以试试下面命令来启动服务，强制服务在当前依赖环境下运行。
```sh
$ bundle exec jekyll serve
```

至此，一般简单的模版都可以搞定了。如果超出任何以上提及内容，我们就要到"特殊安装方法"一节来分析了。


## 特殊安装方法
一般安装方法解决不了的，基本上算是特殊安装方法了。

经过我尝试了下载和安装几十个下载的主题后，发现如果碰见一个连`bundle install`命令都不用，直接`jekyll serve`就打开服务的，那简直是像中大奖一样的。
每个主题的安装都不太一样，且遇到的错误都完全不同。通用性极其小。

要想真正安装好一个主题，必须掌握基本的Debug能力，命令行信息的理解能力，如果精通Ruby那么就再好不过了。

基本上**我不打算**在这里浪费时间把这些情况列出来讨论，只是想把坑分享出来，提醒你不要跳。

如果不是100%确定真的想用这个主题，就不要浪费时间去调试和修改gem环境了，不值得。

> 我的经验是：安装越麻烦的，模版本身其实反而更丑更差劲👎。



## 涉及Node.js技术的模版安装方法
Github社区里的Jekyll模版流行使用nodejs的npm的gulp来编译scss这些东西。
所以如果你没注意到主题的说明文档里提到的`gulp`, `npm`之类，就会发现用`jekyll serve`无法进行网站生成。

这种情况下，只需要：安装`Node.js` -> 使用`npm` -> 安装`gulp` -> 命令行使用`gulp`编译网站中的css文件。不过大多数情况下你的机器已经自带了nodejs和npm（Windows除外），所以：
```sh
$ cd <主题的目录>

# 安装此项目的依赖环境
$ npm install

# 编译此项目中的相关文件
$ gulp run
```

小1分钟后，就会看到gulp开启了一个端口，并自动打开了你的chrome浏览器，打开了这个项目的网页（你会看到无法显示出正常效果，因为这里gulp这是用来编译css的，它运行不了jekyll项目）。
然后ctrl+c退出，再打开jekyll命令编译网站就行了-_-!

> 吐槽一下：请回想，为了安装个jekyll和主题，此时你已经经历了一个真的不算短的学习历程了：
GitHub Pages -> Jekyll框架 -> `.yml`文件语法和配置 -> Liquid动态语言 -> Ruby -> gem -> bundle -> HTML+CSS+JS -> nodejs -> npm -> gulp……
这其中哪一步都值得说上一段时间。
然后回想起当初，其实你只是想在GIthub Pages里建个静态网页而已。



## 常见问题

## 运行Jekyll serve 总报错： ERROR `/sw.js' not found
![image](https://user-images.githubusercontent.com/14041622/42981085-0674e738-8c0d-11e8-9050-721e4c592571.png)

[根据这个Stackoverflow的回答](https://stackoverflow.com/questions/51201045/jekyll-serve-error-sw-js-not-found)：
`sw.js`是Service worker的意思，是自动生成的。
基本上不会造成什么影响，但是主要出现这个错误，jekyll就没法同步更新。

根据我的实际体验，这不是主题的问题，而是jekyll的问题：对每个主题都报有这个错误。


# Jekyll制作模版 (Liquid语法)

> 学习制作模版，其实主要是学习Jekyll语法。
而学习Jekyll语法，其实就是学习`Liquid`语法。

参考：[Liquid官方文档。](https://shopify.github.io/liquid/)

就像PHP、ASP、Python等一切网络动态语言一样，`Liquid`也相当于一种独立的动态语言，没什么大差别，基本功能都有。
说白了就是动态生成HTML，可以输出变量，操作数组，调用外部数据，设置IF ELSE判断，FOR循环等，这些都能达到。

开始讲语法前，大概说明一下运行流程：



# Sphinx+Github+Readthedocs+Rst快速创建规范文档
> 注意：这个服务的文档不能用Markdown，只能用reStructuredText.

虽然比较像Jekyll，是快速建站类服务，但是是完全不同的逻辑和构建思维。
这个方式是快速建立一本书、一份完整文档、一个规范攻略的方式，与github和Readthedocs结合非常棒。

大概运行逻辑是：
- 本地运行Sphinx生成项目文件夹和基本构成文件
- 上传到Github专门的repo仓库
- 在这个repo中的settting设置添加与Readthedocs关联的服务
- 到Readthedocs添加这个repo的地址，并开启关联
- Readthedocs定期（大概每分钟）扫描repo并在远程执行生成命令，更新文档

## 安装配置

Sphinx是基于Python构建的，所以一般在各个平台直接用pip安装最方便：
```sh
# 建议在虚拟环境里安装
$ pip install sphinx --user

# 创建项目文件夹
$ mkdir test
$ cd test

# 生成项目结构
$ python -m sphinx-quickstart
```

在执行`sphinx-quickstart`后，会进入十几二十个问题选择环节，可以一直按回车选择默认选项，但是前几项一定要认真自己选择，要不然很麻烦：
```sh
$ python -m sphinx.quickstart

Welcome to the Sphinx 1.7.6 quickstart utility.

Please enter values for the following settings (just press Enter to
accept a default value, if one is given in brackets).

Selected root path: .

You have two options for placing the build directory for Sphinx output.
Either, you use a directory "_build" within the root path, or you separate
"source" and "build" directories within the root path.
> Separate source and build directories (y/n) [n]: y

Inside the root directory, two more directories will be created; "_templates"
for custom HTML templates and "_static" for custom stylesheets and other static
files. You can enter another prefix (such as ".") to replace the underscore.
> Name prefix for templates and static dir [_]: .

The project name will occur in several places in the built documentation.
> Project name: testtest
> Author name(s): Solomon
> Project release []: 0.01

If the documents are to be written in a language other than English,
you can select a language here by its language code. Sphinx will then
translate text that it generates into that language.

For a list of supported codes, see
http://sphinx-doc.org/config.html#confval-language.
> Project language [en]: en

The file name suffix for source files. Commonly, this is either ".txt"
or ".rst".  Only files with this suffix are considered documents.
> Source file suffix [.rst]: .rst

One document is special in that it is considered the top node of the
"contents tree", that is, it is the root of the hierarchical structure
of the documents. Normally, this is "index", but if your "index"
document is a custom template, you can also set this to another filename.
> Name of your master document (without suffix) [index]: index

Sphinx can also add configuration for epub output:
> Do you want to use the epub builder (y/n) [n]: n
Indicate which of the following Sphinx extensions should be enabled:
> autodoc: automatically insert docstrings from modules (y/n) [n]: n
> doctest: automatically test code snippets in doctest blocks (y/n) [n]:
> intersphinx: link between Sphinx documentation of different projects (y/n) [n]:
> todo: write "todo" entries that can be shown or hidden on build (y/n) [n]:
> coverage: checks for documentation coverage (y/n) [n]:
> imgmath: include math, rendered as PNG or SVG images (y/n) [n]:
> mathjax: include math, rendered in the browser by MathJax (y/n) [n]:
> ifconfig: conditional inclusion of content based on config values (y/n) [n]:
> viewcode: include links to the source code of documented Python objects (y/n) [n]:
> githubpages: create .nojekyll file to publish the document on GitHub pages (y/n) [n]:

A Makefile and a Windows command file can be generated for you so that you
only have to run e.g. `make html' instead of invoking sphinx-build
directly.
> Create Makefile? (y/n) [y]:
> Create Windows command file? (y/n) [y]:
```



# Jekyll 制作模版

## 常用变量及属性

[参考：Jekyll 语法简单笔记](http://github.tiankonguse.com/blog/2014/11/10/jekyll-study.html)

### site对象
site对象是全站都能调用的变量，全部都在`_config.yml`文件中定义。
常用变量如下：
- `site.pages`: 所有`_
- `site.posts`: 所有文章
- `site.categories`: 所有的 categories
- `site.tags`: 所有的 tags
- `site.related_posts`: 从`LSI Keywords`提取出来最相关最新的10篇文章
- `site.collections`: 所有集合（与posts逻辑很大不同，一般用来放members等特殊数据）
- `site.documents`: 所有 collections 里面的文档
- `site.data`: `_data` 目录下的数据
- `site.[abc]`: 自定义的变量（手动在`_config.yml`中指定）

### page对象
- `page.content`: 页面的内容
- `page.title`: 标题 （手动在Front Matters中指定）
- `page.excerpt`: 摘要
- `page.url`: 链接
- `page.date`: 时间
- `page.id`: 唯一标示
- `page.categories`: 分类（手动在Front Matters中指定）
- `page.tags`: 标签（手动在Front Matters中指定）
- `page.path`: 源代码位置
- `page.next`: 下一篇文章
- `page.previous`: 上一篇文章

### categories对象
从`site.categories`列表中循环得到的是一个一个的`category`，其中包括这些属性：
- `cat[0]`: 返回`cat`的名称
- `cat[0].size`: 返回这个分类里的文章数量
- `cat[1]`: 返回一个`post_list`列表，包含这个category里所有的post对象。
- `cat[1].size`: 返回这个`post_list`列表中的对象数量。


### tag对象
从`site.tags`列表中循环得到的是一个一个的`tag`，其中包括这些属性：
- `tag[0]`: 返回`tag`的名称
- `tag[0].size`: 返回这个tags里的文章数量
- `tag[1]`: 返回一个`post_list`列表，包含这个tags里所有的post对象。
- `tag[1].size`: 返回这个`post_list`列表中的对象数量。


### paginator对象
- `paginator.per_page`: 每一页的数量
- `paginator.posts`: 这一页的数量
- `paginator.total_posts`: 所有文章的数量
- `paginator.total_pages`: 总的页数
- `paginator.page`: 当前页数
- `paginator.previous_page`: 上一页的页数
- `paginator.previous_page_path`: 上一页的路径
- `paginator.next_page`: 下一页的页数
- `paginator.next_page_path`: 下一页的路径


## 列表读取（各种归档页面用）
### 循环读取Posts
读取全站所有的posts：
```php
{% for post in site.posts %}
    <h2> {{ post.title }} </h2>
    <h2> {{ post.url }} </h2>
    <h2> {{ post.category }} </h2> 
    <h2> {{ post.excerpt }} </h2>  ◀︎ 文章摘要，自动生成的
{% endfor %}
```

只读取`_posts/`文件夹中某个category中的posts，
例如`_posts/tech`文件夹中放的是一些category为`tech`的文章，那么读取方式是：
```php
{% for post in site.categories.tech %}
    <h2> {{ post.title }} </h2>
{% endfor %}
```
注意，在`_posts`中nested文件夹里的文章，也必须在Front matter中指定分类，要不然读不出来。

### 循环读取categories

读取全站所有的分类：
```php
{% for cat in site.categories %}
    <h2> {{ cat[0] }} </h2>
{% endfor %}
```

读取所有分类下的所有文章：
```php
{% for cat in site.categories %}
    {% for post in cat[1] %}
        <h2> {{ post.title }} </h2>
    {% endfor %}
{% endfor %}
```

读取某个分类下所有的文章：
```php
{% for post in site.categories.blog %}
    <h2> {{ post.title }} </h2>
{% endfor %}
```

### 循环读取tags
读取全站所有的tags：
```php
{% for tag in site.tags %}
    <h1> {{ tag[0] }} </h1>
{% endfor %}
```

读取所有tags下的所有文章：
```php
{% for tag in site.tags %}
    {% for post in cat[1] %}
        <h2> {{ post.title }} </h2>
    {% endfor %}
{% endfor %}
```

读取某个tag下所有的文章：
```php
{% for post in site.tags.math %}
    <h2> {{ post.title }} </h2>
{% endfor %}
```

### 读取某category下所有文章并按tag分组读取
```php
{% for post in site.categories.Tech %}   ◀︎ 先读取某分类下所有的文章
     {% assign tags = tags |concat: post.tags |uniq %}   ◀︎ 把每篇文章的tags存到列表里，并删除重复项
{% endfor %}

{% for tag in tags %}
    <h2> {{ tag }} </h2>   ◀︎ 循环输出这个category中的所有tags
    {% for post in site.categories.calculus %}
        {% if post.tags contains tag %}      ◀︎ 循环判断如果文章属于此tag则显示出来
            <h4> {{ post.title }} </h4>
        {% endif %}
    {% endfor %}
{% endfor %}
```


## Post读取
需要在MD文档里指定`layout`才能调用。比如文档里指定了`layout: post`，那么系统就找到`_layouts/post.html`这个文件；如果文档指定了`layout: blog`，那么系统就会找到`_layout/blog.html`这个文件。
在layout里面读取post数据很简单，不需要for循环，不需要if判断，直接用`post`这个对象就行。因为系统已经把文章的数据传过来了。

假如我们在`_posts/xx.md`文章的头信息中，定义了这些数据：
```yml
---
layout: post
title: I'm a post
category: 'blog'
tags:
    - jekyll
    - wordpress
    - blog
---
```

以下就是这个`post.html`文件读取post数据的方式：
```php
<h2> {{ post.title }} </h2>
<h2> {{ post.category }} </h2>

<h2> {{ post.content }} </h2>

{% for tag in post.tags %}
    <h2> {{ tag }} </h2>
{% endfor %}
```


## group_by 分组和where_exp条件筛选
官方的`group_by`做到了复杂查询的功能，比如查找某个category下的全部文章并按tag分组显示。
相对自己写`for/if`实现来说，虽然官方提供了这个功能，但是你仔细阅读文档就会发现，这个group_by必须配合单独的**静态的**额外的文档才能实现。
也就是说，你必须手动写个`mygroup.doc`文件，一个一个指定每篇文章的分组、分类、顺序等。
那实在太麻烦了。