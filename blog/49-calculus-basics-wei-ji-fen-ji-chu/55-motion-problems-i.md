# Motion problems (Integral calc)

[►Jump to Khan academy for some practice: Motion problems (with integrals)](https://www.khanacademy.org/math/ap-calculus-bc/bc-applications-definite-integrals/modal/e/particle-motion)

### 「Displacement」 vs. 「Distance」

`Displacement` literally means "the change in position", but actually it means the **SHORTCUT** of two points, the shortest distance between two points.

![image](https://user-images.githubusercontent.com/14041622/41458177-6d1a2b26-70b8-11e8-886b-128d9424e22b.png)

[▶Jump over to previous note in Linear Algebra: Displacement is a vector, distance is a scalar.](https://github.com/solomonxie/solomonxie.github.io/issues/48#issuecomment-383118285)

Even if you've been travelling all the time without stops, 
but your `DISPLACEMENT` still can be 0:

![image](https://user-images.githubusercontent.com/14041622/41458843-527045f6-70ba-11e8-8f87-0dd35b9076c9.png)


### Example
![image](https://user-images.githubusercontent.com/14041622/41589291-be2bd2e0-73e6-11e8-9632-612f5afa266c.png)
Solve:
![image](https://user-images.githubusercontent.com/14041622/41589299-c3056088-73e6-11e8-8c62-c2972a6e12d3.png)

### Example
![image](https://user-images.githubusercontent.com/14041622/41589559-5ced7a32-73e7-11e8-8757-13870756a30d.png)
Solve:
- Correct answer:
![image](https://user-images.githubusercontent.com/14041622/41589565-6398b25c-73e7-11e8-9ddd-2fd969115f99.png)
- Incorrect answer:
![image](https://user-images.githubusercontent.com/14041622/41589588-7e162524-73e7-11e8-8303-2b8aae387caf.png)



### Example
![image](https://user-images.githubusercontent.com/14041622/41590573-e5df17c2-73e9-11e8-921d-b0b1ed9e3387.png)
Solve:
- First to know the relationships between `s(t), v(t) and a(t)`:
    - `v(t) = s'(t)` or `s(t) = ʃ v(t) dt`
    - `a(t) = v'(t)` or `v(t) = ʃ a(t) dt`
- Since `a(t) = 1`, so `v(t) = ʃ a(t) dt = ʃ 1 dt = t + C`.
- Substitute: `v(3) = -3 = t + C = 3+C`, so `C=-6` which makes `v(t) = t - 6`
- `s(t) = ʃ v(t) dt = ʃ (t-6) dt = 0.5t² - 6t + C`
- Substitute: `s(2) = 0.5*2² - 6*2 + C = -10`, so `C=0`, which makes `s(t) = 0.5t² - 6t`
- Substitute: `s(4) = 0.5 * 4² - 6*4 = -16`
