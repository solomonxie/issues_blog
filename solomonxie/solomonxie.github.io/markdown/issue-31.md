# AWS为首的云服务器实战钻研
> Amazon Web Services是个真心强大靠谱的真·云服务器。只是玩好了它都可以被人敬仰，可是却真的不很容易配置，服务也太多。所以在这里开一篇，以供随时记录解决方案和发掘过程。
另外，附带性的会有一些DigitalOcean等的其它服务商方案。


# EC2的傻瓜式初始配置方案
> AWS 的服务海洋里面，EC2是最常见最常用的一个。也就是平时我们租用云端服务器最常用的虚拟主机，可以让你把网站代码、数据库等等全都部署在上面，然后用户直接连接这个虚拟主机。相对于其它aws的邮箱、数据库、语音等云服务来说，EC2是一个大杂烩，也是个通用平台，做什么都行，看自己。

1. 登录AWS控制后台，在服务列表中选择EC2 -> 左侧菜单Instances -> Launch Instance
2. 选择合适的映像，推荐社区版的映像：
   社区版有更多Linux发行版，在这里推荐选择ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-20160114.5 ebs hvm
3. 选t2.micro类型的instance，其中会清晰标记这个是免费的
4. 设置详细：全部保持默认就行了
5. 添加存储盘：免费的是20G以内，一般默认的8G足够用
6. Tag可加可不加
7. 安全组：根据需求后期可改，内容较多
8. 综览及确认
9. 选择密钥
   必须要有，创建新的或选择已有的。
   如果这里没创建，则以后ssh登录不了。
10. 用SSH登录
    - 用Linux Shell的SSH命令登录：
      `ssh -i "私有密钥文件路径.pem" 用户名@实例的公网IP`
      其中.pem文件是私有密钥，输入路径即可;
      如果是ubuntu的映像，默认用户名是`ubuntu`，
      如果是AWS定制的映像，默认用户名是`ec2-user`;
    - 用Windows的Putty软件登陆：
      需要先用puttygen.exe把`.pem`私钥文件转换为`.ppk`文件，
      然后在菜单`connection -> SSH -> Auth`中，把文件路径填上，
      然后回到主菜单点击连接即可。


# Shadowsocks在AWS EC2运行时的网关设置 (待验证)
```
Security Groups -> Inbound -> Edit -> Add -> Custom TCP Rule, TCP, 8000 - 9000, 0.0.0.0/0
Security Groups -> Inbound -> Edit -> All traffic, All, All, 0.0.0.0/0
```


# Shadowsocks 服务器安装

1.创建服务器
2.创建时选择SSH Key，上传本地制作的密钥文件，如`~/.ssh/id_rsa.pub`
3.记住本地SSH Key密钥的访问密码，这样每次登录服务器只要输入它就行了。
4.打开终端, 利用SSH连接,如DigitalOcean是`$ ssh root@ip-address`，Lightsails就是`$ ssh ubuntu@ip-address`
```shell
sudo apt-get update
sudo apt-get install python-pip -y
# 如果提示需要升级pip
# pip install --upgrade pip
pip install shadowsocks
sudo vi /etc/shadowsocks.json
{
    "server":"0.0.0.0",
    "server_port": 1111,
    "password":"aaaaaaaa",
    "local_address":"127.0.0.1",
    "method":"aes-256-cfb",
    "local_port":1080,
    "timeout":300,
    "fast_open":false
}
```

sudo ssserver -c /etc/shadowsocks.json -d start

