#####################################################################################
# EXERCISE 1

# Create a variable called 'my_name' and assign it the value of your name as a string.
# Then print out a greeting using the variable, like "Hello, Andrew!"
# my_name =
# print()
### Plan
# 1. Create a variable called `my_name` and assign it the value of your name as a string.
# 2. Use the `print` function to output a greeting using the `my_name` variable.

### Code
# Create a variable called 'my_name' and assign it the value of your name as a string.
my_name = "Alejandro"

# Print out a greeting using the variable
print(f"Hello, {my_name}!")

#####################################################################################
# EXERCISE 2
# Enter your favorite number below and store it in a variable called 'fav_num'.
# Print out a message telling you what your favorite number plus 10 is.
# fav_num =
# print(f"Your favorite number plus 10 is {}")

### Plan
# 1. Define a variable called `fav_num` and assign it your favorite number.
# 2. Calculate your favorite number plus 10.
# 3. Use an f-string to format the output, inserting the calculated value.

### Code
# Enter your favorite number below and store it in a variable called 'fav_num'.
fav_num = 7

# Print out a message telling you what your favorite number plus 10 is.
print(f"Your favorite number plus 10 is {fav_num + 10}")


#####################################################################################
# EXERCISE 3
# Create two variables, 'countries_visited' and 'countries_to_visit' and assign them the number of
# countries you've been to and the number of countries you hope to visit. Then complete the print statement.

# print(f"""I have visited {} countries. I plan to visit {} more countries,
#      and when I'm done I will have visited {} countries.""")

### Plan
# 1. Create a variable called `countries_visited` and assign it the number of countries you've been to.
# 2. Create a variable called `countries_to_visit` and assign it the number of countries you hope to visit.
# 3. Use an f-string to format the output, inserting the values of `countries_visited` and `countries_to_visit`.

### Code

# Create two variables, 'countries_visited' and 'countries_to_visit' and assign them the number of
# countries you've been to and the number of countries you hope to visit.
countries_visited = 10
countries_to_visit = 5

# Complete the print statement
print(f"""I have visited {countries_visited} countries. I plan to visit {countries_to_visit} more countries, 
     and when I'm done I will have visited {countries_visited + countries_to_visit} countries.""")
