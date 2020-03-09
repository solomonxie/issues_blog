# ❖ Linux上各种网络端口流量监控的工具对比使用

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

[参考文章](https://segmentfault.com/a/1190000002797441)
![image](https://user-images.githubusercontent.com/14041622/36032772-0355e7ba-0dea-11e8-8014-b44463277bff.png)



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



