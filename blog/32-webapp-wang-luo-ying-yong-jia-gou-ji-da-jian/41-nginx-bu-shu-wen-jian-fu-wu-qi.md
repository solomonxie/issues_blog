# Nginx 部署文件服务器

```conf
http {
    server {
        listen       8080;
        server_name  localhost;

        location / {
             root   /var/www/html;
             index  index.html index.html;
        }

        location /share {
            alias   /path/to/shared-folder;
            autoindex on;
            autoindex_exact_size on;
            autoindex_localtime on;
        }
    }
}
```
