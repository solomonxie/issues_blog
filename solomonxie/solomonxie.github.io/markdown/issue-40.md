# Linear Algebra with Moocs 线性代数课程笔记
> Quick notes on College level of Maths or Stats for machine learning.

## Study resources
- [x] [Slant: What are the best resources to learn linear algebra?](https://www.slant.co/topics/6073/~resources-to-learn-linear-algebra)
- [x] [Pre Linear Algebra notes](https://github.com/solomonxie/solomonxie.github.io/issues/48)
- [x] [ Khan academy Pre-calculus](https://www.khanacademy.org/math/precalculus)
- [ ] [MIT OCW 18.06 SC Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm)
- [ ] [Mathispower4u](http://www.mathispower4u.com/linear-alg.php)
- [ ] [Essence of linear algebra: Youtube](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [ ] [A First Course in Linear Algebra: PDF](https://github.com/solomonxie/solomonxie.github.io/files/1786068/fcla-3.50-A.First.Course.in.Linear.Algebra.-.Robert.A.Beezer.University.of.Puget.Sound.Version.3.50.pdf)

## Practice & Quizzes
- [ ] [Symbolab (Matrices & Vectors Practice)](https://www.symbolab.com/practice/matrices-vectors-practice?lp=no)
- [ ] [Wolframalpha (Problem Generator: Linear Algebra)](https://www.wolframalpha.com/problem-generator/?scrollTo=Linearalgebra)
- [ ] [Uni of Sydney (Quizzes for Linear algebra Math1002)](http://www.maths.usyd.edu.au/u/UG/JM/MATH1002/Quizzes/)
- [ ] [Yu Tsumura (Linear Algebra Problems and Solutions)](https://yutsumura.com/linear-algebra/)

## Study goals of Linear Algebra
- [x] Systems of linear equations
- [x] Row Reduction Echelon Forms (RREF)
- [x] Matrix operations, including inverses
- [x] Block matrices
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


## MIT OCW Linear Algebra 18.06 
- [ ] Unit I: Ax = b and the Four Subspaces
    - [x] The Geometry of Linear Equations (Watched; Practiced 3/3)
    - [x] An overview of key ideas (Watched)
    - [x] Elimination with matrices (Watched)
    - [x] Multiplication and Inverse matrices (Watched; Practiced.)
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





## TL;DR. Archived link: [Vector section notes of Essence Linear Algebra](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-379985082)

## TL;DR Archived link: [MIT OCW Linear Algebra courses list & compare](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-380001327).


# `What is Linear Algebra`

Linear algebra, Matrix algebra, same thing.

![image](https://user-images.githubusercontent.com/14041622/39481781-25f6f346-4d9f-11e8-988e-0c1623e6edca.png)

## Terms sheet
![image](https://user-images.githubusercontent.com/14041622/39066642-51cd6ce2-4508-11e8-9863-4cc7f0497983.png)


## Consistent & Inconsistant
> If there IS solution or solutions to a `Linear system`, then it's consistent. Otherwise, it's Inconsistent.

![image](https://user-images.githubusercontent.com/14041622/39482015-084f14d0-4da0-11e8-8e0a-5cdec4232732.png)

![image](https://user-images.githubusercontent.com/14041622/39482161-86ec503c-4da0-11e8-9e4e-51207852f3c4.png)




# MIT OCW 18.06 SC Unit 1.1 The geometry of linear equations

[Refer to the review pdf.](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/ax-b-and-the-four-subspaces/the-geometry-of-linear-equations/MIT18_06SCF11_Ses1.1sum.pdf)

Lecture video timeline | Links
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
- Type 3: **Adding** a row from another **row**. (!Note: you can only **ADD** them but not **subtract**, but you can **ADD** a negative)

Confusing operation: See where the `negative sign` was put:
![image](https://user-images.githubusercontent.com/14041622/39507688-b0f759aa-4e11-11e8-89b3-69846f64a53a.png)


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

It doesn't really matter it is a `Square Matrix` or not, there could be a `Diagonal` or `Main diagonal`, or you can't draw a diagonal at all. 
The only thing matters is **WHAT ARE ABOVE 1 AND WHAT ARE BELOW 1.**

- REF: For each column, all numbers **below** 1 MUST BE 0. Doesn't matter what numbers are above 1.
- RREF: For each column, all numbers both **above & below** 1 MUST BE 0. We don't care about it if there's no 1 in the column.

![image](https://user-images.githubusercontent.com/14041622/39506655-9e283416-4e0c-11e8-9e58-1df4f85c25e6.png)

## `Augmented Matrix`
> Means we put another column into the matrix, which represents the **Right side** of the system of equations, numbers of right of the `=` sign.

When we apply elimination to `Linear equations`, we operate both sides at the same time. But for computer programmes, it often apply to **Left side**, and remember the operations, a.g. multiply a number or add equations together, when the left side finished then apply the same operations to the right side.

![image](https://user-images.githubusercontent.com/14041622/39471215-829b2d90-4d74-11e8-97b1-7ce730e92e86.png)

If a given Matrix was told it's an `Augmented Matrix`, so we have to assume that the **Last Column** is **The Solution Column**.

![image](https://user-images.githubusercontent.com/14041622/39482311-20236e3e-4da1-11e8-859e-6954b2d33f4a.png)

## `Equivalent systems & Equivalent Matrices`

- Equivalent systems: Linear systems with the SAME SOLUTION SET.
![image](https://user-images.githubusercontent.com/14041622/39482863-30ad3ee0-4da3-11e8-9314-8e6c9010690e.png)
- Equivalent matrices: Two matrices where One Matrix **can be turned** into the other matrix by some `elementary row operations`.
![image](https://user-images.githubusercontent.com/14041622/39482947-735664c4-4da3-11e8-8d4b-fc1b233adc87.png)

## `Pivot`
> Or called the `Cursor`, or `Basic`, or `Basic variable`.

[Refer to this video from mathispower4u.](http://youtu.be/HFbBclH99d0)

It means the value that represents the `unknown variable`  in each column. There's no `pivot` in a column if you can't get a 1 in that column.

![image](https://user-images.githubusercontent.com/14041622/39506959-5ef42898-4e0e-11e8-89e0-8002688d81fb.png)

### `Free variables`
If there's no pivot in a column, that means this `unknown variable` of the column can be **any number**, so we call it a `free variable`.

![image](https://user-images.githubusercontent.com/14041622/39507131-27751b7e-4e0f-11e8-9761-cef7ee48cd64.png)

### `Pivot columns`

The `pivots` are found after `Row Reduction`, and then **go back** to the Original Matrix, the columns **WITH** pivots are called `pivot columns`.

![image](https://user-images.githubusercontent.com/14041622/39507277-ce962f42-4e0f-11e8-8638-917697b3a341.png)

### `Back Substitution`
It's simple: When you solve out one `unknown variable` in the Linear System, you put the value back to other equations. We call this process as `Back Substitution`.

![image](https://user-images.githubusercontent.com/14041622/39522421-b93a512a-4e44-11e8-970c-b965fdee3808.png)



![image](https://user-images.githubusercontent.com/14041622/39527938-55f55a72-4e55-11e8-9f4e-d5ca9a984596.png)



# `Matrix multiplication`

[Refer to this video by mathispower4u](https://www.youtube.com/watch?v=zAjUyPe-4mI&feature=youtu.be)

Practice:
- [ ] [Khan academy (simple)](https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/e/multiplying_a_matrix_by_a_matrix)
- [ ] [Symbolab (simple/advanced)](https://www.symbolab.com/practice/matrices-practice#area=main&subtopic=Multiply&isTour=false)
- [ ] [Wolfram (beginner/Intermediate/Advanced)](https://www.wolframalpha.com/problem-generator/quiz/?category=Linear%20algebra&topic=MultiplyNMatrices)
- [ ] [UOS](http://www.maths.usyd.edu.au/u/UG/JM/MATH1002/Quizzes/quiz7.html)

A fairly simple way to remember how to do `matrix multiplication`:
Assume that two matrices multiply together as `AB = C`.
**You need to write out each entries of the product, and then place this entry with a row of A and a column of B which numbered as subscriptions of this entry.**
e.g., in the `Product Matrix`, C₁₁ represents `Row-1 of A multiplies Column-1 of B`;
C₂₁ represents `Row-2 of A multiplies Column-1 of B`.
So on and so forth, write down all the **entries** of the product entries, and then use `dot product` to calculate each one. 

![image](https://user-images.githubusercontent.com/14041622/39535582-def1e1ea-4e66-11e8-8ce8-26dfac365f3d.png)

## `Properties of matrix multiplication`

[Refer to Khan academy article.](https://www.khanacademy.org/math/algebra-home/alg-matrices/modal/a/properties-of-matrix-multiplication)

![image](https://user-images.githubusercontent.com/14041622/39564456-e4ba295e-4ee6-11e8-89fa-5347281decc4.png)




# MIT OCW 18.06 SC Unit 1.2 Elimination with Matrices
> `Elimination` is the method **EVERY** softwares use to solve `linear equations`.

prerequisites:
- Terminology(Augmented matrix, elementary matrix, pivot, gauss elimination...), included in [this note](https://github.com/solomonxie/solomonxie.github.io/issues/40#issuecomment-383020020).
- Matrix elimination, review [this note](https://github.com/solomonxie/solomonxie.github.io/issues/40#issuecomment-383020020).
- Gauss elimination, review in simple wiki.

Lecture video timeline | Links
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

## `Column operation` of Matrices Multiplication

> Below it's a `Column Vector multiplied by a 3x3 Matrix`:
![image](https://user-images.githubusercontent.com/14041622/39472961-f1dfd32c-4d7e-11e8-8c0f-2ebf560526d0.png)

The result  above is a `3x1 Matrix`, which is a `Column vector` again. Because:

**THE RESULT OF THAT COLUMN OPERATION IS A LINEAR COMBINATIONS OF THE COLUMNS.**

> **"A MATRIX TIMES A COLUMN, IS A COLUMN."**


## `Row operation` of Matrices Multiplication

> Below it's a `Row Vector to multiply a 3x3 Matrix`:
![image](https://user-images.githubusercontent.com/14041622/39472895-a9e5568c-4d7e-11e8-9d75-07d5224a3f42.png)

The result above is a `1x3 Matrix`, which is a `Row vector` again. Because:

**THE RESULT OF THAT ROW OPERATION IS A COMBINATION OF THE ROWS.**


## `Elementary Matrix`
> It's also called `Elimination Matrix`.

[Refer to this amazing good video by Mathispower4u: Elementary Matrices](https://www.youtube.com/watch?v=7H3JFH3IjB0&feature=youtu.be)
[Refer to Mathispower4u: Write a Matrix as a Product of Elementary Matrices](https://www.youtube.com/watch?v=pMp8RfWtPwQ&feature=youtu.be)

Simply saying, an `Elementary Matrix` is just an `Identity Matrix` with **ONLY ONE ELEMENT CHANGED**.

`Elementary Matrix` must be **ONLY ONE ROW OPERATION** away from the `Identity Matrix`.

![image](https://user-images.githubusercontent.com/14041622/39473567-0bc69f66-4d82-11e8-98d9-d7ff9f49760d.png)

The example above is an `elementary matrix` which only altered the `Row-2 Column-1 entry`, and we'd like to call it the `E₂₁ matrix`, which represents `the elementary matrix which fixed the 2-1 position`.

The reason we need an `elementary matrix` is to apply each one step of `Elimination of linear equations`.
Which means that, 

**FOR EVERY SINGLE STEP OF ELIMINATION, WE NEED AN ELEMENTARY MATRIX.**

So for **two steps of elimination**, we could represent it with `elementary matrices` as below:
![image](https://user-images.githubusercontent.com/14041622/39473976-4b9e3534-4d84-11e8-90bf-4dc88a5ef825.png)

Combining **all elimination steps** in ONE MATRIX:
![image](https://user-images.githubusercontent.com/14041622/39474381-4f43ebf0-4d86-11e8-8b0e-6d3788d67616.png)

## `Permutation Matrix`
> `Permutation Matrix` is **ANOTHER TYPE OF ELEMENTARY MATRIX**, and used only to **switch positions** of elements in the matrix, without changing any numbers.

Review [Dr. Strang's lecture](https://www.youtube.com/watch?v=QVKj3LADCnA&feature=youtu.be&t=36m42s).

Example: To **switch two ROWS of a matrix** by using a `permutation matrix` :
![image](https://user-images.githubusercontent.com/14041622/39474697-cc77de32-4d87-11e8-90ba-f7cff7edd486.png)

Example: To **switch two COLUMNS of a matrix** by using a `permutation matrix`:
![image](https://user-images.githubusercontent.com/14041622/39474756-113f76b0-4d88-11e8-950a-719ba2619094.png)

### `Some common permutation matrices`

![image](https://user-images.githubusercontent.com/14041622/39619697-5605a320-4fbb-11e8-89b6-51a9490314c7.png)




# MIT OCW 18.06 SC  Unit 1.3 Multiplication & Inverse Matrices

prerequisites:
- Matrix multiplication basics(row * col), review [this note](https://github.com/solomonxie/solomonxie.github.io/issues/40#issuecomment-386033645).
- Elementary matrices, review [this video](https://www.youtube.com/watch?v=1SoU0BfhKaI&feature=youtu.be)

[Refer to Juanklopper's jupyter notebook.](https://github.com/solomonxie/jupyter-notebooks/blob/master/forks/MIT_OCW_Linear_Algebra_18_06-master/I_04_Matrix_multiplication_Inverses.ipynb)

Lecture timeline | Links
-- | --
Lecture | [0m0s](https://www.youtube.com/watch?v=FX4C-JpTFgY&t=136s&index=3&list=PLE7DDD91010BC51F8)
Method 1: Multiply matrix by vector | [50s](https://youtu.be/FX4C-JpTFgY?t=50s)
When allowed to multiply matrices | [4m38s](https://youtu.be/FX4C-JpTFgY?t=4m38s)
Method 2: Multiply matrix by COLUMN | [6m12s](https://youtu.be/FX4C-JpTFgY?t=6m12s)
Method 3: Multiply ROW by matrix | [10m4s](https://youtu.be/FX4C-JpTFgY?t=10m4s)
Method 4: Multiply COLUMN by ROW | [11m37s](https://youtu.be/FX4C-JpTFgY?t=11m37s)
Method 5: Block Multiplication | [18m25s](https://youtu.be/FX4C-JpTFgY?t=18m25s)
Inverse Matrices (Square matrices) | [21m15s](https://youtu.be/FX4C-JpTFgY?t=21m15s)
Invertible Matrix | [22m0s](https://youtu.be/FX4C-JpTFgY?t=22m)
Singular Matrix (No-inverse matrix) | [24m39s](https://youtu.be/FX4C-JpTFgY?t=24m39s)
Calculate Inverse of Matrix | [31m52s](https://youtu.be/FX4C-JpTFgY?t=31m52s)
Gauss-Jordan Elimination to solve Inverse of a matrix | [35m20s](https://youtu.be/FX4C-JpTFgY?t=35m20s)

![image](https://user-images.githubusercontent.com/14041622/39558587-692a7a7e-4ec2-11e8-86ed-81f3087d761a.png)


## `Method 1: Multiply matrix by vector`

Calculation of an entry of the Product Matrix.

![image](https://user-images.githubusercontent.com/14041622/39560053-60299bb6-4ecd-11e8-988c-c8359b65fdbc.png)


![image](https://user-images.githubusercontent.com/14041622/39558944-429fcc62-4ec5-11e8-809b-8be93a1660cb.png)

## `Method 2: Multiply matrix by COLUMN`

Each **column** of the `product matrix C`, is `Matrix A * Column of B`.

![image](https://user-images.githubusercontent.com/14041622/39559663-7857ec9a-4eca-11e8-9a71-c969fa48bac6.png)

## `Method 3: Multiply ROW by matrix`

Each **row** of the `product matrix C`, is `Row of A * Matrix B`.

![image](https://user-images.githubusercontent.com/14041622/39559794-77f07a8c-4ecb-11e8-82af-4cdd8c8d9821.png)


## `Method 4: Multiply COLUMN by ROW`

![image](https://user-images.githubusercontent.com/14041622/39559955-ab9ad82c-4ecc-11e8-9d7e-790b76d79975.png)

### `Dot product`
![image](https://user-images.githubusercontent.com/14041622/39560005-08e11582-4ecd-11e8-8f10-53322d584bb3.png)


## `Method 5: Block multiplication`

You can cut each matrix to blocks, each block is no necessary to be equal sized as long as they can match each other well.

![image](https://user-images.githubusercontent.com/14041622/39560231-e0a54096-4ece-11e8-99c7-5d64c5e739ad.png)

After you cut matrices into blocks, the multiplication will just be like a smaller matrix multiplication: **Each block can be seen as a number in a matrix.**

![image](https://user-images.githubusercontent.com/14041622/39560200-a36da5f6-4ece-11e8-9c9b-c729f0418abd.png)

## `Inverses (Square matrices)`

If a matrix's inverse exists, then we call this matrix `Invertible`, or `Non-singular`.

And only with `square matrices`, the inverse can be both **right side** or **left side** with the original matrix to produce the `Identity Matrix`.

![image](https://user-images.githubusercontent.com/14041622/39560342-d9d403f0-4ecf-11e8-8526-c704ad2d4811.png)

### `Singular Matrix (No inverse)`

Simplest way to tell if it's a `singular matrix` is to calculate its `Determinant` which we learnt in high school: It's a singular matrix if its determinant is ZERO.
But there's another way to tell:

![image](https://user-images.githubusercontent.com/14041622/39560934-b1d24c04-4ed4-11e8-9d8c-c0331fc8b2db.png)


## `Use Gauss-Jordan Elimination to get Inverse`

**THIS METHOD IS SO MUCH EASIER TO GET THE INVERSE THAN THE WAY WE LEARNT IN HIGH SHCOOL WHICH LETS YOU TO CALCULATE ALL DETERMINANT, ADJUGATE AND COFACTOR AND SO ON.**

[Refer to Khan academy lecture: Inverting a 3x3 matrix using Gaussian elimination.](https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-determinants-and-inverses-of-large-matrices/v/inverting-matrices-part-3)

[Online Calculator.](https://www.symbolab.com/solver/step-by-step/inverse%20%5Cbegin%7Bpmatrix%7D1%262%261%5C%5C%202%260%260%5C%5C%200%260%262%5Cend%7Bpmatrix%7D)

Practice for Gauss-Jordan Elimination to get Inverse of a matrix:
- [ ] [Khan academy](https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-determinants-and-inverses-of-large-matrices/e/matrix_inverse_3x3)
- [ ] [Symbolab](https://www.symbolab.com/practice/matrices-practice#area=main&subtopic=Inverse&isTour=false)
- [ ] [Wolfram](https://www.wolframalpha.com/problem-generator/quiz/?category=Linear%20algebra&topic=Inverse2Matrix)
- [ ] [UOS](http://www.maths.usyd.edu.au/u/UG/JM/MATH1002/Quizzes/quiz8.html)

![image](https://user-images.githubusercontent.com/14041622/39561075-e257821c-4ed5-11e8-922d-8158a6587525.png)

With this formula above, we got TWO equations, which will help us form a **system of equations**!
That's where Gauss comes in: we **AUGMENT TWO COLUMNS** to the matrix.

![image](https://user-images.githubusercontent.com/14041622/39561501-a6a297d6-4ed8-11e8-9a18-f92b4b309ad2.png)

Why could we use Gauss-Jordan Elimination to solve `Inverse of matrix`?

![image](https://user-images.githubusercontent.com/14041622/39561633-7483dae8-4ed9-11e8-996c-703cc2fcabb4.png)

The `E` above represents `all elementary matrices`.

[For refreshing `how to get elementary matrices` please refer to this video by mathispower4u](https://www.youtube.com/watch?v=1SoU0BfhKaI&feature=youtu.be)
![image](https://user-images.githubusercontent.com/14041622/39562501-89d4b1d8-4ede-11e8-8b38-b46d31ee20cb.png)



# MIT OCW 18.06 SC  Unit 1.4 Factorization into A = LU

prerequisites:
- Matrix Inverses
- Matrix multiplication
- Elementary Matrix
- Permutation Matrix

Lecture timeline | Links
-- | --
Lecture | [0m0s](https://www.youtube.com/watch?v=MsIvs_6vC38&t=130s&index=4&list=PLE7DDD91010BC51F8)
What's the Inverse of a Product | [0m25s](https://youtu.be/MsIvs_6vC38?t=25s)
Inverse of a Transposed Matrix | [4m2s](https://youtu.be/MsIvs_6vC38?t=4m2s)
How's A related to U | [7m51s](https://youtu.be/MsIvs_6vC38?t=7m51s)
3x3 LU Decomposition (without Row Exchange) | [13m53s](https://youtu.be/MsIvs_6vC38?t=13m53s)
L is product of inverses | [16m45s](https://youtu.be/MsIvs_6vC38?t=16m45s)
How expensive is Elimination | [26m5s](https://youtu.be/MsIvs_6vC38?t=26m5s)
LU Decomposition (with Row exchange) | [40m18s](https://youtu.be/MsIvs_6vC38?t=40m18s)
Permutations for Row exchanges | [41m15s](https://youtu.be/MsIvs_6vC38?t=41m15s)



![image](https://user-images.githubusercontent.com/14041622/39564033-17aaeb3e-4ee5-11e8-9bd9-d998edfad405.png)

> "`A = LU` is the BIG FORMULA for elimination. It's a great way to look at Gaussian Elimination."

## `What's the Inverse of a product`
Assume `A & B` are all invertible matrices, so what is `(AB)⁻¹`?

Yes, we multiply their inverses together `A⁻¹ & B⁻¹`, but in what order do we multiply these inverses?
**IN REVERSE ORDER.**
Which makes:
`(AB)(B⁻¹A⁻¹) = 𝐈` or `(B⁻¹A⁻¹)(AB) = 𝐈`. They perform in the same way get the same result.

![image](https://user-images.githubusercontent.com/14041622/39616176-bbd17dc8-4fac-11e8-99ca-ef76bd1bc55b.png)
so:

**`(AB)⁻¹ = (B⁻¹A⁻¹)`**


## `Inverse of a Transposed Matrix`
![image](https://user-images.githubusercontent.com/14041622/39616136-80e71ede-4fac-11e8-87a6-e22360a42818.png)

So the Inverse of `(Aᵀ)⁻¹ = (A⁻¹)ᵀ`


## `LU Decompose (without Row Exhcnage)`

> "L is the product of Inverses."

**`L = E⁻¹`, which means L is the inverse of `elementary matrix`.**

![image](https://user-images.githubusercontent.com/14041622/39617446-580782dc-4fb2-11e8-8ed5-99b2e45cf696.png)

Assume in the elimination process without row exchanges, we only apply `elementary matrices` to the matrix one by one.
So the `L` would be the **Inverse** of those elementary matrices, but in **Reverse order**.

![image](https://user-images.githubusercontent.com/14041622/39617696-45d219b4-4fb3-11e8-87e0-18d5dcec3dde.png)

```py
EA = U
A = LU
```

![image](https://user-images.githubusercontent.com/14041622/39618742-b5a2062e-4fb7-11e8-9fbc-b715793b9963.png)

> So that steps above is the `Inverse Elementary Matrices` picture of getting the L. 
But actually what actually we get is really simple to observe:
**If no row exchanges, multipliers go directly into L.**

So as we've understood the meaning behind it, we can forget it and just remember the **`multipliers`**.



## `LU Decomposition (with Row exchange)`

### `Permutations means Row exchanges or Column Exchanges`

For a 3x3 Identity Matrix, there're 6 permutations of it:
![image](https://user-images.githubusercontent.com/14041622/39620002-460a70a8-4fbc-11e8-8e4b-5ee3ef3b9f7f.png)


**The `Inverse of a Permutation` is its `Transpose`**:

![image](https://user-images.githubusercontent.com/14041622/39619970-2c5b12c0-4fbc-11e8-9cef-03ac2fc3238d.png)



# `LU Decomposition`

For a Matrix A, we could factor it out as `A = LU`, just like we factor a number to two numbers.

[`Online LU Decomposition Calculator`](https://www.wolframalpha.com/input/?i=LU+decomposition+of+%7B%7B7,3,-11%7D,%7B-6,7,10%7D,%7B-11,2,-2%7D%7D&lk=3)

![image](https://user-images.githubusercontent.com/14041622/39573271-176de746-4f05-11e8-9309-26d7d0f664ac.png)

## `Upper Triangular Matrix`

The factor matrix `U` represents the `Upper Triangular Matrix`, which we're already familiar with: the matrix we've got after `Gauss Elimination`.

Refer to video:[ LU Decomposition using Gaussian Elimination](https://www.youtube.com/watch?v=jbeX2HCW6OE)

![image](https://user-images.githubusercontent.com/14041622/39575064-d1531996-4f0b-11e8-995e-239df4d1214a.png)


## `Lower Triangular Matrix`

The factor matrix `L` is not hard to get as well: 
**All the numbers in this matrix are `factor numbers` we used in each elimination step.**

![image](https://user-images.githubusercontent.com/14041622/39574447-d81f9198-4f09-11e8-946d-1f1274111884.png)

### `How to get the Lower Triangular Matrix`

[Refer to this video: LU Decomposition - Shortcut Method by Math is power](https://www.youtube.com/watch?v=UlWcofkUDDU)


## `Solve System of equations using LU Decomposition`
> The final **goal** of learning `LU Decomposition` is to **solve Linear systems**.

[Refer to this video: Solve a System of Linear Equations Using LU Decomposition](https://www.youtube.com/watch?v=m3EojSAgIao&feature=youtu.be)

Assume there's equation `AX = B` as below, and we're to solve for `X`: 
![image](https://user-images.githubusercontent.com/14041622/39588763-ffebdd56-4f2e-11e8-8a07-891176ba45e8.png)

Steps to apply the `LU Decomposition` to solve the Linear System:
- Decompose LU, and represent `AX = B` as `LUX = B`
![image](https://user-images.githubusercontent.com/14041622/39590029-47d16bf6-4f32-11e8-9fec-3c8b8f69b577.png)
- Let `Y = UX`, then solve `LY = B` for `Y`
![image](https://user-images.githubusercontent.com/14041622/39589780-b2228144-4f31-11e8-93f7-29aecf55d008.png)
- Solve `Y = UX` for `X`
![image](https://user-images.githubusercontent.com/14041622/39589848-e32dfdf4-4f31-11e8-8856-20deeb25fc7b.png)



