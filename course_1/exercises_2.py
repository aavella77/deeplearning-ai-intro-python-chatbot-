# EXERCISE 1

# Modify the code to print your age
# print(f"I am {} years old.")

# Plan
# 1. Define a variable to store your age.
# 2. Use an f-string to format the output, inserting the age variable.

# Define your age
age = 52

# Print the age using an f-string
print(f"I am {age} years old.")

###################################################################################
# EXERCISE 2

# Fix this code
# print(f"There are {365/7 weeks in a year")

# Plan
# 1. Correct the syntax of the f-string by closing the curly braces around the expression.
# 2. Ensure the string is properly enclosed in double quotes.

print(f"There are {365/7} weeks in a year")

#####################################################################################
# EXERCISE 3

# Complete the code
# print(f"The area of a square with side 5 cm is {} cm squared.")

# Plan
# 1. Calculate the area of the square by squaring the side length.
# 2. Use an f-string to format the output, inserting the calculated area.

# Define the side length of the square
side_length = 5

# Calculate the area of the square
area = side_length ** 2

# Print the area using an f-string
print(f"The area of a square with side {side_length} cm is {area} cm squared.")

#####################################################################################
# EXERCISE 4

# Plan
# 1. Use an f-string to format the output.
# 2. Use the format specifier .1f to display the number with one decimal place.

# Modify the code to display one decimal place
print(f"The house was a good size: 1200 square feet, or {1200 * 0.092903} meters squared!")

print(f"The house was a good size: 1200 square feet, or {1200 * 0.092903:.1f} meters squared!")