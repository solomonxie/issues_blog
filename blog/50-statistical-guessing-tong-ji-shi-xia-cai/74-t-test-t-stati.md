#  ❖ T Test (t statistics)

[Refer to article: Understanding t-Tests: t-values and t-distributions](http://blog.minitab.com/blog/adventures-in-statistics-2/understanding-t-tests-t-values-and-t-distributions)

T-tests are all based on `t-values`. 
T-values are an example of what statisticians call `Test statistics`. A test statistic is a standardized value that is calculated from sample data during a hypothesis test. 
The procedure that calculates the test statistic compares your data to what is expected under the null hypothesis.

[`▶︎ Jump back to previous note on: T-score`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-418987783)

[`▶︎ t-distribution online calculator`](https://surfstat.anu.edu.au/surfstat-home/tables/t.php)



## Formula of 「One-sample T test」 for Mean

The test statistic gives us an idea of how far away our sample result is from our null hypothesis. 

For a one-sample t test for a mean, our test statistics is:
![image](https://user-images.githubusercontent.com/14041622/45406894-69243700-b69a-11e8-818c-96bbd88854d7.png)
(x⁻ is the _Sample Mean_, μ₀ is mean from _null hypothesis_, sx is the _Sample SD_, n is _Sample size_)

> Understanding the formula:
The `statistic - parameter` results the **DISTANCE** from _Sample mean_ to _Population mean_.
The `Standard Error` represents the **DISTANCE** from _Sample SD_ to _population SD_.
Therefore, dividing the `Distance of mean` by `Distance of SD` will results in a **Normalized Distance for mean**.

## Calculating the 「test statistic」 in a t test for a mean

### Example
![image](https://user-images.githubusercontent.com/14041622/45405038-e9936980-b693-11e8-87d2-32e15b33910b.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45405403-522f1600-b695-11e8-88e0-71a1bd6bdf4a.png)


## Calculating the 「P-value in a t test」 for a mean

### Example
![image](https://user-images.githubusercontent.com/14041622/45407947-7b53a480-b69d-11e8-9d8b-33652b0be94c.png)
Solve:
- Since the sample size = 11, so the degree of freedom is 10.
- Take a T-table and look for a cross section of `df=10 & t=1.368`
![image](https://user-images.githubusercontent.com/14041622/45408116-fe74fa80-b69d-11e8-834d-84ed0715b788.png)
- Since our test statistic is slightly smaller than 1.372, the corresponding P-value will be slightly larger than 0.10
- The P-value is approximately 0.101
- Or another way is to use an online calculator: [SurfStat t-distribution calculator](https://surfstat.anu.edu.au/surfstat-home/tables/t.php)
![image](https://user-images.githubusercontent.com/14041622/45408440-ece02280-b69e-11e8-8d19-a905727bee36.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/45408241-5f9cce00-b69e-11e8-9deb-69412daaabf8.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45408267-76432500-b69e-11e8-8d12-e5d11d96244b.png)

