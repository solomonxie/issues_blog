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