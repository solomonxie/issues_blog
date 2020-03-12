# Matrices Elimination

> `Matrices elimination` (or `solving system of linear equations`) is the very first and fundamental skill throughout Linear Algebra. It's probably the first lesson of all sorts of courses.

## Terminology

Before learning `solving systems of linear equations`, you really need to get familiar with all the core terminologies involved, otherwise it can be very hard to move on to next stage.
And in this case, the best way to learn that is through Wikipedia.

JFR, the core terms are: `Gaussian elimination`, `Gauss-Jordan elimination`, `Augmented Matrix`, `Elementary Row Operations`, `Elementary matrix`, `Row Echelon Form (REF)`, `Reduced Row Echelon Form (RREF)`, `Triangular Form`.

## 「Gaussian elimination」

[Refer to wiki: `Gaussian elimination`](https://en.wikipedia.org/wiki/Gaussian_elimination)

> It's a `Row reduction algorithm` to solve System of linear equations.

[Refer to simple wiki: Gaussian elimination](https://simple.wikipedia.org/wiki/Gaussian_elimination)
[Example: showme.com](http://www.showme.com/sh/?h=3fjkVEW)

To perform `Gaussian elimination`, the `coefficients of the terms in the system of linear equations` are used to create a type of matrix called an `augmented matrix`. 
Then, `elementary row operations` are used to **simplify** the matrix. 
The **goal** of Gaussian elimination is to get the matrix in `row-echelon form`. 
If a matrix is in `row-echelon form`, which is also called `Triangular Form`.
Some definitions of Gaussian elimination say that the matrix result has to be in `reduced row-echelon form`. 
**Gaussian elimination that creates a reduced row-echelon matrix result is sometimes called `Gauss-Jordan elimination`.**

To be simpler, here is the structure:
- Algorithm: `Gaussian Elimination`
    - Step 1: Rewrite system to a `Augmented Matrix`.
    - Step 2: Simplify matrix with `Elementary row operations`.
    - Result:
        - `Row Echelon Form` or
        - `Reduced Echelon Form`

And if we make the result only in `RREF`, so the name of the algorithm could also be called:
- Algorithm: `Gauss-Jordan Elimination`
    - Step 1: Rewrite system to a `Augmented Matrix`.
    - Step 2: Simplify matrix with `Elementary row operations`.
    - Result: Only in `Reduced Echelon Form`

### 「Elementary Row Operations」

Elementary row operations are used to **simplify the matrix**. 

The three types of row operations used are:
- Type 1: **Switching** one row with another **row**.
- Type 2: **Multiplying** a row by a non-zero **number**.
- Type 3: **Adding** a row from another **row**. (!Note: you can only **ADD** them but not **subtract**, but you can **ADD** a negative)

Confusing operation: See where the `negative sign` was put:
![image](https://user-images.githubusercontent.com/14041622/39507688-b0f759aa-4e11-11e8-89b3-69846f64a53a.png)


### Example
Suppose the goal is to find the solution for the linear system below:
![image](https://user-images.githubusercontent.com/14041622/39080182-31be1c9a-455c-11e8-927e-773f3788b77a.png)

First we need to turn it into `Augmented Matrix` form:
![image](https://user-images.githubusercontent.com/14041622/39080192-5804ace8-455c-11e8-96ec-57c0d884a69b.png)

Then we apply `Elementary Row Operations`, and result in `Row Echelon Form`:
![image](https://user-images.githubusercontent.com/14041622/39080203-a26b890a-455c-11e8-9f41-50c66079b22e.png)

At the end, if we'd like, we can further on apply some row operations to get the matrix in `Reduced Row Echelon Form`:
![image](https://user-images.githubusercontent.com/14041622/39080275-2846e60a-455d-11e8-83c5-53b84fd5b45a.png)
Reading this matrix tells us that the solutions for this system of equations occur when x = 2, y = 3, and z = -1.

### 「Row Echelon Form」 vs. 「Reduced Row Echelon Form」

[Refer to this lecture video: REF & RREF](https://www.youtube.com/watch?v=W01H0LcVUdQ&index=10&list=PLHXZ9OQGMqxfUl0tcqPNTJsb7R6BqSLo6).

It doesn't really matter it is a `Square Matrix` or not, there could be a `Diagonal` or `Main diagonal`, or you can't draw a diagonal at all. 
The only thing matters is **WHAT ARE ABOVE 1 AND WHAT ARE BELOW 1.**

- REF: For each column, all numbers **below** 1 MUST BE 0. Doesn't matter what numbers are above 1.
- RREF: For each column, all numbers both **above & below** 1 MUST BE 0. We don't care about it if there's no 1 in the column.

![image](https://user-images.githubusercontent.com/14041622/39506655-9e283416-4e0c-11e8-9e58-1df4f85c25e6.png)

## 「Augmented Matrix」

> Means we put another column into the matrix, which represents the **Right side** of the system of equations, numbers of right of the `=` sign.

When we apply elimination to `Linear equations`, we operate both sides at the same time. But for computer programmes, it often apply to **Left side**, and remember the operations, a.g. multiply a number or add equations together, when the left side finished then apply the same operations to the right side.

![image](https://user-images.githubusercontent.com/14041622/39471215-829b2d90-4d74-11e8-97b1-7ce730e92e86.png)

If a given Matrix was told it's an `Augmented Matrix`, so we have to assume that the **Last Column** is **The Solution Column**.

![image](https://user-images.githubusercontent.com/14041622/39482311-20236e3e-4da1-11e8-859e-6954b2d33f4a.png)

## 「Equivalent systems」 & 「Equivalent Matrices」

- Equivalent systems: Linear systems with the SAME SOLUTION SET.
![image](https://user-images.githubusercontent.com/14041622/39482863-30ad3ee0-4da3-11e8-9314-8e6c9010690e.png)
- Equivalent matrices: Two matrices where One Matrix **can be turned** into the other matrix by some `elementary row operations`.
![image](https://user-images.githubusercontent.com/14041622/39482947-735664c4-4da3-11e8-8d4b-fc1b233adc87.png)

## 「Pivot」

> Or called the `Cursor`, or `Basic`, or `Basic variable`.

[Refer to this video from mathispower4u.](http://youtu.be/HFbBclH99d0)

It means the value that represents the `unknown variable`  in each column. There's no `pivot` in a column if you can't get a 1 in that column.

![image](https://user-images.githubusercontent.com/14041622/39506959-5ef42898-4e0e-11e8-89e0-8002688d81fb.png)

### 「Free variables」

If there's no pivot in a column, that means this `unknown variable` of the column can be **any number**, so we call it a `free variable`.

![image](https://user-images.githubusercontent.com/14041622/39507131-27751b7e-4e0f-11e8-9761-cef7ee48cd64.png)

### `Pivot columns`

The `pivots` are found after `Row Reduction`, and then **go back** to the Original Matrix, the columns **WITH** pivots are called `pivot columns`.

![image](https://user-images.githubusercontent.com/14041622/39507277-ce962f42-4e0f-11e8-8638-917697b3a341.png)

### 「Back substitution」

It's simple: When you solve out one `unknown variable` in the Linear System, you put the value back to other equations. We call this process as `Back Substitution`.

![image](https://user-images.githubusercontent.com/14041622/39522421-b93a512a-4e44-11e8-970c-b965fdee3808.png)

