# Variable names restrictions
# To demonstrate an important fact about variable names in Python, try to run the code below.
#
# my score = 450
# Now, ask the chatbot why that code didn't work. You can use the prompt suggested here.
#
# 🤖 Use the Chatbot: Why doesn't this code work? my score = 450

### Plan
# 1. Identify the issue with the variable name.
# 2. Explain the rules for valid variable names in Python.

### Explanation
# The code `my score = 450` doesn't work because variable names in Python cannot contain spaces. Variable names must follow these rules:
# - They can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# - They cannot start with a digit.
# - They cannot contain spaces or special characters.

# To fix the code, you can use an underscore instead of a space:

my_score = 450
print(my_score)
