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


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
