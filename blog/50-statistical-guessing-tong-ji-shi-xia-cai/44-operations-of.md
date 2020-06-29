#  ❖ Operations of 「Random Variables」

> Some basic "algebraic" operations, like adding/multiplying a number, or combining different R.V.s

## 「Shift」
The **addition** or **subtraction** of `Random Variable X` will have these effects:
- Mean: Shift by the same value with X.
- Variance: Maintain the same.

## 「Scale」
The scale of `Random Variable X` will have these effects:
- Mean: Scale by the same value with X.
- Variance: Scale by the same value with X.


### Example
![image](https://user-images.githubusercontent.com/14041622/44456750-fa703280-a633-11e8-8de5-6101b4929130.png)
Solve:
- Effect on mean(μ): `μY = 10(μX) + 5 = 24.5`, because mean will be effected by both **shift** & **scale**.
- Effect on Standard deviation(σ): `σY = 10μX = 8`, because σ will only be effected by **scale**.


## 「Combine」 Random Variables

[Refer to wiki: Algebra of random variables](https://www.wikiwand.com/en/Algebra_of_random_variables)
[Refer to article on Khan academy: Combining random variables](https://www.khanacademy.org/math/ap-statistics/random-variables-ap/modal/a/combining-random-variables-article)

![image](https://user-images.githubusercontent.com/14041622/44387928-6fbb0500-a559-11e8-9f82-fd8ac5f11411.png)

Important facts about combining variances:
- The variables must be independent to each other.
- We can find the `standard deviation` by taking square root √ of the combined variances.
- The variance **increases** even when we subtract random variables.
- If both Random Variables are **normally distributed**, then the `Difference of them` will also be **normally distributed**.



### Example
![image](https://user-images.githubusercontent.com/14041622/44457101-e8db5a80-a634-11e8-89ec-45ab9c16b9c3.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/44457462-d9a8dc80-a635-11e8-9b37-4797bb6837f0.png)



## Probability of 「Combined Normal Random Variables」

Remember:
**If both Random Variables are normally distributed, then the Difference of them will also be normally distributed.**

### Example
![image](https://user-images.githubusercontent.com/14041622/44507980-34e2d980-a6df-11e8-82d8-52136ab914e6.png)
Solve:
- Let `D` be the new Random Variable which `D = X - Y`
- For calculating the probability of a normal distributed random variable, we need to know the mean, standard deviation, and boundaries.
- Get the basic stats of D:
![image](https://user-images.githubusercontent.com/14041622/44508269-45e01a80-a6e0-11e8-8678-247f8f492054.png)
- According to the condition, the boundary is `-10 < D < 10`
- Input the required information to a calculator:
![image](https://user-images.githubusercontent.com/14041622/44508368-9bb4c280-a6e0-11e8-9a52-af76c693ed47.png)
- The answer is `0.57`.
