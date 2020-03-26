# iOS 9.3.5越狱

这个版本只能用Phoenix越。
[参考官网：Phoenix](https://phoenixpwn.com/)
[参考youtube：Fix Cydia & Phoenix Crashing On 32-Bit Devices (iOS 9.3.5)](https://www.youtube.com/watch?v=zY9TwqFvTK8)

下载好两个文件后：
- iPad用USB连接到电脑
- 本地打开`Cydia Impacter`, Windows或Mac都行
- 如果看到软件上显示设备的名字，则可以正常连接
- 在软件上选择菜单 - Device - Install Package - 选择刚刚下载的`Phoenix4.ipa`文件
- 程序弹出页面后输入Apple ID，即iTunes下载用的登录邮箱
- 弹出密码时候，需要输入苹果的App专用密码，不是登录密码。如果没有，需要到官网注册
- 打开[苹果官网](https://appleid.apple.com/account/manage)
- 找到Security，找到`APP-SPECIFIC PASSWORDS`，点击Generate生成
- 输入密码标签，回车后就会自动弹出一串密码，保存，然后在本地备份一下
- 回到`Cydia Impacter`软件，输入刚才得到的密码，回车
- 等待运行，成功后，回到iPad上会看到桌面多处一个红色Phoenix图标
- 打开iPad设置 - General - Device Management，看到一个device是自己的邮箱名，点进去，点Trust信任
- 回到桌面，打开红色Phoenix图标，按提示操作安装
- 安装成功后，桌面会多一个Cydia图标，说明越狱成功。


![snip20180808_240](https://user-images.githubusercontent.com/14041622/43790913-99da15be-9aa6-11e8-8c34-539a23bde1e5.png)
![snip20180808_241](https://user-images.githubusercontent.com/14041622/43790914-9a402c3c-9aa6-11e8-9e56-7f33ca2d1715.png)
![snip20180808_242](https://user-images.githubusercontent.com/14041622/43790916-9aa712b2-9aa6-11e8-979e-5f872e814b8b.png)
![snip20180808_246](https://user-images.githubusercontent.com/14041622/43822340-6ea12bee-9b1e-11e8-8979-4d35ff96084a.png)
![2018-08-08 00 49 04](https://user-images.githubusercontent.com/14041622/43822359-78391a86-9b1e-11e8-94e5-90af2b5bac6b.png)
![2018-08-08 00 49 29](https://user-images.githubusercontent.com/14041622/43822360-78834ffc-9b1e-11e8-8632-3809770174d3.png)
![2018-08-08 00 49 34](https://user-images.githubusercontent.com/14041622/43822361-78cd6b14-9b1e-11e8-921d-1a81a069d2f1.png)
![2018-08-08 00 49 37](https://user-images.githubusercontent.com/14041622/43822362-791b2854-9b1e-11e8-94e7-26224cc25f2b.png)
![2018-08-08 00 50 06](https://user-images.githubusercontent.com/14041622/43822363-79663ec0-9b1e-11e8-8b36-cff7c61021b0.png)
![2018-08-08 00 53 16](https://user-images.githubusercontent.com/14041622/43822365-79aecfb4-9b1e-11e8-81da-337b915673ce.png)


## 常见问题
### Cydia Impactor 安装时候报错81 9391 说要求开发者账号才可以
其实不是开发者账号的事，不需要开发者账号。
这是因为没有正常把`Phoenix4.ipa`选中，或者这个文件有问题，或者型号不匹配。
选中方法：
    - 直接拖拽，或者
    - 在软件上选择菜单 - Device - Install Package - 选择刚刚下载的`Phoenix4.ipa`文件

### 173 密码错误
一般肯定是输入了登录密码。
注意这里不是输入登录密码，而是专门的`APP-SPECIFIC PASSWORDS`，需要自己去苹果账号管理网页专门生成，很方便。

![image](https://user-images.githubusercontent.com/14041622/43793256-946ac7d4-9aad-11e8-97fd-fe88abfa116e.png)

### 每次重启后越狱都失效
每次重启，或者每隔7天，cyndia和安装的插件都失效。这时候需要点桌面上的Phoenix图标再次越狱，很方便，不用连电脑也不用联网就可以。
但是有时候桌面上的Phoenix也无法打开。这就需要连电脑从头再来过一遍了。
这是因为针对iOS9.3.5的Phoenix是“半越狱”产品。

[参考：How to Re-Enable a Semi-Tethered Jailbreak](https://ios.gadgethacks.com/how-to/cydia-101-re-enable-semi-tethered-jailbreak-0180461/)


### 其它问题
[参考：Cydia Impactor 安裝 IPA檔案時 錯誤碼處理方式](http://bearnear.com/2017/11/cydia-impactor-%E5%AE%89%E8%A3%9D-ipa%E6%AA%94%E6%A1%88%E6%99%82-%E9%8C%AF%E8%AA%A4%E7%A2%BC%E8%99%95%E7%90%86%E6%96%B9%E5%BC%8F/)



