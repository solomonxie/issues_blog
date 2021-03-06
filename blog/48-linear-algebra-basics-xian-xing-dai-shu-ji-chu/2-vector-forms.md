# ❖ Vector forms

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



## 「Unit vectors」

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


### 「Standard Basis Vectors」 & 「Unit vector」 form

> It's also called `Unit Basis Vectors`.
`Unit vector` is easy, but `unit vector form` needs your bit more effort to understand.

**THIS FORM DOESN'T PRESENT VECTOR AS A POSITION ANYMORE, RATHER PRESENT IT AS HOW MUCH IT STRETCHES UNIT VECTORS, OR SAY PRESENT IT AS A SCALAR.**

Assume that there are **TWO** unit vectors, one vertical, one horizontal.
![image](https://user-images.githubusercontent.com/14041622/38548131-9347693e-3ce3-11e8-9600-3b5ee57e70ed.png)

![image](https://user-images.githubusercontent.com/14041622/38547964-1747a326-3ce3-11e8-9f99-ea9024e007fd.png)

### How to find a vector's 「unit vector」

> More intuitively to solve it just to draw it out and solve it with trigonometry. 

![image](https://user-images.githubusercontent.com/14041622/38602559-b0cc106c-3d9d-11e8-9e63-651ac3ab4daf.png)

Example: Find the unit vector of vector (-8, 5)
![image](https://user-images.githubusercontent.com/14041622/38602586-cbb09484-3d9d-11e8-8c2d-35d1a71daa06.png)


## Convert between 「vector forms」

**HIGHLY RECOMMEND TO REVIEW THE COMPLEX NUMBER CONVERSION SKILLS, HAVING THE VERY SAME IDEA.**
[Refer to previous note: complex number forms conversion skills.](https://github.com/solomonxie/solomonxie.github.io/issues/44#issuecomment-379646389)

### How to find the 「direction angle」 of a vector

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
