# Nginx 部署静态网页

```conf
http {
    server {
        listen       8080;
        server_name  localhost;

        location / {
             root   /var/www/html;
             index  index.html index.html;
        }

        location /sub {
             alias   /path/to/some-other-name;  # 注意这里二级目录一定要用alias而不是root，否则404
             index  index.html index.html;
        }
    }
}
```
