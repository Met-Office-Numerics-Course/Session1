import matplotlib.pyplot as plt
import numpy as np

# Recall from the notes that the Taylor series is defined by:
# f(x) = f(a) + f'(a)/1! (x-a) + f''(a)/2!(x-a)^2 + f'''(a)/3!(x-a)^3 + ...

# First set up an interval [a, b] divided into N-1 subintervals:
N = 42
a = -3.
b = 3.
x = np.linspace(a, b, N)

# For the function f(x) = exp(x), we have that f' = exp(x) and f'' = exp(x)
f = np.exp(x)
fp = np.exp(x)
fpp = np.exp(x)

# Look at point x=0 and calculate the first three approximations to plot:
approx0 = np.ones(N)*f[21]
approx1 = approx0 + np.ones(N)*fp[21]*(x-x[21])
approx2 = approx1 + np.ones(N)*fpp[21]*(x-x[21])**2

# 
plt.plot(x, f, 'k')
plt.plot(x[21-5:21+5], approx0[21-5:21+5], 'r--')
plt.plot(x[21-5:21+5], approx1[21-5:21+5], 'b--')
plt.plot(x[21-5:21+5], approx2[21-5:21+5], 'g--')
plt.plot(x[21], f[21], 'ko')
plt.xlim((-1,1))
plt.ylim((0,5))
plt.title("first three approximations from the Taylor series for exp(x)")
plt.show()
