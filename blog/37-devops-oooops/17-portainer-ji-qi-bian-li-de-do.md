# Portainer: 极其便利的Docker管理GUI [DRAFT]

Official: https://www.portainer.io/

一切只需要：
```sh
$ docker volume create portainer_data
$ docker run -d -p 9000:9000 -v /var/run/docker.sock:/var/run/docker.sock -v portainer_data:/data portainer/portainer
```


![image](https://user-images.githubusercontent.com/14041622/57665460-8a289780-762e-11e9-9010-7836c7925e88.png)

