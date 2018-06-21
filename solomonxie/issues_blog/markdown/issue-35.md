# Network Engineering 网络工程师
> 日常的网络问题层出不穷，实在太多有点记忆不够用，在这里开一篇再好不过，随时查阅。
另外，基础的网络学习也一起放在这吧


## 很多github.io个人网站打不开
排除过超多原因（VPN, hosts,ISP,DNS)后，发现只针对github.io的话，最主要的是github.io全线强制性改成了必须用https访问。所以很多repo中显示的github.io的链接前没有加`https://`就会造成打不开链接。


## 访问谷歌被屏蔽 （未解决）
> 访问谷歌时被谷歌强制验证，通过验证后才能访问谷歌。这种一般是走代理访问时才会发现。

![image](https://user-images.githubusercontent.com/14041622/35427767-57c4db66-02a6-11e8-8263-9e7fa7522bae.png)



## ssh的`known_hosts`
位置在`~/.ssh/known_hosts`


# HTTP协议 学习
主要看阮一峰入门：
http://www.ruanyifeng.com/blog/2012/05/internet_protocol_suite_part_i.html

http://www.ruanyifeng.com/blog/2012/06/internet_protocol_suite_part_ii.html

http://www.ruanyifeng.com/blog/2016/08/http.html

互联网协议，实际上不管是7层还是5层，
说白了就是一个洋葱，一层一层被剥开。
不管二进制码怎么样，直接用json直白一点：
```javascript
{ //实体层
    “Head”: "头",
    “Data: { //链接层
        “Head”: “头”,
	    “Data: { //网络层
	        "Head": "头",
	        "Data": { // 传输层
	        	"Head": "头", 
	        	"Data": { //应用层
	        		"Head": "头",
	        		"Data": ""
	        	}
	        }
	    }
    }
}

```


## Chrome无法访问某特定网页 但是Safari和其它浏览器能正常访问
> 实际上这个“疑难杂症”系列的开启，就是源于今天近一个小时解决Chrome无法访问Github.io的问题。
由于现在在国内，所以装了各种Shadowsocks和Chrome切换代理插件，甚至还修改了本地的Hosts文件。所以一旦遇到无法访问网页，真是要伸手到很多地方去开启、关闭、各种调试。不过最终终于在chrome的插件管理里面找到了问题。
### 尝试方法
**由于之前安装了`AdBlock`插件，删除它**
实际上我装了以后一直没有使用这个插件，因为会被很多网站检测到并提示这个做法不道德。所以我就长期将这个插件放在不启动模式。但是没想到即便不启动，它仍然有屏蔽一些网站的功能。导致我无法访问github.io的各种个人主页。

### 解决方案后记
删除adblock插件后没多久就又无法访问了，所以再想别的问题。不断尝试后发现，只要把所有的url地址都强制改为`https://`安全链接，就能访问。


# 用Postman对手机抓包
一般人会抓头，Postman明明是API调试工具，和抓包有什么关系。其实这也就是官方对一个小tip，本身存在是为了监控本机某端口数据包的。但其实，如果指定某一个监视端口，然后让同局域网的手机通过这台电脑的这个端口联网而已。这样的话Postman就间接监控到了手机数据包。
操作没有任何难度，主要就是大家对手机将电脑视为代理连接比较陌生罢了。注意：不是让电脑开启热点充当wifi，而是手机本身已经连了wifi时设置代理为电脑而已。
具体操作在[Postman官网博客中](http://blog.getpostman.com/2016/06/26/using-postman-proxy-to-capture-and-inspect-api-calls-from-ios-or-android-devices/)


# 命令行方式的网络测速 Speed Test
一般最靠谱的网速测速是`Ookla Speedtest`这个网站，不管在国内还是国外。
![snip20180209_69](https://user-images.githubusercontent.com/14041622/36028145-dc3de332-0dd8-11e8-9e7e-8f861ace79b9.png)

不过其实它还有命令行的访问方式，这种方式最适合树莓派或者远端服务器这样的看不到显示器的网速测试。
直接在命令行里一句话（是一个词就够）就能返回一系列的测试结果。
官方Github网站在这里：[https://github.com/sivel/speedtest-cli](https://github.com/sivel/speedtest-cli)
安装方式是：只要在自己或者服务器的命令行里输入`sudo pip install speedtest-cli`即可，下载好后，直接在命令行里输入`sppedtest-cli`，回车，就会出现测试过程和结果。
![snip20180209_67](https://user-images.githubusercontent.com/14041622/36028031-832951fa-0dd8-11e8-9f15-5902bc6baab4.png)



# 让curl通过shadowsocks连接
shadowsocks是Socks5的连接方式。本地打开shadowsocks的客户端后，找到它在本机使用的端口。比如1080。然后输入如下命令就可以查看到效果：
```
curl --socks5-hostname localhost:1080 http://httpbin.org/ip
```
其中 http://httpbin.org/ip 是一个可以返回访问者ip地址的网站。
如果你的命令行返回的是你的服务器ip，那么就成功。
实践成功。


# 查看网络端口的流量
> 尝试过太多了，总结：都没太大用处，顶多也就看看当前系统某网卡的进出流量。最后还是系统默认的`iftop`最靠谱。

一键安装所有常用的网络监视软件：
```shell
# Ubuntu
sudo apt-get install -y iftop dstat nload iptraf ifstat nethogs bmon slurm vnstat bwm-ng cbm speedometer 

#Mac 
brew install iftop dstat nload iftraf ifstat nethogs bmon slurm vnstat bwm-ng cbm speedometer 
```

###  `iftop` 统计所有端口流量 （没法统计某个端口）
一般是默认安装的，
需要sudo权限：`sudo iftop`。
[参考文章](https://my.oschina.net/lionel45/blog/261234)
![image](https://user-images.githubusercontent.com/14041622/36644777-3495a9ac-1a9a-11e8-90a3-617c295fb973.png)


### `iptraf`
能够看到每个网卡的当前流量，如600 kbits/sec
注意，一开始的显示颜色会很难看，需要艰难地在菜单里选择color，然后重启程序，才能正常显示。
![image](https://user-images.githubusercontent.com/14041622/36349500-5d6ed95c-14c3-11e8-958a-b7d9d2bd2851.png)

### `bmom`
动态柱状图显示进、出的流量和秒速。页面比较友好，信息简单。
![image](https://user-images.githubusercontent.com/14041622/36644611-ad365e68-1a97-11e8-9197-ad01433c1d8a.png)

### `vnstat`
画面简单，但不是动态的。只是总结日平均、月平均等。
![image](https://user-images.githubusercontent.com/14041622/36644690-1a011014-1a99-11e8-8427-f21f7a690ab6.png)

### `bwm-ng`
功能超少超简单，只显示进出流量。
![image](https://user-images.githubusercontent.com/14041622/36644702-458c73f4-1a99-11e8-8470-93ad1c965f77.png)

### `cbm`
只显示进出流量。
![image](https://user-images.githubusercontent.com/14041622/36644715-67f06586-1a99-11e8-9fee-22038e5a5640.png)

### `speed-meter`
需要输入`speedometer -r eth0 -t eth0 `执行。
只显示简单信息。但是带颜色和每个峰值的标注的界面好看。
![image](https://user-images.githubusercontent.com/14041622/36644729-aafca56a-1a99-11e8-9a8b-7ebe1d82dbfc.png)

### `slurm`
命令是`slurm -s -i eth0 `。信息很少：
![image](https://user-images.githubusercontent.com/14041622/36644676-e086bd0c-1a98-11e8-921a-3325660a0299.png)

### `ntop`
安装还需要用户名密码，这对于服务器来说太不友善了。装完了后，还打不开。。。

### `dstat`
可读性不强，也没什么好玩的显示出来。
![image](https://user-images.githubusercontent.com/14041622/36349470-b9267224-14c2-11e8-9c28-f08823913467.png)


### `nload`
画面简单，沾满全屏，只告诉你当前incoming和outgoing的流量速度。
![image](https://user-images.githubusercontent.com/14041622/36349472-cf429f92-14c2-11e8-955a-e0b42df65251.png)

### `ifstat`
极其简单只显示两个数值：进和出的秒速。
![image](https://user-images.githubusercontent.com/14041622/36349510-95a4c5ca-14c3-11e8-9b99-f4d1d24b863e.png)

### `nethogs`
需要sudo才有权限运行。
按用户显示每个用户所用的流量，基本上没什么用，数值也少。
![image](https://user-images.githubusercontent.com/14041622/36349525-f70673cc-14c3-11e8-886f-73a740be9401.png)





# Shadowsocks命令行中的本地客户端配置
> 有时候想让树莓派访问一些屏蔽的网址，所以只能用命令行的客户端。

[参考文章](http://www.jeyzhang.com/how-to-install-and-setup-shadowsocks-client-in-different-os.html)

简单说就是：
```shell
sudo apt-get install m2crypto
sudo pip install shadowsocks

#启动Shadowsocks
sslocal -s 服务器域名或IP -p 服务器端口号 -k “密码” -l 1080 -t 600 -m rc4-md5 
```

当然，启动方式还有从配置文件的方法。
首先在某处创建配置文件，比如`~/.shadowsocks-client.json`，内容如下：
```javascript
{
    "server":"服务器IP地址",
    "server_port": 服务器端口,
    "password":"服务器密码",
    "local_port": 1080,
    "timeout": 600,
    "method":"aes-256-cfb"
}
```
然后用这个命令启动：`sslocal -c ~/.shadowsocks-client.json`

## 启动之后
启动之后，就不要关闭命令，只能打开另一个命令行窗口操作。
现在命令行直接访问网络其实没什么变化，因为目前开启的socks5协议端口，也就是说刚刚设置的本地1080端口是socks5协议的，必须在curl里指定socks5协议，再去访问网络：
```shell
curl --socks5-hostname 127.0.0.1:1080 httpbin.org/ip
```
不过功能强大能访问socks5协议端口的，估计也就curl了。如果使用别的命令如wget之类的，就只能访问http和https协议端口。
这样的话我们就必须`把socks5端口转换为http端口`。

## Shadowsocks转换HTTP代理
因为考虑到很多程序都是用http端口为代理出去的，所以我们要把socks5端口映射为某个http端口。
这里就需要用到另一个软件：`polipo`。
[参考文章。](http://baoye.me/2016/10/17/%E5%9F%BA%E4%BA%8E%E6%A0%91%E8%8E%93%E6%B4%BE%E4%BD%BF%E7%94%A8Shadowsocks%E7%BF%BB%E5%A2%99/)

1. 输入命令安装Polipo:
`sudo apt-get install polipo`

2. 修改配置文件:
`sudo vim /etc/polipo/config`

3. 把文件内容全部替换如下：
```shell
# This file only needs to list configuration variables that deviate
# from the default values.  See /usr/share/doc/polipo/examples/config.sample
# and "polipo -v" for variables you can tweak and further information.
logSyslog = false
logFile = /var/log/polipo/polipo.log
socksParentProxy = "127.0.0.1:1080"
socksProxyType = socks5
chunkHighMark = 50331648
objectHighMark = 16384
serverMaxSlots = 64
serverSlots = 16
serverSlots1 = 32
proxyAddress = "0.0.0.0"
proxyPort = 1087
```
注意：上面这个`proxyPort = 1087`是要映射出来的http端口，自己随便设置。但是要记住它。

4. 设置`http_proxy`环境变量
`sudo vim /etc/profile`
写入
`export http_proxy="127.0.0.1:1087/"`

5. 重启Polipo: `sudo /etc/init.d/polipo restart`
6. 检查效果： `curl -x 127.0.0.1:1087 httpbin.org/ip`
完成！

## 在Mac中命令行走代理
由于Mac中使用的GUI客户端，所以很多东西都配置好了，在命令行中访问就方便很多。

[参考文章。](https://github.com/mrdulin/blog/issues/18)
如果是配置的Shadowsocks，那么在GUI启动了shadowsocks的情况下，需要找到正确的本地映射端口。在GUI的设置页面里面可以找到HTTP的映射端口：
![image](https://user-images.githubusercontent.com/14041622/36645118-1e4b0052-1a9f-11e8-84ab-74483827d65f.png)
那么，比如使用curl时，就应当用http如此访问：
`curl -x http://127.0.0.1:1087 httpbin.org/ip`
其它软件也同理，选择http方式的该地址和该端口，就能正确连接了！


# SMTP协议
SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议。

## 邮件协议的理解

首先要理解邮件传输的流程。一直以来都有个**大误会**：以为是别人从他的电脑直接给我的电脑上发邮件。其实真的不是。真实流程和上网浏览网页是一模一样的。来重现一下打开网页的技术流程：

你向网站发出一个request请求，网站答应后发个你一个response网页HTML，然后你就可以看到网页了。

邮件也是一样的。
比如你要给Jason发邮件，他的邮箱是Gmail的。那你就向Gmail发送一个request请求，包括了收件人是谁、内容是什么。然后Gmail就在那里等，等Jason去Gmail查邮件的时候，就告诉他谁给他发了什么邮件。

`Push Mail`真的只是错觉。真的不是别人推送到你手机上或电脑上，只是它们在背后默默地每几秒钟就发送个request到服务器，去申请回应。就像浏览网页一样。

理解了这点，协议就基本上明了了。然后编程发邮件就变得简单起来。
