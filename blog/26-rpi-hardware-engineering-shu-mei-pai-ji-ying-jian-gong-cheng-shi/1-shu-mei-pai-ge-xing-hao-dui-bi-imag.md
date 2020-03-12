# 树莓派各型号对比

![image](https://user-images.githubusercontent.com/14041622/45686373-c29ad300-bb7e-11e8-96fd-46043aec04c2.png)

## 怎么查看硬件信息

查看树莓派硬件型号：
```sh
$ cat /sys/firmware/devicetree/base/model
>> Raspberry Pi 3 Model B Rev 1.2

#或
$ cat /proc/device-tree/model
>> Raspberry Pi 3 Model B Rev 1.2
```

查看全部硬件信息：
```sh
$ sudo apt-get install lshw

$ sudo lshw
```
![image](https://user-images.githubusercontent.com/14041622/45688695-a4d06c80-bb84-11e8-9bda-9b4830f6d36c.png)


