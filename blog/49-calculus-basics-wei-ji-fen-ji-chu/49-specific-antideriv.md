# Specific antiderivatives

Normally the antiderivative is in form of `f(x) +C`.
But actually we could use some additional information to get the `C` and get the function only in terms of `x`.
And we often call the "additional information" as **`Initial Conditions`**, or `f₀(x)`.


### Example
![image](https://user-images.githubusercontent.com/14041622/41338371-90d5b214-6f24-11e8-975c-a6a0dea50ebd.png)
Solve:
- We could Integrate the `f'(x)` to get `f(x) = 9eˣ + C`.
- Since `f(8) = 9e⁸ - 8`, we could easily see that `C = -8`
- So the function under this condition would be: `f(x) = 9eˣ -8`
- Then we will get the result `f(0) = 9*1 - 8 = 1`.


### Example
![image](https://user-images.githubusercontent.com/14041622/41338590-3647b8b4-6f25-11e8-81cb-80d62422d566.png)
Solve:
- We could integrate `f'(x)` to get `f(x) = x³ - x² + 7x +C`
- Since `f(6)=200`, so we could substitute `6` into `f(x)`:
- `f(6) = 6³ - 6² + 7*6 +C = 200` which results `C = -22`
- So the function under this condition should be `f(x) = x³ - x² + 7x - 22`
- And `f(1) = 1³ - 1² + 7*1 - 22 = -15`



### Example (Separable equations with specific solutions)
![image](https://user-images.githubusercontent.com/14041622/41343153-71ade49a-6f30-11e8-9e64-c2f214cf2a37.png)
Solve:
- It looks confusing, but let's assume `f(x)` as `y` so `dy/dx = 2y`
- Separate differential equations to get `dy/y = 2dx`
- Take integral of both sides: 
![image](https://user-images.githubusercontent.com/14041622/41343558-8c8cd0f4-6f31-11e8-9f28-f841778abb02.png)
- Since `f(1) = 5`, so:
![image](https://user-images.githubusercontent.com/14041622/41343760-fb1c1de0-6f31-11e8-840a-5b09e5d788ee.png)
- And `f(3) = 5e⁴`, which means `m = 5, n = 4`



### Example
![image](https://user-images.githubusercontent.com/14041622/41340351-b422c446-6f29-11e8-84a5-df398a07954a.png)
Solve:
Hint: `f(0) = 2`

### Example
![image](https://user-images.githubusercontent.com/14041622/41340656-777620b4-6f2a-11e8-9275-83f808374b9e.png)
Solve
Hint: Don't need to solve `y` completely.
![image](https://user-images.githubusercontent.com/14041622/41340755-b0147768-6f2a-11e8-8be8-2622a2b25597.png)

