# Linear Algebra with Moocs 线性代数课程笔记
> Quick notes on College level of Maths or Stats for machine learning.

## Study resources
- [ ] [Slant: What are the best resources to learn linear algebra?](https://www.slant.co/topics/6073/~resources-to-learn-linear-algebra)
- [x] [High school maths notes](https://github.com/solomonxie/solomonxie.github.io/issues/44)
- [x] [ Khan academy Pre-calculus](https://www.khanacademy.org/math/precalculus)
- [ ] [MIT OCW 18.06 SC Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm)
- [ ] [Essence of linear algebra: Youtube](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [ ] [A First Course in Linear Algebra: PDF](https://github.com/solomonxie/solomonxie.github.io/files/1786068/fcla-3.50-A.First.Course.in.Linear.Algebra.-.Robert.A.Beezer.University.of.Puget.Sound.Version.3.50.pdf)

## MIT OCW Linear Algebra 18.06 
- [ ] Unit I: Ax = b and the Four Subspaces
    - [ ] The Geometry of Linear Equations (Watched; Practiced 3/3)
    - [ ] An overview of key ideas
    - [ ] Elimination with matrices
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

## Review hardcore quiz
- [ ] [Precalculus](https://www.khanacademy.org/math/precalculus?t=practice#precalc-matrices)
    - [ ] [Conversion of complex numbers](https://www.khanacademy.org/math/precalculus/imaginary-and-complex-numbers/modal/quiz/polar-form-of-complex-numbers-quiz)

![image](https://user-images.githubusercontent.com/14041622/39066642-51cd6ce2-4508-11e8-9863-4cc7f0497983.png)



## TL;DR. Archived link: [Vector section notes of Essence Linear Algebra](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-379985082)


## TL;DR Archived link: [MIT OCW Linear Algebra courses list & compare](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-380001327).


# MIT OCW 18.06 - Unit 1.1 The geometry of linear equations

[Refer to the review pdf.](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/ax-b-and-the-four-subspaces/the-geometry-of-linear-equations/MIT18_06SCF11_Ses1.1sum.pdf)

Long lecture video outlines: [Matrix picture](https://youtu.be/ZK3O402wf1c?t=2m47s), [Row picture](https://youtu.be/ZK3O402wf1c?t=3m41s), [Column picture](https://youtu.be/ZK3O402wf1c?t=8m41s), [Matrix picture in 3D](https://youtu.be/ZK3O402wf1c?t=15m26s), [Row picture in 3D: intersects of planes](https://youtu.be/ZK3O402wf1c?t=17m33s), [Column picture in 3D](https://youtu.be/ZK3O402wf1c?t=23m11s)

> "The fundamental problem of linear algebra is to solve n linear equations in `n` unknowns."

![image](https://user-images.githubusercontent.com/14041622/38993221-93ad3a46-4415-11e8-8d2f-c3c88abac23b.png)

We view this problem in three ways:
- `Row picture`: Each row is an equation, and we could draw out each line equation on the graph.
![image](https://user-images.githubusercontent.com/14041622/38993085-38d02db8-4415-11e8-96d8-2f0b0ba20c90.png)
- *`Column picture`: Rewrite equations in the form below, and each column is a vector, and we could each vector (with scalar) on the graph.
![image](https://user-images.githubusercontent.com/14041622/38993157-6636c2da-4415-11e8-9833-a0d61e68f58d.png)
![image](https://user-images.githubusercontent.com/14041622/38993091-3ed60e8a-4415-11e8-81a3-33ba90a04e84.png)
- `Matrix picture`: Rewrite equations into `Coefficient Matrix form`, and see the geometric meaning of a matrix and vector.
![image](https://user-images.githubusercontent.com/14041622/38993281-bc62a2f0-4415-11e8-8489-044900a93d7b.png)




# `Solving System of Linear Equations`

## `Row Echelon Form vs. Reduced Row Echelon Form`
[Refer to this lecture video: REF & RREF](https://www.youtube.com/watch?v=W01H0LcVUdQ&index=10&list=PLHXZ9OQGMqxfUl0tcqPNTJsb7R6BqSLo6).