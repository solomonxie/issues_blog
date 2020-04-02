#  ❖ Sample Proportion

> The full name is `Sampling Distribution of the Sample Proportion`, which's denoted by `p-hat`.

[Refer to youtube: The Sampling Distribution of the Sample Proportion](https://www.youtube.com/watch?v=fuGwbG9_W1c)
[Refer to article: The Sample Proportion](http://www.stat.wmich.edu/s216/book/node68.html)
[Refer to article: Sampling Distribution of the Sample Proportion, p-hat](http://bolt.mph.ufl.edu/6050-6052/module-9/sampling-distribution-of-p-hat/)

`Sample Proportion` is the **proportion of success** in a sample.

> Sample Proportion(p-hat) is a random variable, 
specifically a **`Binomial Random Variable`**. 

So let **X** denotes the _number of success_ in the sample, which is the **Binomial Random Variable** with parameter _n_ and _p_,

![image](https://user-images.githubusercontent.com/14041622/45015015-fd671c00-b052-11e8-8e34-c9221d66c217.png)



## 「Mean & Variance」 of Sample Proportions

Recall that the _binomial random variable X_:
- has a mean of **np**
- has a variance of **np(1-p)**
- is approximately **normally distributed** for LARGE Sample Sizes (Central Limit Theorem).

Hence, we derived the _Mean & Variance_ of Sample Proportion `p-hat` from X:
![image](https://user-images.githubusercontent.com/14041622/45016250-abc09080-b056-11e8-8ebf-ae94ccf87349.png)
![image](https://user-images.githubusercontent.com/14041622/45015847-84b58f00-b055-11e8-84db-c22a022aec98.png)

Why is that?

![image](https://user-images.githubusercontent.com/14041622/45017656-b2510700-b05a-11e8-9f5d-42328342cec0.png)

That's why we say:
`p-hat` is an **unbiased estimator** for `p` of population.

And for Standard Deviation of Sample Proportion:
![image](https://user-images.githubusercontent.com/14041622/45017762-107dea00-b05b-11e8-9f1c-0f041af85fea.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/44943253-d1029400-adf5-11e8-8a1d-bbd9dc284c00.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/44943301-99e0b280-adf6-11e8-8d9d-bdc6a323d8e3.png)



## 「Probabilities」 with Sample Proportions

It's just to find out the probability area in the Normal Distribution.
All you need is the Mean, Standard Deviation and the point you're to measure.

### Example
![image](https://user-images.githubusercontent.com/14041622/44943403-833b5b00-adf8-11e8-8449-f372641e9777.png)
Solve:
- Calculate the mean of sample proportion is `0.63`
- Calculate the standard deviation of sample proportion is `0.019`
- Use an online Normal Distribution calculator, set up the upper boundary as `0.60`
- Get the probability area is about `0.06`

