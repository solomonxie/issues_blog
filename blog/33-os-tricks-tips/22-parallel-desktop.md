# Parallel Desktop (Mac虚拟机) 安装Windows


## 安装Ghost版Win7系统

![image](https://user-images.githubusercontent.com/14041622/45351082-e5aa0d80-b5e7-11e8-8457-585a16392fda.png)

![image](https://user-images.githubusercontent.com/14041622/45351118-f65a8380-b5e7-11e8-983d-c7654b9c9621.png)

![image](https://user-images.githubusercontent.com/14041622/45351146-04a89f80-b5e8-11e8-87c6-e82f4c6ef2d8.png)

无法检测到系统没关系，可以自己手动选：

![image](https://user-images.githubusercontent.com/14041622/45351181-19853300-b5e8-11e8-9d62-32193588cec0.png)

![image](https://user-images.githubusercontent.com/14041622/45351194-2144d780-b5e8-11e8-839b-122013aae579.png)



![image](https://user-images.githubusercontent.com/14041622/45351261-55b89380-b5e8-11e8-90dd-f9aa1ac751c0.png)


设置自己想要的硬件等配置：

![image](https://user-images.githubusercontent.com/14041622/45351299-6e28ae00-b5e8-11e8-8eb3-07e562825936.png)


![image](https://user-images.githubusercontent.com/14041622/45351414-b1831c80-b5e8-11e8-8f2f-f00aedae393b.png)


记得调整好开机的读取顺序，相当于设置主机的BIOS了：

![image](https://user-images.githubusercontent.com/14041622/45351684-56055e80-b5e9-11e8-9d08-b137c4030dfc.png)


开始正常安装：

![image](https://user-images.githubusercontent.com/14041622/45351493-e5f6d880-b5e8-11e8-85a2-e08c976f83d8.png)


进入了光盘或USB的安装界面，选择WinPE系统：

![image](https://user-images.githubusercontent.com/14041622/45355464-12175700-b5f3-11e8-8dc0-f24f31925db2.png)


进到WinPE系统中会看到，本地没有磁盘。
实际上是虚拟机分配了，但没有格式化的原因。
打开分区软件，手动格式化：

![image](https://user-images.githubusercontent.com/14041622/45356362-a5518c00-b5f5-11e8-80e2-57d416122b85.png)

之后就是常规的Ghost安装了。

![image](https://user-images.githubusercontent.com/14041622/45356681-88698880-b5f6-11e8-886a-bee9969abf2b.png)



## 安装正常安装版Win7系统

直接连接ISO光盘文件，正常安装，比Ghost简单的多。



## Reclaim
安装好后，肯定有很多不喜欢的软件，比如Office等。
想方设法把不需要用的软件全部删除，然后用电脑管理软件如模仿、360安全卫士等，清除各种缓存、没用的东西。
然后磁盘会减少几个G的空间，这时候STOP虚拟机，然后在控制页面里面选择`Reclaim`，就可以给U盘节省几个G的空间了。
