# Filming & Media Editing 多媒体编辑及摄影相关



# iphone投影到Mac电脑

一般来讲极其简单：
- 直接把iphone用数据线连接到Mac上
- 打开Quicktime Player
- 打开菜单-> File -> New Movie Recording
- Camera和Microphone都选择iphone
![image](https://user-images.githubusercontent.com/14041622/41190692-4ee71ff2-6c16-11e8-94ac-fc8ff1248e4d.png)
- 这样就可以在Mac上显示iphone画面，且声音也是从Mac上出来了（iphone里的声音自动关闭）

效果：
![image](https://user-images.githubusercontent.com/14041622/41190728-c841a9b2-6c16-11e8-9cd9-b3a8d2b79f8b.png)


## Quicktime上不显示iPhone的选项
那是因为不知道什么东西占用了iphone或什么端口。
需要执行命令来解除占用。在命令行里输入以下两个命令解除一切占用：
```sh
sudo killall VDCAssistant

sudo killall AppleCameraAssistant
```
