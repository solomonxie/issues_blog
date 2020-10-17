#  ❖ Power Series

> Try to think `Power series = Geometric Series`.

[►Refer to Math24: Power series](https://www.math24.net/power-series/)

`Power series` is actually the `Geometric series` in a more general and abstract form.

![image](https://user-images.githubusercontent.com/14041622/42147291-a00d5af4-7dff-11e8-9bbf-7ae10b740788.png)

For easier to remember it, that could be simplified as:

![image](https://user-images.githubusercontent.com/14041622/42147247-7517f930-7dff-11e8-8f11-e283a1ff377f.png)


In this function it's critical to know that:
**`a_n` IS A CONSTANT NUMBER! NOT A VARIABLE !**


## Differentiate 「Power series」

[►Refer to Khan academy: Differentiating power series](https://www.khanacademy.org/math/ap-calculus-bc/bc-series/modal/v/differentiating-power-series)

We have 2 ways to differentiate series, they work same way:
- One way is to expand the series with real numbers (1,2,3...) and take their derivatives:
![image](https://user-images.githubusercontent.com/14041622/42506420-709b1efc-8474-11e8-9acc-4c91ec14f9aa.png)
(▲Note that this is constantly true for power series.)
- Another way is to calculate the term's derivative and then plug in the real numbers (1,2,3):
![image](https://user-images.githubusercontent.com/14041622/42506441-8064c46e-8474-11e8-9c8a-d6d065d6570e.png)


Either way will do, it depends on the actual equation for you to choose which way you're gonna use.


### Example
![image](https://user-images.githubusercontent.com/14041622/42149557-49116f7e-7e09-11e8-90b2-71cc0dbb1755.png)
Solve:
- Let's organize this function to make it clear:
![image](https://user-images.githubusercontent.com/14041622/42150204-99ab2d74-7e0b-11e8-8bbc-b40cd3b32c88.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/42085947-62513c40-7bc4-11e8-8eb4-c6e87a26d5a6.png)
Solve:
- Notice that: If we plug in the `x=0` at beginning, everything will be `0` and we don't have anything to calculate.
- So Let's keep the `x` in the terms until the **last step**.
- It's easier to `expand the series with real numbers`, and we're to try 3 or 4 terms in this case. 
- Because at the end of it you'll notice, if we're doing `Third Derivative`, then more than 3 terms will just bring more `0`s.
- First we're to organize the function in the standard **power series** form:
![image](https://user-images.githubusercontent.com/14041622/42148100-793b43ba-7e03-11e8-97e2-bca413c295e3.png)
- And the **constant number `a_n`** in the function is:
![image](https://user-images.githubusercontent.com/14041622/42148159-aff276a8-7e03-11e8-8b22-deafe3cd3530.png)
- Let's plug in the real number (0,1,2,3,4) for `n` to expand the series:
![image](https://user-images.githubusercontent.com/14041622/42148679-c48ac622-7e05-11e8-9c4e-5807f084f9d5.png)
- Based on that we can take the derivatives:
![image](https://user-images.githubusercontent.com/14041622/42148867-6ef74446-7e06-11e8-9e2d-3ca70f8bff77.png)
- Now we've got the `third derivative`, so let's plug in the `x=0` and see what we get:
![image](https://user-images.githubusercontent.com/14041622/42148892-85613174-7e06-11e8-8236-744492cc4c0f.png)
- And that's the answer.
- And now you know **why in this case it's a waste to calculate more terms.**




## Integrate 「Power Series」



### Example
![image](https://user-images.githubusercontent.com/14041622/42149117-8019f588-7e07-11e8-8750-2c113ca3cf64.png)
Solve:
- Knowing that `Integrate a series` can be turned to `a series of Integrations of terms`:
![image](https://user-images.githubusercontent.com/14041622/42149518-fc263596-7e08-11e8-88e8-aa8e3c621a89.png)
- Integrate the terms:
![image](https://user-images.githubusercontent.com/14041622/42149534-1ca3bac8-7e09-11e8-95f4-9e52a6ca7c53.png)
- And we get a simple `Geometric series`. So that we can apply the formula of calculating geometric series:
![image](https://user-images.githubusercontent.com/14041622/42149454-b8a94d6c-7e08-11e8-9ff4-2cfbb182e18c.png)
- Let's apply the formula:
![image](https://user-images.githubusercontent.com/14041622/42149485-d97c50b6-7e08-11e8-9ed6-9004b48c2b98.png)

## 「Integrals & derivatives」 of functions with 「known power series」

[`► Jump over to have practice at Khan academy.`](https://www.khanacademy.org/math/ap-calculus-bc/bc-series-new/modal/e/creating-power-series-from-geometric-series-using-differentiation-and-integration)

### Example
![image](https://user-images.githubusercontent.com/14041622/42367884-24758736-8138-11e8-8dcd-98d39ad1e42a.png)
Solve:
- Let's assume the function of the **series above** is `f(x)`, and the **series below** is `g(x)`
- It's clear to see that the `g(x) is the `Antiderivative` of the `f(x)`.
- So we just need to **integrate** the function of the `f(x)`:
![image](https://user-images.githubusercontent.com/14041622/42368010-7f00611c-8138-11e8-91af-470e8c4c2dca.png)
- We see that the `antiderivative` can represent the `g(x)`, but only with the `C` in it:
![image](https://user-images.githubusercontent.com/14041622/42368233-172b104a-8139-11e8-88a8-16949514b969.png)
- So we need to solve for `C`. The easiest way is to plug in `0` for `g(x)`:
![image](https://user-images.githubusercontent.com/14041622/42368389-7c8c8b6c-8139-11e8-9a9e-97728eab3149.png)
- Then the answer is:
![image](https://user-images.githubusercontent.com/14041622/42368415-8ab72792-8139-11e8-943d-6780bbdbb81e.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/42368724-658b0398-813a-11e8-9091-c16e61d7e482.png)
Solve:
- Set the two series as `f(x)` and `g(x)`.
- It's clear that `g(x) = -f'(x)`.
- So by differentiate `f(x)` we will get:
![image](https://user-images.githubusercontent.com/14041622/42368873-c4a82356-813a-11e8-8604-fd6efd4c38d5.png)
- Then `-f'(x)` would be:
![image](https://user-images.githubusercontent.com/14041622/42368903-dadb341a-813a-11e8-9fac-515e7eb984e5.png)

