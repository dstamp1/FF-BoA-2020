Afternoon Session- Advanced Functions

# Let's review writing a function. We'll do that in breakout rooms.

# We want to calculate the cost for a family to go to the Disneyland for a certain number of days.
# Let's say: Cost for adults: $100/ticket per day Cost for children: $90/ticket per day

# When cooming up with a function for something with multiple inputs, it's a great strategy to think about some examples.

# How much will it cost for 1 adult and 1 child to go for one day?
# How much will it cost for 2 adults to go for three days?
# How much will it cost for 1 adult and 2 children to go for one day?

# Chat Waterfall - Type but don't send yet: What specific variables do we need to get our final calculation?

# Let's name our function cost_of_disney(number_of_adults,number_of_kids, number_of_days):

## In breakout rooms, complete writing the function such that it returns the final cost
## We'll be sharing this code in a slack channel when we come back together.

### Skip over the scoping section entirely ###
# If a bug arises from it downn the road, we'll deal with it then

### Defaults Arguments ###
# It is common to have a parameter of a function that is typically a default value that the use doesn't need to futz with>
# Python lets us include default values in our custom functiosn too

def greetPlayer(name = "User"):
  print("Welcome to the game, " + name + ".")
  print("Your current level is 1.")

greetPlayer("David") # Code if the user provides their name
greetPlayer()  # Code if the user chooses not to provide their name

## Or perhaps this other example:
def createUser(name, email, password = "abcd1234"):
  # Some code to create the user

createUser("John Smith", "Jsmith123@gmail.com")
createUser("Marta Guzman", "MartaG789@gmail.com", "Puppies1")
createUser("Artie Krausmann")

# Questions for students:
#
# How many arguments does this function take?
# How many of those arguments are required? How many are optional?
# What will John Smith's password be?
# Which line will throw an error? Why?

mario-- git clone https://github.com/upperlinecode/mario-python-functions.git
leap year -- git clone https://github.com/upperlinecode/leap-year-python-functions.git
