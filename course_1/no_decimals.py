
print(f"Isabel is {28/7} dog years old.")
# Isabel is 4.0 dog years old.


# Now, you see that the last print statement did work, but it displayed the number
# with one decimal place. What if you wanted to display a whole number, which is
# much more natural when speaking about ages? You can use the chatbot to answer that
# question. Feel free to copy and paste the prompt provided below or use your own,
# using it as a guideline:
#
# Use the Chatbot: Modify this code to print the answer without any characters after
# the decimal place: print(f"Isabel's dog age is {28/7}.")

# Plan
# 1. Use an f-string to format the output.
# 2. Use the format specifier .0f to display the number without any characters after the decimal place.

print(f"Isabel's dog age is {28/7:.0f}.")