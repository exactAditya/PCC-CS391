import marimo

__generated_with = "0.23.5"
app = marimo.App(width="medium")


@app.cell
def _():
    import numpy as np
    import marimo as mo

    return mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 1D array of int from 0 to 9
    """)
    return


@app.cell
def _(np):
    np.arange(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 2x3 array with zeros
    """)
    return


@app.cell
def _(np):
    np.zeros(6).reshape(2,3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
 
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3x3 identity matrix
    """)
    return


@app.cell
def _(np):
    np.eye(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## array of even numbers from 2 to 20
    """)
    return


@app.cell
def _(np):
    np.arange(2,21, 2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## create 5 values between 0 1 inclusive
    """)
    return


@app.cell
def _(np):
    np.linspace(start=0, stop=1, num=5)
    np.linspace(0,1,5)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 4x4 array filled with ones of dtype `int64`
    """)
    return


@app.cell
def _(np):
    np.ones(16, dtype= np.int64).reshape(4,4)
    np.ones((4,4))
    np.full((2,3),3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 3x2 matrix containing 1 to 6
    """)
    return


@app.cell
def _(np):
    np.arange(1,7).reshape(3,2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## convert list into array
    """)
    return


@app.cell
def _(np):
    np.array([1,2,3,4])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 9. find dtype, shape, size, and ndim of an array and print them
    """)
    return


@app.cell
def _(np):
    a = np.array([[3,4,3,4],[5,6,7,4],[5,6,7,4]])
    print(f"""
    dtype = {a.dtype}
    shape = {a.shape}
    ndim = {a.ndim}""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 10. change array dtype from float64 to int32
    """)
    return


@app.cell
def _(np):
    a = np.array([1,1,1], dtype= np.float64)
    print(a.dtype)
    fa = a.astype('int32')
    print(fa.dtype)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 11. boolean array from mixed list like [True, False, 1, 0]
    """)
    return


@app.cell
def _(np):
    _a = np.array([True, False, 1, 0], dtype= np.bool)
    print(_a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 12. use zeros to create 3x3 float array and assign a value to element (1,2)
    """)
    return


@app.cell
def _(np):
    _a = np.zeros((3,3), dtype= np.float16)
    _a[1,2] = 3
    print(_a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 13. array of 10 random floats between 0 and 1
    """)
    return


@app.cell
def _(np):
    _a = np.random.rand(10)
    _a
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 14. 5x5 array of random ints between 0 and 9
    """)
    return


@app.cell
def _(np):
    _a = np.random.randint(10, size=25).reshape(5,5)
    _a
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 15. seed random generator and show reproducibility of `np.random.rand`
    """)
    return


@app.cell
def _(np):
    np.random.seed(24)
    print(np.random.rand(5))

    np.random.seed(24)
    print(np.random.rand(5))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 16. construct a 3d array of shape (2,3,4)
    """)
    return


@app.cell
def _(np):
    _a = np.arange(24).reshape(2,3,4)
    print(_a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 17. perform vector addition
    """)
    return


@app.cell
def _(np):
    _a = np.arange(5)
    _b = np.arange(5)
    _a + _b
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 18. multiply arrays element-wise and compute dot product
    """)
    return


@app.cell
def _(np):
    _a = np.arange(4)
    _b = np.arange(4)

    sum(_a * _b)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 19. add 5 to 2x4 array
    """)
    return


@app.cell
def _(np):
    _a = np.random.rand(2,4) * 100
    round_vec = np.vectorize(round)
    round_vec(_a)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 20. broadcast 1d array to 2x3 matrix
    """)
    return


@app.cell
def _(np):
    _a = np.array([1,2,3]) + np.zeros((2,3))
    _a
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 21. replace negative values with zero in an array
    """)
    return


@app.cell
def _(np):
    _a = np.arange(-2,4).reshape(2,3)
    _a[_a < 0] = 0
    _a
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 22. find sum, mean, std, var of 1d array
    """)
    return


@app.cell
def _(np):
    _a = np.arange(-2,3)
    print(f"""
    sum = {np.sum(_a)}
    mean = {np.mean(_a)}
    std = {np.std(_a)}
    var = {np.var(_a)}""")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 23. compute row-wise and column-wise sum of 2x4 array
    """)
    return


@app.cell
def _(np):
    _a = np.arange(-4,4).reshape(2,4)
    print(_a)
    print("Row sum", np.sum(_a, axis=1))
    print("Column sum", np.sum(_a, axis=0))

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 24. cumulative sum and cumulative product for 1d array
    """)
    return


@app.cell
def _(np):
    _a = np.array([
        [[3,4,5], [1,2,3]],
        [[3,4,5], [1,2,3]]
    ])
    print(_a)
    print(f"""
    cumulative product = {np.cumprod(_a)}
    cumulative sum = {np.cumsum(_a)}
    """)

    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 25. apply `np.sqrt`, `np.log`, `np.exp` on float array
    """)
    return


@app.cell
def _(np):
    _a = np.random.rand(5)
    print("Original array:\n", _a)
    print("Sqrt array:\n", np.sqrt(_a))
    print("Log array:\n", np.log(_a))
    print("Exp array:\n", np.exp(_a))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 26. apply `sin` and `cos` function on array of angles
    """)
    return


@app.cell
def _(np):
    _a = np.arange(5)
    print("Original array:\n", _a)
    print("Sin array:\n", np.sin(_a))
    print("Cos array:\n", np.cos(_a))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 27. perform element-wise exponentiation of arrays
    """)
    return


if __name__ == "__main__":
    app.run()
