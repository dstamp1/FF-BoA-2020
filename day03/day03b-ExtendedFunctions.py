Mid-Morning Session- Functions Cont'd
debugging practice

# Functions Without Arguments
# Sometimes you need a function performed that doesn't require any arguments. For example, if you wanted to remember what Pi is to 14 digits, you wouldn't need ANY information from the user. You could wrap that in a method like this.

def pi_reminder():
  return 3.14159265358979

# Where have we seen a function that doesn't take any arguments? Chatstorm - Type as many example you can think of in the chat window

# For this particular example of a custom function, how else might we have stored this information?

### Functions without Returns ###
# It is possible to write functions without return statements, but its not a good practice.
# Let's imagine we have this function
def add(x, y):
  total = x + y

# Call
print(add(5, 22))

# Let's make a prediction on what will print. Chat Waterfall: Type but don't send yet, what will print in the terminal

# So we end up returning None and *usually* thats not a helpful or useful. So we want to include return statements. Print statements are helpful for debugging.


## Returns also offer us an opportunity for control flow. Let's try out this function and see what happens
# Definition
def add(x, y):
  return "Adding your numbers"
  return x + y
  return "Your numbers add up to " + str(x + y) + "."
  return "Program finished!"

# Call
print(add(5, 22))

## What will this function return?

# When a function gets to a return statement, the function runs that line of code and then immediately returns that value. It can be a useful strategy in writing your custom functions.

## Lab time

investment-- git clone https://github.com/upperlinecode/investment-functions.git

Dog rater -- git clone https://github.com/upperlinecode/they-rate-dogs-python-functions.git
