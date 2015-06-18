! $MYUWHPSC/homework3/functions.f90

module functions

real(kind=8), parameter :: pi = acos(-1.d0)

contains

real(kind=8) function f_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x

    f_sqrt = x**2 - 4.d0

end function f_sqrt


real(kind=8) function fprime_sqrt(x)
    implicit none
    real(kind=8), intent(in) :: x
    
    fprime_sqrt = 2.d0 * x

end function fprime_sqrt

real(kind=8) function f_g1(x)
	implicit none
	real(kind=8), intent(in) :: x

	f_g1 = x * cos(pi * x)

end function f_g1

real(kind=8) function fprime_g1(x)
	implicit none
	real(kind=8), intent(in) :: x

	fprime_g1 = cos(pi * x) - pi * x * sin(pi * x)
end function fprime_g1

real(kind=8) function f_g2(x)
	implicit none
	real(kind=8), intent(in) :: x

	f_g2 = 1.d0 - 0.6d0 * (x ** 2)

end function f_g2

real(kind=8) function fprime_g2(x)
	implicit none
	real(kind=8), intent(in) :: x

	fprime_g2 = - 1.2d0 * x
end function fprime_g2

real(kind=8) function f_f(x)
	implicit none
	real(kind=8), intent(in) :: x

	f_f = f_g1(x) - f_g2(x)
end function f_f

real(kind=8) function fprime_f(x)
	implicit none
	real(kind=8), intent(in) :: x

	fprime_f = fprime_g1(x) - fprime_g2(x)
end function fprime_f
	
end module functions
