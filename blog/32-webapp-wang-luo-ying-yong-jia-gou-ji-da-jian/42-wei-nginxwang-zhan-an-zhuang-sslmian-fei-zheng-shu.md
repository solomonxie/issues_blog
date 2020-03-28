# 为Nginx网站安装SSL免费证书 (Let's Encrypt)

要安装免费的第三方CA认证的SSL证书，需要：
- 一个SSL证书文件
- 网站服务器后台长期运行的一个程序，即：ACME协议的客户端程序

Refer to: https://letsencrypt.org/getting-started/
Refer to Cerbot for ACME client: https://certbot.eff.org/lets-encrypt


## 安装Cerbot - ACME协议的客户端

Refer to: https://certbot.eff.org/lets-encrypt/ubuntuxenial-nginx

Nginx + Ubuntu 1604
```sh
sudo apt-get update
sudo apt-get install software-properties-common -y
sudo add-apt-repository universe -y
sudo apt-get update
sudo apt-get install certbot -y
# 需要手动按回车确定：
sudo add-apt-repository ppa:certbot/certbot
sudo apt-get install python-certbot-nginx -y

# 生成证书
sudo certbot certonly --nginx
```


