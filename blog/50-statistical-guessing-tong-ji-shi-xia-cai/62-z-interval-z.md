#  ❖ 「Z-Interval」 Z statistics

_Z interval_ is the _Confidence Interval_ constructed using `Z-score`.

[`▶︎ Jump back to previous note on: Z-score`](https://github.com/solomonxie/solomonxie.github.io/issues/50#issuecomment-410644808)


## Conditions for a valid 「Z Interval」

The conditions we need for inference on one proportion are:
- **Random**:
The data needs to come from a random sample or randomized experiment.
- **Normal**:
The normal condition says that we need at least 10 successes and 10 failures in our sample data. 
- **Independent**:
The independence condition says that when sampling without replacement, we can still treat each observation in the sample as independent as long as we sample less than 10%, percent of the population. 

## Formula of 「Z-interval」

![image](https://user-images.githubusercontent.com/14041622/45803045-175b5c80-bceb-11e8-9efb-9d20ac3e9201.png)


### Understanding the formula for 「Margin of Error」

Remember _Standard Error_ is `(X-μ)/Z`, 
in which `(X-μ)` is the distance from Sample to Population, so called the `Margin of Error`, 
which is the thing we're looking for.  
So doing the `Z · (X-μ)/Z = (X-μ)` is kinda **Reversing** the `normalization of the distance` back to the `real distance`.


## 「One-sample」 Z Interval
> Only take the sample once from the population.

[`▶︎ Practice at Khan academy: Calculating a z interval for a proportion`](https://www.khanacademy.org/math/statistics-probability/confidence-intervals-one-sample/modal/e/calculating-one-sample-z-interval-proportion)

[`▶︎ Tool: Omni Online Confidence Interval Calculator`](https://www.omnicalculator.com/statistics/confidence-interval)

[Refer to Khan academy: Critical value (z*) for a given confidence level](https://www.khanacademy.org/math/statistics-probability/confidence-intervals-one-sample/modal/v/critical-value-for-a-given-confidence-level)

Here is the formula for a _one-sample z interval_ for a `sample proportion`:

![image](https://user-images.githubusercontent.com/14041622/45082949-16440000-b12d-11e8-9704-478cdc78d5ca.png)

in which the _margin of error_ is:

![image](https://user-images.githubusercontent.com/14041622/45084302-9ae44d80-b130-11e8-8add-b01f97b86c9b.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/45082319-aa14cc80-b12b-11e8-8c33-aecd9ff82fd3.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45082524-1b547f80-b12c-11e8-935b-3d64f7715b34.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/45082812-c82efc80-b12c-11e8-886f-9fe26a859ccc.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45082868-e5fc6180-b12c-11e8-8abc-afeca522396a.png)

## 「Sample Size」 & 「Margin of Error」

### Example
![image](https://user-images.githubusercontent.com/14041622/45083842-5b693180-b12f-11e8-8803-c10d132626ef.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45083959-a5521780-b12f-11e8-8950-23baccfb806c.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/45084166-32956c00-b130-11e8-975c-7e534deb8aee.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/45084225-640e3780-b130-11e8-90d3-314b27565929.png)


## Estimating 「Margin of Error」

[Refer to Khan academy: Determining sample size based on confidence and margin of error](Determining sample size based on confidence and margin of error)

### Example
![image](https://user-images.githubusercontent.com/14041622/45084689-82286780-b131-11e8-812f-b5e2bb7483d8.png)
Solve:
- We haven't been told what is the probability yet, so we have to estimate it first.
- We know the formula for _margin of error_:
![image](https://user-images.githubusercontent.com/14041622/45084901-f6630b00-b131-11e8-83ed-f8b0f0016b7f.png)
- In the formula above, if we're to set an _upper bound_ on it, we need to find the **largest margin of error**, which require either the _sample size n_ to be **smallest** or the `p(1-p)` to be **largest**.
- Since it's asking for a smallest sample size, so we need to find the **largest** `p(1-p)`.
- We've learnt the optimization from Calculus how to get the **max value** from an equation:
![image](https://user-images.githubusercontent.com/14041622/45085163-a0db2e00-b132-11e8-9fba-9dbd850afb40.png)
- We take the derivative of `p(1-p)` and set to 0, to get the max value: `p = 0.5`
- Calculate the rest:
![image](https://user-images.githubusercontent.com/14041622/45085264-dbdd6180-b132-11e8-8eb1-0c9bd3cc9b6a.png)


## 「Z-table」

![image](https://user-images.githubusercontent.com/14041622/43824925-eaf6a17c-9b25-11e8-86b2-3bd990df76d7.png)
