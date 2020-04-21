# Python利用生成器实现最简单的协程并发


```py
import time

def worker(name):
    while True:
        print(name)
        time.sleep(0.1)
        yield

def use_coroutine():
    w1 = worker('[ 1 ]')
    w2 = worker('[ 2 ]')
    for _ in range(3):
        next(w1)
        next(w2)

if __name__ == "__main__":
    use_coroutine()

# [OUT] ===>
[ 1 ]
[ 2 ]
[ 1 ]
[ 2 ]
[ 1 ]
[ 2 ]
```
