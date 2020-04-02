# 树莓派GPIO第一步：点亮LED

参考：https://blog.csdn.net/LeasonQ/article/details/51531311

![image](https://user-images.githubusercontent.com/14041622/77849941-d908fc80-7201-11ea-81e1-e6e3d99b1749.png)

![image](https://user-images.githubusercontent.com/14041622/77849944-e0c8a100-7201-11ea-84b5-67f7f9b49819.png)


脚本：
```sh
#!/usr/bin/env python
 
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)
while True:
 
     GPIO.output(12,True)
 
     time.sleep(1)
     GPIO.output(12,False)
     time.sleep(1)
```
