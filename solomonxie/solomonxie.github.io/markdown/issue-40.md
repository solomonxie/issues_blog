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

![image](https://user-images.githubusercontent.com/14041622/38659785-831c216e-3e5d-11e8-8623-77fcc365adcb.png)


**What's it for?**
Basically just like the unit circle, make things easier to calculate angles or length or so. 
Actually it's working together with unit circle and all other trigonometric knowledges.
so, 
**UNIT VECTOR IS RATHER A TRIGONOMETRIC WAY TO DEAL WITH VECTORS.**
Easier to think about it, is to think about the `Similar graph` knowledge in the `Dilation` section. 

### `Unit vector form`
> `unit vector` is easy, but `unit vector form` needs your bit more effort to understand.

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

## `Linear combinations`
> `Linear combinations` means to add vectors together: `v₁ + v₂ + v₃.....` to get a new vector. Simple like that.

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

[For an intuitive video refer to Khan academy physics: Dot Product.](https://www.khanacademy.org/science/physics/magnetic-forces-and-magnetic-fields/electric-motors/v/the-dot-product)
[For more explains in detail: Vector Calculus: Understanding the Dot Product](https://betterexplained.com/articles/vector-calculus-understanding-the-dot-product/)
[Maths is fun: dot product.](https://www.mathsisfun.com/algebra/vectors-dot-product.html)
[3Blue1Brown: Dot products and duality | Essence of linear algebra](https://www.youtube.com/watch?v=LyGKycYT2v0&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=10)

![screencast 2018-04-12 15-08-30](https://user-images.githubusercontent.com/14041622/38661569-e3831bc4-3e63-11e8-82a1-326400859d03.gif)



### `Understand Dot product`
> It makes lots more sense to think `dot product` in **physics** way than maths algebraic way.

**Just to think `Two forces` "a & b" are `pulling` a box,** 
so how much power did it pulled on the `direction of a`, or how much on the `direction of b`?

#### `Vectors on same direction`
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

#### `Vectors on different direction`
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

### `Ways of calculating dot product`

There're two ways to calculate the dot product (I made up the names):
- Projection Boost: 
![image](https://user-images.githubusercontent.com/14041622/38635179-24867f34-3df7-11e8-8571-ba6fa706aa3f.png)
- Axes Boost: 
![image](https://user-images.githubusercontent.com/14041622/38635195-2b519c04-3df7-11e8-8a73-34171669a673.png)

Result of two ways are **SAME**.

> Remember: Boosting is not working when two vectors are **Perpendicular**, which product is `0`.

#### `Shadow Boost`
> We reflect one vector on another one, then **Boost** the energy.

Intuition:
![image](https://user-images.githubusercontent.com/14041622/38634997-a69cff08-3df6-11e8-98b4-a66c2e0c1156.png)


#### `Axes Boost`
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

Before learning `matrices multiplication`, have to learn `dot product of vectors` (let's forget about cross product).

And also, it's using the core idea of `dot product`, but "twists" it a bit. Need you to have a strong intuition to understand what's going on.

[Refer to Khan academy article: Multiplying matrices](https://www.khanacademy.org/math/precalculus/precalc-matrices/multiplying-matrices-by-matrices/a/multiplying-matrices)
[Refer to 3Blue1Brown: Dot products and duality](https://www.youtube.com/watch?v=LyGKycYT2v0&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=10)

## Why is it multiplying this way
![screencast 2018-04-12 15-23-39](https://user-images.githubusercontent.com/14041622/38662131-dee63040-3e65-11e8-979d-285bd7c4b325.gif)

