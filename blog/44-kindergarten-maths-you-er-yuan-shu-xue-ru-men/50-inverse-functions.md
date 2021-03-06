# `Inverse functions`

[Refer to math is fun: `Inverse functions`](http://www.mathsisfun.com/sets/function-inverse.html)

> If a `function` means `Map to`, then `inverse function` means `Map back`. `f(x)=y` maps `x` to `y`, then `f'(y)=x` maps `y` back to `x`. Note that `f'` is the inverse function of `f`.

[Khan notes.](https://www.khanacademy.org/math/algebra2/manipulating-functions/verifying-that-functions-are-inverses/a/verifying-inverse-functions-by-composition)

When we have a function, it means we have a `mapping rule`. In this rule, we can map `x` to `y`, expressed as `f(x) = y`. But if we know `y`, how can we map back to `x`? 


## Identify inverse functions by composition

[Refer to khan academy: Identify inverse functions by composition](https://www.khanacademy.org/math/algebra2/manipulating-functions/verifying-that-functions-are-inverses/a/verifying-inverse-functions-by-composition)

> To verify two functions are inverse, we can compose them.

If `f(g(x))` = `g(f(x))`, then they are inverse.

## `invertible functions`

[Refer to khan academy: `invertible functions`](https://www.khanacademy.org/math/algebra2/manipulating-functions/invertible-functions/a/intro-to-invertible-functions)

> Not all functions have inverses. Those who do are called "invertible."

If a function `f(x)` maps `x` to `y`, and another function `f'(y)` can help us mapping `y` back to `x`, 
then the function `f(x)` is `INVERTIBLE`. 
If not, then it is NOT invertible.

### `Horizontal line test`
On the graph of function `f(x)`, if we can draw a `horizontal line` and ends up touches the graph **more than once**, we could say the function is **NOT INVERTIBLE**.

![image](https://user-images.githubusercontent.com/14041622/37600727-1d9b69a0-2bc3-11e8-8aeb-fc1d9cff3400.png)



## Inverse trig function word problems

### EXAMPLE 
![image](https://user-images.githubusercontent.com/14041622/38241148-131e56ac-3764-11e8-899c-e2cf987b8d5d.png)
Solve:
- Set equation `Y(t) = −80`
- Simplify equation and solve for all possible solutions:
    - `base solution` as `θ = 1.7911 + 2πn` 
    - Use trig identity `cos(θ) = cos(2π - θ)` to get second solution as `θ = 4.485 + 2πn`.
- Replace θ with the expression of `t` and solve for t:
    - `t*2π/3 = 1.7911 + 2πn` , and solve it to get `t = 0.9 + 3n`
    - `t*2π/3= 4.485 + 2πn`, and solve it to get  `t = 2.1 + 3n`
- Study the graph of trig function (review the `Sinusoidal Functions`), get informations:
    - Max at `(0, -31)`
    - Min at `(1.5, -111)`
    - Period is `2π/(2π/3)` and get the period is `3`
- According to the situation we know:
    - It passed the `1st Min` and is before the `2nd Max`
    - So it's over `1.5 sec` at Bottom and not yet `3 sec` at top.
- So within the range (1.5, 3), filter out invalid solution, `2.1` is the answer.



### EXAMPLE
![image](https://user-images.githubusercontent.com/14041622/38242513-95720c72-3767-11e8-889b-7699b14bf24d.png)
Solve:
- Simplify and solve to get solutions:
    - `θ = 0.423 + 2πn`
    - `θ = 2.718 + 2πn`, (with trig identity `sin(θ) = sin(π-θ)` when θ is positive)
- Replace θ with expression of t:
    - `t = 24.57 + 365n`
    - `t = 157 + 365n`
- Study the graph of trig function and get informations:
    - Period: 365
    - Y-intersect (Midline) at: `(0, 728)`
    - Max (right after Y-axis) at: `(365/4, 780)`
- Since `750` is not yet the Max `780`, so it's EARLIER than `365/4` aka.`91.25`.
- Filter out the `157` which is later than `91.25`, so the `24.57` is the answer.



### EXAMPLE
![image](https://user-images.githubusercontent.com/14041622/38239728-1cd36bc8-3760-11e8-9f13-882819c626e1.png)
Solve:
- Set equation to `I(t)=5.2`
- Simplify equation to:
![image](https://user-images.githubusercontent.com/14041622/38239775-4173612c-3760-11e8-8f22-e955615d8640.png)
- Get `θ ≃ 0.9273 Rad`
- Get First solution:
![image](https://user-images.githubusercontent.com/14041622/38239979-dca4ca32-3760-11e8-84a8-2741f9d29da0.png)
![image](https://user-images.githubusercontent.com/14041622/38239899-a696dade-3760-11e8-8613-0dd8f9f22976.png)
- Use the trig identity for second solution: `cos(θ) = cos(2π−θ)`.
![image](https://user-images.githubusercontent.com/14041622/38240038-fa9c03fc-3760-11e8-932c-2e9547af26b2.png)
![image](https://user-images.githubusercontent.com/14041622/38240043-fd76168a-3760-11e8-87d7-86ba3c8a7b92.png)
- The answer for SECOND TIME it hits 5.2 is `311 days`.


## Inverse trig function all possible solutions

### Example
> Find all possible solutions: `cos(x)=0.15`

Solve:
![image](https://user-images.githubusercontent.com/14041622/38292383-20aaf1ba-3816-11e8-9065-9779ec38840b.png)
![image](https://user-images.githubusercontent.com/14041622/38292407-367f9d7e-3816-11e8-8265-3d4e3c716b8f.png)
![image](https://user-images.githubusercontent.com/14041622/38292411-3a32e1c4-3816-11e8-8302-1d121f750ad9.png)

