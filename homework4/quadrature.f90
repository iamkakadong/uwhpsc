module quadrature
	implicit none

contains

real(kind=8) function trapezoid(f, a, b, n)
	implicit none
	real(kind=8), intent(in) :: a, b
	integer, intent(in) :: n
	real(kind=8), external :: f
	real(kind=8) :: xj(n), fx(n), h, fx_sum
	integer :: i

	h = (b - a)/(n - 1)
	do i = 1, n
		xj(i) = a + (i-1) * h
		fx(i) = f(xj(i))
		fx_sum = fx_sum + fx(i)
		enddo

	trapezoid = fx_sum * h - 0.5 * h * (fx(1) + fx(n))

end function trapezoid

subroutine error_table(f, a, b, nvals, int_true)
	implicit none
	real(kind=8), intent(in) :: a, b
	real(kind=8), external :: f
	integer, dimension(:), intent(in) :: nvals
	real(kind = 8), intent(in) :: int_true
	integer :: iters, n
	real(kind=8) :: int_trap, error, ratio, last_error

	last_error = 0

	print *, "    n         trapezoid            error       ratio"
	do iters = 1, size(nvals)
		n = nvals(iters)
		int_trap = trapezoid(f, a, b, n)
		error = abs(int_trap - int_true)
		ratio = last_error / error
		last_error = error
		print 11, n, int_trap, error, ratio
11		format(i8, es22.14, es13.3, es13.3)
		enddo

end subroutine error_table

end module quadrature
