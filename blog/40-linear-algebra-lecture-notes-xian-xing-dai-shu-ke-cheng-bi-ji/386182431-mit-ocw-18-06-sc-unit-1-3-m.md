# MIT OCW 18.06 SC  Unit 1.3 Multiplication & Inverse Matrices

Prerequisites | Links
-- | --
Matrix multiplication basics(row * col) | [Note](https://github.com/solomonxie/solomonxie.github.io/issues/40#issuecomment-386033645)
Elementary matrices | [Video](https://www.youtube.com/watch?v=1SoU0BfhKaI&feature=youtu.be)

![image](https://user-images.githubusercontent.com/14041622/39558587-692a7a7e-4ec2-11e8-86ed-81f3087d761a.png)

[Refer to Juanklopper's jupyter notebook.](https://github.com/solomonxie/jupyter-notebooks/blob/master/forks/MIT_OCW_Linear_Algebra_18_06-master/I_04_Matrix_multiplication_Inverses.ipynb)

Lecture timeline | Links
-- | --
Lecture | [0:0](https://www.youtube.com/watch?v=FX4C-JpTFgY&t=136s&index=3&list=PLE7DDD91010BC51F8)
Method 1: Multiply matrix by vector | [0:50](https://youtu.be/FX4C-JpTFgY?t=50s)
When allowed to multiply matrices | [4:38](https://youtu.be/FX4C-JpTFgY?t=4m38s)
Method 2: Multiply matrix by COLUMN | [6:12](https://youtu.be/FX4C-JpTFgY?t=6m12s)
Method 3: Multiply ROW by matrix | [10:04](https://youtu.be/FX4C-JpTFgY?t=10m4s)
Method 4: Multiply COLUMN by ROW | [11:37](https://youtu.be/FX4C-JpTFgY?t=11m37s)
Method 5: Block Multiplication | [18:25](https://youtu.be/FX4C-JpTFgY?t=18m25s)
Inverse Matrices (Square matrices) | [21:15](https://youtu.be/FX4C-JpTFgY?t=21m15s)
Invertible Matrix | [22:00](https://youtu.be/FX4C-JpTFgY?t=22m)
Singular Matrix (No-inverse matrix) | [24:39](https://youtu.be/FX4C-JpTFgY?t=24m39s)
Calculate Inverse of Matrix | [31:52](https://youtu.be/FX4C-JpTFgY?t=31m52s)
Gauss-Jordan Elimination to solve Inverse of a matrix | [35:20](https://youtu.be/FX4C-JpTFgY?t=35m20s)


## Method 1: Multiply 「matrix by vector」

Calculation of an entry of the Product Matrix.

![image](https://user-images.githubusercontent.com/14041622/39560053-60299bb6-4ecd-11e8-988c-c8359b65fdbc.png)


![image](https://user-images.githubusercontent.com/14041622/39558944-429fcc62-4ec5-11e8-809b-8be93a1660cb.png)

## Method 2: Multiply 「matrix by COLUMN」

Each **column** of the `product matrix C`, is `Matrix A * Column of B`.

![image](https://user-images.githubusercontent.com/14041622/39559663-7857ec9a-4eca-11e8-9a71-c969fa48bac6.png)

## Method 3: Multiply 「ROW by matrix」

Each **row** of the `product matrix C`, is `Row of A * Matrix B`.

![image](https://user-images.githubusercontent.com/14041622/39559794-77f07a8c-4ecb-11e8-82af-4cdd8c8d9821.png)


## Method 4: Multiply 「COLUMN by ROW」

![image](https://user-images.githubusercontent.com/14041622/39559955-ab9ad82c-4ecc-11e8-9d7e-790b76d79975.png)

### 「Dot product」

![image](https://user-images.githubusercontent.com/14041622/39560005-08e11582-4ecd-11e8-8f10-53322d584bb3.png)

![image](https://user-images.githubusercontent.com/14041622/39709443-6a62c152-524c-11e8-9137-23904f5b6d5a.png)

## Method 5: 「Block multiplication」

You can cut each matrix to blocks, each block is no necessary to be equal sized as long as they can match each other well.

![image](https://user-images.githubusercontent.com/14041622/39560231-e0a54096-4ece-11e8-99c7-5d64c5e739ad.png)

After you cut matrices into blocks, the multiplication will just be like a smaller matrix multiplication: **Each block can be seen as a number in a matrix.**

![image](https://user-images.githubusercontent.com/14041622/39560200-a36da5f6-4ece-11e8-9c9b-c729f0418abd.png)

## 「Inverses」 (Square matrices)

If a matrix's inverse exists, then we call this matrix `Invertible`, or `Non-singular`.

And only with `square matrices`, the inverse can be both **right side** or **left side** with the original matrix to produce the `Identity Matrix`.

![image](https://user-images.githubusercontent.com/14041622/39560342-d9d403f0-4ecf-11e8-8526-c704ad2d4811.png)

### 「Singular Matrix」 (No inverse)

Simplest way to tell if it's a `singular matrix` is to calculate its `Determinant` which we learnt in high school: It's a singular matrix if its determinant is ZERO.
But there's another way to tell:

![image](https://user-images.githubusercontent.com/14041622/39560934-b1d24c04-4ed4-11e8-9d8c-c0331fc8b2db.png)


## Use 「Gauss-Jordan Elimination」 to get Inverse

**THIS METHOD IS SO MUCH EASIER TO GET THE INVERSE THAN THE WAY WE LEARNT IN HIGH SHCOOL WHICH LETS YOU TO CALCULATE ALL DETERMINANT, ADJUGATE AND COFACTOR AND SO ON.**

[Refer to Khan academy lecture: Inverting a 3x3 matrix using Gaussian elimination.](https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-determinants-and-inverses-of-large-matrices/v/inverting-matrices-part-3)

[Online Calculator.](https://www.symbolab.com/solver/step-by-step/inverse%20%5Cbegin%7Bpmatrix%7D1%262%261%5C%5C%202%260%260%5C%5C%200%260%262%5Cend%7Bpmatrix%7D)

Practice for Gauss-Jordan Elimination to get Inverse of a matrix:
- [ ] [Khan academy](https://www.khanacademy.org/math/algebra-home/alg-matrices/alg-determinants-and-inverses-of-large-matrices/e/matrix_inverse_3x3)
- [ ] [Symbolab](https://www.symbolab.com/practice/matrices-practice#area=main&subtopic=Inverse&isTour=false)
- [ ] [Wolfram](https://www.wolframalpha.com/problem-generator/quiz/?category=Linear%20algebra&topic=Inverse2Matrix)
- [ ] [UOS](http://www.maths.usyd.edu.au/u/UG/JM/MATH1002/Quizzes/quiz8.html)

![image](https://user-images.githubusercontent.com/14041622/39561075-e257821c-4ed5-11e8-922d-8158a6587525.png)

With this formula above, we got TWO equations, which will help us form a **system of equations**!
That's where Gauss comes in: we **AUGMENT TWO COLUMNS** to the matrix.

![image](https://user-images.githubusercontent.com/14041622/39561501-a6a297d6-4ed8-11e8-9a18-f92b4b309ad2.png)

Why could we use Gauss-Jordan Elimination to solve `Inverse of matrix`?

![image](https://user-images.githubusercontent.com/14041622/39561633-7483dae8-4ed9-11e8-996c-703cc2fcabb4.png)

The `E` above represents `all elementary matrices`.

[Refer mathispower4uFor for refreshing on: How to get elementary matrices](https://www.youtube.com/watch?v=1SoU0BfhKaI&feature=youtu.be)

![image](https://user-images.githubusercontent.com/14041622/39562501-89d4b1d8-4ede-11e8-8b38-b46d31ee20cb.png)

