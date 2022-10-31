# The code uses the bisection method to braket a root of a cubic polynomial,
# defined by poly.

def poly(x):
    # evaluate the polynomial ax^3 + bx^2 +cx + d at x
    a = 3
    b = 1
    c = -5
    d = -1
    return d + x*(c + x*(b + x*a))

#  set initial values:
xl = -1
fl = poly(xl)
xr = 1
fr = poly(xr)

# iterate:
for i in range(10):
    print("at iteration %i, root lies between %f and %f" % (i, xl, xr))
    xnew = 0.5*(xl + xr)
    fnew = poly(xnew)
    print("current best guess is: x= %f, which gives f(x)= %f" %(xnew, fnew))
    if fl*fnew > 0:
        xl = xnew
        fl = fnew
    else:
        xr = xnew
        fr = fnew

print("final answer is: x= %f, which gives f(x)= %f" %(xnew, fnew))
