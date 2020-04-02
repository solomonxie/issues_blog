#  ❖ 「U-substitution」 → Chain Rule

> The `u-substitution` is to solve an integral of **composite function**, which is actually to **UNDO** the `Chain Rule`.

[`▶ Back to previous note on: Chain Rule`](https://github.com/solomonxie/solomonxie.github.io/issues/49#issuecomment-390151930)

Compare how we handle the composite functions with derivatives & integrals:
- For taking the **derivative** of a COMPOSITE function, we apply the `Chain rule`.
- For taking the **integral** of a COMPOSITE function, we apply the `u-substitution`.

[Refer to Khan academy: 𝘶-substitution: defining 𝘶](https://www.khanacademy.org/math/ap-calculus-bc/bc-antiderivatives-ftc/modal/v/u-substitution-defining-u)

We use `u-substitution` when we need to integrate an expression of the form of:
![image](https://user-images.githubusercontent.com/14041622/41199461-2b25c604-6cc5-11e8-8f2a-d7437c60e9cc.png)


Strategy:
- Find a function as `u`
- Find or **MAKE** an `u'` at the outside so that you can pair `u'` with `dx`
- Replace `u' · dx` with `du`, because `u' = du/dx`
- Rewrite the Integral in term of `u`, and calculate the integral
- Back substitute the function of `u` back to the result.

![image](https://user-images.githubusercontent.com/14041622/41199604-5e003a30-6cc7-11e8-807f-ee0c5f39673e.png)



## How to select u

Selecting `u` is the most tricky part here.

### Example
![image](https://user-images.githubusercontent.com/14041622/41199364-20690d4a-6cc3-11e8-8321-298f580942ff.png)
Solve:
- Apparently, we ignore the wrapper `sin()` here.
- We notice that the derivative of `-x+2` is `-1` which we could find it at outside.
- So let `u = -x+2` and `u' = -1`
- So rewrite the integral to `ʃ sin(u) · u' · dx = ʃ sin(u) · du`
- It looks quite neat, so the `u = -x+2` is alright.

### Example
![image](https://user-images.githubusercontent.com/14041622/41199651-26c796b6-6cc8-11e8-9cc1-82c162bf71c0.png)
Solve:
- Apparently it's in form of `ʃ u'/u · dx`
- So that we can make `u'·dx = du` and the integral becomes `ʃ 1/u · du`
- Quite nice, so the answer would be out of there.

## How to calculate 「Indefinite Integral」 with u-substitution

### Example
![image](https://user-images.githubusercontent.com/14041622/41199717-4f973988-6cc9-11e8-967d-2ff5c55edc27.png)
Solve:
- With a real quick eyeballing, we see it's in form of `ʃ u' · u⁶ · dx`
- So with `u' · dx = du` we will get the simplified form `ʃ u⁶ · du = u⁷/7`
- Back substitute function of u back to get the result:
![image](https://user-images.githubusercontent.com/14041622/41199726-ab98a69a-6cc9-11e8-8668-81af56546b56.png)


## How to calculate 「Definite Integral」 with u-substitution

### Example
![image](https://user-images.githubusercontent.com/14041622/41199835-b8df21e2-6ccb-11e8-9af1-8792a1246f7f.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/41199860-0c9777bc-6ccc-11e8-82c8-fdd7f9cf2834.png)


### Example (self-made u')
![image](https://user-images.githubusercontent.com/14041622/41199875-4f21f616-6ccc-11e8-8345-88b87776b55e.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/41199928-85363f5e-6ccd-11e8-90fa-85576c7644af.png)


### Example (Inverse Trig Rule)
![image](https://user-images.githubusercontent.com/14041622/41222752-78c54b48-6d9a-11e8-899c-9e70e55541a4.png)
Solve:
- Notice this radical form should directly use the Reversed Inverse Trig Rule:
![image](https://user-images.githubusercontent.com/14041622/41222912-dfe27530-6d9a-11e8-8d02-3c5f763c77e2.png)
- So that we assume `a = 1 & u = 3x`.
- Since `u' = 3` so we need to make a `3` from nowhere.
- Rewrite the formula to: `1/3 ʃ 3/(1+u²) ·dx = 1/3 ʃ 1/(1+u²) ·du`
- Apply the Reversed Inverse Trig Rule to get: `1/3 arctan(u) + C`
- Back substitute `3x` to `u` and the boundaries back to `x` get the result `π/6`.
