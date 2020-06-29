#  ❖ 「Integral Calculus」 basics

Integral calculus is a process to calculate the **`AREA`** between a function and the X-axis (or Y-axis).

## Core idea of 「Integral Calculus」

[Refer to Khan academy: Introduction to integral calculus](https://www.khanacademy.org/math/ap-calculus-bc/bc-accumulation-riemann-sums/modal/v/introduction-to-integral-calculus)

![image](https://user-images.githubusercontent.com/14041622/40873054-ed0e9f42-668b-11e8-8860-0e4778f2c041.png)

## 「Riemann Sums」

A Riemann sum is an **approximation** of the area under a curve by dividing it into multiple simple shapes (like rectangles or trapezoids).


### 「Riemann Sums」 Notation

[Refer to Khan academy: Definite integral as the limit of a Riemann sum](https://www.khanacademy.org/math/ap-calculus-bc/bc-accumulation-riemann-sums/modal/v/riemann-sums-and-integrals)

![image](https://user-images.githubusercontent.com/14041622/40902169-a17a49a2-6805-11e8-9214-bae6f044caa0.png)

The letter `ʃ` (reads as "esh" or just "integral") is called `the Integral symbol/sign`.



### Calculate 「Riemann Sums」

![image](https://user-images.githubusercontent.com/14041622/46062247-c68cad80-c19b-11e8-9bf2-ee2316863301.png)

Finding `𝚫x`:
It's meant to get **HOW MANY** rectangles we're to sum.
![image](https://user-images.githubusercontent.com/14041622/46062301-f3d95b80-c19b-11e8-877e-5b4026a41f08.png)

Finding indices `m & n`:
It's meant to find the `i` for `Σ` sums:
- For `Left Sums` or `Midpoint Sums`: `i` starts from `0` ends with `subdivisions - 1`
- For `Right Sums`: `i` starts from `1` ends with `subdivisions`

Finding `xi`:
With equally spaced points (left/right/mid), the `xi` is a **`Geometric series`** of those points, which the **rate** is the `𝚫x`.
We're gonna find the right pattern/equation for `xi`, so that we can plug `xi` into `f(x)`.

Finding `f(xi)`:
Just to plug in the Geometric series expression of `xi` into `f(x)`, 
and make it as **a function in terms of i**.

### 「Left Riemann Sums」 & 「Right Riemann Sums」 Approximation

[Refer to Maths is fun: Integral Approximations](https://www.mathsisfun.com/calculus/integral-approximations.html)

- `Left Riemann Sum`: take the **Left boundary value** of Δx to be the rectangle's **height**.
![image](https://user-images.githubusercontent.com/14041622/46060851-2765b700-c197-11e8-9fa2-4c90bf6b5fa3.png)
- `Right Riemann Sum`: take the **Right boundary value** of Δx to be the rectangle's **height**.
![image](https://user-images.githubusercontent.com/14041622/46060951-757aba80-c197-11e8-81a1-e99d5880ceb3.png)


![image](https://user-images.githubusercontent.com/14041622/40884539-ed5aff60-6747-11e8-80ee-d1139810c0c2.png)

As you can see, they would be either Over-estimated or Under-estimated. Neither of these approximations would be called a good one, normally.

### 「Midpoint Sums」 Approximation

It's an enhancement to the Left sums and Right sums, it takes the midpoint value, and sometimes makes better approximation.

![image](https://user-images.githubusercontent.com/14041622/46063191-a7434f80-c19e-11e8-8f51-510cb11fbd1f.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/46061052-d1454380-c197-11e8-8232-53e60b6929dc.png)
Solve:



### Example
![image](https://user-images.githubusercontent.com/14041622/41024809-d75ede72-69a2-11e8-9238-504efa457e81.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/41024853-ee9fcd30-69a2-11e8-9f9b-513e17902e34.png)

- It's easy to find the `Δx=2`.
- Then let's find the `f(x𝖎)`. It's actually a progress to find the `Arithmetic Sequence`.
- So the sequnce is `S(𝖎) = a + 𝖎·Δx = 2 + 2𝖎`, where `a` represents the first `x` value which is `2`.
- So `x𝖎 = S(𝖎) = 2+2𝖎`
- Takes it back to the function and gets: `f(x𝖎) = |2+2i-5| = |2i -3|`

### Example
![image](https://user-images.githubusercontent.com/14041622/42703162-4237d7f8-86fe-11e8-9ee6-ef0b6dbdc86e.png)
Solve:


### Example
![image](https://user-images.githubusercontent.com/14041622/42704481-86769edc-8702-11e8-830a-e3d38e6d69de.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/42704699-7788697c-8703-11e8-95a9-705855e85e17.png)
![image](https://user-images.githubusercontent.com/14041622/42704713-80454bfc-8703-11e8-88bb-2812c0ec256a.png)



## How to calculate 「Riemann Sums」

[Refer to Khan academy:  Rewriting definite integral as limit of Riemann sum](https://www.khanacademy.org/math/ap-calculus-bc/bc-accumulation-riemann-sums/modal/v/rewriting-definite-integral-as-limit-of-riemann-sum)

![image](https://user-images.githubusercontent.com/14041622/40902699-810e7538-6807-11e8-93bd-78c9da47b96a.png)


[Refer to the Map of Integration: mrozarka.com](http://stem.mrozarka.com/calculus-1/units/unit-4)
![image](https://user-images.githubusercontent.com/14041622/41091509-474ef4f2-6a79-11e8-887e-d1de61f74aae.png)

