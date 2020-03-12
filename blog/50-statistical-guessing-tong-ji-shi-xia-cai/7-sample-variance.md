# Sample Variance

The Sample Variance, `s²`, is used to calculate how varied a sample is, 
and it's useful to estimate the **`Population Variance`**.

Since the Sample Variance is kind of estimation, so its formula is bit **different**.

![image](https://user-images.githubusercontent.com/14041622/44899569-b4525780-ad34-11e8-9749-867216d53f93.png)

## Why do we need to divide by `n-1`?

[Refer to Quora: Why is the formula of sample variance different from population variance?](https://www.quora.com/Why-is-the-formula-of-sample-variance-different-from-population-variance)

> "The sample variance is an **estimator** for the `population variance`. When applied to **sample data**, the population variance formula is **a biased estimator** of the population variance: it tends to **UNDERESTIMATE** the amount of variability. "

For solving this Underestimation problem, the statisticians found out that by dividing `n-1` we will solve this problem, regards to the idea of `degrees of freedom (DF)`.

![image](https://user-images.githubusercontent.com/14041622/45140936-025cd480-b1e7-11e8-9ee7-02a17a07ef81.png)


## Easy way to calculate Sample Variance
This formula is better for handwriting calculation:
![image](https://user-images.githubusercontent.com/14041622/44901253-6b50d200-ad39-11e8-958f-6fae3d998c82.png)


## `Sample Standard Deviation`

![image](https://user-images.githubusercontent.com/14041622/44899590-bfa58300-ad34-11e8-866d-91e32a0a2250.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/44900499-4eb39a80-ad37-11e8-96d3-744d8a527b09.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/44900573-7e62a280-ad37-11e8-91d5-f88af88bb727.png)
> The age of any gorilla in our sample is likely to be closer to the average of the 4 gorillas we looked at instead of the average of all the gorillas in the zoo. 
Because of that, the squared deviations from the mean we calculated will probably **underestimate** the actual deviations from the population mean.
To compensate for this **underestimation**, rather than simply averaging the squared deviations from the mean, we total them and divide by `n-1`.
