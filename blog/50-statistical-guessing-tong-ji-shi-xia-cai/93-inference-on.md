#  ❖ 「Inference」 on Linear Regression

## Conditions for 「inference on slope」 L-I-N-E-R

It can be concluded as `L-I-N-E-R`:
- `L`: Linear condition (Has linear relationship between x&y )
- `I`: Independent condition (Individual observations with replacement or 10% Rule)
- `N`: Normal condition (Sample size is at least 30)
- `E`: Equal variance condition
- `R`: Random condition


## 「Confidence interval」 for slope

Here's the formula for estimating the slope:

![image](https://user-images.githubusercontent.com/14041622/45804029-a5d0dd80-bced-11e8-942d-06be86859f1e.png)

Notice: 
- We're using `T-interval` for estimating slope
- Degree of freedom(DF) becomes: `n-2`

### Interpreting the output of 「Inference of Slope」

![image](https://user-images.githubusercontent.com/14041622/45804150-edf00000-bced-11e8-8920-abc943a8e06d.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/45804359-7373b000-bcee-11e8-8076-9f3522bd00da.png)
Solve:
- Interpret the table.
- Collect essential values for calculating CI:
    - Expected value of slope
    - T-value
    - Sample size
- Calculate with formula
![image](https://user-images.githubusercontent.com/14041622/45804430-a3bb4e80-bcee-11e8-96f2-ccce15b93f1f.png)



## 「T statistic」 for Slope

Here is the formula for T statistic for slope:
![image](https://user-images.githubusercontent.com/14041622/45805335-188f8800-bcf1-11e8-8e43-3d849652d217.png)

### Example
![image](https://user-images.githubusercontent.com/14041622/45805343-204f2c80-bcf1-11e8-9305-1d4d8511917e.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45805379-36f58380-bcf1-11e8-9099-1881069224e8.png)



## Use 「CI」 to make conclusions about 「slope」

[`▶︎ Jump back to previous note: Significance Testing`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-419806342)

Normally, we can make conclusion simply by comparing `P-value` with `Significance level`.

But there're cases ask us to make conclusion by comparing `Confidence level` with `Significance level`.
In that case, we can judge it by simply examine whether the **Confidence interval** covers `0` or not.

Since `Confidence Level + Significance Level = 100%`:
- CI exlcudes 0 ▶ Smaller interval & larger significance ▶ Significance level > P-value ▶ Not reject
- CI includes 0 ▶ Larger interval & smaller significance ▶ Significance level < P-value ▶ Reject

### Example
![image](https://user-images.githubusercontent.com/14041622/45806174-f6970500-bcf2-11e8-8497-88930707e096.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45806401-8b99fe00-bcf3-11e8-8610-ea0b6fb8fe8b.png)


