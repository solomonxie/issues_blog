# Raspberry Pi 疑难杂症
## 记录学习树莓派过程中遇到的各种问题及解决方案


# 利用`frp`实现树莓派的公网映射（让外网访问本地局域网里的树莓派）
> 一直就想试试把本地电脑公开到公网实现自己做服务器的感觉，有了树莓派后更有这种想法。于是就动手试试。

听说目前两种方法比较流行：`ngrok`和`frp`。但是`ngrok`是收费的且复杂，`frp`则完全开源免费且简单易用，所以这里来尝试下。

大概思路就是：自己先有一台公网的服务器（我是在AWS或DigitalOcean租的），然后让本地的树莓派与公网服务器通过`frp`程序达成一种映射连接，这样别人访问公网服务器ip的某个端口时，就会自动转向来访问本地的树莓派了。

做法是：分别在服务器和本地树莓派上下载frp程序，当然要根据两者自己的系统平台下载不同版本。然后在服务器运行`frps`，即frp-server，在本地运行`frpc`，即frp-client。并且在配置文件里约定好，服务器的哪个端口映射到本地的哪个端口。双方都运行后，就可以正常通过外网访问了。

### 难度
这个服务的环境、启动、安装等简单到让人发指，唯一的难度就在于服务器上和本地上两个`.ini`配置文件。
配置文件搞明白了，就什么都明白了。有一点不明白，就全不明白。。。

[参考文章。](https://mritd.me/2017/01/21/use-frp-for-internal-network-wear/)
[官方下载地址](https://github.com/fatedier/frp/releases)。其中，服务器如果是Ubuntu或Debian系的，就选择`linux_amd64.tar.gz`和`linux_386.tar.gz`结尾的，一个是64位一个是32位。本地树莓派如果是树莓派系统，则选择`linux_arm.tar.gz`结尾的。

## 第一：服务器上安装`frp`
1. 随便找个目录，下载frp：`wget https://github.com/fatedier/frp/releases/download/v0.16.0/frp_0.16.0_linux_amd64.tar.gz`
2. 解压：`tar -xzvf frp_0.16.0_linux_amd64.tar.gz`
3. 进入目录：`cd frp_0.16.0_linux_amd64`
4. 修改服务器端配置文件：`vim frps.ini`，将内容全部替换为如下：
```ini
# frps.ini
[common]
# frp 监听地址
bind_addr = 0.0.0.0
bind_port = 7000

# frp 控制面板
dashboard_port = 7500
dashboard_user = admin
dashboard_pwd = admin

# 默认日志输出位置(这里输出到标准输出)
log_file = /dev/stdout
log_level = info

# 如果需要代理 web(http) 服务，则开启此端口
vhost_http_port = 4080
vhost_https_port = 4443

# 子域名(特权模式需下将 *.domain.com 解析到公网服务器)
subdomain_host = 13.250.230.123
```
保存退出后，就可以在当前目录通过`sudo ./frps -c frps.ini`启动服务器端的这项服务了。
测试：
随便找个浏览器，输入服务器的IP和刚刚设置的后台管理端口号，就可以访问了。比如我的服务器IP是13.250.64.172，那么就输入：`http://13.250.64.172:7500`
然后就可以看到如下:
![image](https://user-images.githubusercontent.com/14041622/36657511-e18570da-1b07-11e8-94a1-bb5c2dbdbc28.png)
然后按照刚才设置的账号密码：admin, admin就能登录到，显示如下图：
![image](https://user-images.githubusercontent.com/14041622/36669981-b0a9c8b0-1b31-11e8-9ea0-57465abab510.png)


## 第二：本地树莓派装`frp`
本地配置要比服务器配置难很多，经常出问题。尤其是我的机器只要一设置ssh，就会出错。
基本配置如下：
```ini
# frpc.ini
[common]
# 服务端地址及端口
server_addr = 13.250.230.123
server_port = 7000

[web01]
type = http
local_ip = 127.0.0.1
local_port = 8000
subdomain = pi
```

保存退出后，在frp的文件夹执行：`sudo ./frp -c frpc.ini`，就能启动了。
但是，很有可能的是，这里会出一些状况不能正确运行。这就要考验自己的研究能力了。
以下是列出一些常见问题：

## frp报错

```

```


# 树莓派修改Wifi和密码
[参考文章。](https://www.cmgine.com/archives/11053.html)
[参考文章2。](http://imchao.wang/2014/01/02/make-you-raspberrypi-auto-connect-to-wifi/)

简单说，只需要改两个文件即可，甚至改一个文件即可。

抛开Linux系统问题，光树莓派的话，只需要打开`/etc/wpa_supplicant/wpa_supplicant.conf`这个文件编辑，里面会有明文显示wifi的登录名和密码，如果想改的话直接在这里改好保存退出就ok了。如下图：

![image](https://user-images.githubusercontent.com/14041622/36774293-65875222-1c98-11e8-8ede-036214065611.png)

图中我配置了两个Wifi的登录信息，这样的话，一个连不上可以自动连第二个。
在文中，很明显就可以找到登录名和密码的位置，增删改都不用多说。如果要增加一个WIFI信息，那就把整个`network={...}`复制出来一个改改就好了。

### 更高级设置
一般Linux系统都不是直接改上面那个文件的，实际上WIFI登录密码是直接写在`/etc/network/interfaces`这个文件里的。
但是树莓派默认不会在这个文件直接写wifi信息，而是让它读取额外的一个文件来找到wifi信息。
`interfaces`这个文件内容非常少非常简单，一看就明了，下图是这个文件的全部内容（忽略掉注释内容）：

![image](https://user-images.githubusercontent.com/14041622/36774493-4187f286-1c99-11e8-93b3-60dd7a9ab250.png)

如图注