# 树莓派无法升级Ruby或安装Jekyll

我对Ruby没什么需求，主要是想在树莓派上安装Jekyll，而Jekyll依赖Ruby。

结果安装Jekyll报错：

![image](https://user-images.githubusercontent.com/14041622/45497453-6d3f7a00-b7aa-11e8-8585-5d24227e23f0.png)

根据Jekyll官方声明，Ruby必须2.2.5以上，可以本地树莓派最高只能升级到2.1.5。

以下是通过各种尝试找到的解决方案：

- 安装Docker，在docker里安装jekyll
