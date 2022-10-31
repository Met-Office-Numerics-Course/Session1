# The aim of this exercise is to fill in the code to calculate sqrt(2)
# using what you have learnt so far.

# Rewrite x = sqrt(2) as x = g(x) for a good choice of g(x) and use this
# to implement a fixed point iteration by completing the definition of
# g and filling in an initial guess for x.

# Extensions:
# 1. Can you compute the error at each iteration and amend the
#    while loop to stop once a certain tolerance has been reached?
# 2. a) Now try a different function: x - cos(x) = 0. Again start with x=1
#    and now print out x at each iteration. What is x converging to?
#    b) The same value of x should satisfy a - arccos(x) = 0. Try this,
#    starting with x=0.7. What happens, and can you explain why?
# 3. Try applying this method to solve the following:
#    i) exp(-x) - x = 0
#    ii) x^x = 5

def g(x):
    # this function returns the right hand side of your iterative method
    return 

# initialise a variable to count the number of iterations and set a
# maximum number of iterations:
count = 0
max_count = 20

# choose an initial guess:
x =

# now iterate!
while count < max_count:
    x = g(x)
    count += 1

print("After %i iterations, x=%f." %(count, x))
