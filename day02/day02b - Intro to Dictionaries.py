### Dictionaries ###
#Let's say we need to store some information about a friend in our phone's contact appear
#Maybe I would do this
anoopa_contact = ['Anoopa','Singh','555-555-5555','Upperline',42]

## How would I access Anoopa's phone number?
## Chatstorm: Send as many answers as you can right away: What does the 42 stand for?
## Let's take hands, what might become confusing about this data structure, especially if we added more information

## wouldn't it be better if there were some labels....

anoopa_contact = {
    'first_name':'Anoopa',
    'last_name':'Singh',
    'cell_phone':'555-555-5555',
    'company':'Upperline',
    'lucky_number':42
}

print(anoopa_contact)
print(anoopa_contact['lucky_number'])

# Chat Waterfall - Type but don't send yet: either what is a similarity or a difference with the synatax of lists

# Dictionaries use {} to start and end
# Dictionary entries consist of a key, value pair separated by a colon
# Dictionaries and lists are read with []

### Dictionary CRUD ####
#Updating a key, value pair in a dictionary is similar to updating an item in a list
anoopa_contact['lucky_number'] = 13
## And adding a brand new key, value pair is identical
anoopa_contact['fav_color'] = 'blue'

##Looping through a dictionary
# There are many different strategies to loop over a dictionary and each has its advantages. You can loop over the keys, the values, or the key, value pair.

## This is just one way to do it and I encourage you to look up other ways depending on what challenged you come up againnst in the lab
superheroes = {
  "jeff": "Static Shock",
  "taylor": "Jessica Jones",
  "danny": "Ms. Marvel",
  "gabe": "Supergirl",
  "sara": "The Hulk",
  "shana": "Miles Morales"
}

for person in superheroes:
  print(person + "'s favorite superhero is " + superheroes[person] + ".")

# Lab time:
git clone https://github.com/upperlinecode/dictionary-iteration-mini-lab-python.git
git clone https://github.com/upperlinecode/name-badges-list-dictionary-python.git
