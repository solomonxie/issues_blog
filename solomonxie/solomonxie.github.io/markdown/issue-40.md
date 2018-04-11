# Calculus & Linear Algebra from the ground up
> Quick notes on College level of Maths or Stats for machine learning.


## Study resources
- [ ] [High school maths notes](https://github.com/solomonxie/solomonxie.github.io/issues/44)
- [ ] Khan academy
    - [ ] [Pre-calculus](https://www.khanacademy.org/math/precalculus)
    - [ ] AP calculus AB
    - [ ] AP calculus BC
    - [ ] Differential calculus
    - [ ] Integral calculus
    - [ ] Multivariable calculus
    - [ ] Differential equations
    - [ ] [AP Statistics](https://www.khanacademy.org/math/ap-statistics)
    - [ ] [Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [ ] [MIT OCW 18.06sc Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm)
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


## TL;DR. Archive Link: [why do I need to learn Linear Algebra?](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-368829945)


## TL;DR. Archived link: [Vector section notes of Essence Linear Algebra](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-379985082)


## TL;DR Archived link: [MIT OCW Linear Algebra course compare](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-380001327).


# `Vector & basic operations`
> Definition: vector is a **MAGNITUDE** with a **DIRECTION**

Notation: 
- `v` as a vector.
- `|v|` or `||v||` as its **Magnitude**, or **Distance**, or **Absolute value**, same idea
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

### `UNDERSTAND VECTOR'S MOVEMENT`
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
Adding & subtracting could be seen as a movement to a vector, or say how it travels.
![image](https://user-images.githubusercontent.com/14041622/38543990-bef3a65c-3cd8-11e8-877c-2e23ea719208.png)

[Refer to Maths is fun.](http://www.mathsisfun.com/algebra/vectors.html)

- Adding vectors:
![image](https://user-images.githubusercontent.com/14041622/38543941-9acd84b4-3cd8-11e8-9314-9a6e8ac975a8.png)
- Subtracting vectors: is just **ADDING** a **NEGATIVE VECTOR**
![image](https://user-images.githubusercontent.com/14041622/38543960-ab2d4844-3cd8-11e8-8a08-3608c9221275.png)

## Multiplying vectors by SCALAR
> It's the very same with the section `DILATION` or `Scaling` in Geometry. 

Just for review of `dilating` a graph geometrically:
When you scale a graph by a factor:
- Every line of the graph scale by the SAME factor
- Every line will be PARALLEL to its origin line.

[Refer to previous note: Transformation.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-371067923)

![image](https://user-images.githubusercontent.com/14041622/38544907-56398f66-3cdb-11e8-8958-9628d87444ee.png)



# Vector forms

[Refer to Khan academy article.](https://www.khanacademy.org/math/precalculus/vectors-precalc/magnitude-direction/a/vector-forms-review)

![image](https://user-images.githubusercontent.com/14041622/38547847-c2e1b29a-3ce2-11e8-9464-a5fbba606102.png)

## Unit vectors
> Simply say, a `unit vector` is just a vector which magnitude is `1`. Kinda like the unit circle idea.
It's also called `Engineering notation`.

**What's it for?**
Basically just like the unit circle, make things easier to calculate angles or length or so. 
Actually it's working together with unit circle and all other trigonometric knowledges.
so, 
**UNIT VECTOR IS RATHER A TRIGONOMETRIC WAY TO DEAL WITH VECTORS.**
Easier to think about it, is to think about the `Similar graph` knowledge in the `Dilation` section. 

### `Unit vector form`
> `unit vector` is easy, but `unit vector form` needs your bit more effort to understand.

`Unit vector form` assume that there are **TWO** unit vectors, one vertical, one horizontal.
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


# `Matrices intro`
> `Matrices` are just a **rectangle array of numbers**.

![image](https://user-images.githubusercontent.com/14041622/38552009-51700eb2-3ced-11e8-86ce-15a21a9b3c0e.png)

### Prerequisites: `Systems of equations`

Matrices could be seen as a group of informations arranged **IN A CERTAIN WAY**.
**IT'S SO SO SO SO SO EASIER TO THINK IT AS A SYSTEM OF EQUATIONS.**

![image](https://user-images.githubusercontent.com/14041622/38552056-6a3a18fc-3ced-11e8-9f40-bae36f2b775d.png)


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
> it's also called the **`Row-echelon form and Gaussian elimination`**.

[Khan lecture: Reduced row echelon form](https://www.khanacademy.org/math/precalculus/precalc-matrices/modal/v/matrices-reduced-row-echelon-form-2)
[Refer to Ck-12: Row Operations and Row Echelon Forms](https://www.ck12.org/c/algebra/row-operations-and-row-echelon-forms/lesson/Row-Operations-and-Row-Echelon-Forms-PCALC/?collectionCreatorID=3&conceptCollectionHandle=algebra-%3A%3A-row-operations-and-row-echelon-forms&collectionHandle=algebra)

First we need to rewrite the system of equation to `matrix` form:
![image](https://user-images.githubusercontent.com/14041622/38552612-41076fc8-3cef-11e8-9654-fdadcb7627ba.png)

Then by `row operations`, we need to achieve this kind of result, which is also called **Reduced row echelon form**:
![image](https://user-images.githubusercontent.com/14041622/38552642-53ad647a-3cef-11e8-9e72-3172da752b5d.png)

It means we eliminated all other variables and only left 1 variable in one equation. Then you could put back the number to the system of equations.


# `Matrices multiplication`

**IT IS A WHOLE NEW AREA ASIDE FROM MATRICES BASIC OPERATIONS**.

> It's very difficult to make sense of it. But mathematicians just somehow make it work, it then is a `Human defined operation`, no sense but just to use it.

Before learning `matrices multiplication`, have to learn `dot & cross product of vectors`.

Two ways to do multiplications of vectors: 
- `Dot product` [(link)](http://www.mathsisfun.com/algebra/vectors-dot-product.html)
- `Cross product` [(link)](http://www.mathsisfun.com/algebra/vectors-cross-product.html)

[Refer to Khan lectures: Vector dot and cross products](https://www.khanacademy.org/math/linear-algebra/vectors-and-spaces/dot-cross-products/v/vector-dot-product-and-vector-length)
[Refer to Khan academy article: Multiplying matrices](https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/a/multiplying-matrices)

## `Dot product`
**FIRST TO MENTION THAT, DOT PRODUCT OF VECTORS DOESN'T END UP GIVING YOU A VECTOR, BUT ONLY A NUMBER, A SCALAR.**

![image](https://user-images.githubusercontent.com/14041622/38624552-ea2e8aa0-3dda-11e8-9f41-f2ca0301b1a9.png)
![image](https://user-images.githubusercontent.com/14041622/38624556-ee196536-3dda-11e8-811f-12b9ec63d8a5.png)

![image](https://user-images.githubusercontent.com/14041622/38600226-ff8bb11a-3d95-11e8-8cfb-f5ab127dfa23.png)


### `Magnitude of higher dimension vector`
We know a 2D vector length( or magnitude) is `||(a, b)|| = √(a²+b²)`. 
But how about **higher dimension**?
Although it makes no sense and hard to imagine with human's mind, but it's still using this rule:

```py
Length(a,b,c,d,....z) = √(a²+b²+c²+d²+...+z²)
```
So that a vector **(a, b)** multiply it self then will be equal to: `||(a,b)||²`, which then would be `a²+b²`

![image](https://user-images.githubusercontent.com/14041622/38558530-0246d6ac-3d03-11e8-921d-7678e83e5178.png)



# Vector span

## `R²` and `R³`
`R²` means a `Real numbers 2D plane`.
Usually the `X/Y Axes plane` is this one.

`R³` means `Real numbers 3D plane`.
Usually the `X/Y/Z Axes plane`.

## `Span of vectors`

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

### Linear combinations
> `Linear combinations` means to add vectors together: `v₁ + v₂ + v₃.....`. Simple like that.
I can say `some vectors`, or just to say `a linear combination`.

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