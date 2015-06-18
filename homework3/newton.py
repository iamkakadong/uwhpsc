"""

A python script that implements Newton's Method to find the root of function f(x)

"""

def solve(fvals, x0, debug = False):
    # Solves f(x) = 0 by using the Newton's Method with initial guess x0
    # Through each iteration, x is updated as x_new = x_old - f(x_old)/f'(x_old)
    # Max iterations is "maxiter", tolerance is set based on f(x) close enough to 0
    maxiter = 20
    tol = 1.e-14
    num_iter = 0
    x = x0
    (fx, fxp) = fvals(x)
    if debug:
        print "Initial guess: x = %22.15e" % x0
    while (num_iter <= maxiter and abs(fx) >= tol):
        x = x - fx/fxp
        (fx, fxp) = fvals(x)
        num_iter = num_iter + 1
        if debug:
            print "After %i iterations, x = %22.15e" % (num_iter, x)
    return x, num_iter

# $UWHPSC/codes/homework3/test_code.py 
# To include in newton.py

def fvals_sqrt(x):
    """
    Return f(x) and f'(x) for applying Newton to find a square root.
    """
    f = x**2 - 4.
    fp = 2.*x
    return f, fp

def test1(debug_solve=False):
    """
    Test Newton iteration for the square root with different initial
    conditions.
    """
    from numpy import sqrt
    for x0 in [1., 2., 100.]:
        print " "  # blank line
        x,iters = solve(fvals_sqrt, x0, debug=debug_solve)
        print "solve returns x = %22.15e after %i iterations " % (x,iters)
        fx,fpx = fvals_sqrt(x)
        print "the value of f(x) is %22.15e" % fx
        assert abs(x-2.) < 1e-14, "*** Unexpected result: x = %22.15e"  % x