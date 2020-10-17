# Cloudflare 个人申请免费TLS/SSL证书

首先需要买一个域名。最简单的就是在阿里云买一个9块钱一年的域名，全程两分钟搞定。
然后要有一个自己的公网服务器，我是在AWS Lightsails买的，$3.5一个月。
然后在阿里云管理后台把域名指向服务器的IP地址。
以上这几步都不详解了，因为做到HTTPS这一步基本上已经有了一定基础。

现在国际上比较知名的免费SSL证书有:
- [Cloudflare](https://www.cloudflare.com/)
- [Let's Encrypt](https://letsencrypt.org/)

这里主要讲`Cloudflare`.


添加后出错：

![image](https://user-images.githubusercontent.com/14041622/46417314-f4559180-c75b-11e8-9113-1d5cfafdaad1.png)

这种情况一般是刚注册域名没多久，还没有生效才产生的。耐心等一等再重试即可。一般24小时是要等的。

### 注册步骤
![snip20181003_23](https://user-images.githubusercontent.com/14041622/46530157-6f898580-c8cb-11e8-84b5-d706ede2e59f.png)
![snip20181004_24](https://user-images.githubusercontent.com/14041622/46530158-70221c00-c8cb-11e8-96de-b690226abfbc.png)
![snip20181004_25](https://user-images.githubusercontent.com/14041622/46530160-70bab280-c8cb-11e8-98ef-b8546d6f8110.png)
![snip20181004_26](https://user-images.githubusercontent.com/14041622/46530163-70bab280-c8cb-11e8-9b97-fe96af999fa9.png)
![snip20181004_28](https://user-images.githubusercontent.com/14041622/46530165-71534900-c8cb-11e8-9667-72c4815336a9.png)
![snip20181004_29](https://user-images.githubusercontent.com/14041622/46530167-72847600-c8cb-11e8-9580-0b7794f3bed6.png)

