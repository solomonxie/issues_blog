# ❖ Virtualbox连接网络设置


## 需求一：让虚拟机又能访问外网又可以与主机对话
[参考：VirtualBox: 为你的虚拟机配置静态 IP](https://huangruichang.github.io/?techniques/virtualbox-static-ip/index)

这就是需要用到Virtualbox 双网卡适配器。
因为要满足虚拟机能访问外网，又能与主机沟通，就需要两块网卡。所以我们要在Virtualbox中给它设置两个Adapter（网卡），然后设置为：

> NAT + Host-only


### 首先在Virtualbox软件的全局设置

![image](https://user-images.githubusercontent.com/14041622/45485618-e333e900-b78a-11e8-8296-41f44e7cf280.png)

设置DHCP（这样虚拟机就能有静态IP了）：
![image](https://user-images.githubusercontent.com/14041622/45485651-fa72d680-b78a-11e8-8295-bb710cfd334e.png)

### 然后设置虚拟主机
首先要在虚拟主机关闭的情况下设置。

开启2个Adapter：NAT和Host-only

NAT适配器采用默认设置：
![image](https://user-images.githubusercontent.com/14041622/45485730-33ab4680-b78b-11e8-8300-8a59cf52ca5f.png)

Host-only设置：
![image](https://user-images.githubusercontent.com/14041622/45485762-4faee800-b78b-11e8-9863-f275fa1e85f6.png)


然后进入虚拟机（Linux）后，就可以通过`ifconfig`看到本机的内网IP了。

![image](https://user-images.githubusercontent.com/14041622/45485880-b502d900-b78b-11e8-8e05-8b4dedc54c74.png)

可以在自己的Host机子上ping一下这个虚拟机，发现可以ping通。

反过来，在虚拟机里ping一下Host（刚才设置全局的一个内网时候的192.168.56.1就是）。


## 需求二：让虚拟机又能访问外网又在Wifi同网段

和需求一差不多，这里只做简单的改变：
双网卡设置为：

> Bridge + Host-only

其中Bridge设置如下：

![image](https://user-images.githubusercontent.com/14041622/45486482-d8c71e80-b78d-11e8-84ed-1ce7593b9df8.png)


进入虚拟机后，输入命令`ifconfig`就会发现，虚拟机具有了和我的主机在Wifi里同样网段的IP地址（我的wifi网段是`192.168.199.xxx`）：

![image](https://user-images.githubusercontent.com/14041622/45486554-1d52ba00-b78e-11e8-9e12-34018a98baf3.png)

