# Statistical Learning (OneNote) [DRAFT]

## Basics

### Learning Goal

> WE FIRST ASSUME THERE EXISTS AN ALMIGHTY FUNCTION Y=f(x) FOR EVERY (x, y)

![image](https://user-images.githubusercontent.com/14041622/52003406-65853580-24ff-11e9-9018-24879bba28cb.png)

![image](https://user-images.githubusercontent.com/14041622/52003388-58684680-24ff-11e9-81a7-dd190f965896.png)

![image](https://user-images.githubusercontent.com/14041622/52003395-5e5e2780-24ff-11e9-99b5-80128722d3cd.png)



### Model Selection

- Interpretability
    - Interpretable (Easy to understand)
    - Predictable (More precise)
- Labeled
    - Supervised (With right answer, labeled)  -> For prediction problem
        - Quantitative -> Regression Models
        - Qualitative -> Classification Models
    - Unsupervised (Without right answer)  -> For clustering analysis
        - Neural Network
- Numeric
    - Regression (Quantitative/Numerical Variables)
        - Linear Regression
            - Simple Linear Regression (One variable)
            - Multiple Linear Regression (Multiple variables)
    - Classification (Qualitative/Categorical Variables)
        - Classifier
            - Logistic Regression
        - Bayes Classifier
        - KNN Classifier
- Accuracy (Bias-Variance Trade-off)
    - Regression settings
        - MSE
        - AVE
    - Classification settings
        - Classifier
        - Bayes Classifier
        - KNN Classifier




## Statistics

### Plots

![image](https://user-images.githubusercontent.com/14041622/52002995-4d60e680-24fe-11e9-8350-985237eac321.png)

### Distribution

![image](https://user-images.githubusercontent.com/14041622/52003007-52259a80-24fe-11e9-9ec7-242e9316018c.png)

![image](https://user-images.githubusercontent.com/14041622/52003011-5487f480-24fe-11e9-961a-8dd440ba40bc.png)


### Inferential Statistics

![image](https://user-images.githubusercontent.com/14041622/52003018-6073b680-24fe-11e9-8198-88956d05d9a1.png)

![image](https://user-images.githubusercontent.com/14041622/52003024-62d61080-24fe-11e9-894b-f459cc0775e9.png)


### Probability

![image](https://user-images.githubusercontent.com/14041622/52003034-68335b00-24fe-11e9-9df8-76490b982206.png)


### Hypothesis Test [DRAFT]



### Random Variable

![image](https://user-images.githubusercontent.com/14041622/52003045-71bcc300-24fe-11e9-8066-f5eb405c08df.png)


### Bayesian Theorem [DRAFT]



## Linear Regression


### Mo: Linear Regression

![image](https://user-images.githubusercontent.com/14041622/52003501-a67d4a00-24ff-11e9-8e5c-c9009ab80f05.png)

![image](https://user-images.githubusercontent.com/14041622/52003512-aed58500-24ff-11e9-80ce-15c4cbf564eb.png)

![image](https://user-images.githubusercontent.com/14041622/52003533-c1e85500-24ff-11e9-91ca-7373b009c8de.png)

![image](https://user-images.githubusercontent.com/14041622/52003546-cc0a5380-24ff-11e9-93c5-ca2f7d2cd6cd.png)


### Linear Least Squares

> Linear least squares is ONE WAY to estimate a Linear function by finding the minimum value of squared-residuals.

The logic is:
	- Since we assume it's a linear function, so the only UNKNOWNS are coefficients β1 & β0
	- Our mission is to guess the two values which produce the minimum value of summed squared-residuals
	
Main Formulations of Linear least squares
	- Ordinary Least Squares (OLS), unweighted
		○ Simple linear regression (SLR)
		○ Multiple linear regression (MLR)
	- Weighted Least Squares (WLS)
	- Generalized Least Squares (GLS) 
Alternative Formulations
	- Iteratively reweighted least squares (IRLS)
	- Instrumental variables regression (IVR)
	- Total least squares (TLS)

Numerical methods for linear least squares
	- Inverting the matrix of the normal equations
	- Orthogonal decomposition methods

![image](https://user-images.githubusercontent.com/14041622/52003576-e2181400-24ff-11e9-87b9-77c1890317b5.png)

Regularized Linear Regression
Modified version of Ordinary linear regression, not only minimize cost function,
but also reduce complexity of the model.
	- Lasso Regression (L1 Regularization): minimize Absolute Sum of Coefficients
	- Ridge Regression (L2 Regularization): minimize Squared Absolute Sum of Coefficients

![image](https://user-images.githubusercontent.com/14041622/52003590-e8a68b80-24ff-11e9-9534-760188cf28e3.png)


### Gradient Descent

Gradient Descent Methods
	- Batch Gradient Descent (BGD)  -> for small dataset
		○ Parameters β1/β0 start from 0
		○ Iterate from 0 and update parameters every time
		○ Stop until cost function cost(β1, β0) ≈ 0
	- Stochastic Gradient Descent (SGD) -> for large dataset
		○ Parameters β1/β0 start from a random number
		○ Random walk

Standard Procedures of Gradient Descent
	- Setup initial value of parameters β1 and β0
	- Form a cost function with β1, β0: cost(β1, β0)
	- Calculate derivative (slope) of cost function: delta = cost(..)'
	- Update parameters β1, β0 with improvement: β? = β? - (alpha * delta)
	- Next iteration with NEW parameters until cost(β1, β0) ≈ 0


Batch Gradient Descent (BGD) 
Calculating the derivative from all training data before calculating an update. 
	- Asdf
	- asdfas

Stochastic Gradient Descent (SGD) 
Calculating the derivative from each training data instance and calculating the update immediately. 
	- Asdfa
	- asfdsafd



### Model Accuracy

Bias-Variance Trade-Off
The prediction error for any machine learning algorithm can be broken down into three parts: 
	- Bias Error: error caused by choosing models on interpretability
		○ High-Bias models: Linear Regression, Logistic Regression …
		○ Low-Bias models: Decision Trees, KNN, SVM
	- Variance Error: error caused by choosing models on flexibility
	- Irreducible Error (ε): cannot be reduced regardless of what algorithm is used. 
		○ High-Variance models: Decision trees
		○ Low-Variance models: Linear Regression

![image](https://user-images.githubusercontent.com/14041622/52003083-91ec8200-24fe-11e9-9a3a-d297425e7de3.png)

![image](https://user-images.githubusercontent.com/14041622/52003093-9dd84400-24fe-11e9-91cd-b787d53f0a0b.png)


### Hypothesis Test for ML

Some examples of statistical hypothesis tests and their distributions from which critical values can be calculated are as follows:
• Z-Test: Gaussian distribution (Normal Distribution).
• Student t-Test: Student’s t-distribution.
• Chi-Squared Test: Chi-Squared (𝜲²) distribution.
• ANOVA: F-distribution (Fisher–Snedecor distribution).

![image](https://user-images.githubusercontent.com/14041622/52003128-b6e0f500-24fe-11e9-8ce2-0f35f35ca61d.png)


### Features Selection [DRAFT]

Features selection approaches
	- Stepwise Regression
		○ Forward selection
		○ Backward selection
		○ Bidirectional elmination
	- LASSO

❶ Stepwise Regression
Main approaches:
	- Forward Selection
	- Backward Selection
	- Bidirectional Elimination

❷ LASSO (least absolute shrinkage & selection operator)


## Classification

### Classification Basics

Encodings of Categories
	- Code with order/rank
	- Binary code: yes or no
	- One-hot Encoding


Why NOT Linear regression?
Because the probability must fall between 0 and 1,
but Linear regression is not sensible and may lead the
result below 0 or above 1.
To avoid that, we MUST model p(X) using a function gives
output between 0 and 1. 
Many functions meet this description, logistic function in 
Logistic Regression is one of them.



### Logistic Regression

> is to predict the probability of a categorical dependent variable, which is a binary variable

![image](https://user-images.githubusercontent.com/14041622/52003251-f4458280-24fe-11e9-939e-3030ee632085.png)

![image](https://user-images.githubusercontent.com/14041622/52003257-f90a3680-24fe-11e9-8767-66e0aea3d021.png)


### Linear Discriminant Analysis

LDA (linear discriminant analysis) is an alternative
to Logistic regression for the following reasons:
	- More reliable on handling more than 2 response classes
	- More stable if dataset size n is small
	- More stable if the classes are well-separated

