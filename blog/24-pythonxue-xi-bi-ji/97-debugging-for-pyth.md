# Debugging for Python C Extension [DRAFT]

Observation:
- If you use `pdb` to debug in the python wrapper of C code, you can't `step in` the function if it's a function from a C extension. `pdb` will **skip** the c function.
- You can `printf(..)` in the C code to do basic debugging.

Not sure if this works:
![image](https://user-images.githubusercontent.com/14041622/56176332-62451480-602d-11e9-8498-1e7602be1113.png)

