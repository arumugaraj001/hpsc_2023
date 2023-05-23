program trapez
implicit none
!$use omp_lib
real(kind=8) :: b, a, dx, x, z, summ, integral
real(kind=8), external :: f
integer n, i
character(len=32) :: arg
!n is number of intervals, a and b are the lower and upper limit respectivey.

call get_command_argument(1, arg)
    read(arg , *) b
    
call get_command_argument(2, arg)
    read(arg , *) a
    
call get_command_argument(3, arg)
    read(arg , *) n

!print *, "Enter the upper limit of the function in radians"
!read *, b

!print *, "Enter the upper limit of the function in radians"
!read *, a

!print *, "Enter the number of intervals"
!read *, n 

dx = (b-a) / n
!z = f(x)
summ = 0
!$omp parallel do reduction( + :summ)
	do i=1,n
	x = a + i*dx
	 if (i==0) then
	 	summ = summ + f(x)
	 elseif (i==n) then
	 	summ = summ + f(x)
	 elseif (i/=0 .or. i/=n) then
	 	summ = summ + 2.d0*f(x)
	 endif
	end do
!$omp end parallel do

integral = summ * (dx/2.d0)
print *, "The value of the integral cos(y) from  b to a is ", integral

end program trapez

function f(y)
implicit none
real(kind=8), intent(inout) :: y
real(kind=8) :: f
	f = cos(y)
end function f


