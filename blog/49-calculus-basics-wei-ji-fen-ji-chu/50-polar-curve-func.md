# 「Polar Curve」 Functions (Differential Calc)

[`▶ Practice at Khan academy.`](https://www.khanacademy.org/math/ap-calculus-bc/bc-advanced-functions-new/bc-9-7/e/differentiate-polar-functions)

[Refer to Khan academy: Polar functions derivatives](https://www.khanacademy.org/math/ap-calculus-bc/bc-advanced-functions-new/bc-9-7/v/derivatives-in-polar-coordinates)
 
> [`▶ Proceed to: Area of Polar Curves (Integral Calc)`](https://github.com/solomonxie/solomonxie.github.io/issues/49#issuecomment-398657472)

![image](https://user-images.githubusercontent.com/14041622/42408971-cec59e88-8205-11e8-9e14-bc1a910846da.png)

> In the `Polar World`, 
instead of the relationship between `y & x`, 
the function is now representing the relationship between `Radius & Angle`, 
which could be presented as:

![image](https://user-images.githubusercontent.com/14041622/42408955-8bb18e9a-8205-11e8-8750-67370131d552.png)


## Finding the right 「boundaries」

> The most tricky part in Polar system, is finding the right boundaries for `θ`, and it will be the first step for polar integral as well.




## Differentiate 「Polar Functions」

**Taking derivative of Polar function** is actually **DIFFERENTIATING PARAMETRIC FUNCTION**.
To take the derivative we need to:
- Convert the `Polar function` in terms of `x & y`:
![image](https://user-images.githubusercontent.com/14041622/42409085-7f99bb26-8207-11e8-9b8f-53fd99405428.png)
- Take derivative of the parametric function.

### Example
![image](https://user-images.githubusercontent.com/14041622/42408886-70192f54-8204-11e8-9eaf-ff0d0b4cc7b7.png)
Solve:
- Since it's asking for the `Rate of change of y-coordinate`, so we convert the polar function to `rectangular function`:
![image](https://user-images.githubusercontent.com/14041622/42409148-900f2008-8208-11e8-8433-6ec1dc53eaa2.png)
- And we take the derivative `dy/dΘ`:
![image](https://user-images.githubusercontent.com/14041622/42409155-b66604e2-8208-11e8-9b4a-1cfd57b53964.png)
- Plug in the point `Θ=π` and get:
![image](https://user-images.githubusercontent.com/14041622/42409162-ce8d4f58-8208-11e8-8bd5-a1b4062f71a4.png)


## 「Tangents」 to Polar curves
Steps:
- Find the slope `dy/dx`
- Convert the polar function to get the `x(θ)` and `y(θ)` parametric equations
- Solve `dy/dx` and get the slope
- Plug in the point's information to solve for `x & y`
- Get the equation of the line (tangent).


### Example
![image](https://user-images.githubusercontent.com/14041622/42409334-61386854-820b-11e8-84de-f5676a5543f4.png)
Solve:
- To find the tangent line, we need to get the slope first, which is `dy/dx`.
- And `dy/dx` would be a `parametric problem`:
![image](https://user-images.githubusercontent.com/14041622/42409359-d9da5704-820b-11e8-9dd3-6bcce56f25f4.png)
- Plug in the Θ value, to evaluate the slope:
![image](https://user-images.githubusercontent.com/14041622/42409371-119c3dc4-820c-11e8-8eaf-8a0b6da1ca8f.png)
- Find the `x & y` value according to the Θ:
![image](https://user-images.githubusercontent.com/14041622/42409376-38b1ac46-820c-11e8-91f4-cb088fcc8ed6.png)
- Now we got everything to form the equation for the tangent line:
![image](https://user-images.githubusercontent.com/14041622/42409378-4c5659f4-820c-11e8-9675-dd1bc5d54907.png)
![image](https://user-images.githubusercontent.com/14041622/42409379-512ce470-820c-11e8-882c-d0265c077d41.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/42410082-d26ab8fa-8216-11e8-9362-9e88eb6f2a9f.png)
Solve:
- First, we need to convert the polar function to `x(θ) & y(θ)`:
![image](https://user-images.githubusercontent.com/14041622/42410205-4a6413a0-8218-11e8-8721-95acf2208c63.png)
- And we need to find the slope `dy/dx`:
![image](https://user-images.githubusercontent.com/14041622/42410164-d9a5b8f8-8217-11e8-9bd5-1355d13c31ff.png)
- Since it's a horizontal tangent, so `Slope =0`, which means `dy/dx =0`. But `dx` is dominator can't be zero, so we can set `dy = 0` and solve for θ:
![image](https://user-images.githubusercontent.com/14041622/42410215-74fd8092-8218-11e8-85c2-975a74be7fc7.png)
- So the answer is:
![image](https://user-images.githubusercontent.com/14041622/42410218-940013c4-8218-11e8-8065-15bee832ee77.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/42410271-bcbc245a-8219-11e8-8f8d-0e8bd320f408.png)
Solve:
- To find a vertical tangent, we have to set the dominator of the slope as 0, that's the only thing makes it **undefined**.
- The slope is `dy/dx`, so we set `dx = 0`.
- The equation for `x` is:
![image](https://user-images.githubusercontent.com/14041622/42410294-0226d9c2-821a-11e8-91e3-cdf2809609b2.png)
....

