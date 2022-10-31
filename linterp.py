#
# This python program demonstrates linear interpolation
#
import numpy as np
import matplotlib.pyplot as plt

#  Set up data values: 9 points on a sine curve
pi = np.pi
x  = np.arange(9)*2.*pi/8.
f  = np.sin(x)

# loop over intervals
for i in range(1,9):
    xl=x[i-1]
    fl=f[i-1]
    xr=x[i]
    fr=f[i]
    #  Plot linear fit in this interval
    npoints=21
    xx = np.arange(npoints)*(xr-xl)/float(npoints-1) + xl
    beta=(xx - xl)/(xr - xl)
    ff=(1.0 - beta)*fl + beta*fr
    plt.plot(xx,ff,'go')

plt.plot(x,f,'b-')

plt.show()
