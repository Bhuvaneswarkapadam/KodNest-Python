# To print Hello World
print ("Hello World")

# To find whether number (n) is even or odd

"""START
INPUT n
IF n % 2 == 0 
   PRINT "Even"
ELSE
  PRINT "Odd"
ENDIF
END"""
n =  10
if n%2 == 0:
    print ("Even")
else:
    print ("Odd")
# To find whether number (n) is positive, negative or zero
n = 1
if n > 0:
    print ("Positive")

elif n < 0:
    print ("Negative")

else:

    print ("Zero")

# To find the largest among 3 numbers a, b, c

"""START

INPUT a
INPUT b
INPUT c

IF a >= b AND a >= c THEN

    PRINT "a is largest"

ELSE IF b >= a AND b >= c THEN

    PRINT "b is largest"

ELSE

    PRINT "c is largest"

ENDIF

END"""

a = 10
b = 2
c = 8

if a >= b and a >= c:
    print("a is largest")
elif b >= a and b >= c:
    print("b is largest")
else:
    print("c is largest")