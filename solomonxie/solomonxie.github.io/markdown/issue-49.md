# Calculus Basics 微积分基础
> Mainly some basic Calculus knowledges for Machine Learning

## Study resources
- [ ] [Khan academy: AP Calculus AB](https://www.khanacademy.org/mission/ap-calculus-ab)
- [ ] [Mathispower4u](http://www.mathispower4u.com/calculus.php)

## Practice To-do List (Linked with Unit tests)
- [ ] [Limits and continuity](https://www.khanacademy.org/math/ap-calculus-ab/ab-limits-continuity/modal/test/ab-limits-continuity-unit-test)
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



# Special Limits

## `Limits at infinity of quotients with trig`
Calculating limits related to a trig function, is necessary to use the **`Squeeze theorem`**.

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