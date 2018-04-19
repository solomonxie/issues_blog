# Linear Algebra from the ground up 线性代数从零学起
> Quick notes on College level of Maths or Stats for machine learning.

## Survey
[Slant: What are the best resources to learn linear algebra?](https://www.slant.co/topics/6073/~resources-to-learn-linear-algebra)

## Study resources
- [x] [High school maths notes](https://github.com/solomonxie/solomonxie.github.io/issues/44)
- [x] [ Khan academy Pre-calculus](https://www.khanacademy.org/math/precalculus)
- [ ] [MIT OCW 18.06 SC Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm)
- [ ] [Essence of linear algebra: Youtube](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [ ] [A First Course in Linear Algebra: PDF](https://github.com/solomonxie/solomonxie.github.io/files/1786068/fcla-3.50-A.First.Course.in.Linear.Algebra.-.Robert.A.Beezer.University.of.Puget.Sound.Version.3.50.pdf)

## Prerequisites
Vectors:
- [ ] Trigonometry: Unit circle, Inverse trig function
- [ ] Geometry: Transformation
- [ ] Precalculus: Conversion of complex numbers
- [ ] Algebra: Line equation

Matrices:
- [ ] Algebra: Systems of equations
- [ ] Vector: Dot product & Cross product


## Study goals of Linear Algebra
- [ ] Systems of linear equations
- [ ] Row reduction and echelon forms
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

## TOC TO-DO LIST
Khan Academy:
- [x] [Precalculus](https://www.khanacademy.org/math/precalculus?t=practice)

Introduction to Linear Algebra by Gilbert Strang:
- [ ] 1.Introduction to Vectors
    - [ ] 1.1 Vectors and Linear Combinations
    - [ ] 1.2 Lengths and Dot Products
    - [ ] 1.3 Matrices
- [ ] 2.Solving Linear Equations
- [ ] 3.Vector Spaces & Subspaces

MIT OCW Linear Algebra 18.06:
- [ ] Unit I: Ax = b and the Four Subspaces
    - [ ] The Geometry of Linear Equations
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

## Review hardcore quiz
- [ ] [Precalculus](https://www.khanacademy.org/math/precalculus?t=practice#precalc-matrices)
    - [ ] [Conversion of complex numbers](https://www.khanacademy.org/math/precalculus/imaginary-and-complex-numbers/modal/quiz/polar-form-of-complex-numbers-quiz)


## TL;DR. Archive Link: [why do I need to learn Linear Algebra?](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-368829945)


## TL;DR. Archived link: [Vector section notes of Essence Linear Algebra](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-379985082)


## TL;DR Archived link: [MIT OCW Linear Algebra courses list & compare](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-380001327).


# `Vector & basic operations`

## What is a vector
> Definition: vector is a **MAGNITUDE** with a **DIRECTION**

Notation: 
- `v` as a vector.
- `|v|` or `||v||` as its **Magnitude**, or **Length**, or **Distance**, or **Absolute value**, same idea
- **Slope or angle** as its **Direction.**
- `(a, b)` the two position there are called `X-component & Y-component`.

It's not hard to understand the basic ideas of a vector, which consists of very basic knowledges form what we learned previously in high school:
- Magnitude of vector: is the same with calculating the **distance of two points**
- Direction of vector: is the same with calculating the **slope of a line**.

### `Distance` vs. `Displacement`
- Distance is a **scalar** ("3 km")
- Displacement is a **vector** ("3 km Southeast")
![image](https://user-images.githubusercontent.com/14041622/38606213-fe8d426c-3da7-11e8-8851-9b3c67e7d5cd.png)

### `Speed` vs `Velocity`
- Speed is how fast something moves.
- Velocity is speed with a direction.

## `UNDERSTAND VECTOR'S MOVEMENT`
Now we got a vector start from `(-3,8)` to the point `(4, 5)`.  
We say this vector has a magnitude `||v|| = √40` and has a direction to the bottom right.
But we could also represent the vector as only `one point with two components`: `(7, -3)`.
Which has a **HIDDEN INFORMATION** that it start from the **origin** and direction is to the point `(7, -3)`.
Are they different vectors? NO! They're the same vector, just starts at different places.
> Because **vector doesn't specify where it starts.** A vector only means `A magnitude & a direction`.

That's why we could represent a vector in two ways:
- `v is (-3,8) to (4, 5)`
- `v = (7, -3)`

**IT'S VERY IMPORTANT TO UNDERSTAND THIS IDEA, SO THAT WE COULD FURTHER UNDERSTAND WHY WE COULD MOVE VECTORS, AND BY SO WE COULD DO SUMS AND MULTIPLICATIONS AND SO ON**

## Adding & subtracting vectors
> "Linear algebra is built on these operations `v + w` and `cv`: **Adding vectors and multiplying by scalars.**" - Gilbert Strang

Adding & subtracting could be seen as a movement to a vector, or say how it travels.
![image](https://user-images.githubusercontent.com/14041622/38543990-bef3a65c-3cd8-11e8-877c-2e23ea719208.png)

[Refer to Maths is fun.](http://www.mathsisfun.com/algebra/vectors.html)

- Adding vectors:
![image](https://user-images.githubusercontent.com/14041622/38543941-9acd84b4-3cd8-11e8-9314-9a6e8ac975a8.png)

- Subtracting vectors: is just **ADDING** a **NEGATIVE VECTOR**
![image](https://user-images.githubusercontent.com/14041622/38543960-ab2d4844-3cd8-11e8-8a08-3608c9221275.png)

### `Understand vector's addition & subtraction`
Refer to _Intro to Linear Algebra by Gilbert Strang: 1.1_.

**"You can't add apples and oranges."**
But you can add **fruits**!
Imagine you have one bag of fruits `(3 apples, 4 oranges)`, and another bag of fruits `(1 apple, 2 oranges)`.
So adding them together you will get one big bag of fruits `(4 apples, 6 oranges)`,
from this big bag you could also split a smaller bag of fruits, and then you will call it `subtraction`.

A vector is the very idea of **a bag of fruits**.


## `Scalar Multiplication`
> It's the same with the section `DILATION` or `Scaling` in Geometry. 

Just for review of `dilating` a graph geometrically:
When you scale a graph by a factor:
- Every line of the graph scale by the SAME factor
- Every line will be PARALLEL to its origin line.

[Refer to previous note: Transformation.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-371067923)

![image](https://user-images.githubusercontent.com/14041622/38544907-56398f66-3cdb-11e8-8958-9628d87444ee.png)



# Vector forms

[Refer to Khan academy article.](https://www.khanacademy.org/math/precalculus/vectors-precalc/magnitude-direction/a/vector-forms-review)

![image](https://user-images.githubusercontent.com/14041622/38547847-c2e1b29a-3ce2-11e8-9464-a5fbba606102.png)

In Gilbert Strang's _Intro to Linear Algebra_, it's different point of view:

For row form or column form:
- `Row form`: v = (1, 1, -1)
- `Column form`: 
![image](https://user-images.githubusercontent.com/14041622/38878583-dfea6254-4293-11e8-896c-8d77dc9f8cfb.png)
> "The reason for the row form (in parentheses) is to save space. But v = (1,1, -1) is not a row vector! It is in actuality a column vector, just temporarily lying down. "

For representing method:
![image](https://user-images.githubusercontent.com/14041622/38878751-4877e99a-4294-11e8-9e86-aee4d47bf80b.png)



## Unit vectors
> Simply say, a `unit vector` is just a vector which length is `1`. Kinda like the unit circle idea.
It's also called `Engineering notation`, or the `basis vector`.

![image](https://user-images.githubusercontent.com/14041622/38917048-17088350-431c-11e8-9f52-3da7b4e8fced.png)
Which means, it could lie on axis or in between.

![image](https://user-images.githubusercontent.com/14041622/38659785-831c216e-3e5d-11e8-8623-77fcc365adcb.png)

**What's it for?**
Basically just like the unit circle, make things easier to calculate angles or length or so. 
Actually it's working together with unit circle and all other trigonometric knowledges.
so, 
**UNIT VECTOR IS RATHER A TRIGONOMETRIC WAY TO DEAL WITH VECTORS.**
Easier to think about it, is to think about the `Similar graph` knowledge in the `Dilation` section. 


### `Standard Basis Vectors` & `Unit vector form`
> It's also called `Unit Basis Vectors`.
`Unit vector` is easy, but `unit vector form` needs your bit more effort to understand.

**THIS FORM DOESN'T PRESENT VECTOR AS A POSITION ANYMORE, RATHER PRESENT IT AS HOW MUCH IT STRETCHES UNIT VECTORS, OR SAY PRESENT IT AS A SCALAR.**

Assume that there are **TWO** unit vectors, one vertical, one horizontal.
![image](https://user-images.githubusercontent.com/14041622/38548131-9347693e-3ce3-11e8-9600-3b5ee57e70ed.png)

![image](https://user-images.githubusercontent.com/14041622/38547964-1747a326-3ce3-11e8-9f99-ea9024e007fd.png)

### `How to find a vector's unit vector`
> More intuitively to solve it just to draw it out and solve it with trigonometry. 

![image](https://user-images.githubusercontent.com/14041622/38602559-b0cc106c-3d9d-11e8-9e63-651ac3ab4daf.png)

Example: Find the unit vector of vector (-8, 5)
![image](https://user-images.githubusercontent.com/14041622/38602586-cbb09484-3d9d-11e8-8c2d-35d1a71daa06.png)


## `Convert between vector forms`

**HIGHLY RECOMMEND TO REVIEW THE COMPLEX NUMBER CONVERSION SKILLS, HAVING THE VERY SAME IDEA.**
[Refer to previous note: complex number forms conversion skills.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-379646389)

### `How to find the direction angle of a vector`
> It's the very same problem of the topic `Inverse trig function`. 

**NOT EASY! NEED TO CONSIDER LOTS OF CONDITIONS, LIKE QUADRANTS, POSSIBLE SOLUTIONS, PRINCIPLE SOLUTION AND SO. RECOMMEND TO REVIEW INVERSE TRIG FUNCTIONS.**

[Refer to previous notes: Inverse Trigonometric equations.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-377686394)

Example: Find the direction angle of vector `(-2, 5)` between 0° to 360°.
Solve:
- `tanθ = (-5/2)`
- `θ₁ = -68.2`
- `θ₂ = 180° + -68.2 = 111.8` because θ₁ is negative could use this trig identity.
- Vector `(-2, 5)` is located on Quadrant-2, 
- So the answer is `111.8`.


# Vector span
**It's extending the `unit vector` idea.**

Refer to famous visualisation of 3Blue1Brown's video: [Linear combinations, span, and basis vectors](https://www.youtube.com/watch?v=k7RM-ot2NWY&t=0s&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=3)

## `R²` and `R³`
`R²` means a `Real numbers 2D plane`.
Usually the `X/Y Axes plane` is this one.

`R³` means `Real numbers 3D plane`.
Usually the `X/Y/Z Axes plane`.

## `Linear combinations (Vector Addition)`
> DEFINITION: The sum of `cv` and `dw` is a linear combination of `v` and `w`.

`Linear combinations` means to add vectors together: `v₁ + v₂ + v₃.....` to get a new vector. Simple like that.

## `Span of vectors`
> It's the Set of all the `linear combinations` of two vectors.
![image](https://user-images.githubusercontent.com/14041622/38660579-4af5843a-3e60-11e8-8143-ca0ab77198f1.png)


```py
# v, w are vectors
span(v, w) = R²

span(0) = 0
```

`One vector` with a `scalar`, no matter how much it stretches or shrinks, **it ALWAYS on the same line**, because the direction or slope is not changing. So **ONE VECTOR'S SPAN IS A LINE.**

`Two vector` with `scalars`, we then **COULD** change the slope! So that we could get to any position that we want in the 2D plane, i.e., R².

Exceptions:
- `span(0) = 0`, it only stay at origin.
- `v = w`, if two vectors are the same, or `collinear`, then it's still ONE vector.

## `Linearly dependent & independent`

- `Linear dependence`: two vectors are **`COLLINEAR`**, means on the same line.
- `Linear independence`: two vectors are **`NOT COLLINEAR`**, means they're not on the same line.

Vectors `(2, 3)` and `(4, 6)` are the **SAME VECTOR**! 
Because `(4,6) = 2*(2,3)`, so it's just a scaled version of the first vector.

So we say the vectors `(2, 3)` and `(4, 6)` are **`DEPENDENT`**, because they're **`COLLINEAR`**.

Other than that, any two vectors are **`INDEPENDENT`**, if they're not **NOT COLLINEAR**.


### List of some linear combinations
Let's list some `vector combinations`:
- Zero Vector: `span(0) = 0`.
- One vector: `span(v) = a line`.
- Two vector: `span(v₁, v₂) = R²`, if they're not collinear.
- Three vector or more: `span(v₁, v₂, v₃...) = R²`. Other than two vectors, are all **`REDUNDANT`**. 
In another word:
**IF ANY TWO VECTORS ARE INDEPENDENT, THEN OTHERS ARE ALL DEPENDENT.**

### How to know whether a linear combination is dependent

[Refer to Khan lecture: Span and linear independence example](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/linear-independence/v/span-and-linear-independence-example)

A `linear combination` is **dependent**, **iff** it could satisfy this equation:
```py
c₁v₁ + c₂v₂ + c₃v₃ .... = 0
```
`c..` means the scalar for each vector, and you could change the scalar to any number, positive or negative.
Note that: `c ≠ 0`, and vectors are not all zeros.

Assume that there's a linear combination of two vectors `v₁ + v₂ + v₃`, 
with scalars it could be `c₁v₁ + c₂v₂ + c₃v₃`.
To verify whether it's dependent or independent, 
we assume `c₁v₁ + c₂v₂ + c₃v₃= (0,0,0)` and solve for `c₁, c₂, c₃`:
- it's **independent** <=> if `c₁ = c₂ = c₃ = 0` **all** are zeros
- it's **dependent** <=> If `c₁, c₂, c₃` **at least one** is NON-ZERO number

Example 1: `Is vectors (2,1) and (3,2) dependent or independent?`
Solve:
- Assume `c₁(2,1) + c₂(3,2) = (0,0)`
- Get system of equations:
    - `2c₁ + 3c₂ = 0`
    - `1c₁ + 2c₂ = 0`
- Solve system of equations get: `c₁=c₂=0`
- So it's a **independent linear combination**.

Example 2: `Is vectors (1,-1,2), (1,1,3) and (-1,0,2) dependent or independent?`
- Assume `c₁v₁ + c₂v₂ + c₃v₃= (0,0,0)`
- get the system of equations of 3 unknowns `c₁, c₂, c₃`
- solve equations get solutions get `c₁ = c₂ = c₃ = 0`
- So they're **independent**.


# `Vectors multiplication`
> Vector multiplication is FUNDAMENTAL skill to solve `Matrices multiplication`.

**THE VERY FIRST THING TO DO WITH A `VECTOR MULTIPLICATION` OR `MATRIX MULTIPLICATION`, IS TO FORGET EVERYTHING ABOUT `ARITHMETIC MULTIPLICATION` !!**
OTHERWISE, YOU WILL FALL INTO AN ENDLESS CONFUSION!

Just to know, multiplication of vectors or matrices, **AREN'T** really multiplication, but just look like that. You can see them as **operations to get SOMETHING**.

There're two operations are called `multiplication` for vectors:
- `Dot product`: express as `V₁ · V₂`, named for the dot symbol. It's meant to get the `Product of two magnitudes`.
- `Cross product`: express as `V₁ × V₂`, named for the cross symbol. It's meant to get a `new vector`.

> The `cross product` is very very very limited in use, and NOT as fairly often in use as the `dot product`. So don't waste time on this unless having certain use of it.


## `Boosting`
**IT'S THE VERY CORE SENSE OF MAKING A MULTIPLICATION OF VECTORS OR MATRICES.**

Multiplication **ISN'T** just `Repeat counting in Arithmetic` anymore.
Not `4×3 = 4+4+4` anymore!

It's rather kind of `Growth`, or empowerment, or **boosting**.
We'd say `we tripled 4`, or say `number 4 grow with speed of 3`, or to say `number 4 grows with a boosting of 3`.
Whatever you'd say, you get the idea.
Multiplication a process of `double, triple, quadruple ...`.

**JUST TO REMEMBER: FORGET ABOUT ARITHMETIC MULTIPLICATION, ALWAYS SEE MULTIPLICATION AS BOOSTING.**

## `Dot product`
**REMEMBER: A DOT PRODUCT DOESN'T GIVE YOU A VECTOR, BUT ONLY A NUMBER, A SCALAR, A PRODUCT OF TWO MAGNITUDES.**

> The purpose:
It is **NOT** to get a new vector, and **NOT** to `Reduce dimension`, 
its only purpose **IS** to get a **quantity**, a magnitude, a number!

[For an intuitive video refer to Khan academy physics: Dot Product.](https://www.khanacademy.org/science/physics/magnetic-forces-and-magnetic-fields/electric-motors/v/the-dot-product)
[For more explains in detail: Vector Calculus: Understanding the Dot Product](https://betterexplained.com/articles/vector-calculus-understanding-the-dot-product/)
[Maths is fun: dot product.](https://www.mathsisfun.com/algebra/vectors-dot-product.html)
[3Blue1Brown: Dot products and duality | Essence of linear algebra](https://www.youtube.com/watch?v=LyGKycYT2v0&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=10)

![screencast 2018-04-12 15-08-30](https://user-images.githubusercontent.com/14041622/38661569-e3831bc4-3e63-11e8-82a1-326400859d03.gif)

## `Understand Dot product in business`

Refer to _Intro to linear algebra by Gilbert Strang: 1.2_.

![image](https://user-images.githubusercontent.com/14041622/38916654-ccbf081a-431a-11e8-8ecc-d84d01dfcdc2.png)


## `Understand Dot product in physics`
> It makes lots more sense to think `dot product` in **physics** way than maths algebraic way.

**Just to think `Two forces` "a & b" are `pulling` a box,** 
so how much power did it pulled on the `direction of a`, or how much on the `direction of b`?

### `Vectors on same direction`
Let's make it easier before digging in:
assume there's no angle, `Two forces` "a & b" are `pulling` to the same way, the same direction,
so how much power would it be pulled?
![image](https://user-images.githubusercontent.com/14041622/38633159-62e797d2-3df1-11e8-8e6e-b7600a0b7d32.png)
Well, the force `a & b` working together, it's a process of **`Boosting`** the energy! 
**It's not ADDING together anymore**, it's `BOOSTING`!
Let's say the force `a` has `3 units` power, `b` has `6 units` power. 
So every `1 unit` power `a` pulls, `b` will pull `2 units` power.
Then it make sense:
The total power pulling the thing would be `3 · 6 = 18 units`

### `Vectors on different direction`
So the `Two forces` AREN'T pulling the box at the same direction anymore, how much power did it pulled on the `direction of a`, or how much on the `direction of b`?

![image](https://user-images.githubusercontent.com/14041622/38632862-91a762ce-3df0-11e8-9545-1e19ed677936.png)
![screencast 2018-04-12 15-13-15](https://user-images.githubusercontent.com/14041622/38661687-4d62303e-3e64-11e8-9529-78cc511f52c1.gif)

Let's think about how much power it's pulling on the direction of `b`.
Since `a` is pulling on a bit **wrong way**, so **`a`'s power ISN'T 100% working on `b`'s way**.
How much power left there?
It depends on the angle.
So to calculate how much left, we use `|a| × cos(θ)`, 
and we got a **PROJECTION** or a reflection or a **shadow** of `a` on `b`! 
Then it become like this picture again:
![image](https://user-images.githubusercontent.com/14041622/38633159-62e797d2-3df1-11e8-8e6e-b7600a0b7d32.png)
How amazing it is!
And now we could **Boost** the power on b: `|b| ×  |a|×cosθ`

## `Ways of calculating dot product`

There're two ways to calculate the dot product (I made up the names):
- Shadow Boost: 
![image](https://user-images.githubusercontent.com/14041622/38635179-24867f34-3df7-11e8-8571-ba6fa706aa3f.png)
- Axes Boost: 
![image](https://user-images.githubusercontent.com/14041622/38635195-2b519c04-3df7-11e8-8a73-34171669a673.png)

Result of two ways are **SAME**.

> Remember: Boosting is not working when two vectors are **Perpendicular**, which product is `0`.

### `Shadow Boost`
> We reflect one vector on another one, then **Boost** the energy.

Intuition:
![image](https://user-images.githubusercontent.com/14041622/38634997-a69cff08-3df6-11e8-98b4-a66c2e0c1156.png)


### `Axes Boost`
> We break two vectors to `X-axis` and `Y-axis`, and BOOST on each axis.

Easier to remember the formula is:
![image](https://user-images.githubusercontent.com/14041622/38634475-2a08a182-3df5-11e8-989e-11218ff847f8.png)

Intuition:
![image](https://user-images.githubusercontent.com/14041622/38635041-bf54e088-3df6-11e8-9562-3f18002d288e.png)


### Examples:
![image](https://user-images.githubusercontent.com/14041622/38624552-ea2e8aa0-3dda-11e8-9f41-f2ca0301b1a9.png)
![image](https://user-images.githubusercontent.com/14041622/38624556-ee196536-3dda-11e8-811f-12b9ec63d8a5.png)

### Example
![image](https://user-images.githubusercontent.com/14041622/38635344-a3359fb8-3df7-11e8-81f2-5a5debe95e22.png)
![image](https://user-images.githubusercontent.com/14041622/38635363-aed95e0e-3df7-11e8-900c-d8f38dc4a4a2.png)





# `Cross product`
> Actually the `cross product` is very very very limited in use, and as fairly often as the `dot product`. 

**So don't waste time on this unless having certain use of it.**

**REMEMBER: A CROSS PRODUCT ONLY HAS USE IN 3-DIMENSIONS, AND ORDER MATTERS, AND GIVES YOU A NEW VECTOR.**

List it again:
- Only work for 3-Dimensions
- Order matters
- Gives a new vector

![image](https://user-images.githubusercontent.com/14041622/38636646-6275cdb4-3dfb-11e8-9f81-df6e398d27f1.png)

![image](https://user-images.githubusercontent.com/14041622/38636670-7130ed0c-3dfb-11e8-8a09-87049837bd42.png)

`Right-handed system`:
![image](https://user-images.githubusercontent.com/14041622/38636675-74a32202-3dfb-11e8-9b61-024bf9b0d219.png)



# `Matrices intro`
> `Matrices` are just a **rectangle array of numbers**.
Prerequisites: `Systems of equations`

![image](https://user-images.githubusercontent.com/14041622/38552009-51700eb2-3ced-11e8-86ce-15a21a9b3c0e.png)


Matrices could be seen as a group of informations arranged **IN A CERTAIN WAY**.
**IT'S SO SO SO SO SO EASIER TO THINK IT AS A SYSTEM OF EQUATIONS.**

![image](https://user-images.githubusercontent.com/14041622/38552056-6a3a18fc-3ced-11e8-9f40-bae36f2b775d.png)

![image](https://user-images.githubusercontent.com/14041622/38731392-9ab1ae9e-3f4c-11e8-8c8b-7c53436ad624.png)

## `Matrix row operations & Systems of equations`
> It's very SAME with operations of `systems of equations`.

[Refer to Khan academy article: Matrix row operations](https://www.khanacademy.org/math/precalculus/precalc-matrices/elementary-matrix-row-operations/a/matrix-row-operations)

![image](https://user-images.githubusercontent.com/14041622/38552166-dff4d4d8-3ced-11e8-8ae4-3d9144c35473.png)


There're different types of row operations:
- Switch any two rows
- Multiply a row by a nonzero constant
- Add one row to another

They all relate to the operations of systems of equations:
### Switching any two rows:
![image](https://user-images.githubusercontent.com/14041622/38552224-08aa1bea-3cee-11e8-93c2-61943babeb98.png)

### Multiply a row by a nonzero constant:
![image](https://user-images.githubusercontent.com/14041622/38552233-138a8cca-3cee-11e8-8569-f3a8238e554c.png)

### Add one row to another:
![image](https://user-images.githubusercontent.com/14041622/38552241-1c33501e-3cee-11e8-9604-3704346237a7.png)

## `Solve system equations using Matrix`
> it's also called the **`Row-Echelon form and Gaussian elimination`**.

[Khan lecture: Reduced row echelon form](https://www.khanacademy.org/math/precalculus/precalc-matrices/modal/v/matrices-reduced-row-echelon-form-2)
[Refer to Ck-12: Row Operations and Row Echelon Forms](https://www.ck12.org/c/algebra/row-operations-and-row-echelon-forms/lesson/Row-Operations-and-Row-Echelon-Forms-PCALC/?collectionCreatorID=3&conceptCollectionHandle=algebra-%3A%3A-row-operations-and-row-echelon-forms&collectionHandle=algebra)
[Example of "RREF": Lec 01 - Linear Algebra | Princeton University](https://youtu.be/Ncu9Pks3AJQ?t=29m54s)

> It's a so serious problem in all the first lesson of Linear algebra courses. It seems simple yet not easy to solve by yourself. You need to understand all the steps of how to do a `REF` or `RREF`, aka. `Reduce Row Echelon Form`.

The important note to apply the `RREF` is to know how the `Pivot`, or the `Cursor` moves. 
It's more efficient to understand it with 1 or 2 practice rather than see notes here.

First we need to rewrite the system of equation to `matrix` form:
![image](https://user-images.githubusercontent.com/14041622/38552612-41076fc8-3cef-11e8-9654-fdadcb7627ba.png)

Then by `row operations`, we need to achieve this kind of result, which is also called **Reduced Row Echelon Form**:
![image](https://user-images.githubusercontent.com/14041622/38552642-53ad647a-3cef-11e8-9e72-3172da752b5d.png)

It means we eliminated all other variables and only left 1 variable in one equation, which is called **`Identity Matrix`**. Then you could put back the number to the system of equations.



# `Matrix multiplication`
**IT IS A WHOLE NEW AREA ASIDE FROM MATRICES BASIC OPERATIONS**.

It's very difficult to make sense of it. But mathematicians just somehow make it work, it then is a `Human defined operation`, it makes no sense but you just have to deal with it. 
If you just need to solve the problem, you only need 5 minutes to get it around, and then you can skip all these below. 
But if you'd like to understand it, then prepare yourself for a couple of hours or days on this.


> It's necessary to make you confused with the operation below. Because that's most teachers start with to teach you how to multiply matrices. Don't worry, we're to skip this one and find a better perspective to solve it.
![image](https://user-images.githubusercontent.com/14041622/38692046-3d25a65a-3eb5-11e8-9609-0157bdcae291.png)


[Refer to Khan academy article: Multiplying matrices](https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/a/multiplying-matrices)
[Refer to 3Blue1Brown: Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=10)
[Refer to maths is fun: How to Multiply Matrices](https://www.mathsisfun.com/algebra/matrix-multiplying.html)

This topic is very easy to use but very difficult to understand! 
But I rather to understand it instead of just memorising it. 
So this is the **Learning path** of this topic:
1. Dot product
2. **Linear transformations**
2. Matrix-vector product
3. Matrix-matrix product


## `Understand Matrix multiplication`
There're so many different ways to understand it, to make sense of it, because it's so hard to understand.

The major fond of ways to understand are:
- Through `Matrix transformation`
- Through `Real-life example`
- ~Through Algebraic methods~

Although `Real-life example` makes sense easily, but it aren't gonna help solving problems well.
So `Matrix transformation` is the ultimate way to understand Matrix multiplications.
And it proved that it is the best way for that, and for all core ideas of `Linear Algebra`.

Before we start, let's make things clear:
- Dot product: Vector * Vector
- Matrix-vector product: Matrix * Vector
- Matrix-Matrix product: Matrix * Matrix

![image](https://user-images.githubusercontent.com/14041622/38662516-29af0b78-3e67-11e8-997c-63760193eba9.png)


Refer to Khan lecture video: [Matrix vector products as linear transformations](https://www.khanacademy.org/math/linear-algebra/matrix-transformations/linear-transformations/v/matrix-vector-products-as-linear-transformations)

> In the GPU of a computer,
**"ALL THE GRAPHIC PROCESSORS ARE JUST HARD-WIRED MATRIX MULTIPLIERS! ALL THEY DO IS JUST MULTIPLYING MATRICES!" - SAL KHAN**



# `Linear transformation`
> There're so many different ways to understand Matrix Multiplications, 
and **Linear Transformations** is the best and probably the only one makes sense and perfect intuition to you, i.e. it might be the only chance to understand it after all.

**LINEAR TRANSFORMATION IS THE VERY KEY TO OPEN UP ALL GETES IN LINEAR ALGEBRA, BECAUSE IT MAKES PERFECT SENSE OF MATRIX MULTIPLICATION.**

To understand `matrix multiplication`, Linear Transformation is the very first thing you want to learn. It's fairly important and can't get away with.

> `Linear transformation` is a special kind of Transformation, which deals with `vectors`.

Need to mention that, 3Blue1Brown has done well on build intuition on this topic:
Refer to 3Blue1Brown's video: [Linear transformations and matrices](https://www.youtube.com/watch?v=kYB8IZa5AuE&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=4)
Refer to the same video: [How does linear transformation work on unit vectors](https://youtu.be/kYB8IZa5AuE?t=3m47s)
Refer to 3Blue1Brown's video: [Three-dimensional linear transformations](https://www.youtube.com/watch?v=rHLEWRxRGiM&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=6)
Refer to 3Blue1Brown's video: [Matrix multiplication as composition](https://www.youtube.com/watch?v=XkY2DOUCWMU&index=5&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)


> "Matrices give us  **a language** to describe these transformations, where the columns represent those coordinates. 
And matrix-vector multiplication is just a way to compute what that transformation does to a given vector. 
Every time you see a matrix, you can interpret it as a certain transformation of space. 
Once you digest the idea, you’re in a great position to understand the linear algebra deeply. 
**Almost all of the topics in linear algebra will become easy to understand once you start thinking about matrices as transformations of space.**" - 3Blue1Brown


**YOU JUST HAVE TO MEMORISE THIS EQUATION AND GET THE IDEA. THAT IS GONNA HELP YOU OUT FROM ALL THE IDEAS AND PROBLEMS IN LINEAR ALGEBRA.**
![image](https://user-images.githubusercontent.com/14041622/38699787-a0232910-3ecb-11e8-844e-30ccf58a5500.png)


## `Change the basis`
> `Changing basis` is the very core of Linear Transformation. Every single move is based on this.

Remember a vector `(a, b)` could also present in `unit vector` form as `v = ai + bj`,
and unit vectors are `i = (1, 0) & j = (0, 1)`.

If we want to transform a vector, like `move, flip, rotate, scale`, the thing we'll do is:
**TO CHANGE THE UNIT VECTOR `i` AND `j`**.

For example, there's a vector `v = (-1, 2)`, and it can present as `v = -1i + 2j`, then we're to do some movement to it:
- Move: We let unit vector `i = (100, 0)`, then the vector moves to the right becomes `(-100, 2)`.
- Rotate: we let unit vector `i = (0, 1)` and `j = (-1, 0)`, then the vector rotates 90° becomes `(-2, -1)`.
**THAT'S THE MAGIC!!**

By telling where the `unit vectors` are to go, we can create a pattern, a mapping rule, so that every vector uses this map, this rule, this pattern will have the same transformation!

Another example: 
Assume there's a vector `v=(5,7)`, and let the unit vector `i=(3,-2)` and `j=(2,1)`, and present this **`TRANSFORM PATTERN`** as below:
![image](https://user-images.githubusercontent.com/14041622/38697466-ae386936-3ec4-11e8-82b8-b88130a4906b.png)

And we present this `Applying a transformation to a vector` in the form below:
![image](https://user-images.githubusercontent.com/14041622/38697449-9b20935a-3ec4-11e8-917a-342a23259eec.png)

**SO WHENEVER YOU ENCOUNTER MATRIX MULTIPLICATION AGAIN, NEVER READ IT AS TWO VECTORS OR TWO MATRICES MULTIPLYING TOGETHER!**




## `How to interpret a Matrix Multiplication`

There're only TWO part of this matrix multiplication:
- `The Graph`: the 1st on right item.
- `The Rules`: All the rest Matrices on the left of `The Graph`.

`The Graph` could be one point (vector) or many points (vectors), e.g.:
- A point: `(2,3)`
- A triangle: `[ (3,0)   (0,4)   (3,4) ]`
- A rectangle: `[ (3,0)   (3,4)    (0,4)  (0,0)]`
- Any shape in any dimension.....

SO ALL YOU NEED TO DO, IS JUST TO APPLY THOSE RULES ONE BY ONE, `LEFT BY RIGHT`, AND GET A NEW GRAPH!!!

For example, we apply two transform rules to a vector `(x, y)`:

![image](https://user-images.githubusercontent.com/14041622/38699596-0936739a-3ecb-11e8-93ea-8fdd79af23e4.png)

It's exactly same with the function principles: `Shear( Rotate(x, y) )`.

![image](https://user-images.githubusercontent.com/14041622/38699833-cb3ac450-3ecb-11e8-8364-bb1540ab33ae.png)



## `Break up the Matrices with its Geometric meaning`

In the `transform rule` as below:
![image](https://user-images.githubusercontent.com/14041622/38698610-39ec988c-3ec8-11e8-9fac-759fe64ff376.png)

**WE HAVE TO BREAK THE MATRICES INTO SINGLE PARTS BEFORE WE DO THE CALCULATION.** 

![image](https://user-images.githubusercontent.com/14041622/38698753-b2b7801a-3ec8-11e8-843b-3431c4955d46.png)

And since we made the rule for `i & j`, so let's apply the `unit vector` to `the Graph`:
![image](https://user-images.githubusercontent.com/14041622/38698988-632deb46-3ec9-11e8-9fd1-5edfef552f0f.png)

Note that: 
- The original graph is `v = 5i + 7j`, so after applying the new rule of `i & j`, we get: 
`v = 5(3,-2) + 7(2,1)`
- And now we could do the `Vector multiply a scalar` method, to get this:
`v = (15,-10) + (14,7)`
- Then we could do `Add two vectors`:
`v = (19, -3)`
- So after applying the transformation rule, we successfully transformed the vector to a new position:
 `(19, -3)`













# `Matrix Transformation`
> It's a subset of `Linear transformation`, just with `higher dimension rules` & `multiple points graph` multiplying together. 

**YOU BREAK `THE RULE` IN TO DIFFERENT UNIT VECTORS i, j, k... AND BREAK THE GRAPH INTO DIFFERENT POINTS, AND APPLY EACH i, j, k RULES TO EACH POINT.**

### `Size of Matrix multiplication`
Unlike `Vector multiplication` gives you only a number, `Matrix multiplication` gives you another `Matrix`, but a **SHRINK-SIZED** Matrix.
![image](https://user-images.githubusercontent.com/14041622/38666945-c23e7800-3e72-11e8-9428-8aba02e7234d.png)

In General:
To multiply an `m×n matrix` by an `n×p matrix`, the `n`s must be the same, 
and the **RESULT** is an `m×p matrix`.
![image](https://user-images.githubusercontent.com/14041622/38667056-0763bae4-3e73-11e8-88d4-7fc89cce8880.png)

### Example: 3x2 Matrix with 2x2 Matrix
![image](https://user-images.githubusercontent.com/14041622/38701147-bb7e535c-3ecf-11e8-8fe4-bf5582950785.png)
Solve:
- First we know it's a 3x2 Matrix multiply a 2x2 Matrix, it's valid, and the new Matrix's size would be 3x2.
- And then we multiply each by each according to their **dimension**:
![image](https://user-images.githubusercontent.com/14041622/38701686-1e31f46c-3ed1-11e8-94f9-b569f6e7fdf7.png)
- We get the answer:
![image](https://user-images.githubusercontent.com/14041622/38701899-b3ad71d8-3ed1-11e8-9a88-fd535ebe30ea.png)

### Example: 2x2 Matrix with 2x3 Matrix
![image](https://user-images.githubusercontent.com/14041622/38701919-c187acd8-3ed1-11e8-8997-dc15d5acf4ca.png)
Solve:
- It's will get a 2x3 new Matrix (just for intuition), then we get the answer:
![image](https://user-images.githubusercontent.com/14041622/38702654-c433b952-3ed3-11e8-97af-5adaa79fa1c6.png)


### Example: Transform Graphs
![image](https://user-images.githubusercontent.com/14041622/38702739-fbd6997e-3ed3-11e8-9dac-cfd2b742e951.png)
![image](https://user-images.githubusercontent.com/14041622/38702750-023c3c4c-3ed4-11e8-88dd-7568e10d798f.png)
Solve:
- Just to list all points of this graph:
`(-4,8), (-8,-4), (-4,-4), (0,4)`
- Arrange points to a Matrix:
![image](https://user-images.githubusercontent.com/14041622/38702890-5def64c4-3ed4-11e8-87a4-4dcc1db9c7ec.png)
- Apply the Matrix R to the Graph's matrix. Do the math.


### `More examples`

Refer to [Symbolab the Online math solver](https://www.symbolab.com/solver/matrix-vector-calculator/%5Cbegin%7Bpmatrix%7D-1%5C%5C%204%5C%5C%204%5Cend%7Bpmatrix%7D%5Ccdot%5Cbegin%7Bpmatrix%7D0%26-2%5Cend%7Bpmatrix%7D), which offers answers of any matrices operation step by step.


## `Most common Matrix Transformations`
> One single matrix to present the movement? Yes!

[Refer to Math planet: Transformation using matrices](https://www.mathplanet.com/education/geometry/transformations/transformation-using-matrices)

### Rotation
![image](https://user-images.githubusercontent.com/14041622/38721496-0a0e4f9c-3f2d-11e8-8e8c-f83a4b69a41f.png)

### Reflection
![image](https://user-images.githubusercontent.com/14041622/38721364-7f5ab8d6-3f2c-11e8-81ca-b8084a627ca2.png)
![image](https://user-images.githubusercontent.com/14041622/38721371-85145e1c-3f2c-11e8-91f4-fe424ab86a5a.png)





# `Composition of Matrix Multiplication`
> `Composition of Matrix Multiplication` means **More than one linear transformations applies to a graph one by one.**

**Although you can see two matrices multiplying together as `a transform applying to a graph`.
But actually sometime you can see it in slightly different perspective.**

[Refer to 3Blue1Brown: Matrix multiplication as composition](https://www.youtube.com/watch?v=XkY2DOUCWMU&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=5)

![image](https://user-images.githubusercontent.com/14041622/38725499-1684462a-3f3a-11e8-93f4-483a20fe6fee.png)

So extend from the equation above, we know that the `transformation rules` could **Unite together as one** and then apply it to `the graph`.
And here it comes, **MATRICES MULTIPLICATION COULD ALSO REPRESENT TRANSFORM RULES UNITE TOGETHER AS A RESULT RULE, RATHER THAN ONE RULE WORK ON A GRAPH.**

![image](https://user-images.githubusercontent.com/14041622/38726260-398149d2-3f3c-11e8-8c5a-97d7726a6368.png)

## Order matters!
![image](https://user-images.githubusercontent.com/14041622/38726318-671f2f9e-3f3c-11e8-96d3-2b3086cc1cb5.png)





# `Determinant of Transformation`
It's quite easy to calculate, and not too hard to understand what's behind it.
> The `Determinant of a transformation` is **How much the AREA of the new Graph scaled.**

**JUST TO REMEMBER: THE DETERMINANT IS ABOUT AREA OF THE GRAPH!**

[Refer to 3Blue1Brown: The determinant](https://www.youtube.com/watch?v=Ip3X9LOh2dk&index=7&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&t=0s)

![image](https://user-images.githubusercontent.com/14041622/38727000-5d6a07e2-3f3e-11e8-9239-d40c128378ac.png)


### `Unit vector graph`
![image](https://user-images.githubusercontent.com/14041622/38726803-d05d599e-3f3d-11e8-9f94-9904eb22ffdf.png)

We all know the `unit vector i & j`  made an area of `1`.
But when we do a `Linear transformation` to the `unit vector graph`, the area is not `1` anymore, might be bigger or smaller. 
So how much it re-sized we call it the `determinant`.

![image](https://user-images.githubusercontent.com/14041622/38726771-b9f41b66-3f3d-11e8-8f7f-3b81368238e2.png)

Note that:
- Since `a/1 = a`, so calculating the **Area** of the `new unit vector graph`, is equal to the scalar itself.
- Calculating how much the `unit vector graph` scaled, is exactly equal to how much the whole graph scaled.

## Irregular shape
> If it's not a `grid square` can be approximately very well  by many many `small piece of grid squares`.
![image](https://user-images.githubusercontent.com/14041622/38726881-04f79232-3f3e-11e8-9ca1-83ef2416ca0b.png)


## `Determinant formula for 2x2 Matrix`
![image](https://user-images.githubusercontent.com/14041622/38727472-ab8f4d64-3f3f-11e8-8f32-05f87b346989.png)

[Refer to Khan video.](https://www.khanacademy.org/math/precalculus/precalc-matrices/modal/v/finding-the-determinant-of-a-2x2-matrix)

> It will be so much easier if you just to memorise the formula, than to understand where it comes from, which is also not necessary to do.

![image](https://user-images.githubusercontent.com/14041622/38727512-cab770b8-3f3f-11e8-91e2-2335f275c11f.png)

## `Determinant formula for 3x3 Matrix`
> I hope you're not gonna have chance to apply this formula.

![image](https://user-images.githubusercontent.com/14041622/38727569-f9c986b6-3f3f-11e8-87db-d84be4386175.png)


## `Zero determinant`
If the determinant of a transformation `det(M) = 0`, then it means the Transformation squishes the graph to a line or a point!

![image](https://user-images.githubusercontent.com/14041622/38727164-d8a84fa4-3f3e-11e8-9a4c-154024847b1d.png)


## `Negative determinant`
A `negative determinant` means the graph has been **`flipped over`** by the transformation. 
Then the `j unit vector` flip over to the **LEFT** side of `i unit vector`.

[Refer to 3Blue1Brown for visualisation](https://youtu.be/Ip3X9LOh2dk?t=3m46s)

![image](https://user-images.githubusercontent.com/14041622/38727271-19c1fa62-3f3f-11e8-9fda-da457f2cf4d9.png)



# `Inverse Matrices`
> There is actually no concept of `division of matrix`. But similarly we can let it `multiply an inverse` to achieve the same goal.

Refer to 3Blue1Brown: [Inverse matrices, column space and null space ](https://www.youtube.com/watch?v=uQhTuRlWMxw&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=8)
[Refer to maths is fun: Inverse of a Matrix.](http://www.mathsisfun.com/algebra/matrix-inverse.html)

**SPOILER ALERT: EVEN 3x3 MATRIX INVERSE IS ALREADY TOO HEAVY TO CALCULATE, SO BETTER JUST TO MEMORISE THE 2x2  AND LET COMPUTER DO ALL THE HIGHER DIMENSIONS.**

![image](https://user-images.githubusercontent.com/14041622/38729660-3e545774-3f46-11e8-94e8-928dde93154f.png)

## `Understand the Inverse Matrix`
> 3Blue1Brown's video perfect explained the intuition of it, pretty much everything you need to know.
[Link: Inverse matrices, column space and null space ](https://youtu.be/uQhTuRlWMxw?t=3m58s)

**It makes lots more sense in geometric meanings, that an Inverse Matrix just to RECOVER the transformation of a graph back to before.**

![image](https://user-images.githubusercontent.com/14041622/38731998-1c629514-3f4f-11e8-8e67-7678eea7ac35.png)

![image](https://user-images.githubusercontent.com/14041622/38732004-2409df0c-3f4f-11e8-8d34-fe2c9c86ab2d.png)

![image](https://user-images.githubusercontent.com/14041622/38731792-5a980a18-3f4e-11e8-8ebb-dd3a11f3b540.png)

![image](https://user-images.githubusercontent.com/14041622/38731911-c38a8000-3f4e-11e8-9484-00f53cb2dda0.png)

### Why is the Inverse Matrix on the Left of Vector
Because Matrix `A` is always as a `"Coefficient"` to the vector, or as a `transformation rule` to the vector, so it's always on the left of the vector ( or the graph).

![image](https://user-images.githubusercontent.com/14041622/38735715-33449f86-3f5c-11e8-92f1-eee513f4956b.png)



## `Identity Matrix`
> It's a simple yet important notation for doing dividing a matrix.

The `Identity Matrix` is the matrix equals to the number of `1`:
![image](https://user-images.githubusercontent.com/14041622/38728577-d929f67c-3f42-11e8-9e0b-fb6d4b36bb50.png)

> It's very much more intuitive to think a `identity matrix` as **`one unit vector`**.
- 1-Dimension: `x = 1`
- 2-Dimensions: `v = (1, 1)`
- 3-Dimensions: `v = (1, 1, 1)`

![image](https://user-images.githubusercontent.com/14041622/38728979-0b516648-3f44-11e8-9b52-ed7737029f3a.png)


### The features of Identity Matrix
- It is `square` (m×m Matrix)
- It can be large or small (2×2, 3×3, 100×100, ... whatever)
- It has `1`s on the diagonal and `0`s everywhere else
- Its symbol is the capital letter `𝗜`

More importantly, **IT CAN SWITCH SIDE WHEN MULTIPLYING ANOTHER MATIRX!**
It's very special, and is the **ONLY** matrix can IGNORE the order when multiplying another matrix.
![image](https://user-images.githubusercontent.com/14041622/38729092-6086a8f8-3f44-11e8-861b-8d8e9f1bb592.png)

## Not Invertible Matirces
Two conditions make a matrix NOT invertible:
- The matrix is not a `Square Matrix` (m×m matrix).
- The `Determinant` is **ZERO**. Such matrix is also called a **`Singular matrix`**

![image](https://user-images.githubusercontent.com/14041622/38730081-c76d03ca-3f47-11e8-8730-2a83613f8f17.png)

## `Adjugate Matrix`
> It's also called the `Adjoint of a matrix`, or `Classical Adjoint`.

Refer to maths is fun: [Inverse of a Matrix using Minors, Cofactors and Adjugate.](https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html)

### Adjugate of 2x2 Matrix
![image](https://user-images.githubusercontent.com/14041622/38730850-c295be48-3f4a-11e8-8ede-eb652ea0cc43.png)


## `Calculate the Inverse of a Matrix`
> "Calculating it for a 2x2 is fairly straightforward, 3x3 becomes a little bit hairy, 4x4 will take you all day, 5x5 you're almost definitely gonna do a careless mistake if you do an inverse of matrix." - Sal Khan

![image](https://user-images.githubusercontent.com/14041622/38730748-54e85cc0-3f4a-11e8-9667-994efe1193c1.png)

### 2x2 Matrix inverse
> With a 2x2 matrix, you really don't need to think much and waste time on the full steps, just simply follow this formula `1/Determinant × Adjugate`

[Refer to Khan lecture.](https://www.khanacademy.org/math/precalculus/precalc-matrices/modal/v/inverse-of-a-2x2-matrix)

![image](https://user-images.githubusercontent.com/14041622/38729138-92aa20c6-3f44-11e8-93e0-828fadb5cd01.png)


### 3x3 Matrix inverse
We can calculate the Inverse of a Matrix by:
- Step 1: calculating the Matrix of Minors,
- Step 2: then turn that into the Matrix of Cofactors,
- Step 3: then the Adjugate, and
- Step 4: multiply that by 1/Determinant.

**I seems not tend to really note the full content here, because it's so useless in normal math life. Because it's way to hairy to calculate even with a 3x3 matrix. So just get the idea and let computer do the rest.** 

## `Solving Systems of equations with Inverse Matrices`

[Khan lecture: Solving linear systems with matrix equations](https://www.khanacademy.org/math/precalculus/precalc-matrices/modal/v/solving-matrix-equation)

![image](https://user-images.githubusercontent.com/14041622/38735551-ac48e136-3f5b-11e8-958d-7466e6b63226.png)



## `Rank of Transformation`
Means the `Dimension of output of a transformation`.

[Refer to 3Blue1Brown: Inverse matrices, column space and null space](https://youtu.be/uQhTuRlWMxw?t=8m)

![image](https://user-images.githubusercontent.com/14041622/38732340-69d15604-3f50-11e8-89fe-90beeeccbde6.png)

After doing a transformation to a graph, it is:
- Rank 1: if the output of the graph is 1-Dimensional, which is a line.
- Rank 2: if the output of the graph is 2-Dimensional, which is a plane.
- Rank 3: .....

In the case of 2x2 Matrices, the `Rank 2` is the best it can be.
In the case of 3x3 Matrices, the `Rank 2` means it collapsed, or dimensional reduced.

When it's the highest rank the Matrix can be, we call it **`THE FULL RANK`**.




## `Column space of Matrix`
Means `The SET of all possible outputs a matrix`.
In another word, it's `THE SPAN OF THE COLUMNS OF THE MATRIX`.

The columns of the matrix tell where the `basis vectors` land, like `i & j`.
And the `span of all basis vectors` gives you all possible outputs, which is the `Column space`.

![image](https://user-images.githubusercontent.com/14041622/38732534-08ca67f0-3f51-11e8-966c-9cdb0cc1e25f.png)

![image](https://user-images.githubusercontent.com/14041622/38732562-2a3fb93a-3f51-11e8-96df-0a048a26c170.png)



# `The geometry of linear equations` (MIT)

[Refer to the pdf.](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/ax-b-and-the-four-subspaces/the-geometry-of-linear-equations/MIT18_06SCF11_Ses1.1sum.pdf)

"The fundamental problem of linear algebra is to solve n linear equations in `n` unknowns."
We view this problem in three ways:
- Row picture: The "row method" focuses on the individual equations
- *Column picture: The "column method" focuses on combining the columns
- Matrix picture: The "matrix method" is an even more compact and powerful way of describing systems of linear equations.
