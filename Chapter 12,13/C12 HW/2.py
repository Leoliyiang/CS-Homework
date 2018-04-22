'''Open help for the math module.
How many functions are in the math module?
A: 49

What does math.ceil do? What about math.floor? (hint: both floor and ceil expect floating point arguments.)
A: math,ceil: Return the ceiling of x, the smallest integer greater than or equal to x. If x is not a float, delegates to x.__ceil__(), which should return an Integral value.
   math.floor: Return the floor of x, the largest integer less than or equal to x. If x is not a float, delegates to x.__floor__(), which should return an Integral value.

Describe how we have been computing the same value as math.sqrt without using the math module.
A:the number to the 1/2 square.

What are the two data constants in the math module?
A: au is a circle constant equal to 2π

Record detailed notes of your investigation in this exercise.
A: math.acos(x)
Return the arc cosine of x, in radians.

math.asin(x)
Return the arc sine of x, in radians.

math.atan(x)
Return the arc tangent of x, in radians
math.copysign(x, y)
Return a float with the magnitude (absolute value) of x but the sign of y. On platforms that support signed zeros, copysign(1.0, -0.0) returns -1.0.

math.fabs(x)
Return the absolute value of x.

math.factorial(x)
Return x factorial. Raises ValueError if x is not integral or is negative.
'''

