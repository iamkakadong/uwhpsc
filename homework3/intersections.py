"""

This script searches for intersecions of the two functions:

	g1(x) = x * cos(pi * x)
	g2(x) = 1 - 0.6 * (x ^ 2)

Using the Newton's Method, this script finds the root of the function g1(x) - g2(x) = 0
The resulting values would be the intersections of interest here.

Initial guesses are acquired by first observing the plots of two functions in ipython

"""

from newton import solve
from numpy import sin, cos, pi, linspace
from matplotlib.pyplot import *

### Define functions to be used
def fvals_g1(x):
	"""
	Returns g1(x) and g1'(x)
	"""
	f = x * cos(pi * x)
	fp = cos(pi * x) - pi * x * sin(pi * x)
	return f, fp

def fvals_g2(x):
	"""
	Returns g2(x) and g2'(x)
	"""
	f = 1. - 0.6 * (x ** 2)
	fp = - 1.2 * x
	return f, fp

def fvals_f(x):
	"""
	Returns g1(x) - g2(x) and g1'(x) - g2'(x)
	"""
	f = fvals_g1(x)[0] - fvals_g2(x)[0]
	fp = fvals_g1(x)[1] - fvals_g2(x)[1]
	return f, fp

### Set parameters
debug_solve = True
init_guess = [-2.5, -1.7, -1., 1.5]
pts_x = []
pts_y = []

### Solving for intersections
for x0 in init_guess:
	print " "
	x, iters = solve(fvals_f, x0, debug = debug_solve)
	print "With intial guess x0 = %22.15e," % x0
	print "		solve returns x = %22.15e after %i iterations " % (x,iters)
	fx = fvals_g1(x)[0]
	pts_x.append(x)
	pts_y.append(fx)

### Plotting two curves and intersection points
x = linspace(-5,5,1000)
y1 = fvals_g1(x)[0]
y2 = fvals_g2(x)[0]

figure(0)
clf()
plot(x, y1, 'b-', label = 'g1(x)')
plot(x, y2, 'r-', label = 'g2(x)')
plot(pts_x, pts_y, 'ko', label = 'intersections')
legend(loc = 'best')
savefig('intersections.png')