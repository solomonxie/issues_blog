# Calculus Basics 微积分基础
> Mainly some basic Calculus knowledges for Machine Learning

## Study resources
- [ ] [Khan academy: AP Calculus AB](https://www.khanacademy.org/mission/ap-calculus-ab)
- [ ] [Mathispower4u](http://www.mathispower4u.com/calculus.php)
- [ ] [Kristan King: Calculus I](https://www.youtube.com/playlist?list=PLJ8OrXpbC-BOYyyC-Gunxrh-jYnSfsQy0)
- [ ] [Kristan King: Calculus II](https://www.youtube.com/playlist?list=PLJ8OrXpbC-BMdeuQfJDVRJ5DPMduSzVow)
- [ ] [Kristan King: Calculus III](https://www.youtube.com/playlist?list=PLJ8OrXpbC-BMObozItpbiZ8f2pjf3qS9M)
- [ ] [The Organic Chemistry Tutor](https://www.youtube.com/playlist?list=PL0o_zxa4K1BWYThyV4T2Allw6zY0jEumv)
- [ ] [MIT OCW 18.01SC: Single Variable Calculus](https://ocw.mit.edu/courses/mathematics/18-01sc-single-variable-calculus-fall-2010/index.htm)
- [ ] [MIT OCW 18.02SC: Multivariable Calculus](https://ocw.mit.edu/courses/mathematics/18-02sc-multivariable-calculus-fall-2010/)

## Practice To-do List (Linked with Unit tests)
- [x] [Limits and continuity](https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-continuity/modal/test/ab-limits-continuity-unit-test)
- [x] [Derivatives introduction](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro/modal/test/ab-derivative-intro-unit-test)
- [x] [Derivative rules](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/modal/test/ab-derivative-rules-unit-test)
- [x] [Advanced derivatives](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-advanced/modal/test/ab-derivatives-advanced-unit-test)
- [ ] [Existence theorems](https://www.khanacademy.org/math/ap-calculus-ab/ab-existence-theorems/modal/test/ab-existence-theorems-unit-test)
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
And the entire Calculus is built upon this concept.


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
> Simply saying, it's just the SLOPE of ONE POINT of a graph (line or curves or anything).

[Refer to Mathsisfun: Introduction to Derivatives](https://www.mathsisfun.com/calculus/derivatives-introduction.html)

![image](https://user-images.githubusercontent.com/14041622/40104999-4f4ccb18-5924-11e8-9baf-d9e43e3e1cd8.png)


A Derivative, is the `Instantaneous Rate of Change`, which's related to the `tangent line` of a point, instead of a secant line to calculate the Average rate of change.

“Derivatives are the result of performing a differentiation process upon a function or an expression. ”

## `Derivative notations`

[Refer to Khan academy article: Derivative notation review.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro/modal/a/derivative-notation-review)

![image](https://user-images.githubusercontent.com/14041622/40266166-d90e5e1a-5b78-11e8-9fdf-20e72b432012.png)

### `Lagrange's notation`
In Lagrange's notation, the derivative of `f(x)` expressed as `f'(x)`, reads as `f prime of x`.

### `Leibniz's notation`
In this form, we write `dx` instead of `Δx heads towards 0`.
And `the derivative of` is commonly written as: 
![image](https://user-images.githubusercontent.com/14041622/40105095-9470659c-5924-11e8-8e8d-8916bef4c995.png)

> For memorizing, just see `d` as `Δ`, reads `Delta`, means change. So `dy/dx` means `Δy/Δx`. Or it can be represent as `df / dx` or `d/dx · f(x)`, whatever.

![image](https://user-images.githubusercontent.com/14041622/40105113-9d98cdd0-5924-11e8-86a2-e918c0109b23.png)

![image](https://user-images.githubusercontent.com/14041622/40102277-a5ba5b26-591c-11e8-9d8f-ecdb59db5b69.png)

### `How to understand dy/dx`

This is a review from "the future", which means while studying Calculus, you have to come back constantly to review what the `dy/dx` means.  ---- It's just so confusing.
Without fully understanding the `dy/dx`, you will be lost at topics like `Differentiate Implicit functions`, `Related Rates` and such.

![image](https://user-images.githubusercontent.com/14041622/40266233-1868f164-5b7a-11e8-9516-712cd539fd91.png)


## `Tangent line & Secant line`

- The `secant line` is drawn to connect TWO POINTS, and gets us the `Average Rate of Change` between two points.
- The `Tangent line` is drawn through ONE POINT, and gets us the `Rage of change at the exact moment`.

As for the `secant line`, its interval gets smaller and smaller and APPROACHING to `0` distance, it actually is a process of calculating `limits` approaching `0`, which will get us the `tangent line`, that been said, is the whole business we're talking about: the `Derivative`, the `Instantaneous Rate of Change`.

![image](https://user-images.githubusercontent.com/14041622/40102814-125b24e4-591e-11e8-9d6d-f51e0fc85ee6.png)

![image](https://user-images.githubusercontent.com/14041622/40102982-8c9e92c2-591e-11e8-9893-6f4d4c7fc876.png)

![secant to tangent animation](https://user-images.githubusercontent.com/14041622/40102854-2ef65b6e-591e-11e8-8041-a9e7a4b58b40.gif)




# `Differentiability`
> "If the point of a function IS differentiable, then it MUST BE continuous at the point."

Example of NOT `differentiable` points:
![image](https://user-images.githubusercontent.com/14041622/40107341-8e16a390-592a-11e8-9d9a-82a01c2c64e1.png)

You can see, if the point DOES NOT have `limit`, it's NOT DIFFERENTIABLE. 
In another word, the point is not CONTINUOUS, it's `Jump Discontinuity`, or `Removable Discontinuity`, or any type of discontinuities.

## Not differentiable situations
- Vertical Tangent (∞)
- Not Continuous
- Two sides' limits are different

![image](https://user-images.githubusercontent.com/14041622/40108012-64c1e426-592c-11e8-99c9-357d59ee9a87.png)



# `Derivative equation`
The idea of derivative equation is quite simple: **The LIMIT of the SLOPE.**

> The slope is equal to `change in Y / change in X`. 
So for a point `a`, we IMAGINE we have another near point which lies on the SAME LINE with `a`, 
and since we have TWO POINTS now, 
we can then let their `Y-value Change` divided by their `X-value Change` to get the slope.

There're two equations for calculating derivative at a point, and the only different thing is how to express the IMAGINARY POINT with respect to the point `a`, it could either be `x` or `a+h` :

![image](https://user-images.githubusercontent.com/14041622/40187586-70e7343c-5a2a-11e8-83ab-e36804921b73.png)
or:
![image](https://user-images.githubusercontent.com/14041622/40187604-78b086b4-5a2a-11e8-8539-76872a76996e.png)


## `How to calculate derivative`
Strategy:
- Determine if it's **CONTINUOUS** at this point, by:
    - See if the point is defined in the interval
    - Calculate **LIMITS** of both RIGHT SIDE and LEFT SIDE of the point.
    - If two sides' limits are the same, then it's continuous. Otherwise it's discontinuous.
- Determine if it's **DIFFERENTIABLE** (Actually is the process of getting its **derivative**):
    - Apply Derivative equation to get both RIGHT SIDE LIMIT and LEFT SIDE LIMIT.
    - If two sides' limits are the same, then that value is the **Derivative** at the point. If not, then it's NOT DIFFERENTIABLE.

Example:
![image](https://user-images.githubusercontent.com/14041622/40156524-990fb1fe-59cc-11e8-939c-104e910309ab.png)
Solve:
- See that the point `3` is defined in the interval.
- Left side limit of the point, is using the first equation, and gets the `lim g(x) = -7`
- Right side limit of the point, is using the second equation, and gets the `lim g(x) = -7`
- Limits of both sides are the SAME, so it's continuous, and let's see if it's differentiable.
- Apply the derivative equation for both Left side  & Right side:
![image](https://user-images.githubusercontent.com/14041622/40156768-197072c4-59ce-11e8-9a2f-d9e09cd354c7.png)
- Both sides' limits exists but not that same, so it's not differentiable.

Example2:
![image](https://user-images.githubusercontent.com/14041622/40156269-fa328364-59ca-11e8-97fa-af21bfa10de9.png)
Solve:
- See that the point `-1` is defined in the interval.
- Left side limit of the point, is using the first equation, and gets the `lim g(x) = 1`
- Right side limit of the point, is using the second equation, and gets the `lim g(x) = 4`
- Limits of both sides are NOT SAME, so it's not continuous, then of course not differentiable.


# `Local linearity & Linear approximation`
> `Local linearity` is for approximating of a point's value by its near known point.

Just think of a curve, a good way to approximate its Y-value, is to find another known point near it, and make a line connecting two points, then gets the value by linear equation.

[Refer to Khan academy lecture.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-intro/modal/v/local-linearization-intro)

![image](https://user-images.githubusercontent.com/14041622/40158438-1ff4586e-59d7-11e8-901f-b76764884a83.png)

![image](https://user-images.githubusercontent.com/14041622/40158363-b07acc02-59d6-11e8-8d62-76ab8643c7c9.png)


Example: 
![image](https://user-images.githubusercontent.com/14041622/40158643-2fb7a9da-59d8-11e8-9ca0-956bf405ff79.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/40158702-81d93242-59d8-11e8-87ad-9622f18ddbc7.png)




# Basic Differentiation Rules

![image](https://user-images.githubusercontent.com/14041622/40227636-a305cc52-5ac1-11e8-9fbe-ac7e11dd4a6f.png)

[Refer to Math is fun: Derivative Rules](https://www.mathsisfun.com/calculus/derivatives-rules.html)

## Derivative of Single Common Functions
Functions | Function | Derivative
-- | -- | --
Constant | c | 0
Line | x | 1
        | ax | a
Square | x² | 2x
Square Root | √x | ![image](https://user-images.githubusercontent.com/14041622/40228460-eca5310c-5ac3-11e8-91c1-1ef393f60202.png)
Exponential | eˣ | eˣ
                     | aˣ | aˣ · ln(a)
Logarithms | ln(x) | 1/x
                    | loga(x) | 1 / (x·ln(a))
Trigonometry (x is in radians) | sin(x) | cos(x)
                                                   | cos(x) | −sin(x)
                                                   | tan(x) | sec²(x)
Inverse Trigonometry | sin⁻¹(x) | 1/√(1−x²)
                                     | cos⁻¹(x) | −1/√(1−x²)
                                     | tan⁻¹(x) | 1/(1+x²)



## Common Rules for multiple functions
Rules | Function | Derivative
-- | -- | --
With constant | c·f | c·f’
Power Rule | xⁿ | n·xⁿ⁻¹
Sum Rule | f + g | f’ + g’
Difference Rule | f - g | f’ − g’
Product Rule | f · g | fg’ + f’ g
Quotient Rule | f / g | (f’g − g’f ) / g²
Reciprocal Rule | 1 / f | −f’ / f²
Chain Rule | f(g(x)) | f’(g(x)) · g’(x)



# `Chain Rule`
> One of the **core principles** in Calculus is the Chain Rule.

![image](https://user-images.githubusercontent.com/14041622/40289431-ce3b8652-5cea-11e8-9aba-c40a24f19bdd.png)

[Refer to Khan academy article: Chain rule](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/modal/a/chain-rule-review)

It tells us how to differentiate `Composite functions`.

![image](https://user-images.githubusercontent.com/14041622/40225236-178dc84c-5abb-11e8-8bbf-098d8df7d3b9.png)

**It must be composite functions, and it has to have `inner & outer` functions, which you could write in form of `f(g(x))`.**
![image](https://user-images.githubusercontent.com/14041622/40225120-c6ddf174-5aba-11e8-8b1b-2859c7eeb749.png)

### Common mistakes
- Not recognizing whether a function is composite or not
- Wrong identification of the inner and outer function
- **Forgetting to multiply by the derivative of the inner function**
- Computing `f(g(x))` wrongly:
![image](https://user-images.githubusercontent.com/14041622/40225381-7744459a-5abb-11e8-848d-9a28c39db99c.png)

### How to identify Composite functions
> Seems a basic algebra101, but actually a quite tricky one to identify.

[Refer to Khan lecture: Identifying composite functions](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/modal/v/recognizing-compositions-of-functions)

The core principle to identify it, is trying to re-write the function into a nested one: `f(g(x))`. If you could do this, it's composite, if not, then it's not one.

Examples:
![image](https://user-images.githubusercontent.com/14041622/40226233-add7f910-5abd-11e8-8522-853ca335a2a1.png)
It's a composite function, which the inner is `cos(x)` and outer is `x²`.

![image](https://user-images.githubusercontent.com/14041622/40226318-f2bbe668-5abd-11e8-9f47-405b4476c054.png)
It's a composite function, which the inner is `2x³-4x` and outer is `sin(x)`.

![image](https://user-images.githubusercontent.com/14041622/40226383-24b4fe48-5abe-11e8-9cb0-9c0bda203c89.png)
It's a composite function, which the inner is `cos(x)` and outer is `√(x)`.

## `Two forms of Chain Rule`

The general form of Chain Rule is like this:
![image](https://user-images.githubusercontent.com/14041622/40289487-313c6d84-5ceb-11e8-85a9-2aee2108aa60.png)

But the Chain Rule has another **more commonly used** form:
![image](https://user-images.githubusercontent.com/14041622/40289493-3ddcdfa6-5ceb-11e8-9771-2d93d210a85b.png)

Their results are exactly the same.
It's just some people find the first form makes sense, some more people find the second one does.



Example:
![image](https://user-images.githubusercontent.com/14041622/40268880-38210900-5ba8-11e8-8e45-3691ad3b5163.png)
Solve:
[Refer to Symbolab worked example.](https://www.symbolab.com/solver/step-by-step/%5Cfrac%7Bd%7D%7Bdx%7D%5Cleft(sqrt%5Cleft(3cos%5E%7B3%7D%5Cleft(x%5Cright)%5Cright)%5Cright))


# `Derivatives of Trig functions`

![image](https://user-images.githubusercontent.com/14041622/40227555-69eb9e74-5ac1-11e8-98cf-75d6088b5b4f.png)

## Reminder of Trig identities & Unit circle values
```py
# Reciprocal and quotient identities
tan(θ) = sin(θ) / cos(θ)
csc(θ) = 1/sin(θ)
sec(θ) = 1/cos(θ)
cot(θ) = 1/tan(θ)
```

[Refer to previous note of all trig identities.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-377684464)

![unit circle](https://user-images.githubusercontent.com/14041622/38487029-724164d8-3c11-11e8-9913-17a6da068090.png)




# `Implicit differentiation`
> Bit hard to understand it in the first place.

![image](https://user-images.githubusercontent.com/14041622/40266041-b0ae9720-5b76-11e8-823f-33d3935a9124.png)


## `What is Implicit & Explicit Function`
[Refer to video by Krista King: What is implicit differentiation?](https://www.youtube.com/watch?v=GpWCFoCznGI)

- `Explicit function`: it's the normal function we've seen a lot before, which's in the form of `y = x....`
- `Implicit function`: it't NOT YET in the general form of a function and not easily separated, like `x² + y² = 1`

So knowing how to differentiate an `implicit function` is quite helpful when we're dealing with those NOT EASILY SEPARATED functions.

## `How to Differentiate Implicit function`

[Refer to video: Use implicit differentiation to find the second derivative of y (y'') (KristaKingMath)](https://www.youtube.com/watch?v=MzwcOw27ZRE)
[Refer to video by The Organic Chemistry Tutor: Implicit Differentiation Explained - Product Rule, Quotient & Chain Rule - Calculus](https://www.youtube.com/watch?v=LGY-DjFsALc)

[Refer to Symbolab: Implicit Derivative Calculator](https://www.symbolab.com/solver/implicit-derivative-calculator/implicit%20derivative%20%5Cfrac%7Bdy%7D%7Bdx%7D%2C%20x%5E%7B2%7D%2Bxy%2By%5E%7B3%7D%3D0)

Assume you are to differentiate `Y` **WITH RESPECT** to `X`, written as `dy/dx`:
- Differentiate terms with `X` as normal
- Differentiate terms with `Y` as the same to `X`, BUT multiply by `(dy/dx)`
- Differentiate terms **MIXED** with `X & Y` by using `Product Rule`, then differentiate each term.

### How to differentiate `Y` with respect to `X`
![image](https://user-images.githubusercontent.com/14041622/40266769-864f311c-5b83-11e8-9f35-f6087c87e85d.png)

### How to differentiate term MIXED with both `X & Y`
![image](https://user-images.githubusercontent.com/14041622/40266809-34b13dfe-5b84-11e8-8981-cd6b0349fb80.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/40271196-87e4a61c-5bcc-11e8-9b9a-bfe940549680.png)
Solve:
[Refer to Symbolab: Implicit Derivative Calculator](https://www.symbolab.com/solver/implicit-derivative-calculator/implicit%20derivative%20%5Cfrac%7Bdy%7D%7Bdx%7D%2C%20x%5E%7B2%7D%2Bxy%2By%5E%7B3%7D%3D0)

- Treat `y` as `y(x)`
- Apply the Sum Rule:
![image](https://user-images.githubusercontent.com/14041622/40271287-c61ce952-5bcd-11e8-92d4-3ed3c706cd2f.png)
- Apply the normal rules to `X term`, and
- Apply the Product Rule to the `Mixed term`, and
- Apply the Chain Rule to the `Y term`:
![image](https://user-images.githubusercontent.com/14041622/40271324-5448fa9a-5bce-11e8-9d89-f30ad9a81658.png)
- Operate the equation and **solve for `dy/dx`**, and get:
![image](https://user-images.githubusercontent.com/14041622/40271337-94837f9a-5bce-11e8-8861-3b894ff5f0b9.png)



# `Related Rates`

Just so you know, `related rates` is actually the **Application** of `Implicit Differentiation` by using Chain Rule in the form of `dy/dx = dy/du * du/dx`.

![image](https://user-images.githubusercontent.com/14041622/40288873-ff4bacf2-5ce7-11e8-9729-fb9d1bd1d9f2.png)

Btw, at Khan academy it's called the `Differentiate related functions`.

[Refer to Khan lecture.](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-advanced/modal/v/differentiating-related-functions-intro)
[Refer to video by KristaKingMath: Related rates](https://www.youtube.com/watch?v=Vi5KBiXg0Co)
[Refer to video by The Organic Chemistry Tutor: Introduction to Related Rates](https://www.youtube.com/watch?v=I9mVUo-bhM8&t=0s&index=78&list=PL0o_zxa4K1BWYThyV4T2Allw6zY0jEumv)

### Example
![image](https://user-images.githubusercontent.com/14041622/40301867-f537cfd8-5d1f-11e8-87d7-308a2ebb320b.png)
Solve:
- First thing we need to find the **RIGHT** equation of Chain rule. Since it's asking us to find `dy/dt`, so we will re-write it to this one to form an equation:
![image](https://user-images.githubusercontent.com/14041622/40303119-18105648-5d24-11e8-9825-91f14654faa6.png)
- Then since we've given the `dx/dt = -3`, we only need to find out the `dy/dx` to get the result.
- We've got an equation of `x & y`, regardless whom it's respecting to. So we can do either `Implicit or Explicit differentiation` to the equation `y²=7x+1`, with respect to `y`:
![image](https://user-images.githubusercontent.com/14041622/40303322-e0535cc2-5d24-11e8-9176-d082e0c68a70.png)
- Use the implicit differentiation method, we got the `dy/dx = 7/2y`
- And since `y=6`, so `7/2y = 7/12`
- Back to the Chain Rule equation, we get `dy/dt = 7/12 · (-3) = -7/4 = -1.75`



### Example
![image](https://user-images.githubusercontent.com/14041622/40303447-5c3a1196-5d25-11e8-9239-b95c743b8be0.png)
Solve:
- Remind you that, in this problem, it's **NOT** respecting to `x` anymore, so you need to change mind before getting confused.
- First thing we need to find the **RIGHT** equation of Chain rule. Since it's asking us to find `dx/dt`, so we will re-write it to this one to form an equation:
![image](https://user-images.githubusercontent.com/14041622/40303475-78622dd6-5d25-11e8-9912-bd3744e514e9.png)
- Then since we've given the `dy/dt = -0.5`, we only need to find out the `dx/dy` to get the result.
- We've got an equation of `x & y`, regardless whom it's respecting to. It seems easier to **differentiate** explicitly:
![image](https://user-images.githubusercontent.com/14041622/40303547-c07bde32-5d25-11e8-8e6c-2c2d532a45b8.png)
- Then we use `d/dx` to differentiate the equation to get: `dx/dy = y⁻² = (0.2)⁻² = 25`
- Back to the Chain Rule equation, we get `dx/dt = dx/dy · dy/dt = 25 * (-0.5) = -12.5`.

### Example
![image](https://user-images.githubusercontent.com/14041622/40303696-6b528324-5d26-11e8-879e-e923697a8eaa.png)
Solve (Same with above examples):
- Form an equation: 
![image](https://user-images.githubusercontent.com/14041622/40303793-e113564c-5d26-11e8-94b8-fce0631e50b6.png)
- `dx/dt` has been given equals to `5`, so just to find out `dy/dx`:
![image](https://user-images.githubusercontent.com/14041622/40303865-20a8bfd6-5d27-11e8-9a70-e1d51f5451cf.png)
- And get:
![image](https://user-images.githubusercontent.com/14041622/40303898-3e7eac96-5d27-11e8-908d-e492d292c78b.png)
![image](https://user-images.githubusercontent.com/14041622/40304158-238d9892-5d28-11e8-8588-c1923d4c33b4.png)
- Now let's see what is `sin(x)` equal to:
![image](https://user-images.githubusercontent.com/14041622/40304151-1b93eee8-5d28-11e8-970b-04df4099abcb.png)
- All done.



# `Second derivatives`
The second derivative of a function is simply the derivative of the function's derivative.

Notation:
Leibniz's notation for second derivative is:
![image](https://user-images.githubusercontent.com/14041622/40231289-2c34f3da-5acd-11e8-9348-2ba4fb04a2aa.png)
![image](https://user-images.githubusercontent.com/14041622/40231293-344c4e10-5acd-11e8-886d-39457c2efb2d.png)



# `Derivative of Inverse functions`

![image](https://user-images.githubusercontent.com/14041622/40294394-f6786cb2-5d07-11e8-8d47-1d71456b4d2f.png)

It's developed by the Chain rule:
![image](https://user-images.githubusercontent.com/14041622/40294502-6f80d4c8-5d08-11e8-82a5-5b91e20a2e7f.png)

## `Derivative of Inverse Trig functions`
![image](https://user-images.githubusercontent.com/14041622/40313487-801adde8-5d48-11e8-8260-a631d6be6c6a.png)



## `Derivative of exponential functions`
> It's save a lot of time of life not to dig in how mathematicians developed these formulas.
If you do want to, [refer to Khan's lecture: Exponential functions differentiation intro](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivatives-advanced/modal/v/exponential-functions-differentiation-intro)

Reminder: **Don't forget it's a `composite function` and you need to apply the chain rule.**

![image](https://user-images.githubusercontent.com/14041622/40298682-8ae4c95a-5d16-11e8-8115-1363d8ae637c.png)

## `Derivative of logarithm functions`
![image](https://user-images.githubusercontent.com/14041622/40300440-d3893a06-5d1b-11e8-9103-4461535d8023.png)

## Examples
Find the derivative of:
![image](https://user-images.githubusercontent.com/14041622/40298914-3a2b92f4-5d17-11e8-884e-be6cf50eb431.png)
Solve:

![image](https://user-images.githubusercontent.com/14041622/40298961-6157e9e0-5d17-11e8-8f73-56ca14655ccf.png)
