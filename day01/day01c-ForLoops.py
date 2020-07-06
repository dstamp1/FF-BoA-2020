### For Loops ###
# Computers are really good at repeating the same task over and over again without making any mistakes/typos
# Let's imagine we were having a competition to see who could type out "print('hello')" as many times as we could without using copy and paste.
# We might type out 
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
print('hello')
# and quickly get bored or maybe a typo!

## What kind of tasks do you often have to repeat or maybe a company might need to repeat? Let's chatstorm. annticipated responses: marketing emails, order emails, happy birthday emails, etc.

## the most basic way to complete a task multiple times is too use a for loop like so:
for i in range(10):
  print("Hello")

## Let's do a chat waterfall, so type but don't send yet, how many times "Hello" will print on the screen?

## let's examine what that i is doing by modifying our code
for i in range(10):
  print(f"i is currently {i}")
  print("Hello")

## The letter i is used as this placeholder (this placeholder frustratingly doesn't have a name, but is most commonly called the "iterator", "loop counter", "iteration variable" or "constant of iteration"), but the term i isn't special or reserved, it's just the most common. You might have seen it before in a math class during summations

## since it's a variable, we can call it anything we want so we can referennce it later.

### There are soooo many things you can do with loops. Let's talk about finding sums and you can think about other uses of the superpower.

## Lets say we want to find the sum of the numbers 5,6,7 and 8

## We could use this code:

sum = 0
for i in range(5,9):
  sum += i
  print(f"The sum is currently {sum}.")

print(f"The loop is over, and the total is {sum}!")

# What is the value of sum before the loop starts?
# What is the value of sum after the loop has gone one round?
# What is the value of sum after the loop has gone two rounds?

#### Let's skip over 'looping with a condition' in the teacherhub for time purposes ###### 
## I will mention it's something we can do

## Looping over strings ###
## So we've looked at looping over a range(), but we can loop over any 'iterable' like a string.
your_word = input("Give me a word and I'll spell it.")

print(f"Okay! I'll try to spell {your_word}.")
for letter in your_word:
  print(letter)

## Lab Time: we'll be working on the loopy math lab
# git clone https://github.com/upperlinecode/loopy-math-python-iteration.git
## You might want to explore the documentation for the range() function https://www.w3schools.com/python/ref_func_range.asp
## and if you might want to know more about the modulo function to find even numbers https://www.pythoncentral.io/using-python-to-check-for-odd-or-even-numbers/