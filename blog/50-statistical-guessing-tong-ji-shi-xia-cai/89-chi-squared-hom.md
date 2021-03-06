#  ❖ Chi-squared Homogeneity Test

![image](https://user-images.githubusercontent.com/14041622/45671252-8ef88280-bb57-11e8-92d3-229e5e39302c.png)


For the Chi-square homogeneity test we're gonna use this online calculator instead:
[`▶ Chi-Square Calculator`](https://www.di-mgt.com.au/chisquare-calculator.html)

## 「Expected counts」

- Intuitively, we just need to get the **Ratio** from the Total counts, and apply the ratio to the corresponding cell, as what we **expected**.
- In general, it can be calculated with this formula:
![image](https://user-images.githubusercontent.com/14041622/45616324-ad03ab80-baa1-11e8-8745-6b046658569f.png)

> The `Ratio` can either be `RowTotal / TableTotal` or `ColumnTotal / TableTotal`.


### Example
![image](https://user-images.githubusercontent.com/14041622/45616176-45e5f700-baa1-11e8-968e-bad7d850ce9c.png)
Solve:
- For the intuition, we just look at the Frequency Table, and get the _Ratio from total counts_, which is `65/262` in this case
- and apply the ratio to the Row total, which is `90` in this case, so it's `(65/262) * 90`
- Or we can just use the formula:
![image](https://user-images.githubusercontent.com/14041622/45616553-606ca000-baa2-11e8-9ab4-4eec2d61bb4b.png)
- which gets us:
![image](https://user-images.githubusercontent.com/14041622/45616559-66fb1780-baa2-11e8-9d05-daf616eea60b.png)


## Test statistic 「𝐗²」

![image](https://user-images.githubusercontent.com/14041622/45670116-8bafc780-bb54-11e8-8e43-6a67082d5a71.png)


## 「P-value」

Degree of Freedom (DF) in the `Chi-square Homogeneity Test` would be:
![image](https://user-images.githubusercontent.com/14041622/45669912-05938100-bb54-11e8-86cf-f6346b2da3a0.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/45669951-1c39d800-bb54-11e8-8c14-eff93a9d8bfc.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45670076-720e8000-bb54-11e8-91e8-98175548f6b0.png)



## Making conclusions in chi-square tests for 「two-way tables」

[Refer to the "hint" of each practice problem: Making conclusions in chi-square tests for two-way tables](https://www.khanacademy.org/math/ap-statistics/chi-square-tests/modal/e/conclusions-chi-square-tests-for-two-way-tables)

**Selecting appropriate hypotheses**
The chi-square statistic is such a versatile tool that we can use the exact same calculations to answer very different questions with it, depending on whether we draw our data from one sample or from independent samples or groups.

**Ⓐ Multiple independent Sample groups**
A chi-square test can help us when we want to know whether different populations or groups are alike with regards to the distribution of a variable. Our hypotheses would look something like this:
- H₀: The distribution of a variable is the **SAME** in each population or group.
- Ha: The distribution of a variable **DIFFERS** between some of the populations or groups.

We call this the chi-square test for `Homogeneity`

etc.,
![image](https://user-images.githubusercontent.com/14041622/45672346-835a8b00-bb5a-11e8-96ef-78444197f9b5.png)


**Ⓑ One Sample group**
A chi-square test can help us see whether individuals from a sample who belong to a certain category are more likely than others in the sample to also belong to another category. Our hypotheses would look something like this:
- H₀: There is **NO** association between the two variables (they are independent).
- Ha: There **IS** an association between the two variables (they are not independent).

We call this the `chi-square test of association/independence`.

etc.,
![image](https://user-images.githubusercontent.com/14041622/45672392-966d5b00-bb5a-11e8-8101-fe2ce5262c50.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/45671775-ee0ac700-bb58-11e8-9800-94146d0c8bce.png)
Solve:
- The people in this study came from one sample, so a test of independence/association is most appropriate. We could state the null and alternative hypotheses in this problem as:
    - Ho: There is no association between service and age.
    - Ha: There is an association between service and age.
- Since `𝐗² > ɑ`, so we should fail to reject Ho.
- So the conclusion is "This isn't enough evidence to say there is an association between service and age."
