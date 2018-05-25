# Shadowsocks等`相关`技巧
## Shadowsocks 服务器安装

1.CREATE SERVER
2.CREATE SSH KEY AND MAP TO LOCAL
3.REMEMBER SSH PHRASE AS A PASSWORD EVERYTIME CONNECT TO SERVER
4.OPEN TERMINAL

ssh root@ip-address

sudo apt-get update
apt-get install python-pip -y
pip install shadowsocks

vi /etc/shadowsocks.json

```json
{
    "server":"IP",
    "server_port": 1111,
    "local_address":"127.0.0.1",
    "local_port":1080,
    "password":"shadow999",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open":false
}
```

ssserver -c /etc/shadowsocks.json -d start

if encounter the error permission denied, then change permission of that file:

```shell
sudo chmod 777 /var/run/shadowsocks.pid
sudo chmod 777 /var/log/shadowsocks.log
```


## Shadowsocks Linux客户端

sudo apt-get install python-pip
sudo pip install shadowsocks

安装好后有两种方法可以运行服务

1. 命令行：
   格式为：
   sslocal ‐s 服务器地址 ‐p 服务器端口 ‐l 本地端口 ‐k 密码 ‐t 600 ‐m aes‐256‐cfb
   应用如：
   sslocal -s 200.200.200.200 -p 8111 -l 1080 -k 123123 -t 600 -m aes-256-cfb
   回车后就已经运行本地端口映射了 
   （命令行下，运行了这个服务就无法输入别的指令了，可以Ctrl+Z切换到后台运行。）
2. GUI图形化管理
   这个GUI软件叫shadowsocks-qt5，

sudo add-apt-repository ppa:hzwhuang/ss-qt5
sudo apt-get update
sudo apt-get install shadowsocks-qt5

安装好后在桌面菜单中找到这个软件，运行后在connection菜单中选择手动添加。
然后设置和windows上一样， 保存后选择服务器点击连接。服务就运行了

在服务映射运行情况下， 还不能联网。还需要在浏览器里设置才能用。
火狐的话，浏览器本身的代理设置是不行的，需要用到autoProxy插件才行。
搜索官方autoproxy插件安装好后，倒腾下在菜单中添加代理，设置和GUI中一样。
然后就简单了。


