#  ❖ Significant Difference Test (Means)


[`▶ Jump back to previous note on: One-sample T test`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-420521963)

> Reminder: One-sample T Test
![image](https://user-images.githubusercontent.com/14041622/45405555-eef1b380-b695-11e8-8bbb-0369788dfa02.png)


## Formula for 「Two-sample T Test」

![image](https://user-images.githubusercontent.com/14041622/45538406-90fdd100-b839-11e8-8897-74c4b9806f2d.png)

The difference `μ1 - μ2` comes from the null hypothesis. In this type of test, we assume `μ1 = μ2` in the population means, which results in `μ1 - μ2 =0`.

## 「T-value」 for Two-sample Test


### Example
![image](https://user-images.githubusercontent.com/14041622/45538059-9575ba00-b838-11e8-8921-b07e73713b9b.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45538539-ea660000-b839-11e8-87fc-c5f7644a99af.png)



## 「P-value」 for Two-sample Test

For the _Degree of freedom_ in the Two-sample Test, we're gonna use the **SMALLER** sample size.

### Example
![image](https://user-images.githubusercontent.com/14041622/45540596-6e6eb680-b83f-11e8-889c-0e6eb6a1663d.png)
Solve:
- Calculate the _t-value_ to get `t=2.12621542`
- Decide `df`, which will be the **smaller** sample size `46- 1 = 45`
- Since it's asking `Ha: μ1 ≠ μ2`, so we're to calculate **both tails**:
![image](https://user-images.githubusercontent.com/14041622/45540767-e0470000-b83f-11e8-811b-e300a304f326.png)
- Get an online calculator and input the values:
![image](https://user-images.githubusercontent.com/14041622/45540811-f9e84780-b83f-11e8-8a02-813325c6b1e2.png)



## Use 「CI」 to make conclusions about the 「difference of means」

[`▶︎ Jump back to previous note: Significance Testing`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-419806342)


Normally, we can make conclusion simply by comparing `P-value` with `Significance level`.

But there're cases ask us to make conclusion by comparing `Confidence level` with `Significance level`.
In that case, we can judge it by simply examine whether the **Confidence interval** covers `0` or not.

Since `Confidence Level + Significance Level = 100%`:
- CI exlcudes 0 ▶ Smaller interval & larger significance ▶ Significance level > P-value ▶ Not reject
- CI includes 0 ▶ Larger interval & smaller significance ▶ Significance level < P-value ▶ Reject



### Example
![image](https://user-images.githubusercontent.com/14041622/45541082-a32f3d80-b840-11e8-98a0-531fc65678f6.png)
Solve:
- No, because the `P-value > ⍺`, means there's no sufficient evidence against the null hypothesis.


### Example
![image](https://user-images.githubusercontent.com/14041622/45541441-b393e800-b841-11e8-8470-cd4303f66161.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45541479-daeab500-b841-11e8-811c-1adffa4cf4dd.png)

