#  ❖ Least-square Regression

> _Least-square Regression_ is one way of calculating _Linear Regression_. 
Most regressions' calculations are done by **computer**, but we want to do that by hand to have better understanding.

What is Linear Regression?
Trying to fit a line as closely as possible, and as many of points as possible, is called "Linear Regression".

[Refer to Khan academy: Introduction to residuals and least-squares regression](https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/modal/v/regression-residual-intro)

![image](https://user-images.githubusercontent.com/14041622/45735579-ef042d00-bc1a-11e8-97dd-eb5bf7a27f70.png)



## 「Residuals」

> Residuals are **errors**. More specifically, they are the differences between the actual value of the response variable and the value predicted by the least squares regression line.

![image](https://user-images.githubusercontent.com/14041622/45736304-24aa1580-bc1d-11e8-8305-db1d5d1a3a4b.png)

At a certain X-position, the value of _residual_ is the **VERTICAL DISTANCE** from the actual value to the Regression Line.

- When the `residual` is **positive**, the **actual point** is **ABOVE** the `regression line`,
- When the `residual` is **negative**, the **actual point** is **BELOW** the `regression line`.

![image](https://user-images.githubusercontent.com/14041622/45735633-1b1fae00-bc1b-11e8-9b41-477c1a38572e.png)

> The way that we calculate the `Regression Line` with `Least Square` method, is to **MINIMIZE** the **square of residuals**.


### Example
![image](https://user-images.githubusercontent.com/14041622/45736405-620ea300-bc1d-11e8-8797-14c26fdf6053.png)
Solve:
- This dish's actual taste rating was 4 points higher than predicted **based on its appearance**


### Example
![image](https://user-images.githubusercontent.com/14041622/45736532-cfbacf00-bc1d-11e8-8bf7-e0cf53a0cc97.png)
Solve:
- Recognize the **VARIABLES**: Y -> mass, X -> breadth
- So the expected mass is `-47 + 2*40 = 33`
- Since the observed mass is 29,
- So `residual = observed - expected = 29 - 33 = -4`


## Calculate the equation of 「Least-square line」

[`▶ Practice at Khan academy: Calculating the equation of the least-squares line`](https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/modal/e/calculating-equation-least-squares)

[Refer to Khan academy: Calculating the equation of a regression line](https://www.khanacademy.org/math/ap-statistics/bivariate-data-ap/modal/v/calculating-the-equation-of-a-regression-line)

Formula of Regression line:
![image](https://user-images.githubusercontent.com/14041622/43884348-77a305d0-9be8-11e8-9fc1-5bd881686fb4.png)

1. As we said the `Correlation Coefficient r` is kind like the **`Unit Slope`** which is between `-1 to 1`, so we have to apply the `unit slope` in real case by multiply `r` with the **ratio** of Standard Deviation of `y` & `x`, which is `Sy/Sx`.
2. A "must go through point" is the **MEAN** of the dataset, which is: `(Ẋ, Ẏ)`. At the mean, the `residual = actual`

With two informations above, we can easily calculate out the estimated Regression Line.


### 「Slope」 of Regression line

![image](https://user-images.githubusercontent.com/14041622/45736922-faf1ee00-bc1e-11e8-81a9-69a619f89fd2.png)


### 「Intercept」 of Regression line



### Example
![image](https://user-images.githubusercontent.com/14041622/45736841-bebe8d80-bc1e-11e8-8d67-cebdeee31d73.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45737075-6d62ce00-bc1f-11e8-8ea7-e44482a6c9ec.png)

