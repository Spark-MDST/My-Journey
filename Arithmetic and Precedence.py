## ~~ Basic Math Commands ~~ ##   

##################### 

# ~~ Addition ~~ #

print('''
10 + 3 is equal to:''') 

print(10 + 3)

#####################

# ~~ Subtraction ~~ #

print('''
10 - 3 is equal to:''')

print(10 - 3)


#####################


# ~~ Multiplication ~~ #

print('''
10 * 3 is equal to:''')

print( 10 * 3)

#####################

# ~~ Division ~~ #

print('''
10 / 3 is equal to:''')

print(10 / 3)   # This way of division will print a float

print('''
10 // 3 is equal to:''')

print(10 // 3)  # This way of division will print an integer

#####################

# ~~ Modulus ~~ # 

print('''
10 % 3 is equal to:''')

print(10 % 3)   # This will print the remainder of the division (10 can only be divided by 3, 3 times. Thus making 1 the reminaing value)

#####################

# ~~ Exponents ~~ #

print('''
10 ** 3 is equal to:''')

print(10 ** 3)  # The |**| is putting the number 10 to the power of 3. AKA: (10^3)

#####################

# ~~ Augemented Assigned Operator ~~ #

###
# Start Simple. 
# Below, we have a variable |x| that is equal to |10|.
# We also have an equation to figure out the value of |y|, given that |x| equals |10|. What is 10 + 3?

x = 10          #   This is stating x = 10
y = x + 3       #   This will fill 10 in for x inside the equation to get the answer of y on the outside

print('''
y is equal to:''')

print(y)        #   This will print the answer to the equation above.

###
# The equation can be simplified as:

a = 10 
a += 3          #   This is the same equation as the one in line 52, just more simplified.

print('''
a is equal to:''')

print(a)        #   This is printing the above equation

# It could also be subtracted like this: 

b = 10
b -= 3          #   This is a similar equation, instead of adding it is subtracting.

print('''
b is equal to:''')

print(b)        #   This is printing the above equation

# I use different variables in these examples so that you can see the differences in the 3 print functions: (y, a, and b)

#####################

#       ~~ Lets Always Remember PEMDAS ~~       #

#   For those of you knew to this or may have forgotten
#   PEMDAS is the order or precednce in which math gets calculated.

#  1| P   =   Parentheses
#  2| E   =   Exponents
#  3| M   =   Multiplication
#  4| D   =   Division
#  5| A   =   Addition
#  6| S   =   Subtraction

q = 10 + 3 * 2          # In this example the order goes: 2 * 3 |-->| 6 + 10
print('''
q is equal to:''')

print(q)

#---

w = 10 + 3 * 2 ** 2     # In this example the order goes: 2 ** 2 |-->| 4 * 3 |-->| 12 + 10
print('''
w is equal to:''')

print(w)

#--- 

e = (10 + 3) * 2 ** 2   # In this example the order goes: 10 + 3 |-->| 2 ** 2 |-->| 13 * 4
print('''
e is equal to:''')

print(e)

#---

r = (2 + 3) * 10 - 3     # In this example the order goes: 2 + 3 |-->| 5 * 10 |-->| 50 - 3
print('''
r is equal to:''')

print(r)

#---

t = (5 - 3) ** 2 * 5    # In this example the order goes: 5 - 3 |-->| 2 ** 2 |-->| 4 * 5
print('''
t is equal to:''')

print(t)

#---

y = (21 / 3) ** 2 / 7   # In this example the order goes: 21 / 3 |-->| 7 ** 2 |-->| 49 / 7
print('''
y is equal to:''')

print(y)

#####################

#       ~~ Mathmatic Functions ~~       #

import math ## This imports a number of mathmatics functions, you can put this at the very top of your file.

# Here are two examples of some Math Functions, round & abs

#---

x = 2.9             # Here is our Variable

print(round(x))     # The (round()) function will round the number in the given variable or string

print(abs(-2.9))    # The (abs()) function, will make any negative number a positive

##If you'd like to see the entirety of all of the math functions in python you can search them up online.