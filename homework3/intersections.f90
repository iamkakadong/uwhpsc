! Main program for Fortran part of homework 3. 
! This program calls module that implements Newton's Method to find the
! intersections of two lines specified by g1 and g2.

program main

	use newton, only: solve
	use functions, only: f_g1, fprime_g1, f_g2, fprime_g2, f_f, fprime_f

	implicit none
	real(kind=8) :: x, x0, fx
	real(kind=8) :: x0vals(4)
	integer :: iters, itest
	logical :: debug

	print *, "Test routine of using Newton's Method to compute roots"
	debug = .false.

	!values to test f
	x0vals = (/-2.5d0, -1.7d0, -1.d0, 1.5d0/)

	do itest = 1,4
		x0 = x0vals(itest)
		print *, ' '	! blank line
		call solve(f_f, fprime_f, x0, x, iters, debug)

		print 11, x, iters
11		format ('solver returns x = ', e22.15, ' after', i3, ' iterations')

		fx = f_f(x)
		print 12, fx
12		format ('the value of f(x) is ', e22.15)
		enddo

end program main