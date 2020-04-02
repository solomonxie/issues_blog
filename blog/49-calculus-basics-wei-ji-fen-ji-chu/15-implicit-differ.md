#  ❖ Implicit Differentiation

> Bit hard to understand it in the first place.

![image](https://user-images.githubusercontent.com/14041622/40266041-b0ae9720-5b76-11e8-823f-33d3935a9124.png)


## What is 「Implicit」 & 「Explicit Function」

[Refer to video by Krista King: What is implicit differentiation?](https://www.youtube.com/watch?v=GpWCFoCznGI)

- `Explicit function`: it's the normal function we've seen a lot before, which's in the form of `y = x....`
- `Implicit function`: it't NOT YET in the general form of a function and not easily separated, like `x² + y² = 1`

So knowing how to differentiate an `implicit function` is quite helpful when we're dealing with those NOT EASILY SEPARATED functions.

## How to Differentiate 「Implicit function」

[Refer to video: Use implicit differentiation to find the second derivative of y (y'') (KristaKingMath)](https://www.youtube.com/watch?v=MzwcOw27ZRE)
[Refer to video by The Organic Chemistry Tutor: Implicit Differentiation Explained - Product Rule, Quotient & Chain Rule - Calculus](https://www.youtube.com/watch?v=LGY-DjFsALc)

[Refer to Symbolab: Implicit Derivative Calculator](https://www.symbolab.com/solver/implicit-derivative-calculator/implicit%20derivative%20%5Cfrac%7Bdy%7D%7Bdx%7D%2C%20x%5E%7B2%7D%2Bxy%2By%5E%7B3%7D%3D0)

Assume you are to differentiate `Y` **WITH RESPECT** to `X`, written as `dy/dx`:
- Differentiate terms with `X` as normal
- Differentiate terms with `Y` as the same to `X`, BUT multiply by `(dy/dx)`
- Differentiate terms **MIXED** with `X & Y` by using `Product Rule`, then differentiate each term.

### How to differentiate 「Y with respect to X」

![image](https://user-images.githubusercontent.com/14041622/40266769-864f311c-5b83-11e8-9f35-f6087c87e85d.png)

### How to differentiate 「term MIXED with both X & Y」

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



## 「Vertical & Horizontal Tangents」 of 「Implicit Equations」

[`► Jump over to Khan academy for practice.`](https://www.khanacademy.org/math/ap-calculus-bc?t=practice)

### Example
![image](https://user-images.githubusercontent.com/14041622/42391885-65e08432-8183-11e8-9d05-d4c14413999f.png)
Solve:
- Plug in `y = 0` into the equation and get that `x = -6`, which is the answer.

### Example
![image](https://user-images.githubusercontent.com/14041622/42391958-b03754de-8183-11e8-8dad-bbf8cdbc3258.png)
Solve:
- To have a `Vertical Tangent`, we have to let the **derivative** become `Undefined`,
- which in this case is to let the denominator equal to zero:
![image](https://user-images.githubusercontent.com/14041622/42392639-1a998264-8186-11e8-9a48-99f6b296c1f9.png)
- Solve this equation out we get that `x = 3y²`, which means this relationship is true at the point of vertical tangent line.
- Plug that back to the original function to get `y = -1`, which means the vertical tangent goes through this point.
- Substitute y back and get `x = 3`
- The answer is `(3, -1)`.
