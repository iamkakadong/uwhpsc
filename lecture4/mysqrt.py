"""
Module for approximating square-root of number x using the Newton's Method
"""

def sqrt2(x, debug=False):
	"""
	More details.
	"""
	from numpy import nan

	if x == 0.:
		return 0.
	elif x < 0:
		print "*** Error, x must be nonnegative"
		return nan
	assert x > 0. and type(x) is float, "Unrecognized input"

	s = 1.
	tol = 1.e-14
	kmax = 100
	for k in range(kmax):
		if debug:
			print "Before iteration %s, s = %20.15f." % (k+1,s)
		s0 = s
		s = 0.5 * (s + x/s)
		delta_s = s - s0
		if abs(delta_s) < tol:
			break
	if debug:
		print "After iteration %s, s = %20.15f." % (k+1,s)
	return s

def test():
	from numpy import sqrt
	xvalues = [0., 2., 1000., 1.e-4]
	for x in xvalues:
		print "Testing with x = %20.15e" % x
		s = sqrt2(x)
		s_numpy = sqrt(x)
		print "s = %20.15e, numpy.sqrt = %20.15e" % (s, s_numpy)
	assert abs(s - s_numpy) < 1e-14, "Disagree for x = %20.15e" % x