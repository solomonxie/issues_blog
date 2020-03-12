# Chain Rule

> One of the **core principles** in Calculus is the Chain Rule.

![image](https://user-images.githubusercontent.com/14041622/40289431-ce3b8652-5cea-11e8-9aba-c40a24f19bdd.png)

[Refer to Khan academy article: Chain rule](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/modal/a/chain-rule-review)
[`▶ Proceed to Integral rule of composite functions: U-substitution`](https://github.com/solomonxie/solomonxie.github.io/issues/49#issuecomment-395677669)

It tells us how to differentiate `Composite functions`.

![image](https://user-images.githubusercontent.com/14041622/40225236-178dc84c-5abb-11e8-8bbf-098d8df7d3b9.png)

**It must be composite functions, and it has to have `inner & outer` functions, which you could write in form of `f(g(x))`.**
![image](https://user-images.githubusercontent.com/14041622/40225120-c6ddf174-5aba-11e8-8b1b-2859c7eeb749.png)

### Common 「mistakes」

- Not recognizing whether a function is composite or not
- Wrong identification of the inner and outer function
- **Forgetting to multiply by the derivative of the inner function**
- Computing `f(g(x))` wrongly:
![image](https://user-images.githubusercontent.com/14041622/40225381-7744459a-5abb-11e8-848d-9a28c39db99c.png)

### How to identify 「Composite functions」

> Seems a basic algebra101, but actually a quite tricky one to identify.

[Refer to Khan lecture: Identifying composite functions](https://www.khanacademy.org/math/ap-calculus-ab/ab-derivative-rules/modal/v/recognizing-compositions-of-functions)

The core principle to identify it, is trying to re-write the function into a nested one: `f(g(x))`. If you could do this, it's composite, if not, then it's not one.

### Examples
![image](https://user-images.githubusercontent.com/14041622/40226233-add7f910-5abd-11e8-8522-853ca335a2a1.png)
It's a composite function, which the inner is `cos(x)` and outer is `x²`.

![image](https://user-images.githubusercontent.com/14041622/40226318-f2bbe668-5abd-11e8-9f47-405b4476c054.png)
It's a composite function, which the inner is `2x³-4x` and outer is `sin(x)`.

![image](https://user-images.githubusercontent.com/14041622/40226383-24b4fe48-5abe-11e8-9cb0-9c0bda203c89.png)
It's a composite function, which the inner is `cos(x)` and outer is `√(x)`.

## Two forms of 「Chain Rule」

The general form of Chain Rule is like this:
![image](https://user-images.githubusercontent.com/14041622/40289487-313c6d84-5ceb-11e8-85a9-2aee2108aa60.png)

But the Chain Rule has another **more commonly used** form:
![image](https://user-images.githubusercontent.com/14041622/40289493-3ddcdfa6-5ceb-11e8-9771-2d93d210a85b.png)

Their results are exactly the same.
It's just some people find the first form makes sense, some more people find the second one does.


### Example
![image](https://user-images.githubusercontent.com/14041622/40268880-38210900-5ba8-11e8-8e45-3691ad3b5163.png)
Solve:
[Refer to Symbolab worked example.](https://www.symbolab.com/solver/step-by-step/%5Cfrac%7Bd%7D%7Bdx%7D%5Cleft(sqrt%5Cleft(3cos%5E%7B3%7D%5Cleft(x%5Cright)%5Cright)%5Cright))


## Chain rule for 「exponential function」

Formula:
![image](https://user-images.githubusercontent.com/14041622/46215093-17a0cb00-c36f-11e8-9bf0-5162ea68f30e.png)

Because:
![image](https://user-images.githubusercontent.com/14041622/46215176-4ae35a00-c36f-11e8-973b-10ead67e8e8c.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/46215200-59ca0c80-c36f-11e8-96f9-17989b088acf.png)
Solve:
- Apply the `Log power rule` to simplify the exponential function:
![image](https://user-images.githubusercontent.com/14041622/46215265-8bdb6e80-c36f-11e8-9e0c-cb8aa8670b9d.png)
- Differentiate both sides:
![image](https://user-images.githubusercontent.com/14041622/46215364-c7763880-c36f-11e8-8233-182d5f7c4888.png)


