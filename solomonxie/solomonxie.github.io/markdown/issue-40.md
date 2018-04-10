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


## Vector's `magnitude`, `direction`, `unit vector`, `components`

View this [Khan review page](https://www.khanacademy.org/math/precalculus/vectors-precalc/magnitude-direction/a/vector-forms-review), 
and [another  Khan review page ](https://www.khanacademy.org/math/precalculus/vectors-precalc/component-form-of-vectors/a/vector-magnitude-and-direction-review) for this section.

![image](https://user-images.githubusercontent.com/14041622/36725910-d03ed410-1bf2-11e8-9bf8-d85acf4f6dd6.png)

![image](https://user-images.githubusercontent.com/14041622/36725667-f959a5a6-1bf1-11e8-9f7d-cd9c16957938.png)





# Adding vectors in `magnitude & direction form`
![image](https://user-images.githubusercontent.com/14041622/36966785-d510d402-2098-11e8-8b68-1d645d13020c.png)
![image](https://user-images.githubusercontent.com/14041622/36967241-285034d6-209a-11e8-9757-14f263ec0d75.png)



# `MIT OpenCourseWare Linear Algebra` 18.06/18.06c/18.07/18.2....
There are a bunch of different version of courses on Linear Algebra on MIT OpenCourseWare with the same lecturer Gilbert Strang. 
It could be quite confusing, but everything became clear after read [this answer on Quora](https://www.quora.com/What-is-the-difference-among-MIT-opencourseware-Linear-Algebra-18-06SC-Linear-Algebra-18-06-Linear-Algebra-18-06CI-Linear-Algebra-18-700).

![image](https://user-images.githubusercontent.com/14041622/36984701-742d91b0-20d0-11e8-8a93-e7a21be03086.png)

This list below is [a section of page from MIT OCW](https://ocw.mit.edu/courses/mathematics/):
![image](https://user-images.githubusercontent.com/14041622/36985159-7efc60de-20d1-11e8-8f43-2dcc263ae287.png)



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

