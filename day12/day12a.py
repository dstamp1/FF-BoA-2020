Morning Session


### Morning Routine ###

## Stretch and Share ##
# Question....if you could be a contestant on any tv show to win a million dollars, which show do you think you'd do the best?

### Buzzfeed Quizzes ###

https://www.buzzfeed.com/quizparty

######## Why do we even need a database #######

# Let's say we wanted to build a site where we could post community events and important dates. I want to site to be able to show events + add events.
# I coded together this app last night: https://community-board-dstamp.herokuapp.com/

## Take 2 minutes to explore my site (it only has two pages) and add an event


### At this point, you probabl noticed that the events we added individually aren't showing up on everyone elses page even though we all visited the same website.

## If we look at the code, we see that the original evennts list is hard coded.

### To have a site where multiple users can access and add data for other users to interact with, we need a centralized way to store data. Databases give us the way to do that. We will learn how to user MongoDB.

## This app is just an example of what's possible by incorporating MongoDB. Before we explore how to do that, first let's learn how to interact with an existing MongoDB database.


#### Set up for the stocks lab.

## MongoDB is a database that consists of documents. Each document is like a dictionary that can have nested lists and dictionaries inside of it. Not too different from the APIs we looked at yesterday.

## Just like we talked about CRUD for lists and dictionarries, we can think about CRUD for our database as well.

## For this first lab, we'll focus on reading information from a database.

# Let's clone down the Stocks lab and start to look over

## Stocks Lab
git clone https://github.com/upperlinecode/stock-query-mongodb.git


## MongoDB isn't written in Python and it has documentation on how to send it queries. Pymongo is a python module that will do the work to turn Python code into code Mongo will understand.

## To make the connection to a database, we need to use the MongoClient class. The information on line 4 and 5 make that connection. In order to access the url with +srv in it, python needs an additional package called dnspython
sudo pip3 install flask-pymongo
sudo pip3 install dnspython

# In MongoDB, a group of documents is known as a collection. Line 6 defines a collection as the prices database. A single Mongo instance can have multiple databases in it.

# And to access all of the documents in a collection, we use the .find method and pass an empty dictionary as the argument. The find method will filter down the collection and include all documents that match the query parameter.

# When you search a Mongo collection to get back a Mongo Cursor which is sort of like the response object we got back using requests.get(API_URL). To get out just the list of documents, we use the list() function.

## Before turning yoou over to working through the lab, let's think about what verbs we might want to do to a collection.

# Chat waterfall: Type but don't send yet. What kind of verbs might you do to a collection of documents?
# find, sort, filter, limit

# So lets say we want to sort by a particular field.
## IF we loook at the MongoDB documentation:
https://docs.mongodb.com/manual/reference/method/cursor.sort/index.html
## We see that we would do
collection.find({}).sort({ field: value })
# where value = 1 for ascending and -1 for descending.

#But if we type this in, it won't work! Python requires the key to be a string and it is a list of lists
collection.find({}).sort([['field1',1],['field2',-1]])

# You and your partner will work through the stocks lab



## Sign up for MongoDB + create your first database connection
# To get started using MongoDB as a database, you'll want to sign up for an Atlas (free) account at mongodb.com. The sign up process is a bit lengthy, but it involves:
#
# Signing up with a (valid) email address
# If you're demoing this sign-up for students and you have a gmail account you've already used to sign up, consider using yourname+mongo@gmail.com (or some variant) to sign up as a new user.
#
# Submitting your name and creating a password
# When asked to create your first cluster, you can either follow the prompts, or close the dialog box.
# If you close the dialog, you'll be presented with options for the "Cloud Provider" and "Region".
# We suggest using AWS as the "Cloud Provider" and the region geographically closest to you.
#
# Choose the "M0" cluster tier to keep things free.
# No "Backup" is needed.
# And you can give the cluster a name or use the default "Cluster0"
# Finally, tap the green "Create Cluster" button

## While we wait ~10 minute, let's play a quick game
##### Insert Game ######

# Once the cluster is created on MongoDB, we need to do three things to complete the database setup before we can connect to it from our app:
#
# Create a database
# Create a database user
# Whitelist IP addresses

# To create a database in the MongoDB interface, click on the name of the cluster, e.g. Cluster0 and then on the "Collections" heading (or just on the "Collections" button below the cluster name)
#
# You'll notice a MongoDB "checklist" pop up as you get set up. It's worth calling out the user experience of building a new cluster/database/collection on MongoDB. Do students think it's good? bad? intuitive? confusing?
#
# In the "Collections" tab, you'll be prompted with a big green button to "Create Database" - tap that button.
#
# You'll then be prompted to give the database a name (it can be anything, e.g. test) and to create the first collection by giving it a name (it can also be anything, e.g. events). Later, we'll see that when adding data to a database, if you are sending data to a collection that doesn't (yet) exist, MongoDB will create that collection for you. So there's no need to stress about getting this perfect from the beginning.
#
# You don't need to check "Capped Collection".
#
# We now have our first database! But before we can connect to it, we need to set up our first database user
#
# To create a database user, return to the Clusters overview by clicking on "Clusters" in the left sidebar. Once there, select the "Security" tab.
#
# Notice the green button in the top-right corner that says "+ ADD NEW USER" - go ahead and tap that.
#
# Choose a username, e.g. admin and (secure) password, e.g. Ypzb8UvmWKXJsubU, and make a note of the password you've selected.
#
# We suggest tapping "Autogenerate Secure Password" to create a compliant password. Then tap "Show" and copy-and-paste the password somewhere safe.
#
# When creating a user, you can set various privileges for that user. For this app, we're just going to keep the default "Read and write to any database" permissions.
#
# Tap "Add User" to complete the creation of your first database user!
#
# Now we need to let MongoDB know the IP addresses from which it is safe to access our database and to which it is safe to send data from the database.
#
# Still on the "Security" tab, you'll now see the user you just created. Tap the "IP Whitelist" sub-tab to view a list of the safe IP addresses
#
# Again, tap the green button in the top-right labeled "+ ADD IP ADDRESS".
#
# We're presented with an option to just add the current IP address, to allow access from anywhere, or to list a particular IP address. Since most students will want their app to be accessed by anyone anywhere (and since they should not be storing particularly sensitive data), it's ok to tap the "Allow Access from Anywhere" button. Add a comment, e.g. "Global access", then tap "Confirm"


#### I say we take a break here no matter what? Or maybe give some more time with the stocks lab? I'm not sure of the timing, tbh
