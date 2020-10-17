# ❖ Vectors multiplication

> Vector multiplication is FUNDAMENTAL skill to solve `Matrices multiplication`.

**THE VERY FIRST THING TO DO WITH A `VECTOR MULTIPLICATION` OR `MATRIX MULTIPLICATION`, IS TO FORGET EVERYTHING ABOUT `ARITHMETIC MULTIPLICATION` !!**
OTHERWISE, YOU WILL FALL INTO AN ENDLESS CONFUSION!

Just to know, multiplication of vectors or matrices, **AREN'T** really multiplication, but just look like that. You can see them as **operations to get SOMETHING**.

There're two operations are called `multiplication` for vectors:
- `Dot product`: express as `V₁ · V₂`, named for the dot symbol. It's meant to get the `Product of two magnitudes`.
- `Cross product`: express as `V₁ × V₂`, named for the cross symbol. It's meant to get a `new vector`.

> The `cross product` is very very very limited in use, and NOT as fairly often in use as the `dot product`. So don't waste time on this unless having certain use of it.


## 「Boosting」

**IT'S THE VERY CORE SENSE OF MAKING A MULTIPLICATION OF VECTORS OR MATRICES.**

Multiplication **ISN'T** just `Repeat counting in Arithmetic` anymore.
Not `4×3 = 4+4+4` anymore!

It's rather kind of `Growth`, or empowerment, or **boosting**.
We'd say `we tripled 4`, or say `number 4 grow with speed of 3`, or to say `number 4 grows with a boosting of 3`.
Whatever you'd say, you get the idea.
Multiplication a process of `double, triple, quadruple ...`.

**JUST TO REMEMBER: FORGET ABOUT ARITHMETIC MULTIPLICATION, ALWAYS SEE MULTIPLICATION AS BOOSTING.**

## 「Dot Product」

**REMEMBER: A DOT PRODUCT DOESN'T GIVE YOU A VECTOR, BUT ONLY A NUMBER, A SCALAR, A PRODUCT OF TWO MAGNITUDES.**

> The purpose:
It is **NOT** to get a new vector, and **NOT** to `Reduce dimension`, 
its only purpose **IS** to get a **quantity**, a magnitude, a number!

[For an intuitive video refer to Khan academy physics: Dot Product.](https://www.khanacademy.org/science/physics/magnetic-forces-and-magnetic-fields/electric-motors/v/the-dot-product)
[For more explains in detail: Vector Calculus: Understanding the Dot Product](https://betterexplained.com/articles/vector-calculus-understanding-the-dot-product/)
[Maths is fun: dot product.](https://www.mathsisfun.com/algebra/vectors-dot-product.html)
[3Blue1Brown: Dot products and duality | Essence of linear algebra](https://www.youtube.com/watch?v=LyGKycYT2v0&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=10)

![screencast 2018-04-12 15-08-30](https://user-images.githubusercontent.com/14041622/38661569-e3831bc4-3e63-11e8-82a1-326400859d03.gif)

## Understand Dot product in 「business」

Refer to _Intro to linear algebra by Gilbert Strang: 1.2_.

![image](https://user-images.githubusercontent.com/14041622/38916654-ccbf081a-431a-11e8-8ecc-d84d01dfcdc2.png)


## Understand Dot product in 「physics」

> It makes lots more sense to think `dot product` in **physics** way than maths algebraic way.

**Just to think `Two forces` "a & b" are `pulling` a box,** 
so how much power did it pulled on the `direction of a`, or how much on the `direction of b`?

### Vectors on 「same direction」

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

### Vectors on 「different direction」

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

## Ways of calculating dot product

There're two ways to calculate the dot product (I made up the names):
- Shadow Boost: 
![image](https://user-images.githubusercontent.com/14041622/38635179-24867f34-3df7-11e8-8571-ba6fa706aa3f.png)
- Axes Boost: 
![image](https://user-images.githubusercontent.com/14041622/38635195-2b519c04-3df7-11e8-8a73-34171669a673.png)

Result of two ways are **SAME**.

> Remember: Boosting is not working when two vectors are **Perpendicular**, which product is `0`.

### 「Shadow Boost」

> We reflect one vector on another one, then **Boost** the energy.

Intuition:
![image](https://user-images.githubusercontent.com/14041622/38634997-a69cff08-3df6-11e8-98b4-a66c2e0c1156.png)


### 「Axes Boost」

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


## 「Dot product」 & 「Symmetry」

> Dot product has a relationship with Symmetry.

[Refer to lecture of Imperial College London: Einstein summation convention and the symmetry of the dot product](https://www.coursera.org/learn/linear-algebra-machine-learning/lecture/kI0DB/introduction-einstein-summation-convention-and-the-symmetry-of-the-dot-product)

![image](https://user-images.githubusercontent.com/14041622/39709237-ecf3e4e4-524b-11e8-80db-67d0085f2920.png)

