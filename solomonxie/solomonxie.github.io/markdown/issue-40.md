# Calculus & Linear Algebra from the ground up
> Quick notes on Math or Stat (currently Linear Algebra). 


## Study resources
- [ ] [MIT OCW 18.06sc](https://ocw.mit.edu/courses/mathematics/18-06sc-linear-algebra-fall-2011/index.htm)
- [ ] [Khan academy Linear Algebra](https://www.khanacademy.org/math/linear-algebra)
- [ ] [Khan academy Pre-calculus](https://www.khanacademy.org/math/precalculus)
- [ ] [Essence of linear algebra](https://www.youtube.com/playlist?list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab)
- [ ] [A First Course in Linear Algebra](https://github.com/solomonxie/solomonxie.github.io/files/1786068/fcla-3.50-A.First.Course.in.Linear.Algebra.-.Robert.A.Beezer.University.of.Puget.Sound.Version.3.50.pdf)


## TL;DR. Archive Link: [why do I need to learn Linear Algebra?](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-368829945)


## TL;DR. Archived link: [Vector section notes of Essence Linear Algebra](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-379985082)


## TL;DR Archived link: [MIT OCW Linear Algebra course compare](https://github.com/solomonxie/solomonxie.github.io/issues/21#issuecomment-380001327).


## How to calculate the ratio of an `direction angle`
> `direction angle` is a term for vectors. It is the angle we care about for a vector, which is in between of the vector line and the positive side of axis-x.

**The ratio of a `direction angle` is always drawn from the positive side of axis-x, so that you could know what direction is this vector going to.**

For a vector we only know its x-distance and y-distance, so in terms of trigonometry, or in `right triangle`, they're `Opposite` and `Adjacent`.  So that we could use `Tangent` to calculate the ratio, such as `tan⁻¹(y/x)`.

**But the thing is**, `tan⁻¹(...)` always gives you a number less then 90. So we have to do some tricks for doing this when the direction angle's ratio of a vector is greater than 90, or lesser 0.

To classify those situations, we use the idea of `4 quadrant` of the axis system.

> And once we see x and y, we could immediately identify which quadrant the vector will fall into, then use the different method to calculte as follow:

### [1st Quadrant ](https://www.khanacademy.org/math/precalculus/vectors-precalc/magnitude-direction/v/angles-of-vectors-from-components) (+x, +y):
```
Ratio = tan⁻¹(y/x)
```

![snip20180227_91](https://user-images.githubusercontent.com/14041622/36723018-1758cbf2-1bea-11e8-88dd-ae3753bbe2db.png)

### [2nd Quadrant](https://www.khanacademy.org/math/precalculus/vectors-precalc/magnitude-direction/v/angles-of-vectors-from-components) (-x, +y):
```
Ratio = tan⁻¹(y/x) + 180
```

![image](https://user-images.githubusercontent.com/14041622/36723008-12b4d618-1bea-11e8-988e-840d942b66a0.png)

### [3rd Quadrant](https://www.khanacademy.org/math/precalculus/vectors-precalc/magnitude-direction/v/more-examples-finding-vector-angles) (-x, -y):
```
Ratio = tan⁻¹(y/x) + 180
```

![snip20180227_89](https://user-images.githubusercontent.com/14041622/36722966-f68032ee-1be9-11e8-808e-c623a3c248da.png)

### [4th Quadrant](https://www.khanacademy.org/math/precalculus/vectors-precalc/magnitude-direction/v/more-examples-finding-vector-angles) (x, -y):
```
Ratio = tan⁻¹(y/x) + 360
```

![snip20180227_90](https://user-images.githubusercontent.com/14041622/36722956-eee1defc-1be9-11e8-9dcc-ab3c935afa48.png)




# Vector's magnitude & direction
> Definition: vector is a **MAGNITUDE** with a **DIRECTION**

Notation: 
- `v` as a vector.
- `|v|` or `||v||` as its **Magnitude**, or **Distance**, or **Absolute value**, same idea
- **Slope** as its **Direction.**
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