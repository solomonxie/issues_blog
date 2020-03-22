#  ❖ Disc Method

`Disc Method` is a method for calculating the **`Volume of a 3D shape by rotating a 2D shape`**.

The strategy of this method is:
- First to **ROTATE** an infinitely small piece of the whole graph
- Calculate the **AREA** of this `Rotated Circle`, or so called `disc`.
- Integrate all the discs.

[►Jump to Khan academy for some practice: Disc Method](https://www.khanacademy.org/math/ap-calculus-bc/bc-applications-definite-integrals/modal/e/the-disk-method)
[▼Refer to the article: Finding volumes of 3-D objects with circular symmetry in at least one dimension](http://xaktly.com/VolumesDisk.html)

![image](https://user-images.githubusercontent.com/14041622/41714591-62213a3c-7583-11e8-82a1-c0967491172d.png)
![image](https://user-images.githubusercontent.com/14041622/41715073-e242afe2-7584-11e8-9a75-ca2e4682d75d.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/41706686-fb877624-756e-11e8-883a-c52a4e8568b1.png)
Solve:
- First need to completely understand the question and visualize it using `Disc Method`:
![image](https://user-images.githubusercontent.com/14041622/41707154-12c95f04-7570-11e8-9b82-15a00ec77033.png)
- Calculate the **area of disc** and integrate them:
![image](https://user-images.githubusercontent.com/14041622/41707593-0c8352e8-7571-11e8-970f-da84649b55fc.png)

### Example
![image](https://user-images.githubusercontent.com/14041622/41708102-42dcd264-7572-11e8-9291-ed1bbc0e88a2.png)
Solve:
- The radius of the disc is exactly equal to `y` value, means `r = y = eˣ`
- The area of the disc then be `Area(x) = πr² = π · e²ˣ`
- Since We're integrating `Horizontally` along X-axis, so the integral should be `ʃ A(x) dx`
- Integral all the discs: `Volume = ʃ A(x) dx = ʃ π · e²ˣ dx`
- Calculate the integral.


### Example
![image](https://user-images.githubusercontent.com/14041622/41709868-e077eac8-7576-11e8-9605-e3b4bacd0502.png)
Solve:
- The 2D shape is like this one:
![image](https://user-images.githubusercontent.com/14041622/41710275-d8b1b5f2-7577-11e8-85e1-8c0b4c517af6.png)
- So we are to integrate discs along X-axis: `ʃ Area(x) dx`
- The interval is `[0, 4]`.
- It's tricky to get the radius of the disc: `r = y - 1 = √x +1 -1 = √x`
- So the area of each disc is: `Area(x) = πr² = πx`
- Integrate those discs over inteval `[0, 4]`: `Volume = ʃ Area(x) dx = ʃ πx dx = 8π`.
