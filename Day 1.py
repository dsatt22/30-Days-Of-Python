### Day 1 ###

# use single quotes or double quotes for strings
# use triple quotes (''' ''') when a string is too long and needs to be on multiple lines
# use a hashtag to create a comment. comments are not part of our code

# Data Types:

# String:       A string is a collection of one or more charaters using single or double quotes 
# Numbers:      Integer (-1, 0, 1) is a whole number, whether negative, zero or positive
#               Float (-1.1, 0.0, 2.1) is a decimal point number whether negative, zero or positive
#               Complex (1 + d, 5 + 3d) is a number and a letter in a mathematical equation
# Booleans:     A boolean is either True or False
# List:         An ordered collection that allows you to store different data types. Lists also use brackets to hold information ([])Ex. ['Hello', 1, True, 10.1]
# Dictionary:   Stores information in a key value pair. Uses curly brackets ({}) 
# Tuple:        An ordered collection that allows you to store different data types. Different from lists though, using parentheses instead of brackets and are immutable
# Set:          Collection of data types similar to lists and tuples, but are not an ordered collection. Utilize curly brackets ({})    


## Exercises

# Checking data types
print(type(10))                 # Int
print(type(3.14))               # Float
print(type(1 + 3j))             # Complex
print(type('String'))           # String
print(type([1, 2, 3]))          # List
print(type({'name': 'Dustin'})) # Dictionary
print(type({9.8, 3.14, 2.7}))   # Set              
print(type((9.8, 3.14, 2.7)))   # Tuple

# Mathematical Operators
print(3 + 4)  # addition (+)
print(4 - 3)  # subtraction (-)
print(3 * 4)  # multiplication (*)
print(4 / 3)  # division (/)
print(4 ** 3) # exponential (**)
print(4 % 3)  # modulus (%)
print(4 // 3) # Floor division operator (//)

# Create a string and find the length of it

string_length = "What is the length of this string?"
print(len(string_length))
