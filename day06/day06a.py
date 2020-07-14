Morning Session

## Morning Routine

## Breakout rooms of 4 students and have each group answer
# If you could only eat one meal for the rest of your life, what would it be?

c
## Intro to Object Orientation

## Why classes?
# Let's imagine we were designing a social media website and we're in charge of designing the photos component.
# Let's chatstorm some features of the photos you would keep track of.
# Would you want to create variables for all of these features everytime a new photo was added?

# Object Based Programming let's us define a blueprint that is sort of like a dictionary where we can store information about our object and use it as a blueprint. We also get additional functionality that we can write functions that only work on that blueprint. 

#We'll start with the "nouns/adjectives" that live as attributes of the class and then we'll make our way to the "verbs" the methods that only work on our defined class.

## Initializing Instances
#let's get started by mkdir day06 and touch classes.py. When you have that file open on your screen, green checkmark in the participants window.

#Since we're going to build up an online store, the first class we want to create represents a product.

#First line of code is:
class Product:
#Chat storm: What do you notice about this first line?
#it's typical for a class in Python to start with a capital letter. No parenthesis. Still use a colon to end the line (like a function)

#next, we need to define a function inside of the class.
 def __init__(self, this_product_name, this_product_price):
    print(this_product_name + " created successfully!")

# Let's take a moment and look over this function.

# Let's do a bit of quick review about functions.
## Rapid fire these questions via hands up in participants window.

## How many arguments does the __init__() take in? What are they called? What are their data types?

## Chat waterfall: __init__ is a very special, specific method. Based on this code, what does it seem to do?

# So let's create some example of the Product class
# Initialize the first products
product1 = Product("Pillow Pal", 24.99)
product2 = Product("Colored Pencils", 5.99)

## Let's take a moment and run our code. What do you notice? What do you wonder?

## Instance Variables
#Let's add two more lines of code to our Product class definition.
self.name = this_product_name
self.price = this_product_price

#In Python, we use the keyword self within a class to refer to the specific instance of the class in which the code is running. This let's us differentiate different instances of the class in our code. We call variables reffered to with "self." as instance variables because the data will be specific to that particular instance.

## Mini-challenge - Let's modify the statement that prints the product was created successfully to use an instance variable.


## Chatstorm: What other inforrmation about a product might we want to keep trrack of forr each product we have in our store? ...hopefully a student pitches stock (or amount of the product)

## Instance Methods
#So now we'll add another instance variable to keep track of the amount of stock we have for each product.
# We'll set things up wherre the initial stock is set to zero when the product is instantiated.
self.stock = 0

# If we think of variables as nouns, things we keep track of, then we can think of functions as verrbs. Things we can do to the variables. If we focus on the stock instance varriable, what kind of actions (verbs) might you take? Let's chatstorm some ideas for stock. #add stock, sell stock, etc.

#Since this verb is specific only to the Product class, we will define the function inside of the class definition.

def add_stock(self, quantity):
    self.stock += quantity

#Let's try it out:
# Initialize the first products
product1 = Product("Pillow Pal", 24.99)
# Receive 100 pillow pals
product1.add_stock(100)
# Confirm that we have 100 in stock, as expected.
print(product1.stock)


#Now to sell product...
#What must we consider when selling a product? Let's chat waterfall some ideas.

#Yes, we should only sell product if we have enough of it to sell. We might wantt to prrint something specific if we're currrently sold out versus not having enough stock to meet the sell request.

# in breakout rooms, you're going to work through implementing a sell method. Your first line of defining the function will look like def sell(self, quantity):
# You'll test your method for all scenarios of your .sell() method.

## 5 minutes in breakout rooms ##

## Have a student show off their code!

def sell(self, quantity):
    if self.stock == 0:
      print("Sorry, we're currently sold out of " + self.name)
    elif self.stock >= quantity:
      self.stock -= quantity
    else:
      print(f"Sorry, we only have {self.stock} of that item available.")

### Lab Time -
# git clone https://github.com/upperlinecode/user-class-python-oop.git
# after some time....
# git clone https://github.com/upperlinecode/neighborhood-objects-python-oop.git

#students sharing code
## students come back from breakout rooms and shre code they are proud of