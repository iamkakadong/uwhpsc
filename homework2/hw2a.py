import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import solve

# Specify datapoints for the problem
xi = np.array([-1., 1., 2.])
yi = np.array([0., 4., 3.])

# Define the linear system to be solved
A = np.array([np.ones(3), xi, xi ** 2])
A = A.T
b = yi

# Solve the linear system
c = solve(A, b)

print "The polynomial coefficients are"
print c

# Plot resulting polynomial
x = np.linspace(-3., 3., 1001)
y = c[0] + c[1] * x + c[2] * x ** 2

plt.figure(1)
plt.clf()
plt.plot(x, y, 'b-')

plt.plot(xi, yi, 'ro')
plt.ylim(-8, 5)

plt.title("Data points and interpolating polynomial")

plt.savefig('hw2a.png')