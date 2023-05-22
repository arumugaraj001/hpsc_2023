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


