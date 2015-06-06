"""
Module for approximating square-root of number x using the Newton's Method
"""

def sqrt2(x):
	"""
	More details.
	"""
	s = 1.
	tol = 1.e-14
	kmax = 100
	for k in range(kmax):
		print "Before iteration %s, s = %s." % (k+1,s)
		s0 = s
		s = 0.5 * (s + x/s)
		delta_s = s - s0
		if abs(delta_s) < tol:
			break
	print "After iteration %s, s = %s." % (k+1,s)