# Linear Algebra with Moocs 线性代数课程笔记
> Quick notes on College level of Maths or Stats for machine learning.

## Study resources
- [x] [Slant: What are the best resources to learn linear algebra?](https://www.slant.co/topics/6073/~resources-to-learn-linear-algebra)
- [x] [High school maths notes](https://github.com/solomonxie/solomonxie.github.io/issues/44)
- [x] [ Khan academy Pre-calculus](https://www.khanacademy.org/math/precalculus)
- [ ] [MIT OCW 18.06 SC Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm)
- [ ] [Essence of linear algebra: Youtube](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [ ] [A First Course in Linear Algebra: PDF](https://github.com/solomonxie/solomonxie.github.io/files/1786068/fcla-3.50-A.First.Course.in.Linear.Algebra.-.Robert.A.Beezer.University.of.Puget.Sound.Version.3.50.pdf)

## MIT OCW Linear Algebra 18.06 
- [ ] Unit I: Ax = b and the Four Subspaces
    - [x] The Geometry of Linear Equations (Watched; Practiced 3/3)
    - [x] An overview of key ideas (Watched.)
    - [ ] Elimination with matrices (Watched; Practiced 0/3)
    - [ ] Multiplication and Inverse matrices
    - [ ] Factorization in to A = LU
    - [ ] Transposes, Permutations, Vector Spaces
    - [ ] Column space and Null space
    - [ ] Solving Ax = 0: Pivot variables, Special solutions
    - [ ] Solving Ax = B: Row reduced from R
    - [ ] Independence, Basis and Dimension
    - [ ] The four fundamental Subspaces
    - [ ] Matrix spaces; Rank 1; Small world graphs
    - [ ] Graphs, Networks, Incidence matrices
    - [ ] Exam 1 review
    - [ ] Exam 1
- [ ] Unit II: Least Squares, Determinants and Eigenvalues
- [ ] Unit III: Positive Definite Matrices and Applications


## Study goals of Linear Algebra
- [ ] Systems of linear equations
- [ ] Row Reduction Echelon Forms (RREF)
- [ ] Matrix operations, including inverses
- [ ] Block matrices
- [ ] Linear dependence and independence
- [ ] Subspaces and bases and dimensions
- [ ] Orthogonal bases and orthogonal projections
- [ ] Gram-Schmidt process
- [ ] Linear models and least-squares problems
- [ ] Determinants and their properties
- [ ] Cramer's Rule
- [ ] Eigenvalues and eigenvectors
- [ ] Diagonalization of a matrix
- [ ] Symmetric matrices
- [ ] Positive definite matrices
- [ ] Similar matrices
- [ ] Linear transformations
- [ ] Singular Value Decomposition

![image](https://user-images.githubusercontent.com/14041622/39066642-51cd6ce2-4508-11e8-9863-4cc7f0497983.png)





## TL;DR. Archived link: [Vector section notes of Essence Linear Algebra](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-379985082)

## TL;DR Archived link: [MIT OCW Linear Algebra courses list & compare](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-380001327).


## TL;DR Archived link: [MIT OCW Linear Algebra courses list & compare](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-380001327).


# MIT OCW 18.06 SC Course Notes

## Unit 1.1 The geometry of linear equations

[Refer to the review pdf.](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/ax-b-and-the-four-subspaces/the-geometry-of-linear-equations/MIT18_06SCF11_Ses1.1sum.pdf)

Lecture video outlines | Links
-- | --
Lecture | [0m0s](https://www.youtube.com/watch?v=ZK3O402wf1c&t=0s&index=1&list=PLE7DDD91010BC51F8)
Matrix picture | [2m47s](https://youtu.be/ZK3O402wf1c?t=2m47s)
Row picture | [3m41s](https://youtu.be/ZK3O402wf1c?t=3m41s)
Column picture | [8m41s](https://youtu.be/ZK3O402wf1c?t=8m41s)
Matrix picture in 3D | [15m26s](https://youtu.be/ZK3O402wf1c?t=15m26s)
Row picture in 3D: intersects of planes | [17m33s](https://youtu.be/ZK3O402wf1c?t=17m33s)
Column picture in 3D | [23m11s](https://youtu.be/ZK3O402wf1c?t=23m11s)
Permutation Matrix | [36m42s](https://youtu.be/QVKj3LADCnA?t=36m42s)

> "The fundamental problem of linear algebra is to solve n linear equations in `n` unknowns."

![image](https://user-images.githubusercontent.com/14041622/38993221-93ad3a46-4415-11e8-8d2f-c3c88abac23b.png)

We view this problem in three ways:
- `Row picture`: Each row is an equation, and we could draw out each line equation on the graph.
- **`Column picture`**: Rewrite equations in the form below, and each column is a vector, and we could each vector (with scalar) on the graph.
- `Matrix picture`: Rewrite equations into `Coefficient Matrix form`, and see the geometric meaning of a matrix and vector.

![image](https://user-images.githubusercontent.com/14041622/39082877-d8f0be02-458c-11e8-9da5-fdcc95edeefc.png)

## Unit 1.2 Elimination with Matrices
> `Elimination` is the method **EVERY** softwares use to solve `linear equations`.

Lecture video outlines | Links
-- | -- 
Lecture | [0m0s](https://www.youtube.com/watch?v=QVKj3LADCnA&t=0s&index=2&list=PLE7DDD91010BC51F8)
Elimination pivots and an example | [3m9s](https://youtu.be/QVKj3LADCnA?t=3m9s) 
Failure of Elimination method | [10m34s](https://youtu.be/QVKj3LADCnA?t=10m34s) 
Augmented matrix | [14m50s](https://youtu.be/QVKj3LADCnA?t=14m50s)
Operations of matrices elimination | [19m24s](https://youtu.be/QVKj3LADCnA?t=19m24s)
Row operations of Matrices Multiplication | [20m22s](https://youtu.be/QVKj3LADCnA?t=20m22s)
Column operations of Matrices multiplication | [21m43s](https://youtu.be/QVKj3LADCnA?t=21m43s)
Elementary Matrix | [24m46s](https://youtu.be/QVKj3LADCnA?t=24m46s)
Include all elimination steps in one Matrix | [33m29s](https://youtu.be/QVKj3LADCnA?t=33m29s)

> To do `column operations`, the matrix multiplies on the right. To do `row operations`, the matrix multiplies on the left.

### `Column operation` of Matrices Multiplication

> Below it's a `Column Vector multiplied by a 3x3 Matrix`:
![image](https://user-images.githubusercontent.com/14041622/39472961-f1dfd32c-4d7e-11e8-8c0f-2ebf560526d0.png)

The result  above is a `3x1 Matrix`, which is a `Column vector` again. Because:

**THE RESULT OF THAT COLUMN OPERATION IS A LINEAR COMBINATIONS OF THE COLUMNS.**

> **"A MATRIX TIMES A COLUMN, IS A COLUMN."**


### `Row operation` of Matrices Multiplication

> Below it's a `Row Vector to multiply a 3x3 Matrix`:
![image](https://user-images.githubusercontent.com/14041622/39472895-a9e5568c-4d7e-11e8-9d75-07d5224a3f42.png)

The result above is a `1x3 Matrix`, which is a `Row vector` again. Because:

**THE RESULT OF THAT ROW OPERATION IS A COMBINATION OF THE ROWS.**


### `Elementary Matrix`
> It's also called `Elimination Matrix`.

Simply saying, an `Elementary Matrix` is just an `Identity Matrix` with **ONLY ONE ELEMENT CHANGED**.

![image](https://user-images.githubusercontent.com/14041622/39473567-0bc69f66-4d82-11e8-98d9-d7ff9f49760d.png)

The example above is an `elementary matrix` which only altered the `Row-2 Column-1 entry`, and we'd like to call it the `E₂₁ matrix`, which represents `the elementary matrix which fixed the 2-1 position`.

The reason we need an `elementary matrix` is to apply each one step of `Elimination of linear equations`.
Which means that, 

**FOR EVERY SINGLE STEP OF ELIMINATION, WE NEED AN ELEMENTARY MATRIX.**

So for **two steps of elimination**, we could represent it with `elementary matrices` as below:
![image](https://user-images.githubusercontent.com/14041622/39473976-4b9e3534-4d84-11e8-90bf-4dc88a5ef825.png)

Combining **all elimination steps** in ONE MATRIX:
![image](https://user-images.githubusercontent.com/14041622/39474381-4f43ebf0-4d86-11e8-8b0e-6d3788d67616.png)

### `Permutation Matrix`
> `Permutation Matrix` is used only to **switch positions** of elements in the matrix, without changing any numbers.

Example: To **switch two ROWS of a matrix** by using a `permutation matrix` :
![image](https://user-images.githubusercontent.com/14041622/39474697-cc77de32-4d87-11e8-90ba-f7cff7edd486.png)

Example: To **switch two COLUMNS of a matrix** by using a `permutation matrix`:
![image](https://user-images.githubusercontent.com/14041622/39474756-113f76b0-4d88-11e8-950a-719ba2619094.png)



## Unit 1.3 Multiplication & Inverse Matrices

Lecture outlines | Links
-- | --
Lecture | [0m0s](https://www.youtube.com/watch?v=FX4C-JpTFgY&t=136s&index=3&list=PLE7DDD91010BC51F8)


# `Matrices Elimination`
> `Matrices elimination` (or `solving system of linear equations`) is the very first and fundamental skill throughout Linear Algebra. It's probably the first lesson of all sorts of courses.

## Terminology
Before learning `solving systems of linear equations`, you really need to get familiar with all the core terminologies involved, otherwise it can be very hard to move on to next stage.
And in this case, the best way to learn that is through Wikipedia.

JFR, the core terms are: `Gaussian elimination`, `Gauss-Jordan elimination`, `Augmented Matrix`, `Elementary Row Operations`, `Elementary matrix`, `Row Echelon Form (REF)`, `Reduced Row Echelon Form (RREF)`, `Triangular Form`.

### [`Gaussian elimination`](https://en.wikipedia.org/wiki/Gaussian_elimination)
> It's a `Row reduction algorithm` to solve System of linear equations.

[Refer to simple wiki: Gaussian elimination](https://simple.wikipedia.org/wiki/Gaussian_elimination)
[Example: showme.com](http://www.showme.com/sh/?h=3fjkVEW)

To perform `Gaussian elimination`, the `coefficients of the terms in the system of linear equations` are used to create a type of matrix called an `augmented matrix`. 
Then, `elementary row operations` are used to **simplify** the matrix. 
The **goal** of Gaussian elimination is to get the matrix in `row-echelon form`. 
If a matrix is in `row-echelon form`, which is also called `Triangular Form`.
Some definitions of Gaussian elimination say that the matrix result has to be in `reduced row-echelon form`. 
**Gaussian elimination that creates a reduced row-echelon matrix result is sometimes called `Gauss-Jordan elimination`.**

To be simpler, here is the structure:
- Algorithm: `Gaussian Elimination`
    - Step 1: Rewrite system to a `Augmented Matrix`.
    - Step 2: Simplify matrix with `Elementary row operations`.
    - Result:
        - `Row Echelon Form` or
        - `Reduced Echelon Form`

And if we make the result only in `RREF`, so the name of the algorithm could also be called:
- Algorithm: `Gauss-Jordan Elimination`
    - Step 1: Rewrite system to a `Augmented Matrix`.
    - Step 2: Simplify matrix with `Elementary row operations`.
    - Result: Only in `Reduced Echelon Form`

### `Elementary Row Operations`
Elementary row operations are used to **simplify the matrix**. 

The three types of row operations used are:
- Type 1: **Switching** one row with another **row**.
- Type 2: **Multiplying** a row by a non-zero **number**.
- Type 3: **Adding or subtracting** a row from another **row**.

### Example
Suppose the goal is to find the solution for the linear system below:
![image](https://user-images.githubusercontent.com/14041622/39080182-31be1c9a-455c-11e8-927e-773f3788b77a.png)

First we need to turn it into `Augmented Matrix` form:
![image](https://user-images.githubusercontent.com/14041622/39080192-5804ace8-455c-11e8-96ec-57c0d884a69b.png)

Then we apply `Elementary Row Operations`, and result in `Row Echelon Form`:
![image](https://user-images.githubusercontent.com/14041622/39080203-a26b890a-455c-11e8-9f41-50c66079b22e.png)

At the end, if we'd like, we can further on apply some row operations to get the matrix in `Reduced Row Echelon Form`:
![image](https://user-images.githubusercontent.com/14041622/39080275-2846e60a-455d-11e8-83c5-53b84fd5b45a.png)
Reading this matrix tells us that the solutions for this system of equations occur when x = 2, y = 3, and z = -1.

### `Row Echelon Form vs. Reduced Row Echelon Form`
[Refer to this lecture video: REF & RREF](https://www.youtube.com/watch?v=W01H0LcVUdQ&index=10&list=PLHXZ9OQGMqxfUl0tcqPNTJsb7R6BqSLo6).

## `Augmented Matrix`
> Means we put another column into the matrix, which represents the **Right side** of the system of equations, numbers of right of the `=` sign.

When we apply elimination to `Linear equations`, we operate both sides at the same time. But for computer programmes, it often apply to **Left side**, and remember the operations, a.g. multiply a number or add equations together, when the left side finished then apply the same operations to the right side.

![image](https://user-images.githubusercontent.com/14041622/39471215-829b2d90-4d74-11e8-97b1-7ce730e92e86.png)
