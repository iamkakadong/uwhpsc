program main

	use newton, only: solve, tol
	use functions, only: f_quartic, fprime_quartic, epsilon

	implicit none
	real(kind=8) :: x, x0, fx, xstar
	real(kind=8) :: x0vals(2), xstarvals(2), epsvals(3), tolvals(3)
	integer :: iters, itest, ieps, itol
	logical :: debug

	print *, "Test routine for Newton's Method on quadratic function"
	debug = .false.

	! values to test f
	x0vals = (/4.d0,0.d0/)
	epsvals = (/1.e-4, 1.e-8, 1.e-12/)
	tolvals = (/1.e-5, 1.e-10, 1.e-14/)

	do itest = 1, 2
		x0 = x0vals(itest)
		print 10, x0
10		format ("Starting with initial guess ", e22.15)
		print *, '    epsilon        tol    iters          x                 f(x)        x-xstar'
		do ieps = 1, 3
			epsilon = epsvals(ieps)
			xstarvals = (/1.d0 + (epsilon ** 0.25), 1.d0 - (epsilon ** 0.25)/)
			xstar = xstarvals(itest)
			do itol = 1, 3
				tol = tolvals(itol)
				call solve(f_quartic, fprime_quartic, x0, x, iters, debug)
				fx = f_quartic(x)
				print 11, epsilon, tol, iters, x, fx, x - xstar
11				format(2es13.3, i4, es24.15, 2es13.3)
				enddo
			print *, ' '
			enddo
		enddo

end program main