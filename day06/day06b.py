Mid-Morning Session


### Class Variables


# Class Variables let us store information that will be shared across all instances of the class.

# For example, let's imagine we needed to keep track every new item we added and be able to print it out.

# To add a *class variable* we need to add the variable before the __init__ method.

# And to get it to incrememnt when we instantiate a new Product, we add that code in the __init__ method

# Define the class
class Product:
  # Before we ever initialize our first object, we should set a total
  total_products_created = 0

  # Define the __init__ method
  def __init__(self, this_product_name, this_product_price):
    # Set up the product
    self.name = this_product_name
    self.price = this_product_price
    print(self.name + " created successfully!")
    # Increase our total items
    Product.total_products_created += 1
    print("We currently offer " + str(Product.total_products_created) + " products on our site.")

Let's test it out

# Initialize the first product
product1 = Product("Pillow Pal", 24.99)

### Let's go into our breakout rooms and work on this Banking Lab
git clone https://github.com/upperlinecode/oo-banking-python.git


## At the end of mid-morning, let's have students to a Slack poll to get a sense of object orientation
#1) I feel strong with object orientation and I want to try building out an object orientation game (would do the CL video game)
#2) I feel good with object orientation and would like to practice more (would do amazon shopping cart)
#3) I feel okay with object orientation and would like some more direct instruction with a teache (would do Advanced OO script with teacher in breakout room)
