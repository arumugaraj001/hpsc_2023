Demonstrate the magic command ! to run terminal codes through ipython

# Use ! to run a terminal command - this is for serial version of code
! /usr/bin/time ./mcpi.exe 10000000 4

# Use ! to run a terminal command - this is for parallel version of code
! /usr/bin/time ./mcpiP.exe 10000000 4

Os.system command to execute terminal commands
import os
command="ls"
command_suffix="-l"
os.system(command+" "+command_suffix)

Time() function of python to time system commands
 Use the time.time() function to calculate time in Python
import os
import time
points=2 * 10**8
threads=2
command = "./mcpiP.exe "+str(points)+" "+str(threads)
print("threads = ",threads)
print(f"number of points = {points: .1e}")
print(command)
time1=time.time()
os.system("/usr/bin/time -p "+command)
time2=time.time()
print(f"time taken = {time2-time1 : .3}sec")


Strong scaling
# Perform strong scaling
import os
import time
points=2 * 10**8
max_num_threads = 8
scaling=[]
for threads in range(1,max_num_threads):
    command = "./mcpiP.exe "+str(points)+" "+str(threads)
    print("threads = ",threads)
    print(f"number of points = {points: .1e}")
    print(command)
    time1=time.time()
    os.system(command)
    time2=time.time()
    time_taken=time2-time1
    print(f"time taken = {time_taken : .3}sec\n")
    scaling.append([threads,time_taken])
    
# plot the data for visualisation
from matplotlib.pylab import plt
import numpy as np

print("Raw data")
print(scaling)

x = [item[0] for item in scaling]
y = [item[1] for item in scaling]
plt.plot(x,y,'*')
plt.xlabel("Number of threads")
plt.ylabel("Elapsed time in sec")


# plot the data for visualisation for speedup
from matplotlib.pylab import plt
import numpy as np

xx=np.array(x)
yy=np.array(y)
yy=yy/yy[0]
yy=1./yy
plt.plot(xx,yy,'^')
plt.xlabel("Number of threads")
plt.ylabel("Speedup")


Estimate the algorithm order
# Algorithm order
import os
import time
pb=2* 10**7
threads = 2
points_list = [pb,2*pb,4*pb,8*pb,16*pb]
scaling=[]
for points in points_list:
    command = "./mcpiP.exe "+str(points)+" "+str(threads)
    print("threads = ",threads)
    print(f"number of points = {points: .1e}")
    print(command)
    time1=time.time()
    os.system(command)
    time2=time.time()
    time_taken=time2-time1
    print(f"time taken = {time_taken : .3}sec\n")
    scaling.append([points,time_taken])

# plot the data for visualisation
from matplotlib.pylab import plt
import numpy as np

print("Raw data")
print(scaling)

x = [item[0] for item in scaling]
y = [item[1] for item in scaling]
plt.plot(x,y,'*')
plt.xlabel("Number of points")
plt.ylabel("Elapsed time in sec")


Weak Scaling

# Perform weak scaling
import os
import time
pb=2* 10**7
threads_list = [1,2,3,4]
points_list = [pb,2*pb,3*pb,4*pb]
scaling=[]
for points,threads in zip(points_list,threads_list):
    command = "./mcpiP.exe "+str(points)+" "+str(threads)
    print("threads = ",threads)
    print(f"number of points = {points: .1e}")
    print(command)
    time1=time.time()
    
    
    
import matplotlib.pyplot as plt
import numpy as np
x = []
u = []
with open('heatsoln.txt') as f:
    for line in f:
        row=line.split()
        x.append(row[0])
        u.append(row[-1])
x=x[1:]
u=u[1:]
x_ar=np.array(x)
x_array = x_ar.astype(np.float64)
u_ar=np.array(u)
u_array = u_ar.astype(np.float64)
u_exact=(100*np.exp(1.)-60)*x_array + 120 - 100*np.exp(x_array)
plt.plot(x_array[0:-1:1],u_array[0:-1:1],'bo')
plt.plot(x_array,u_exact,'r')

plt.xlabel('x')
plt.ylabel('u')
plt.show()



import matplotlib.pyplot as plt
import numpy as np
x = []
u = []
with open('heatsoln.txt') as f:
    for line in f:
        row=line.split()
        x.append(row[0])
        u.append(row[-1])
x=x[1:]
u=u[1:]
x_ar=np.array(x)
x_array = x_ar.astype(np.float64)
u_ar=np.array(u)
u_array = u_ar.astype(np.float64)
u_exact=(100*np.exp(1.)-60)*x_array + 120 - 100*np.exp(x_array)
plt.plot(x_array[0:-1:3],u_array[0:-1:3],'bo')
plt.plot(x_array,u_exact,'r')

plt.xlabel('x')
plt.ylabel('u')
plt.show()



from pylab import *

# read in three columns from file and unpack into 3 arrays:
n,int_approx,error = loadtxt('mc_laplace_error.txt',unpack=True)

figure(1)
clf()
loglog(n,error,'-o',label='Monte-Carlo')
loglog([1,1e7],[1,sqrt(1e-7)],'k',label='1 / sqrt(N)')
legend()
xlabel('number of random walks taken')
ylabel('abs(error)')
title('Log-log plot of relative error in MC Laplace')
savefig('mc_laplace_error.png')


import matplotlib.pyplot as plt
from numpy import *
x=linspace(0,6*pi,100)
y=sin(x)
plt.plot(x,y)
#print(x)


from numpy import exp
import numpy as np
import matplotlib.pyplot as plt

def recur_factorial(n):                           #Calculating factorial of a number
                if n == 1 or n== 0:
                    return 1
                else:
                    return n*recur_factorial(n-1)
                
def your_exp(a,b,n=100):                          #Calculating exponential using user-defined function your_exp()
    '''
    To calculate the exponent of a series of numbers.
    
    Input: Enter the first and last term of the series and the number of intervals you want inbetween
    
    Output: The exponential of the series is displayed from both your_exp() and numpy_exp() and the output is also plotted.
    '''
    import numpy as np
    exp_array= np.zeros(n)
    exp_list = []
    my_array = np.linspace(a,b,n)
    tol = 1e-6
    for x in my_array:
        expon = 0
        for y in range(150):
            expon0 = expon
            expon += x**y / recur_factorial(y)   #function calling to find factorial of a number
            delta_expon = expon - expon0
            if(abs(delta_expon)/expon)<tol:
                print(expon)                     #Printing of your_exp()
                break
        exp_list.append(expon)
    print ( exp(np.linspace(a,b,n)))             #Calculating and printing exponential using numpy exp() function
    
    
    
    plt.plot(my_array,exp_list, 'r', label='your_exp')    #Plotting of your_exp() and numpy_exp()
    plt.ylabel ('exponential')
    plt.xlabel('values')
    plt.plot( my_array, exp(np.linspace(a,b,n)),'x', label = 'numpy_exp')
    plt.title('Graph for your_exp vs numpy_exp')
    plt.legend(['your_exp', 'numpy_exp'], loc= 'upper left')
    plt.savefig('your_exp vs numpy_exp .png')
    plt.show()

