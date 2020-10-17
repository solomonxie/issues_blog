# ❖ Python os.walk() 文件遍历

> 学习os.walk文件遍历，最最最重要的是了解这种遍历方法的逻辑，它的路径！！不了解的话，永远也学不会。

os.walk()是Python原生的遍历文件夹方法，但是表现出来的逻辑真的不是很好记忆。

用法：
```py
os.walk(顶级目录地址, topdown=True, onerror=None, followlinks=False) 
```
函数返回一个三元Tupple: `(目录路径(字符串), 子目录名(列表), 文件名(列表))`

![image](https://user-images.githubusercontent.com/14041622/40161575-cdfbb2f2-59e3-11e8-8efd-8db59fe88c96.png)

## 遍历路径
`os.walk()`是**逐层扫描**的，一层一层来。
比如上图中，从`Root`根目录下开始扫，
- 先扫第一层，获得`pics1.jpg`, `pic2.jpg`, 然后是一个目录`New`和目录`Old`。
- 这个时候还不深入每个子目录，现在算完成一个循环，返回一个子目录列表: `[pics1.jpg, pics2.jpg, New, Old]`
- 然后在从上面的第一个子目录开始，往下扫，如同上面的过程。
- 完成第一个目录后，再继续第二个子目录。

记住，它不会无穷尽深入每一个目录一直到底，而是逐层扫。
**扫完一层后，再跳出来需要遍历的目录深入下一层。**

## 指定深度
os.walk默认是深入到底的，遍历所有的位置。有时候我们只需要一层或两层。
抱歉，os.walk()没这个功能，只能自己写。
方法就是：声明一个`depth`变量记录当前深度，循环到一定深度后，用`break`语句退出循环。
以下为示例代码：
```py
depth = 1
for root, subdir, filenames in os.walk():
    if depth is 2:
        break
    depth += 1
```


## 示例：只看文件
```py
search_dir = '/home/me/`
for root, subdir, filenames in os.walk(search_dir):
    print(root, subdir)
    for fn in filenames:
        print(fn)
```
