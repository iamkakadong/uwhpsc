
program test2_omp

    use quadrature_omp, only: trapezoid, error_table
    use omp_lib

    implicit none
    real(kind=8) :: a,b,k,int_true2
    integer :: nvals(15), i
    real(kind=8) :: t1, t2
    integer(kind=8) :: tclock1, tclock2, clock_rate
    !Specify number of threads to use
    !$ call omp_set_num_threads(2)
    !$ print *, "Using OpenMP:"

    a = 0.d0
    b = 2.d0
    k = 1000.d0
    int_true2 = (b-a) + (b**4 - a**4) / 4.d0 - (1.d0/k) * (cos(k*b) - cos(k*a))

    print 10, int_true2
 10 format("true integral: ", es22.14)
    print *, " "  ! blank line

    ! values of n to test:
    do i=1,15
        nvals(i) = 5 * 2**(i-1)
        enddo
        
    call system_clock(tclock1)
    call cpu_time(t1)

    call error_table(f, a, b, nvals, int_true2)

    call cpu_time(t2)
    call system_clock(tclock2, clock_rate)

    print 11, nvals(size(nvals)), t2-t1
11  format ("Performed numerical integration using quadrature for up to ", i5, " points. The CPU time is: ", f12.8)
    print 12, float(tclock2-tclock1)/float(clock_rate)
12  format ("The total elapsed time is: ", f12.8)

contains

    real(kind=8) function f(x)
        implicit none
        real(kind=8), intent(in) :: x 

        f = 1.d0 + x**3 + sin(k * x)
    end function f

end program test2_omp
