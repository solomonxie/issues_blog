# 各种云服务器网络连接之 常见异常 [DRAFT]


## AWS Lightsail 新加坡服务器“整体沦陷”

> solomonxie commented on Oct 15

自从十一假日以来（为什么是十一？也许是历史原因？），在Lightsail里创建的新加坡服务器就一直不稳定，shadowsocks断线频率高到每次打开网页都要刷新几次才能刷出来的地步。连基本的SSH都要几次才能连上，换端口完全不影响这个状态，换IP，换服务器，换Shadowsocks算法，换程序，SSH Tunnel，V2Ray（各种配置都试过了），全都不行。外加Cloudflare+Websocket+TLS加持，都没用，这太奇怪了。

一时间懵了。。。。为什么所有东西都试过了，完全不影响这种状态？很奇怪啊。
于是进入了长达两个多礼拜的沉默期，想着忍一忍过去了。直到昨天想到：我还有最后一招，如果这个也不管用就真没办法了——换服务区。
虽然新加坡一直以来是连接大陆最快的线路，但是为了试验，我挑选了次优的日本。

没想到效果出奇的好！日本线路虽然在ping时明显比新加坡慢很多，但是完全没有阻碍、没有屏蔽的话，完全可以忽略那个问题。连接youtube时候"connection speed"一度达到9000 kb/s，真的目瞪口呆。而且无论换哪种shadowsocks算法，或v2ray服务，都没有影响，速度都很快。

所以由此可以得出结论：新加坡服务区整体被盯上了，而且绝对不是破解了某些算法，而是大频率打压一切可疑的连接，甚至打压一切前往新加坡的连接（连最基本的ssh都一样）。




## 每周日所有地区服务器连接频繁掉线
已经很多个月了，每周日都会频繁掉线，无论是是shadowsocks／ssh／v2ray／甚至http连接，都会连接困难，减速等等。换了无数的主机、地区（东京、首尔、新加坡。。）、服务商（aws、Digitalocean等）。
所以问题在，周日，这个问题上。不知道为什么。
