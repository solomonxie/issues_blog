# Matrix intro

> `Matrices` are just a **rectangle array of numbers**.

Prerequisites: `Systems of equations`

![image](https://user-images.githubusercontent.com/14041622/38552009-51700eb2-3ced-11e8-86ce-15a21a9b3c0e.png)


Matrices could be seen as a group of informations arranged **IN A CERTAIN WAY**.
**IT'S SO SO SO SO SO EASIER TO THINK IT AS A SYSTEM OF EQUATIONS.**

![image](https://user-images.githubusercontent.com/14041622/38552056-6a3a18fc-3ced-11e8-9f40-bae36f2b775d.png)

![image](https://user-images.githubusercontent.com/14041622/38731392-9ab1ae9e-3f4c-11e8-8c8b-7c53436ad624.png)

## 「Matrix row operations」 & 「Systems of equations」

> It's very SAME with operations of `systems of equations`.

[Refer to Khan academy article: Matrix row operations](https://www.khanacademy.org/math/precalculus/precalc-matrices/elementary-matrix-row-operations/a/matrix-row-operations)

![image](https://user-images.githubusercontent.com/14041622/38552166-dff4d4d8-3ced-11e8-8ae4-3d9144c35473.png)


There're different types of row operations:
- Switch any two rows
- Multiply a row by a nonzero constant
- Add one row to another

They all relate to the operations of systems of equations:
### Switching any two rows:
![image](https://user-images.githubusercontent.com/14041622/38552224-08aa1bea-3cee-11e8-93c2-61943babeb98.png)

### Multiply a row by a 「nonzero constant」

![image](https://user-images.githubusercontent.com/14041622/38552233-138a8cca-3cee-11e8-8569-f3a8238e554c.png)

### Add one row to another

![image](https://user-images.githubusercontent.com/14041622/38552241-1c33501e-3cee-11e8-9604-3704346237a7.png)

## Solve 「system equations」 using Matrix

> it's also called the **`Row-Echelon form and Gaussian elimination`**.

[Khan lecture: Reduced row echelon form](https://www.khanacademy.org/math/precalculus/precalc-matrices/modal/v/matrices-reduced-row-echelon-form-2)
[Refer to Ck-12: Row Operations and Row Echelon Forms](https://www.ck12.org/c/algebra/row-operations-and-row-echelon-forms/lesson/Row-Operations-and-Row-Echelon-Forms-PCALC/?collectionCreatorID=3&conceptCollectionHandle=algebra-%3A%3A-row-operations-and-row-echelon-forms&collectionHandle=algebra)
[Example of "RREF": Lec 01 - Linear Algebra | Princeton University](https://youtu.be/Ncu9Pks3AJQ?t=29m54s)

> It's a so serious problem in all the first lesson of Linear algebra courses. It seems simple yet not easy to solve by yourself. You need to understand all the steps of how to do a `REF` or `RREF`, aka. `Reduce Row Echelon Form`.

The important note to apply the `RREF` is to know how the `Pivot`, or the `Cursor` moves. 
It's more efficient to understand it with 1 or 2 practice rather than see notes here.

First we need to rewrite the system of equation to `matrix` form:
![image](https://user-images.githubusercontent.com/14041622/38552612-41076fc8-3cef-11e8-9654-fdadcb7627ba.png)

Then by `row operations`, we need to achieve this kind of result, which is also called **Reduced Row Echelon Form**:
![image](https://user-images.githubusercontent.com/14041622/38552642-53ad647a-3cef-11e8-9e72-3172da752b5d.png)

It means we eliminated all other variables and only left 1 variable in one equation, which is called **`Identity Matrix`**. Then you could put back the number to the system of equations.


