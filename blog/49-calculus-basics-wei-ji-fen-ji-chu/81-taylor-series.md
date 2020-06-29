#  ❖ Taylor Series

`Taylor series`, or `Taylor polynomial` is a series that can **REPRESENT** a function,
**regardless** what function it is.

[▼Refer to 3Blue1Brown for animation & intuition: Taylor series | Chapter 10, Essence of calculus](https://www.youtube.com/watch?v=3d6DsjIBzJ4&t=56s)
> "Taylor Series is one of the most powerful tools Math has to offer for **approximating functions.**" - 3Blue1Brown

[►Refer to Khan academy: Taylor & Maclaurin polynomials intro (part 1)](https://www.khanacademy.org/math/old-ap-calculus-bc/bc-series/bc-taylor-series/v/maclaurin-and-taylor-series-intuition)
[▼Refer to xaktly: Taylor Series](http://www.xaktly.com/TaylorSeries.html)
![image](https://user-images.githubusercontent.com/14041622/42205356-d96aef1e-7ed6-11e8-8c2d-82b0b408bb4e.png)


![image](https://user-images.githubusercontent.com/14041622/42205070-f8bc7ffa-7ed5-11e8-851a-6ac45201b5ee.png)
(▲ `C` represents the **centre** where we're centred at to approximate the function.)

> ▲ Notice: The **`Taylor Series`** is a **`Power Series`**, which means we can use a lot of techniques of power series on this to operate it easily.

We could expand it and make it clearer ▼:
![image](https://user-images.githubusercontent.com/14041622/42205239-73484920-7ed6-11e8-8f88-80b08440261a.png)


The **main purpose** of using a `Taylor Polynomial` is to **REPLACE** the original function with a **polynomial**, which it is **easy to work with**.

etc., we can express the function `f(x) = eˣ` as ▼:
![image](https://user-images.githubusercontent.com/14041622/42203582-d55cde1e-7ed1-11e8-8eda-7f00d635e001.png)

**More importantly**, by **adding more & more terms** into the polynomial, we can approximate the function more precisely:

[►Refer to joseferrer: Mathematical explanation - Taylor series](https://steemit.com/mathematics/@joseferrer/mathematical-explanation-taylor-series)
[►For More animation, visit Desmos: Taylor Series Visualization](https://www.desmos.com/calculator/oiexhzavjp)

![97f5384c9b8d6ceebf3b894efc106adb](https://user-images.githubusercontent.com/14041622/42213417-4083dc38-7eeb-11e8-91d8-1d7c90abc4dd.gif)



### Example
![image](https://user-images.githubusercontent.com/14041622/42154228-c8084e84-7e17-11e8-9388-1e4817228c0d.png)
Solve:
- First to know the formula of `Taylor Series` centred at `x=1`:
![image](https://user-images.githubusercontent.com/14041622/42154259-d6b14404-7e17-11e8-9fb5-50deb8f09a15.png)
- The problem is asking the coefficient of `(x-1)³`, means **all the rest part** in the formula, which is:
![image](https://user-images.githubusercontent.com/14041622/42154421-4bfa9c24-7e18-11e8-91af-dfded4db92e9.png)
- And it also means the `n=3`, so the coefficient becomes:
![image](https://user-images.githubusercontent.com/14041622/42154540-9c099f26-7e18-11e8-8eb9-625771b3c88b.png)
- Let's evaluate the `f'''(1)`:
![image](https://user-images.githubusercontent.com/14041622/42154522-91a67d2e-7e18-11e8-878a-4324dd932448.png)
- So the coefficient is:
![image](https://user-images.githubusercontent.com/14041622/42154558-abe0a26e-7e18-11e8-8115-ef65f579cf0b.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/42206442-b2846152-7ed9-11e8-8539-cf4c0c2bcaed.png)
Solve:
- Let's express the Taylor polynomial to the `nth degree` as:
![image](https://user-images.githubusercontent.com/14041622/42206602-37675a1e-7eda-11e8-9560-07e69c826435.png)
- Since it's asking for the series to the `3rd degree`, then it becomes:
![image](https://user-images.githubusercontent.com/14041622/42206807-c8dd4468-7eda-11e8-808e-a37f4e38d65f.png)
- And we only need to find out every degree of derivatives, and we will get:
![image](https://user-images.githubusercontent.com/14041622/42206703-7bdcc7b0-7eda-11e8-8be3-7aa7591f902e.png)
- So the Taylor polynomial then is:
![image](https://user-images.githubusercontent.com/14041622/42206818-cdede50c-7eda-11e8-8c4c-0bff77d285d1.png)



