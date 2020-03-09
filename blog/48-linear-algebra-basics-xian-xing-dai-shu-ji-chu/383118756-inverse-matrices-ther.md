# ❖ Inverse Matrices

> There is actually no concept of `division of matrix`. But similarly we can let it `multiply an inverse` to achieve the same goal.

Refer to 3Blue1Brown: [Inverse matrices, column space and null space ](https://www.youtube.com/watch?v=uQhTuRlWMxw&list=PLZHQObOWTQDPD3MizzM2xVFitgF8hE_ab&index=8)
[Refer to maths is fun: Inverse of a Matrix.](http://www.mathsisfun.com/algebra/matrix-inverse.html)

**SPOILER ALERT: EVEN 3x3 MATRIX INVERSE IS ALREADY TOO HEAVY TO CALCULATE, SO BETTER JUST TO MEMORISE THE 2x2  AND LET COMPUTER DO ALL THE HIGHER DIMENSIONS.**

![image](https://user-images.githubusercontent.com/14041622/38729660-3e545774-3f46-11e8-94e8-928dde93154f.png)

## Understand the 「Inverse Matrix」

> 3Blue1Brown's video perfect explained the intuition of it, pretty much everything you need to know.
[Link: Inverse matrices, column space and null space ](https://youtu.be/uQhTuRlWMxw?t=3m58s)

**It makes lots more sense in geometric meanings, that an Inverse Matrix just to RECOVER the transformation of a graph back to before.**

![image](https://user-images.githubusercontent.com/14041622/38731998-1c629514-3f4f-11e8-8e67-7678eea7ac35.png)

![image](https://user-images.githubusercontent.com/14041622/38732004-2409df0c-3f4f-11e8-8d34-fe2c9c86ab2d.png)

![image](https://user-images.githubusercontent.com/14041622/38731792-5a980a18-3f4e-11e8-8ebb-dd3a11f3b540.png)

![image](https://user-images.githubusercontent.com/14041622/38731911-c38a8000-3f4e-11e8-9484-00f53cb2dda0.png)

### Why is the 「Inverse Matrix」 at the Left of Vector

Because Matrix `A` is always as a `"Coefficient"` to the vector, or as a `transformation rule` to the vector, so it's always on the left of the vector ( or the graph).

![image](https://user-images.githubusercontent.com/14041622/38735715-33449f86-3f5c-11e8-92f1-eee513f4956b.png)



## 「Identity Matrix」

> It's a simple yet important notation for doing dividing a matrix.

The `Identity Matrix` is the matrix equals to the number of `1`:
![image](https://user-images.githubusercontent.com/14041622/38728577-d929f67c-3f42-11e8-9e0b-fb6d4b36bb50.png)

> It's very much more intuitive to think a `identity matrix` as **`one unit vector`**.
- 1-Dimension: `x = 1`
- 2-Dimensions: `v = (1, 1)`
- 3-Dimensions: `v = (1, 1, 1)`

![image](https://user-images.githubusercontent.com/14041622/38728979-0b516648-3f44-11e8-9b52-ed7737029f3a.png)


### The features of 「Identity Matrix」

- It is `square` (m×m Matrix)
- It can be large or small (2×2, 3×3, 100×100, ... whatever)
- It has `1`s on the diagonal and `0`s everywhere else
- Its symbol is the capital letter `𝗜`

More importantly, **IT CAN SWITCH SIDE WHEN MULTIPLYING ANOTHER MATIRX!**
It's very special, and is the **ONLY** matrix can IGNORE the order when multiplying another matrix.
![image](https://user-images.githubusercontent.com/14041622/38729092-6086a8f8-3f44-11e8-861b-8d8e9f1bb592.png)

## 「Not Invertible」 Matirces

Two conditions make a matrix NOT invertible:
- The matrix is not a `Square Matrix` (m×m matrix).
- The `Determinant` is **ZERO**. Such matrix is also called a **`Singular matrix`**

![image](https://user-images.githubusercontent.com/14041622/38730081-c76d03ca-3f47-11e8-8730-2a83613f8f17.png)

## 「Adjugate Matrix」

> It's also called the `Adjoint of a matrix`, or `Classical Adjoint`.

Refer to maths is fun: [Inverse of a Matrix using Minors, Cofactors and Adjugate.](https://www.mathsisfun.com/algebra/matrix-inverse-minors-cofactors-adjugate.html)

### 「Adjugate」 of 2x2 Matrix

![image](https://user-images.githubusercontent.com/14041622/38730850-c295be48-3f4a-11e8-8ede-eb652ea0cc43.png)


## Calculate the 「Inverse」 of a 「Matrix」

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

> **I tend not to note the full content here, because it's so useless in normal math life. Because it's way to hairy to calculate even with a 3x3 matrix. So just get the idea and let computer do the rest.** 


### Example
![image](https://user-images.githubusercontent.com/14041622/46570833-2e61a600-c99d-11e8-814f-3d7d7d419bd3.png)

Solve:
- The formula for Inverse Matrix is `Adjugate(A) / Determinant(A)`.
- The Determinant of A is `-3*-5 - 2*6 = 3`
- The Adjugate of A is `[(-5, -2), (-6, -3)]`
- So the answer is :
![image](https://user-images.githubusercontent.com/14041622/46570915-b0060380-c99e-11e8-9e5c-cf8a9603adfd.png)



## Solving 「Systems of equations」 with 「Inverse Matrices」

[Khan lecture: Solving linear systems with matrix equations](https://www.khanacademy.org/math/precalculus/precalc-matrices/modal/v/solving-matrix-equation)

![image](https://user-images.githubusercontent.com/14041622/38735551-ac48e136-3f5b-11e8-958d-7466e6b63226.png)

