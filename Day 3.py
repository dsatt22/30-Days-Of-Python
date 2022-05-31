## Day 3 ##


# Operators

# Boolean
#   - A boolean is a data type that is either True or False.
#   - This will be mainly used with comparison operators.
#   - The T in true and F in false must be capitalized.

# There are 4 types of operators
#   1) Assignment Operators
#   2) Arithmetic Operators
#   3) Comparison Operators
#   4) Logical Operators

# Assignment Operators
#   - These are used to assign values to variables
#   - In mathematics, the equals sign shows that two values are equal, but not in Python
#   - In Python it means storing a value in a certain variable, which is called assignment or assigning value to a variable
#   - Some examples:
#       1) =
#       2) +=
#       3) -=
#       4) **=
#       5) //=
#       6) >>=

# Arithmetic Operators
#   - Addition       (+):  a + b
#   - Subtraction    (-):  a - b
#   - Multiplication (*):  a * b
#   - Division       (/):  a / b
#   - Modulus        (%):  a % b
#   - Exponentation  (**): a ** b
#   - Floor division (//): a // b

# Examples
print('Addition: ', 1 + 2)       #3  
print('Subtraction: ', 2 - 1)    #1
print('Multiplication: ', 2 * 3) #6
print('Division: ', 4 / 2)       #2.0  -Division in Python gives a floating number
print('Modulus: ', 3 % 2)        #1    -Modulus will give you what the remainder is
print('Exponentation: ', 2 ** 3) #8
print('Floor: ', 7 // 2)         #3    -Floor division will give you an integer without the remainder or a floating number

# Assigning variables to a numberical data type and then doing arithmetic operations and assigning them to variables

# Declaring variables and assigning them a integer data type
a = 3
b = 2

# Arithmetic operations and assigning them to a variable
total = a + b
diff = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponent = a ** b

# Printing the results
print(total)
print('a + b = ', total)
print('a - b = ', diff)
print('a * b = ', product)
print('a / b = ', division)
print('a % b = ', remainder)
print('a // b = ', floor_division)
print('a ** b = ', exponent)


#Exercise 1

# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3
print(density, 'Kg/m^3')


# Comparison Operators
#   - Used to compare 2 values
#   - You can check if a value is greater or less or equal to other values
#   - When comparing, you will either get a True or False result
#   - Examples or comparison operators:
#       1) == (equal)                      x == y
#       2) != (not equal)                  x != y
#       3) >  (greater than)               x > y
#       4) <  (less than)                  x < y
#       5) >= (greater than or equal to)   x >= y
#       6) <= (less than or equal to)      x <= y

# More examples
print(3 > 2)  # True
print(3 >= 2) # True
print(3 < 2)  # False
print(2 <= 3) # True
print(3 == 2) # False
print(3 != 2) # True
print(len('mango') == len('avocado')) # False
print(len('mango') != len('avocado')) # True
print(len('mango') < len('avocado'))  # True
print(len('python') > len('HTML'))    # True

# In addition to the above comparison operators Python also uses the following:
#   1) 'is': which returns True if both of the variables are the same object (x is y)
#   2) 'is not': which returns True if both variable are not the same object (x is not y)
#   3) 'in': which return True if the queried list contains a certain item (x in y)
#   4) 'not in': which returns True if the queried list does not contain a certain item (x not in y)

print('1 is 1', 1 is 1)               # True
print('1 is not 2', 1 is not 2)       # True
print('D in Dustin', 'D' in 'Dustin') # True
print('Z in Dustin', 'Z' in 'Dustin') # False
print('coding' in 'coding for all')   # True
print('a in an:', 'a' in 'an')        # True
print('4 is 2 ** 2:', 4 is 2 ** 2)    # True


# Logical Operators
#   - Python uses keywords 'and', 'or' and 'not' for logical operators
#   - These are used to combine conditional statements
#   - Examples:
#       1) and (x < 5 and x < 10) : will return True if BOTH conditions are met
#       2) or  (x < 5 or x < 10)  : will return True if EITHER condition is met
#       3) not (not (x < 5 and x < 10)) : will return False if the result is True

print(3 > 2 and 4 > 3) # True
print(3 > 2 and 4 < 3) # False
print(3 > 2 or 3 > 5)  # True
print(3 < 2 and 4 < 3) # False
print(not 3 > 2)       # False because 3 is greater than 2, therefore not True gives False
print(not True)        # False
print(not False)       # True
print(not not True)    # True
print(not not False)   # False


# Day 3 Exercises
# Create 3 variables and store the following information in those variables (age as int, height as float, complex number)
age = 28
height = 5.10
complex_number = 3 + 4j

# Write a script to prompt a user to enter values and then calculate the the area of a triangle (area = 0.5 * b * h)
base = float(input('Enter the base of the triangle: '))
height = float(input('Enter the height of the triangle: '))
area_of_triangle = .5 * base * height

print('The area of the triangle is', area_of_triangle)

# Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c)
side_a = int(input('Enter length of side a: '))
side_b = int(input('Enter length of side b: '))
side_c = int(input('Enter length of side c: '))
perimeter_of_triangle = side_a + side_b + side_c

print('The perimeter of the triangle is', perimeter_of_triangle)

# Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
length = int(input('Enter the length: '))
width = int(input('Enter the width: '))
area_of_rectangle = length * width
perimeter_of_rectangle = 2 * (length + width)

print('The area of the rectangle is', area_of_rectangle)
print('The perimeter of the triangle is', perimeter_of_rectangle)

# Find the length of 'python' and 'dragon' and make a falsy comparison statement
print(len('Python'))
print(len('Dragon'))
print('Python' is 'Dragon')

# Use and operator to check if 'on' is found in both 'python' and 'dragon'
print('on' in ('Python' and 'Dragon'))

# I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence
print('jargon' in 'I hope this course is not full of jargon')

# There is no 'on' in both dragon and python
print(not 'on' in ('Python' and 'Dragon'))

# Find the length of the text python and convert the value to float and convert it to string
print(len('Python'))
print(float(len('Python')))
print(str(len('Python')))

# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
num = int(input('Enter a number: '))
if num % 2 == 0:
    print('This is an even number!')
else: 
    print('This is an odd number.')

# Check if the floor division of 7 by 3 is equal to the int converted value of 2.7
print(7 // 3 == int(2.7)) # True

# Check if type of '10' is equal to type of 10
print('10' == 10) # False

# Check if int('9.8') is equal to 10
print(int(9.8) == 10) # False

# Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person
hours_worked = float(input('Enter number of hours worked: '))
rate_per_hour = float(input('Enter your hourly rate: '))
earnings = hours_worked * rate_per_hour

print('Your weekly earnings is', earnings)

# Write a script that prompts the user to enter number of years. Calculate the number of seconds a person can live. Assume a person can live hundred years
number_of_years = int(input('Enter the number of years you have lived: '))
number_of_seconds = number_of_years * 31536000 # number of seconds in a year (365(days) * 24(hours) * 60(minutes) * 60(seconds))

print('You have lived for ' + str(number_of_seconds) + ' seconds!')

# Write a Python script that displays the following table
# 1 1 1 1 1
# 2 1 2 4 8
# 3 1 3 9 27
# 4 1 4 16 64
# 5 1 5 25 125

print("X" + "\t" + "X^0" + "\t" + "X^1" + "\t" "X^2" + "\t" + "X^3")

print('-----------------------------------------')

for x in range(1,6):
    print(str(x) + "\t" + str(x**0) + "\t" + str(x**1) + "\t" + str(x**2) + "\t" + str(x**3))

