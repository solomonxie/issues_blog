# RPi & Hardware Engineering 树莓派及硬件工程师
这里将记录以下话题：
- 树莓派
- 科技设备使用技巧
- 硬件相关工程


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


# 通过VNC远程连接树莓派桌面

在已经成功用ssh连接到树莓派到话，如果连接树莓派桌面，需要在树莓派中安装一个叫`tightvncserver`vnc服务。

操作如下：

终端中输入`sudo apt-get install tightvncserver`

安装好后，输入`tightvncserver`回车，启动vnc服务。

然后就可以连接了。

Mac中，在文件夹Finder的菜单中，打开Go下的连接服务器，然后输入`vnc://树莓派IP地址:5901`。其中5901是默认的端口。
Windows上可能需要安装个软件来连接，可以自己查一查。


![image](https://user-images.githubusercontent.com/14041622/36931496-b85af8fe-1ef1-11e8-95a0-b997c0f9220a.png)

![image](https://user-images.githubusercontent.com/14041622/36931498-c0a2cb18-1ef1-11e8-9081-83699f96ce45.png)


## VNC中无法连接互联网
通过vnc连接到了树莓派桌面后，无论是浏览器还是桌面中打开的终端，皆无法连接到互联网。
但是SSH连接树莓派时，在命令行里均可以正常连接网络。
那么问题在于vnc了。目前暂没有找到解决方案。


# 树莓派命令行找不到`ifconfig`命令
> command not found: ifconfig

[参考回答。](https://www.raspberrypi.org/forums/viewtopic.php?f=28&t=23405)

可以用`sudo ifconfig`,或直接指定位置`/sbin/ifconfig`，或者先设置别名`alias ifconfig="/sbin/ifconfg`，然后再正常使用。


# 树莓派用HDMI连接电视显示"无信号"问题

试了很多次，用HDMI线把树莓派连接电视机，但每次都显示“无信号”。所以搜索了一圈，下面是解决方案。

[参考树莓派官网论坛：HDMI monitors says NO SIGNAL (solved)](https://www.raspberrypi.org/forums/viewtopic.php?t=34061)

> The Pi outputs a relatively weak HDMI signal. Some devices may not immediately notice the Pi's HDMI or may not do the negotiation.
Setting the hdmi_force_hotplug=1 makes sure the Pi believes the monitor/TV is really there.
You might also need to set config_hdmi_boost=4 or even higher (up to 9) if your display needs a stronger signal.
If the display is a computer monitor, use hdmi_group=1 and if it is an older TV, try hdmi_group=2.
Do not set hdmi_safe=1 as that overrides many of the previous options.
Using a shorter or better quality HDMI cable might help.
Make sure your Pi's power supply delivers 1A and not 500mA.
If you see a problem with the red colour - either absent, or interference - then try a boost. However it might simply be that the display requires a stronger signal than the Pi can give.


主要方法是：
- 拔出树莓派的SD卡，然后插到电脑上
- 找到SD卡根目录的`config.txt`文件，打开编辑。
- 找到`#hdmi_force_hotplug=1`这句话，把前面的`#`注释符号去掉，启用HDMI热插拔功能。
- 找到`#config_hdmi_boost=4`这句话，把前面的`#`注释符号去掉，启用加强HDMI信号。

![image](https://user-images.githubusercontent.com/14041622/41811132-4a3c88d0-773c-11e8-8deb-b632965a8fff.png)


如果还是有问题，那么可以试着这么操作（不推荐）：
- 找到`#hdmi_group=1`这句话，把前面的`#`注释符号去掉，把数字改成`2`，强行指定显示器类型：`1`是连接老式电视，`2`代表连接新电视。

> 用HDMI插上电视后，就连声音都有啦！（不用插音频线，HDMI自带音频传输）


# 树莓派控制风扇自动开启关闭

树莓派风扇一直开着确实很吵，所以即使会对cpu造成负担，我也不愿意插上风扇。
偶然看到了这篇文章，解决了这个大问题：
[《让树莓派根据温度自动控制散热风扇的启停》WuSiYu Blog](https://wusiyu.me/%E8%AE%A9%E6%A0%91%E8%8E%93%E6%B4%BE%E6%A0%B9%E6%8D%AE%E6%B8%A9%E5%BA%A6%E8%87%AA%E5%8A%A8%E6%8E%A7%E5%88%B6%E6%95%A3%E7%83%AD%E9%A3%8E%E6%89%87%E7%9A%84%E5%90%AF%E5%81%9C/)




# 树莓派连接USB摄像头

手头有一个闲置的USB摄像头，插在自己的笔记本上，能够正常使用，且不用装驱动。
然后想把它插在树莓派上试试。

[参考：树莓派基于motion的usb摄像头监控](https://blog.csdn.net/coolwriter/article/details/75568250)

方法如下：
- 进入树莓派`/dev/`目录，查看有没有`video0`这个文件。
![image](https://user-images.githubusercontent.com/14041622/41845587-93a174fc-78a6-11e8-9c14-bed63a77173b.png)
- 安装`motion`程序：
```sh
$ sudo apt-get install motion
```
- 修改`motion`程序的daemon:
```sh
sudo vim /etc/default/motion
```
- 把`no`改成`yes`，开启motion的daemon一直检测设备：
![image](https://user-images.githubusercontent.com/14041622/41845696-e9a7833c-78a6-11e8-920f-3eb9b13155bf.png)
- 打开`motion`程序的配置文件：
```sh
$ sudo vim /etc/motion/motion.conf
```
- 把`daemon off`改成`daemon on`:
![image](https://user-images.githubusercontent.com/14041622/41845849-7a1d52c0-78a7-11e8-84ed-a32fae3d9c19.png)
- 确认视频流的接口是`8081`：
![image](https://user-images.githubusercontent.com/14041622/41845879-99d91220-78a7-11e8-82f1-aa17ac2798ee.png)
- 把`stream_localhost on`改成`stream_localhost off`，关闭localhost本地的限制：
![image](https://user-images.githubusercontent.com/14041622/41845929-bd5d1764-78a7-11e8-9931-fae1168bad84.png)
- 把`sdl_threadnr`注释屏蔽掉：
![image](https://user-images.githubusercontent.com/14041622/41845977-dfffc7da-78a7-11e8-9a20-f704c122c697.png)
- 保存文件，退出。
- 开启`motion`程序的daemon，`sudo motion`:
![image](https://user-images.githubusercontent.com/14041622/41846068-257fd85e-78a8-11e8-89c7-dfdc750192c8.png)
- 打开浏览器查看树莓派的摄像头影像，地址是：`http://树莓派IP地址:8081`:

然后会看到浏览器一直在刷新显示这个小图像（分辨率不高）▼：

![image](https://user-images.githubusercontent.com/14041622/41846176-777c95d4-78a8-11e8-90aa-a150c4bb4c01.png)

经过测试，只要这个`motion`一直开着，就支持热插拔，随时插上随时都有（需要刷新浏览器）。

关闭`motion`的daemon：
```sh
$ sudo killall -TERM motion
```

## 修改分辨率
默认的显示大小是`320*240`的，非常小，不清楚。所以我们可以把它改大。

还是到`motion`的配置文件里，找到`width`和`height`，改成`800`和`600`，如下：
![image](https://user-images.githubusercontent.com/14041622/41847550-e24a32fa-78ac-11e8-91de-4cfc120aee99.png)

然后关闭重启`motion`：
```sh
$ sudo killall -TERM motion
$ sudo motion
```

就会看到改大了的显示了：

![image](https://user-images.githubusercontent.com/14041622/41847820-fd2fdda8-78ad-11e8-81a2-91f37674d113.png)

注意，每次修改如果不显示，或者不成功。可能需要重启下树莓派，或者你的设置比例有问题。



# 树莓派挂载外置存储

## 树莓派挂载U盘
[参考文章](https://segmentfault.com/a/1190000014173634)

```shell
# 检查设备名字
sudo fdisk -l

# 设定映射目录
sudo mkdir /media/pi/udisk
# 将指定设备映射到刚刚创建到目录
sudo mount -o uid=pi,gid=pi /dev/sda1 /media/pi/udisk

# 开机自动执行
sudo vim /etc/rc.local
# 将下面这句加到文件内容中(rc.local最后的exit 0之前都行)
mount -o uid=pi,gid=pi /dev/sda1 /media/pi/udisk

# 弹出优盘方法
sudo umount /media/pi/udisk

# 如果提示device is busy
ps -ef | grep /media/pi/udisk
sudo kill -9 xxx
```

## 树莓派挂载exFAT格式的移动硬盘
如果移动硬盘是exFAT格式，那么`mount`命令无法正常挂载这个移动硬盘。
所以我们需要安装`exfat-fuse`插件，让`mount`支持这个格式：
```sh
$ sudo apt-get install exfat-fuse
```
安装好后，就正常的使用`mount`命令挂载就OK了。


## 树莓派挂载NTFS格式移动硬盘

```sh
# 先查找当前已经插上的NTFS格式硬盘的设备位置，如：/dev/sda1
$ sudo fdisk -l | grep NTFS

# 随便找个地方建立一个空目录，用来映射硬盘内容
$ sudo mkdir /media/pi/drive

# 挂载硬盘
$ sudo mount -t ntfs-3g /dev/sda1 /media/pi/drive 
```



## 常用硬盘调试命令

显示所有正常连接的存储设备：
```sh
$ lsblk
```
这个命令可以看到有那些外置盘连接上了，有没有映射，映射到哪个目录。
![image](https://user-images.githubusercontent.com/14041622/42690227-0656113c-86d6-11e8-99c9-803e5a3d9895.png)

显示一切硬件连接的流水账信息：
```sh
# 显示最新的20条信息 且友好的输出时间(-T)
$ dmesg -T | tail -20

# 显示所有SD卡或U盘相关
$ dmesg |grep sda

# 显示一切USB相关
$ dmesg |grep usb
```
这个显示出刚刚插上的USB设备出了问题：供电不足
![image](https://user-images.githubusercontent.com/14041622/42723600-7e230b9e-8793-11e8-9b54-1a91926ee53c.png)


## 禁止树莓派自动挂载
我自己挂载的目录失效，树莓派自动挂载到另一个目录。
这是树莓派自动的，就像Windows一样插上硬盘就会挂载成一个驱动盘。
但是这个不方便我们操作，因为目录和路径图都是不确定的，所以就关闭掉树莓派自动挂载。

[参考：禁止u盘自动弹出](https://blog.csdn.net/luckywang1103/article/details/50829812)

```sh
# 查看各个设备的uuid号
$ ls -l /dev/disk/by-uuid/
lrwxrwxrwx 1 root root 10  6月 27 16:24 0000678400004823 -> ../../sdb1

#  在fstab中关闭这个设备的自动挂载 noauto
$ vim /etc/fstab
UUID=0000678400004823 /media vfat noauto 0 0
```


## 常见错误

## `mount 映射时显示 Transport endpoint is not connected`
这个是在`mount`命令挂载的过程中出现的错误。
一般是被映射的空目录本身出了问题，所以只要删除这个目录，或者换个地方再映射，就好了。

如果删不掉这个目录，就重启一下就可以删了。

## `弹出硬盘时显示 Target Busy`
看看有没有哪个设备正在连接这个目录，有的话就关掉。
或者重启电脑。


# 树莓派安装Samba文件共享服务器（NAS）

终于有点时间来解决下家中NAS需求了。一般自制NAS，只有选Samba。速度比FTP快，便利性比Windows文件夹共享好，设置多等等。

[▶参考：samba简介](https://github.com/jaywcjlove/handbook/blob/master/CentOS/samba.md)

## 安装Samba
```sh
$ sudo apt-get update
$ sudo apt-get install samba samba-common-bin
```

## 核心步骤：配置Samba

> Samba唯一设置的入口就算一个`smb.conf`文件，所有变化都依次而来，出了问题也只需要在这里找原因。

配置之前先说明，
这里我不打算只共享一个文件夹，而是共享树莓派连接上的所有外置硬盘。
树莓派的外置硬盘默认挂载在了`/media/pi`目录下，每个硬盘挂载为`/media/pi/drive1`，`/media/pi/drive2`等。
所以不用一个一个共享，直接把`/media/pi`共享就OK了。
下面配置还会限制：只有`pi`这个用户可以访问。

常用且肯定没问题的最简单配置如下：
```sh
# 编辑Samba的配置文件
sudo vim /etc/samba/smb.conf

# 文件末尾添加这个共享文件夹的定义：
[NAS]
comment = NAS External drive
path = /media/pi
public = Yes
browseable = Yes
writeable = Yes
valid users=pi
```

## 设置Samba用户名和密码
这一步也至关重要，直接影响各设备的访问。
注意，这个用户必须是本机已经在group和user里面都存在的用户，且必须权限设置什么的符合samba要求才行。否则会导致有些设备完全无法访问这个文件夹。
之前试了自己`groupadd`和`useradd`本地用户后，又在samba里`smbpasswd -a`添加用户名密码，结果Mac完全访问不了，Windows也是根据系统的不同有的能访问有的不能访问。
所以这里推荐用树莓派的默认用户名`pi`：
```sh
# 输入Samba用户的访问密码
sudo smbpasswd -a pi
```

## 重启Samba
```sh
# 推荐重启方法（可以看到自检过程）
$ sudo /etc/init.d/samba restart
```

到这一步，如果没出问题的话，就会显示成功：
![image](https://user-images.githubusercontent.com/14041622/42730143-053748c0-8820-11e8-814e-d85bf7090dce.png)

按照之前的配置，现在你就可以访问Samba共享文件夹了。

## 访问方法

一般访问方法如下：
- Windows：直接打开桌面的网络（网上邻居）-> RaspberryPi(树莓派的网络名)，然后就可以看到树莓派上所有共享的文件夹和设备了。
- Mac: 稍微麻烦一点，在Finder中点击菜单 -> Go -> Connect to server -> 输入`smb://IP地址`，按照要求输入本机或树莓派的Samba用户名密码：
![image](https://user-images.githubusercontent.com/14041622/42736889-41f02f68-88a0-11e8-9b9c-87a1de108457.png)


然后可以看到，目录中和本地目录几乎没什么区别：能看预览，支持所有文件夹正常的快捷键，随意拷贝粘贴，这是FTP远不能比的。

![image](https://user-images.githubusercontent.com/14041622/42730221-a50fd88e-8821-11e8-8221-13bf36273ec4.png)

## Samba自检
Samba的自检程序`testparm`，可以自动测试，并显示Samba所有的共享和定义
```sh
$ testparm
```
![image](https://user-images.githubusercontent.com/14041622/42730699-a3387ab4-882d-11e8-85bb-8c669fa1495b.png)


## 将Samba的共享目录映射到本地

Windows上，直接在文件夹里点击菜单->工具->映射网络驱动器。然后选择映射出来的驱动盘字母，点击浏览，选择网络邻居里的树莓派，确定完成。就会在本地的计算机里显示出映射磁盘了。

Mac上，一般在文件夹里面通过`Cmd+K`连接服务器后打开共享文件夹后，系统就会自动把它挂载到`/Volumes/你的共享文件夹名`这里。可以直接通过命令行随意访问。然后即使桌面上的文件夹关闭后，也还是可以在命令行里正常访问。


## 只允许指定的用户访问
如果限定只允许那些用户登录的可以访问这个文件夹， 需要在刚刚的Samba文件夹的配置文件里加上一句：
```
valid users = samba01, samba02
```

## Mac访问加速以及消除.DS_Store安全隐患
Mac上访问远程文件夹会留下`.DS_Store`文件，其中包含太多信息这样很不安全。
所以我们要在Mac上设置，在访问远程文件夹时不留下这个文件：
```sh
$ defaults write com.apple.desktopservices DSDontWriteNetworkStores true
```

## 常见问题

### Mac上能用guest访问却不能用设置了的用户访问
这个是你的Samba用户设置出了问题。
有可能是Samba中定义的用户，在本机中权限不够。
解决方法就是：
- 直接用树莓派的原生用户`pi`，或
- 仔细研究新创建的用户权限，添加好了再到Samba配置中设置


### 访问外置硬盘Permission Denied
这个也是用户权限问题，配置原生`pi`用户就没问题了。


### 禁止树莓派自动挂载：自己挂载的目录失效，树莓派自动挂载到另一个目录
这是树莓派自动的，就像Windows一样插上硬盘就会挂载成一个驱动盘。
但是这个不方便我们操作，因为目录和路径图都是不确定的，所以就关闭掉树莓派自动挂载。

[参考：禁止u盘自动弹出](https://blog.csdn.net/luckywang1103/article/details/50829812)

```sh
# 查看各个设备的uuid号
$ ls -l /dev/disk/by-uuid/
lrwxrwxrwx 1 root root 10  6月 27 16:24 0000678400004823 -> ../../sdb1

#  在fstab中关闭这个设备的自动挂载 noauto
$ vim /etc/fstab
UUID=0000678400004823 /media vfat noauto 0 0
```