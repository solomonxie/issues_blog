# Python操作MySQL的中文乱码解决之路
## 第一步：小心翼翼地正常去触碰（连接）数据库
## 第二步：几个循环读取数据库
## 第三步：插入英文数据，前方高能：再插入中文数据！
## 第四步：对网上各种乱码解决方案的测试
### Solution 1: Python编码的基本设置

``` python
# coding:utf-8
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
```
### Solution 2: 创建数据库连接时指定编码

``` python
db = MySQLdb.connect(charset='utf8',host='localhost', db='dbTest', user='root',passwd='000000') 
```

光是这么设置一下，不但中文传不进去，而且还会报错！：
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/841144-1ec7d053a6c69ccf.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
所以要配合下面的方法再试一下。
### Solution 3: 在excute(sql)时传入一个奇妙形式的字符串

``` python
# 注：这里必须是'utf8'，而不是'utf-8'
db = MySQLdb.connect(charset='utf8', host='localhost', db='dbTest', user='root',passwd='000') 
cursor = db.cursor() 
values = [u"中文测试 Unicode, charset='utf8'"]
print value
cursor.execute('insert into test(txt) values(%s) ', values)
db.commit()
db.close()
print 'OK'
```

下面是各种情况下成测试：
- 传入列表的字符串为普通字符串，且设置了charset='utf8'，以及
- 传入列表的字符串为Unicode字符串，且设置了charset='utf8'，**OK 通过！**
  ![Paste_Image.png](http://upload-images.jianshu.io/upload_images/841144-a202021f07d37856.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 传入列表的字符串为普通字符串，但**未设置**charset='utf8'：
  结果**失败！**依然是乱码。
  ![Paste_Image.png](http://upload-images.jianshu.io/upload_images/841144-73d8070cfdfa9be6.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 传入列表的字符串为Unicode字符串，但**未设置**charset='utf8'：
  会直接报错。
  ![Paste_Image.png](http://upload-images.jianshu.io/upload_images/841144-b8fd36551570cfb9.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
- 不传列表，直接传入普通字符串，且设置了charset='utf8',以及
- 不传列表，直接传入Unicode字符串，且设置了charset='utf8'：
  ![Paste_Image.png](http://upload-images.jianshu.io/upload_images/841144-b4a9150d2d2d690c.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 总结：也就是说，目前有两个条件是必须的——
1. 传入excute()第二个参数，必须是`list`列表变量
2. connect()构造函数中，必须设置`charset='utf8'`
### Solution 4: 在Python里面给MySQL数据库设定编码

代码如下：

``` python
cursor = db.cursor() 
cursor.execute("SET NAMES 'utf8'") 
cursor.execute("SET CHARACTER_SET_CLIENT=utf8") 
cursor.execute("SET CHARACTER_SET_RESULTS=utf8")
# OK 测试成功
cursor.execute('insert into test(txt) values("我是中文") ') 
# OK 第二次不写以上三条也通过
# cursor.execute('insert into test(txt) values("我是中文2，看看会不会保存设置。") ') 
# Failed 无论怎么玩，charset=不设置就不通过
# cursor.execute('insert into test(txt) values("我是中文3，看看不带charset=管不管用。") ') 
# cursor.execute('insert into test(txt) values("我是中文4") ') # OK 测试成功
cursor.execute('insert into test(txt) values("我是中文5，看看重新打开mysql终端，还会不会保留设置。") ') # OK 测试成功
db.commit()
db.close()
```

具体情况是：
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/841144-ae37a740b8167731.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
![Paste_Image.png](http://upload-images.jianshu.io/upload_images/841144-adae3e7d2d2a9267.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
#### 也就是说：这种方法也必须有2个条件：
1. connect()构造函数中，必须设置charset='utf8'
2. 必须显示地写三句excute语句，来设置MySQL端的编码

只要遵守这2个条件，



