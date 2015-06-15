
"""
Demonstration module for quadratic interpolation.
Update this docstring to describe your code.
Modified by: ** Tianshu Ren **
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve

def quad_interp(xi,yi):
    """
    Quadratic interpolation.  Compute the coefficients of the polynomial
    interpolating the points (xi[i],yi[i]) for i = 0,1,2.
    Returns c, an array containing the coefficients of
      p(x) = c[0] + c[1]*x + c[2]*x**2.

    """

    # check inputs and print error message if not valid:

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 3"
    assert len(xi)==3 and len(yi)==3, error_message

    # Define the linear system to be solved
    A = np.vstack([np.ones(3), xi, xi ** 2]).T
    b = yi

    # Solve the linear system
    c = solve(A, b)

    return c

def plot_quad(xi, yi):
    """
    
    Plot results of quadratic interpolation. The quadratic curve is plotted in
    solid blue line and data points used for interpolation is plotted in red dots
    Calls function quad_interp as defined in this file

    """
    # Compute coefficients for linear system
    c = quad_interp(xi, yi)

    # Establish points for plotting
    x = np.linspace(xi.min() - 1, xi.max() + 1, 1001)
    y = c[0] + c[1] * x + c[2] * x ** 2

    # Plot figure
    plt.figure(1)   # open plot window
    plt.clf()   # clear plot frame
    plt.plot(x, y, 'b-')    # plot interpolated line

    plt.plot(xi, yi, 'ro')  # plot points of interpolation
    plt.ylim(y.min() - 1, y.max() + 1)  # specify limit of y axis

    plt.title("Data points and interpolating polynomial")   # set title
    plt.savefig("hw2b_quad.png")    # save figure

def cubic_interp(xi, yi):

    error_message = "xi and yi should have type numpy.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have length 4"
    assert len(xi) == 4 and len(yi) == 4, error_message

    # Define the linear system to be solved
    A = np.vstack([np.ones(4), xi, xi ** 2, xi ** 3]).T
    b = yi

    # Solve the linear system
    c = solve(A, b)

    return c

def plot_cubic(xi, yi):
    c = cubic_interp(xi, yi)

    x = np.linspace(xi.min() - 1, xi.max() + 1, 1001)
    y = c[0] + c[1] * x + c[2] * x ** 2 + c[3] * x ** 3

 # Plot figure
    plt.figure(1)   # open plot window
    plt.clf()   # clear plot frame
    plt.plot(x, y, 'b-')    # plot interpolated line

    plt.plot(xi, yi, 'ro')  # plot points of interpolation
    plt.ylim(y.min() - 1, y.max() + 1)  # specify limit of y axis

    plt.title("Data points and interpolating polynomial")   # set title
    plt.savefig("hw2b_cubic.png")    # save figure

def poly_interp(xi, yi):
    
    # check inputs and print error message if not valid:

    error_message = "Incorrect type: xi and yi should be np.ndarray"
    assert (type(xi) is np.ndarray) and (type(yi) is np.ndarray), error_message

    error_message = "xi and yi should have the same length"
    assert (len(xi) == len(yi)), error_message

    # Define the linear system to be solved
    dim = len(xi)   # compute the dimension of this problem
    A = np.ones(dim)    # initialize matrix A with correct 1 dimension

    for i in range(dim - 1):
        A = np.vstack([A, xi ** (i + 1)])   # stacking xi^n layerwise
    A = A.T
    b = yi

    # Solve the linear system
    c = solve(A, b)

    return c

def plot_poly(xi, yi):
    # Compute coefficients
    c = poly_interp(xi, yi)
    
    # Infer dimensions
    dim = len(c)

    # Establish points for plotting
    x = np.linspace(xi.min() - 1, xi.max() + 1, 1001)
    # Hornor's Rule
    y = c[dim-1]
    for i in range(dim - 2, -1, -1):
        y = y * x + c[i]

   # Plot figure
    plt.figure(1)   # open plot window
    plt.clf()   # clear plot frame
    plt.plot(x, y, 'b-')    # plot interpolated line

    plt.plot(xi, yi, 'ro')  # plot points of interpolation
    plt.ylim(y.min() - 1, y.max() + 1)  # specify limit of y axis

    plt.title("Data points and interpolating polynomial")   # set title
    plt.savefig("hw2b_poly.png")    # save figure

def test_quad1():
    """
    Test code, no return value or exception if test runs properly.
    """
    xi = np.array([-1.,  0.,  2.])
    yi = np.array([ 1., -1.,  7.])
    c = quad_interp(xi,yi)
    c_true = np.array([-1.,  0.,  2.])
    print "c =      ", c
    print "c_true = ", c_true
    # test that all elements have small error:
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c,c_true)

def test_quad2():
    """
    Test code, no return value or exception if test runs properly
    """
    xi = np.array([-2.3, 1.2, 3.4])
    yi = np.array([5.4, -2.3, 4.2])
    c = quad_interp(xi, yi)
    plot_quad(xi, yi)

def test_cubic1():
    """
    Test code, no return value or exception if test runs properly
    """
    xi = np.array([-1., 0., 1., 2.])
    yi = np.array([-2., 1., 10., 49.])
    c = cubic_interp(xi, yi)
    plot_cubic(xi, yi)
    c_true = np.array([1., 2., 3., 4.])
    print "c =      ", c
    print "c_true = ", c_true
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c, c_true)

def test_poly1():
    """
    Test code, no return value or exception of test runs properly
    """
    xi = np.array([1., 2., 3., 4., 5.])
    yi = np.array([1., 3., 7., 13., -2.])
    c = poly_interp(xi, yi)
    c_true = np.polyfit(xi, yi, 4)[::-1]    # reverse results from polyfit to match format of our poly_interp
    plot_poly(xi, yi)

    print "c =      ", c
    print "c_true = ", c_true
    assert np.allclose(c, c_true), \
        "Incorrect result, c = %s, Expected: c = %s" % (c, c_true)

if __name__=="__main__":
    # "main program"
    # the code below is executed only if the module is executed at the command line,
    #    $ python demo2.py
    # or run from within Python, e.g. in IPython with
    #    In[ ]:  run demo2
    # not if the module is imported.
    print "Running test..."
    test_quad1()
    tets_quad2()
    test_cubic1()
    test_poly1()

