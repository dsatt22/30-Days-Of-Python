## Day 2 ##

# Built in functions
# Examples
#   print(), len(), type(), int(), str(), float(), list(), set(), dict(), min(), max(), sorted(), open(), file(), etc. 

# Variables
#   -Stores data in computer memory
#   -Mnemonic variables are recommended in most prog languages. Mnemonic variables just means it is a variable name that can be easily remembered
#   -A variable referes to a memory address in which data is stored
#   -The following are not allowed when created/naming a variable
#       -Numbers
#       -Hyphen (-)
#       -Special characters (ex. !, @, $, % ...)
#   -Variable names can be as short as a single letter (x, y, z), but a more descriptive name is highly recommended
#   -Variables must start with a letter or underscore (_)
#   -Can only contain letters, numbers and underscores
#   -Variables are case sensitive. Here are some examples of the same names, but are considered different variables:
#       -firstname
#       -Firstname
#       -FirstName
#       -firstName
#       -first_name
#       -First_name
#       -First_Name
#       -first_Name
#       -FIRSTNAME
#       -FIRST_NAME
#   -Snake case (snake_case) is the standard naming convention and is what I am going to use
#   -The equals sign (=) is an assignment operator. It does not mean equality
#   -Multiple variables can also be declared in 1 line

# Variable Examples
from itertools import count


first_name = 'Jon'
last_name = 'Doe'
full_name = first_name + ' ' + last_name 
age = 30
year = 2022
country = 'United States'
city = 'Jacksonville'
is_married = 'False'
skills = ['SQL', 'Python', 'HTML', 'CSS', 'C#', 'PHP']
person_info = {
    'firstname': 'Jon',
    'lastname': 'Doe',
    'country': 'United States',
    'city': 'Jacksonville'
}
temperature = 98.6
height, weight, eye_color, hair_color = "5'10", 200, 'blue', 'brown'

# Using the print() and len() functions on the variables I just created
print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name:', last_name)
print('Last name length:', len(last_name))
print('Full name:', full_name)
print('Full name length:', len(full_name))
print('Country:', country)
print('City:', city)
print('Age:', age)
print('Year:', year)
print('Married:', is_married)
print('Skills:', skills)
print('Person information:', person_info)
print('What is the temperature:', temperature)
print('What other attributes do you have:', height, weight, eye_color, hair_color)

# Getting user input
first_name = input('What is your name: ')
age = input('What is your age: ')

print(first_name)
print(age)

# Data types
print(type(first_name))
print(type(last_name))
print(type(country))
print(type(age))
print(type(year))
print(type(is_married))
print(type(skills))
print(type(person_info))
print(type(temperature))

# Mathematical problems
num1 = 5
num2 = 4
exp = num1 ** num2

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(exp)
print(num1 % num2)
print(num1 // num2)

radius = 30
pi = 3.14

area_of_circle = pi * radius ** 2
print(area_of_circle)

circ_of_circle = 2 * pi * radius
print(circ_of_circle)

radius = input('What is the radius: ')
circ_of_circle = 2 * pi * int(radius)
area_of_circle = pi * int(radius) ** 2
pi = 3.14
print(area_of_circle)
print(circ_of_circle)