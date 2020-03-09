# 更多Python2编码的小细节

## 数组`.join()`合并
数组中必须所有的元素都是字符串，且都是统一的编码才能合并，否则报错。统一后，如果全是unicode，那么返回的字符串就是unicode；如果元素全是str，那么返回的就是str。
![image](https://user-images.githubusercontent.com/14041622/35965010-6c01a23c-0cf4-11e8-81ce-9340217d9553.png)


