# Calculus & Linear Algebra from the ground up
> Quick notes on College level of Maths or Stats for machine learning.


## Study resources
- [ ] [Khan academy Pre-calculus](https://www.khanacademy.org/math/precalculus)
- [ ] [Khan academy Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [ ] [MIT OCW 18.06sc Linear Algebra](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm)
- [ ] [Essence of linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [ ] [A First Course in Linear Algebra](https://github.com/solomonxie/solomonxie.github.io/files/1786068/fcla-3.50-A.First.Course.in.Linear.Algebra.-.Robert.A.Beezer.University.of.Puget.Sound.Version.3.50.pdf)

## Prerequisites
Vectors:
- [ ] Trigonometry: Unit circle, Inverse trig function
- [ ] Geometry: Transformation
- [ ] Precalculus: Complex number forms conversion
- [ ] Algebra: Line



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

## `Convert between vector forms`

**HIGHLY RECOMMEND TO REVIEW THE COMPLEX NUMBER CONVERSION SKILLS, HAVING THE VERY SAME IDEA.**
[Refer to previous note: complex number forms conversion skills.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-379646389)

### `How to get the direction (the angle) of a vector`
> It's the very same problem of the topic `Inverse trig function`. 

**NOT EASY! NEED TO CONSIDER LOTS OF CONDITIONS, LIKE QUADRANTS, POSSIBLE SOLUTIONS, PRINCIPLE SOLUTION AND SO. RECOMMEND TO REVIEW INVERSE TRIG FUNCTIONS.**

[Refer to previous notes: Inverse Trigonometric equations.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-377686394)


# `Matrices`
> `Matrices` are just a **rectangle array of numbers**.

Matrices could be seen as a group of informations arranged **IN A CERTAIN WAY**.


## `Matrix row operations`
