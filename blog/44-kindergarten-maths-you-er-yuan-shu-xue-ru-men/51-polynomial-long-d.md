# `Polynomial long division`

[Refer to Wiki: `Polynomial long division`](https://en.wikipedia.org/wiki/Polynomial_long_division)

> It's very import to understand it in the first place. Once get the idea, it's easy to solve this problem.

First need to understand, 
this usually is a **`Degrading process`**.

For instance, we don't need to divide `7/13` or `2/3`, 
because the `numerator` is lower than the `dominator`. 
But we could divide `20/7` to `2 6/7`, and the `6/7` is the `remainder`.

In `polynomials division`, we don't compare the value of them, 
but we could compare the `degrees` of both parts. 
`Higher one` CAN BE divided by a `lower one`, 
and probably left over a `remainder` that even lower than the `dominator`.


There're a few main ideas act in the division process:
- `Numerator`: This polynomial usually has `higher degrees`.
- `Dominator`: This polynomial (or monomial/binomial) usually `lower degrees`.
- `Remainder`: After the `degrading` all the `higher degree` terms, left some terms can't be lower than the `dominator`'s degree, we then stop here, and call it remainder.

A normal division: 

![image](https://user-images.githubusercontent.com/14041622/37637509-27551d80-2c43-11e8-9b56-9709144ca232.png)

We can also write this division as below, which replace `R` with `+`, makes it more intuitive:

![image](https://user-images.githubusercontent.com/14041622/37637646-cf22d7e6-2c43-11e8-9b8c-4895571ab04d.png)

Same thing we can apply to the `polynomial division`, 
Assume that there's a division: 
```javascript
f(x) ÷ d(x) = q(x) with a remainder of r(x)
```
and we can rewrite it to:

![image](https://user-images.githubusercontent.com/14041622/37637592-938fa998-2c43-11e8-89ec-8379f04fee81.png)



Example: 
We got two polynomials need to be divided one by another, and we could represent it as below:

![image](https://user-images.githubusercontent.com/14041622/37610168-e1de8868-2bd9-11e8-8386-825c8f47779b.png)

By multiplying `x²` to `(x-3)`, we could get `x³ − 3x²`, which could be use to `cancel out` it from the `numerator`, to `degrade` it. 

![image](https://user-images.githubusercontent.com/14041622/37610365-5b89e81a-2bda-11e8-95e3-eda8abfe17f1.png)

After the first `degrading`, it gets a `lower degree polynomial`, 
and the `left over` is still `higher` than the dominator, 
so we can repeat the same process to do it again, 
until the `left over` is `zero` or lower than the `dominator`.

![image](https://user-images.githubusercontent.com/14041622/37611460-6222ee30-2bdd-11e8-837e-dad40895a84d.png)

### Example
![image](https://user-images.githubusercontent.com/14041622/37635362-1b67c8c2-2c36-11e8-8961-4085f0472c6f.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/37635386-441cf9ea-2c36-11e8-9bce-7bfa69cdbf8c.png)
![image](https://user-images.githubusercontent.com/14041622/37635394-4aa14776-2c36-11e8-9518-ce39188f3c84.png)




## `The Remainder Theorem`

[Refer to Math is fun](http://www.mathsisfun.com/algebra/polynomials-remainder-factor.html)

> When we divide a polynomial `f(x)` by `x − c` and the remainder is `r`, then:
`r = f(c)`.

### Example
[Practice.](https://www.khanacademy.org/math/algebra2/modal/e/remainder-theorem-of-polynomials)

![image](https://user-images.githubusercontent.com/14041622/37637143-08dcc472-2c41-11e8-9407-8d5b160a32c8.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/37637213-5d99f1ba-2c41-11e8-871d-6528d53eaea1.png)
![image](https://user-images.githubusercontent.com/14041622/37637222-68247ec0-2c41-11e8-8e02-b65a425a2892.png)


## `The factor theorem`




