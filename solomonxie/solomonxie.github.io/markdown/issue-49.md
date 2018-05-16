# Calculus Basics 微积分基础
> Mainly some basic Calculus knowledges for Machine Learning

## Study resources
- [ ] [Khan academy: AP Calculus AB](https://www.khanacademy.org/mission/ap-calculus-ab)
- [ ] [Mathispower4u](http://www.mathispower4u.com/calculus.php)

## Practice To-do List (Linked with Unit tests)
- [x] [Limits and continuity](https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-continuity/modal/test/ab-limits-continuity-unit-test)
- [ ] [Derivatives introduction](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro/modal/test/ab-derivative-intro-unit-test)
- [ ] Derivative rules
- [ ] Advanced derivatives
- [ ] Existence theorems
- [ ] Using derivatives to analyze functions
- [ ] Applications of derivatives
- [ ] Accumulation and Riemann sums
- [ ] Antiderivatives and the fundamental theorem of calculus
- [ ] Differential equations
- [ ] Applications of definite integrals

## Study goals 
- [ ] Limits
- [ ] Derivatives




# `Limits`
> Limits are all about approaching.


# `Function's Continuity`

Pencil Definition: 
**IF YOU CAN DRAW THE FUNCTION WITH A PENCIL WITHOUT PICKING UP THE PENCIL, THEN THE FUNCTION IS A CONTINUOUS FUNCTION**


# Strategy in finding Limits

[Refer to Khan academy.](https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-continuity/ab-limit-strategy/a/limit-strategies-flow-chart)

![image](https://user-images.githubusercontent.com/14041622/40041663-65775634-5851-11e8-9382-e6de982dc496.png)



# `Limits at infinity`

No matter why kinds of Limits you're looking for, 
to understand it better, 
the best way is to read the `Step-by-Step Solution` from `Symbolab`:
[Limit Calculator from Symbolab.](https://www.symbolab.com/solver/limit-calculator/%5Clim_%7Bx%5Cto%5Cinfty%7D%5Cleft(%5Cfrac%7B6x%5E%7B2%7D-x%7D%7B%5Csqrt%7B9x%5E%7B4%7D%2B7x%5E%7B3%7D%7D%7D%5Cright))

## `Rational functions`
> The KEY point is to look at the powers & coefficients of Numerator & Dominator.
Just the same with `Finding the Asymptote`.

[Refer to previous note on the `How to find Asymptote`](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-374894945).

![image](https://user-images.githubusercontent.com/14041622/40049084-5303489a-5866-11e8-9ba5-d2ffe6045955.png)

Example:
![image](https://user-images.githubusercontent.com/14041622/40048425-c4959c30-5864-11e8-947d-cd5c59375f72.png)
Solve:


## `Quotients with square roots`
> The KEY point is to calculate both `numerator & dominator`, then calculate the limit of EACH term with in the square root.

Example:
![image](https://user-images.githubusercontent.com/14041622/40047707-c2a05052-5862-11e8-805a-5d8c6ca98d47.png)
Solve:
[Refer to Symbolab step-by-step solution.](https://www.symbolab.com/solver/limit-calculator/%5Clim_%7Bx%5Cto%5Cinfty%7D%5Cleft(%5Cfrac%7B6x%5E%7B2%7D-x%7D%7B%5Csqrt%7B9x%5E%7B4%7D%2B7x%5E%7B3%7D%7D%7D%5Cright))
- Divide by **highest** dominator power to get:
![image](https://user-images.githubusercontent.com/14041622/40047885-48fdaf46-5863-11e8-85b8-118c09272fbf.png)
- Calculate separately the limit of `Numerator` & `Dominator`:
![image](https://user-images.githubusercontent.com/14041622/40047966-896c2990-5863-11e8-924e-8898d747fafd.png)
- Calculate the `Square root`: Need to find limits for **EACH** term **inside** the square root.
![image](https://user-images.githubusercontent.com/14041622/40048191-2dc755d2-5864-11e8-8733-e91ca609069f.png)
![image](https://user-images.githubusercontent.com/14041622/40048201-330160c4-5864-11e8-9b7b-b98fbae043f5.png)
![image](https://user-images.githubusercontent.com/14041622/40048216-3c8970b4-5864-11e8-8496-68e2e638df1d.png)
- Then get the result easily.

## `Quotients with trig`
> The KEY point is to apply the **`Squeeze theorem`**, and it is a MUST.

Example:
![image](https://user-images.githubusercontent.com/14041622/40047015-e86fb63a-5860-11e8-9f72-b97d62f785c2.png)
Solve:
- Know that `-1 ≦ cos(x) ≦ 1`, so we can tweak it to apply the `squeeze theorem` to get its limit.
- Make the inequality to: `3/-1 ≦ 3/cos(x)/-1 ≦ 3/1`
- Get that right side `3/-1 = -1` and left side `3/1 =1` is not equal.
- So the limit doesn't exist.

**Easier solution steps**:
- Know the inequality `-1 ≦ cos(x) ≦ 1`
- Replace `cos(x)` to ` ±1` in the equation, `3/±1`.
- Calculate limits of two sides.
- If the results are exactly the same, then the limit is the result; Otherwise the limit doesn't exist.

Example 2:
![image](https://user-images.githubusercontent.com/14041622/40047463-2181c778-5862-11e8-8658-d439cdcecf65.png)
Solve:
- Know that `-1 ≦ sin(x) ≦ 1`
- Replace `sin(x)` as `±1`
- Left side becomes `(5x+1)/(x-5)`, right side becomes `(5x-1)/(x-5)`
- Both sides' limits are `5`, so the limit exists, and is `5`.


# `All types of discontinuities`

[Refer to Mathwarehouse: What are the types of Discontinuities?](http://www.mathwarehouse.com/calculus/continuity/what-are-types-of-discontinuities.php)

## `Jump Discontinuities`
> A `Jump discontinuity` occurs at some point, the `left side limit` is DIFFERNT with the `right side limit`.

![image](https://user-images.githubusercontent.com/14041622/40050621-8b4da930-586a-11e8-909f-424af8b6c04e.png)
We see that clearly:
![image](https://user-images.githubusercontent.com/14041622/40050642-9cbaa704-586a-11e8-9c82-adc8f0032a15.png)


## `Removable Discontinuities`
> A `removable discontinuity` occurs at some point, both `left side limit` & `right side limit` are the SAME.

![image](https://user-images.githubusercontent.com/14041622/40050774-0466bc94-586b-11e8-981c-7427d765f794.png)


## `Infinite Discontinuities`
> An `Infinite Discontinuity` occurs  at some point, both `left side` & `right side` are approaching to INFINITY, which means both sides DO NOT have limits.

![image](https://user-images.githubusercontent.com/14041622/40050881-5c76418e-586b-11e8-9f03-eb66464a8730.png)


## `Endpoint Discontinuities`
> An `Endpoint Discontinuity` occurs at some point, it DOESN'T HAVE **both** sides, it only has ONE SIDE.

![image](https://user-images.githubusercontent.com/14041622/40051007-d0196e0e-586b-11e8-930a-c2f1c392a019.png)


## `Mixed Discontinuities`
![image](https://user-images.githubusercontent.com/14041622/40051076-06f92d38-586c-11e8-9d2e-415a2c6e95ad.png)



# `Analyzing functions for discontinuities: algebraic`
> If the limits of both side of some point, are EQUAL, then it's continuous at this point.

At a point `a`, for `f(x)` to be continuous at `x=a`, we need `lim(x→a)f(x) = f(a)`.

Example:
![image](https://user-images.githubusercontent.com/14041622/40051602-eb4faf88-586d-11e8-91d8-504937405601.png)
Solve:
- Got the limit of left side is `-1/2`
- Got the limit of right side is `-1/2`
- They're equal, so it's continuous at this point.


# Application of Removable Discontinuities

Example:
![image](https://user-images.githubusercontent.com/14041622/40052537-b4a9ec66-5870-11e8-8451-89d2e640f220.png)
Solve:
It's just the same with calculating the limits of both sides.


# `Derivative Basics`
> Simply saying, it's just the SLOPE of a POINT of a graph (line or curves or anything).

“Derivatives are the result of performing a differentiation process upon a function or an expression. ”

## `Derivative notations`

[Refer to Khan academy article: Derivative notation review.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro/modal/a/derivative-notation-review)

![image](https://user-images.githubusercontent.com/14041622/40072454-82645990-58a6-11e8-9c48-190f832a37cc.png)

### `Lagrange's notation`
In Lagrange's notation, the derivative of `f` expressed as `f'`.

### `Leibniz's notation`
![image](https://user-images.githubusercontent.com/14041622/40102277-a5ba5b26-591c-11e8-9d8f-ecdb59db5b69.png)

## `Tangent line & Secant line`

![image](https://user-images.githubusercontent.com/14041622/40102814-125b24e4-591e-11e8-9d6d-f51e0fc85ee6.png)

![image](https://user-images.githubusercontent.com/14041622/40102982-8c9e92c2-591e-11e8-9893-6f4d4c7fc876.png)

![secant to tangent animation](https://user-images.githubusercontent.com/14041622/40102854-2ef65b6e-591e-11e8-8041-a9e7a4b58b40.gif)