如果遇到 permission denied错误, 试一下改变下面文件权限:
```shell
sudo chmod 777 /var/run/shadowsocks.pid
sudo chmod 777 /var/log/shadowsocks.log
```
如果还是不行，那么试试直接按照ssserver的路径启动：
```
sudo /usr/local/bin/ssserver -c /etc/shadowsocks.json -d start
```
![image](https://user-images.githubusercontent.com/14041622/35665785-835dfcf6-0762-11e8-9d84-d730cec37146.png)



# Shadowsocks 创建好后无法访问
如果开着ss，打不开谷歌，那么最先尝试的是用ssh连接。如果连接成功，那么说明服务器和网络都没问题。剩下只是配置的事了。
1. 检查防火墙配置。亚马逊AWS的防火墙是很严格的，所以多半都会卡在这。
如果是AWS的Lightsails的话，直接在Networking配置里，开启全部端口，如下图：
![image](https://user-images.githubusercontent.com/14041622/35667037-20aa38cc-0767-11e8-814e-504fae373de4.png)
或者谨慎点，在默认配置的基础上，添加自己连接的端口：
![image](https://user-images.githubusercontent.com/14041622/41410425-0b3458d4-700c-11e8-8a1c-5be75194f033.png)
(注意：这里的Custom处是你在设置/etc/shadowsocks.json时候里面的端口)

2. 还不行的话，就在命令行里主动添加防火墙设置：
```shell
# 下载防火墙设置的软件
sudo apt-get install firewalld
# 开启相应的端口
sudo firewall-cmd --zone=public --add-port=你当前服务器的IP地址/tcp --permanent
sudo firewall-cmd --zone=public --add-port=你当前服务器的IP地址/udp --permanent
```
改好后，就可以通过`cat /etc/firewalld/zones/public.xml`这个文件里看到，刚刚的防火墙设置已经生效了。
3. 如果还不行，就试试这招，把ss配置文件的服务器段IP改为`0.0.0.0`（如果已经是这个设置则反之设置成服务器IP地址），然后保存，并重启ssserver，`sudo ssserver -c /etc/shadowsocks.json -d restart`。如下图：
![image](https://user-images.githubusercontent.com/14041622/35667184-a97dc4d4-0767-11e8-9ea7-eff766e65dd8.png)



# Shadowsock多用户配置

```json
{
    "server": "0.0.0.0",
    "port_password": {
        "8381": "foobar1",
        "8382": "foobar2",
        "8383": "foobar3",
        "8384": "foobar4"
    },
    "timeout": 300,
    "method": "aes-256-cfb"
}
```


# AWS Lightsail 无法ping通
ping某一个服务器，是需要服务器防火墙允许ICMP协议的数据包的。经查阅，AWS的所有服务是默认关闭icmp的。
除独立的Lightsail外，其它AWS服务都可以在安全组中设置防火墙开启icmp。
然而Lightsail的防火墙设置页面，并没有icmp选项，官方也没有任何相关解决方案。

    因此目前来说，也就是无法使用ping来测试服务器连接的了。


## 搭建的SS服务开始几天很快然后就经常掉线，速度也变慢
不管是在DigitalOcean还是AWS的Lightsail搭建ss服务，都有这个问题。
都是出现在我将ip绑定到阿里云的域名之后，在想是不是和阿里云的域名有关系。出现掉线的情况后，无论是ip直连还是用域名连，情况都没有改善，所以怀疑是不是只要在阿里云绑定了域名和ip，就会被更严格的监控到使用ss服务，导致经常掉线。


# AWS各国节点测试
根据[CloudPing](http://www.cloudping.info/)的测试，得出如下结果：
![image](https://user-images.githubusercontent.com/14041622/35795505-50bc8f6c-0a94-11e8-89fa-e8f589be259c.png)
除了加拿大没试过外，其它亲测完全属实，新加坡远快于日本和韩国。


# Shadowsocks开机启动
参考了好几篇文章，怎么说的都有，看起来靠谱的不多。最后挑了一个最简单的方法，生效了。[原文在这里](https://www.zybuluo.com/Hederahelix/note/245179)。
编辑`rc.local`开机启动项：
```
sudo vi /etc/rc.local
ssserver -c /etc/shadowsocks.json -d start
```
保存退出，用`sudo reboot`重启，有效。


# 各服务商的各国节点测试（不定期更新）
自从今天发现命令行里可以运行ookla的`speedtest`，就赶快到自己的树莓派、国外租的主机查看连接网速。之前一直用shadowsocks觉得网速慢的时候，总是怀疑有可能节点没选好，一会儿东京，一会儿新加坡，一会儿加拿大，可还是有问题。

## AWS Lightsail 主机 -- Singapore 节点
下载速度近500M/s，上传速度150M/s，这是什么级别？!
![snip20180209_70](https://user-images.githubusercontent.com/14041622/36030420-1d5b99f0-0de2-11e8-9037-0db28113f53d.png)

> 在网上看到过一个帖子说得很对，不管怎么测试，还有什么比Youtube 1080P更有说服力呢？

看到这个，才明白原来服务器本地访问的速度和上传的速度再快，也敌不过传输过程中的丢失。。
另外，我是在本机连接服务器访问youtube的，我本机的测速是15M/s，宽带的带宽是100M。
![image](https://user-images.githubusercontent.com/14041622/36031150-b886ea72-0de4-11e8-8675-781ab022ac76.png)
此时我本机访问bilibili视频的速度比访问youtube快了一倍，如下：
![image](https://user-images.githubusercontent.com/14041622/36031623-4f78fd70-0de6-11e8-8880-1898a79d7d1d.png)






# `iftop`命令统计服务器网络流量运行情况
[参考文章](https://segmentfault.com/a/1190000002797441)
![image](https://user-images.githubusercontent.com/14041622/36032772-0355e7ba-0dea-11e8-8014-b44463277bff.png)




# 服务器安装FTP
> 需要说明下，Linux最常用的ftp服务器端就是`vsftpd`了。
但是，配置起来非常麻烦，网上众说纷纭，怎么写的都有，怎么出错的也都有。
下面我尽量小心的总结一些我使用通过的配置。

主要步骤是：
- 安装：很简单，`sudo apt-get install vsftpd`
- 配置文件：`sudo vim /etc/vsftpd.conf`，然后按照自己的需求配置文件
- 重启ftp服务：`sudo /etc/init.d/vsftpd restart`

以下是我尝试过的几种常用的`/etc/vsftpd.conf`配置方法：

## 最简单配置
> 以下内容为我所知道的最简单配置：不允许匿名登录，使用默认的linux用户和密码登录，完全权限。

```shell
#禁止匿名访问
anonymous_enable=NO
#允许上传
write_enable=YES
```
然后使用FileZilla这样的FTP客户端试着登录一下：输入ip地址，用户名和密码，选择快速登录。
注意，要选择`sftp`而不是`ftp`，否则无法成功登录。

![image](https://user-images.githubusercontent.com/14041622/40574349-c9903348-6102-11e8-958b-56e6c7212818.png)

## 匿名用户配置
> 如果是本地虚拟机或是自己家里的电脑的话，完全匿名就OK了，不需要设置那么麻烦的安全限制。

完整配置如下：
```shell
#
```

## 单独ftp用户配置
> 这种方式的好处在于，可以专门创建一个user用户，限制它能访问的目录和权限。
但是就是这种配置，是最麻烦最容易访问失败的。做好心理准备。

完整配置方案如下：
```shell
# 
```

## `本地FTP客户端命令工具：sftp`
除了FileZilla这种GUI工具外，我们在命令行里也能轻松登录远程的FTP服务器。Mac和一些Linux上都自带`ftp`和`sftp`工具，操作很简单。
比如上述`最简单配置`，我们就可以用`sftp`工具来登录ftp服务器，方便的上传和下载文件。

命令很简单：
- 进入sftp的互动shell： `$ sftp USER@IP`，如：
![image](https://user-images.githubusercontent.com/14041622/40578181-4e68fb38-6142-11e8-9c40-05b85b4fc699.png)
- 上传：`$ put LOCAL-FILE-PATH`
- 下载：`$ get REMOTE-FILE-PATH`

![image](https://user-images.githubusercontent.com/14041622/40578198-9ed8f85c-6142-11e8-8aae-47bd5097b981.png)



# 利用`VNC`连接远程服务器桌面：使用`xfce`桌面
实际上可以在服务器上安装桌面，然后用`VNC`服务从Linux、Mac和Windows等各种地方连接远程桌面。
[参考DigitalOcean的这篇攻略。](https://www.digitalocean.com/community/tutorials/how-to-install-and-configure-vnc-on-ubuntu-16-04)

这里选择的是xfce桌面，非常轻量化，和vnc的配合也很融洽。

1. 第一步：安装 -> 桌面和vnc服务
```shell
sudo apt-get update
sudo apt install xfce4 xfce4-goodies tightvncserver
```

2. 第二步：配置桌面环境

3. 第三步：启动VNC服务
```
$ vncserver
```
第一次启动时，会提示你创建一个登录密码和只供浏览用的登录密码。
![image](https://user-images.githubusercontent.com/14041622/36931821-50c5d788-1ef9-11e8-9725-ff053e93e8fd.png)

4. 第四步：开启服务器端口
服务器端口开放需要在供应商的网页控制面板里调整，各不相同。
因为vnc使用的是从`5900`端口开始，第1个桌面为`5901`，第2个为`5902`以此类推。所以就索性设置为`5900-5999`之间的端口都开放。
下面的是Lightsail的配置：
![image](https://user-images.githubusercontent.com/14041622/36932254-5a9f4160-1f01-11e8-9080-36ae23a1a038.png)



5. 第五步：从本地计算机利用vnc访问
每种平台方式不同。Mac上直接在文件夹菜单里的`Connect to Server`就可以连上，地址格式是：`vnc://USER:IP:5901`

引用DigitalOcean的说明：
> A local computer with a VNC client installed that supports VNC connections over SSH tunnels. If you are using Windows, you could use TightVNC, RealVNC, or UltraVNC. Mac OS X users can use the built-in Screen Sharing program, or can use a cross-platform app like RealVNC. Linux users can choose from many options: vinagre, krdc, RealVNC, TightVNC, and more.

连接成功：
![image](https://user-images.githubusercontent.com/14041622/36932263-77706940-1f01-11e8-9f72-7758731e004f.png)



# 服务器安装`gnome`桌面供vnc远程访问
上面写了xfce桌面，不过样子比较丑，所以想试一试Ubuntu的gnome桌面。
[参考阿里云官方参考文章。](https://help.aliyun.com/knowledge_detail/59330.html)




# 远程服务器一键安装开启Shadowsocks脚本

AWS的Lightsails在创建服务器时允许运行初始脚本，这个非常方便，省的我一个一个去敲代码了。

![image](https://user-images.githubusercontent.com/14041622/41411213-9566f1ea-700e-11e8-8be1-6101491b3966.png)



以下为脚本内容：
```sh
#! /bin/bash
# ---UBUNTU SERVER INITIAL SETUP---
# Notice: 
#    This script should be run by "$ sudo bash xxx.sh"

# Update server & install essentials
sudo apt-get update -y
#sudo apt-get upgrade -y
sudo apt-get install htop

# Install Shadowsocks & create config file
sudo pip install shadowsocks
sudo cat>/etc/shadowsocks.json<<EOF
{
    "server":"0.0.0.0",
    "server_port": 1111,
    "password":"abc123",
    "local_address":"127.0.0.1",
    "method":"aes-256-cfb",
    "local_port":1080,
    "timeout":300,
    "fast_open":false
}
EOF
# Auto start Shadowsocks service when system starts
#sudo echo "ssserver -c /etc/shadowsocks.json -d start" >> /etc/rc.local

# Start Shadowsocks server
sudo ssserver -c /etc/shadowsocks.json -d start
```

不要忘记ssh登录的设置，把本地`~/.ssh/id_rsa.pub`的内容复制到`SSH Keypair`里面，这样之后就不需要登录密码了。

注意，生成好服务器后，一定要去开启端口才能生效。
方法是：
点击这个服务器页面 -> Networking -> Firewall，
然后添加一个Custom端口，号码为刚刚脚本中设定的端口号码。


另外，如果不是使用Launch Script初始脚本，也可以直接自己用ssh把脚本上传到服务器，再执行。
方法如下：
```sh
# 上传shell脚本到服务器用户目录
$ scp ./server-init.sh user@ip-address:~

# ssh进入服务器终端
$ ssh user@ip-address

# 运行脚本
# sudo bash ~/server-init.sh
```


# Linux安装Shadowsocks客户端

有时候想让树莓派等Linux机也用shadowsocks，这时就没有GUI客户端用了。
所以我们直接使用Shadowsocks官方命令行客户端：`sslocal`。

安装：
```sh
# 服务端和客户端都包括了
$ sudo pip install shadowsocks
```

启动客户端：
```sh
# 连接IP为54.254.184.22 端口为2222的服务器，映射到本地1080端口
# 格式为：sslocal -s 服务端IP  -p 服务端端口 -l 1080 -k "密码" 回车
$ sslocal -s 54.254.184.22 -p 2222  -l 1080 -k "PASSWORD" -t 600 -m aes-256-cfb
```

这样启动其实听不方便的，而且还占用命令行，不能断开。
所以我们用配置文件+start命令的方式启动客户端：
```sh
# 创建一个配置文件
$ touch ~/ss-local.json

# 存入以下内容：
{
  "server":"服务端IP地址",
  "local_address": "127.0.0.1",
  "local_port":1080,
  "server_port": 2222,
  "password":"服务端密码",
  "timeout":300,
  "method":"aes-256-cfb"
}

# 启动客户端
$ sudo sslocal -c ~/ss-local.json -d start
```

重启或关闭客户端：
```sh
# 重启客户端
$ sudo sslocal -c ~/ss-local.json -d restart

# 关闭客户端
$ sudo sslocal -c ~/ss-local.json -d stop
```