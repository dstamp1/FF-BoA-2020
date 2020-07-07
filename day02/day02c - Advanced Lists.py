## Complex Data Structures ##
# So we've looked at lists and we've looked at dictionaries, and so it seems like we should eb able to do both.

# For example, a list of dictionaries
actors  = [
  {"name": "Molly Ringwald", "role": "Claire Standish", "grade": 10},
  {"name": "Judd Nelson", "role": "John Bender", "grade": 12},
  {"name": "Ally Sheedy", "role": "Allison Reynolds", "grade": 11},
  {"name": "Anthony Michael Hall", "role": "Brian Johnson", "grade": 10}
]

#Chat Waterfall - Type but don't send yet:what should I type to access the actor Ally Sheedy?
actors[2]
# And if I wanted to access Ally Sheedy's role?
actors[2]['role']

#Python will work from left to right in each level of accessing the information.

# And of course we can still use our for loops to iterate over a complex data structure
for actor in actors:
  print("The role of " + actor["role"] + " was played by " + actor["name"])


# And time for anoother lab
git clone https://github.com/upperlinecode/survey-says-nested-data-structures-python.git
