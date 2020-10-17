# ~Calculating Confidence Interval~ [DEPRECATED]

> Calculating the _Confidence Interval_ basically is just to convert a _confidence level_ , say 95%,  to a real value range, etc., (13kg, 28kg).

[Refer to _Head First Statistics_: Chapter.12](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-418623355)


There're a few ways to calculate:
- Traditional Normal-based
- Informal
- Bootstrapping

We use the traditional Normal-based method more often.

Assume we've decided which _population statistic_ we'll be estimating, 
and which _level of confidence_ we need it to be,
then there're 2 steps to calculate the _Confidence Interval_:
1. Find the Sampling Distribution
2. Find the Confidence Limits



### Finding the Sampling Distribution
We know for constructing a Sampling Distribution we need the **Mean & Variance**:
![image](https://user-images.githubusercontent.com/14041622/45032478-80ed3100-b084-11e8-89b4-1bcfaeafd732.png)

Since the _population variance_ `𝜎²` is **UNKNOWN** to us,
so we are to **estimate** the _population variance_ by the sample's "_best estimator_" (point estimator), which is _Sample Variance_ s² in this case.
![image](https://user-images.githubusercontent.com/14041622/45032715-138dd000-b085-11e8-9b1a-4f6bfbc4c9b4.png)

_s²_ is the _Sample Variance_, there're two types of formula:
here is the common formula:
![image](https://user-images.githubusercontent.com/14041622/45076891-34563400-b11e-11e8-82c1-b68c0c4a6186.png)

here is the formula for sample proportion:
![image](https://user-images.githubusercontent.com/14041622/45085763-10055200-b134-11e8-9cde-a4c041c592ec.png)


We assume the Sampling Distribution is **normally distributed**.

### Finding the Confidence Limits

Now we 



### Inverse Cumulative Normal Probability
Invert the given _cumulative normal probability_ (Confidence Level) back to z-score.

We've learnt how to convert a _percentile_ to z-score, and how about the `Cumulative Normal Probability`?

It's easy, in the graph we see that the _Confidence Level_ is the **middle part**.
if we cut the middle off, we'll get **two tails**, and either one can tell us the **percentile** position.

![image](https://user-images.githubusercontent.com/14041622/45081405-b9931600-b129-11e8-847e-1284ee9e7917.png)




