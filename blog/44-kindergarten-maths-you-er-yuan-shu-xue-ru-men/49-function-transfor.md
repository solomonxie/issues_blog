# `Function Transformations`

[Refer to math is fun: `Function Transformations`](http://www.mathsisfun.com/sets/function-transformations.html)

> Express different transformations in the function.

Refer to the previous note [Graph transformations](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-371067923).

Let's assume:
- the function is `f(x) = x^2` (it could be any other function instead).
- and the **transformed** new function is `g(x)`.

## `Translation` (Shift)

```javascript
g(x) = f(x) + C
```
- If `C` is positive, the graph of `f(x)` moves **UP**.
- If `C` is negative, the graph of `f(x)` moves **DOWN**.

```javascript
g(x) = f(x+C)
```
- If `C` is positive, the graph of `f(x)` moves **LEFT**.
- If `C` is negative, the graph of `f(x)` moves **RIGHT**.

## `Reflection` (Flip/Mirror)

- Reflect the graph about the `x-axis` (Mirror it upside down, or downside up).
```javascript
g(x) = -f(x)
```

- Reflect the graph about the `y-axis` (Mirror the graph left to right, or right to left)
```javascript
g(x) = f(-x)
```

## `Dilation` (Scale/Stretch/Compress)
> Stretching the graph when `C` bigger than 1, compress it when `C` less than 1.

- Scale the graph about the `y-axis` (Vertically stretch or compress)
```javascript
g(x) = C・f(x)
```

- Scale the graph about the `x-axis` (Horizontally stretch or compress).
```javascript
g(x) = f(C・x)
```

Summary:
![image](https://user-images.githubusercontent.com/14041622/37594703-f3992f0a-2bb0-11e8-903b-8e2c50d12ec3.png)

