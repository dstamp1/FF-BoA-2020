Morning Session

## Morning Routine
# Stretch and share....which app on your phone do you use the most?

## Let's try 1 word proverbs ---
# I'll rename students to include a number in their name. Students each say one word added to the proverb going in order. When the proverb feels right, a student can say "ommmm" and we'll start over
 

### Set Up ###
# Let's imagine you're creating a social media website where users can sign up, post pictures, and like/comment these photos. Let's call it SlowstaBook.

# Originally you thought users could email you the photo and you would write the HTML files for the website. Sure, that was a lot of work, but you're getting better at HTML by the day. So no big deal!

# Then, of course, how do you get the right pages to the right users. You need something to connect the user to the photo they're looking for. AGain, I guess you'll get really good at responding to emails. No big deal!

# So now your website had hundreds of photos and you realize you need to change the background color for all of these pages. Uh oh...how are you going to edit 100s of files all at the same time. And, at this point, you realize that scaling your website by maximiming your coding has reached a breaking point.

# But it seems like...can't we get a computer to do all of this for us? To write the HTML files, to send them where they need to go, and to take advantage of templates so you can make a change in one place? 

# There are many solutions to this problem, we will be using Flask with gets Python to on-the-fly create HTML pages and a web server to do all the communicating. Flask is a quick way to get a site started and is used by some big companies like Pinterest and AirBnB.

# Today we will do a codealong to create a basic flask app and then we will have some time to extend another flask app. We'll finish up by deploying our apps to Heroku (I think time spent doing this right now will pay major dividends later in the course)



#### Cloudshell Setup #####
#Before we can work with FLask, we have to do a bit of setup for our cloudshell. Some of this setup is because cloudshell resets after a period of inactivity.
sudo pip3 install flask
# and then we'll create a startup script
touch ~/.customize_environment
echo 'sudo pip3 install flask' >> ~/.customize_environment
echo 'sudo pip3 install python-dotenv' >> ~/.customize_environment

# Finally, restart your environment using the "..." menu in the top right corner of the Cloud Shell window. When it asks you why you're doing this, select "want a clean VM state" as your reason. Your Cloud Shell will probably take about 2 minutes to restart.

# Now we're ready to copy down the Flask Template we'll be using
https://github.com/upperlinecode/flaskproject
# And we'll use the template button to create your own copy. Once you've done that, we can copy our individual .git lines so we can clone to cloudshell. We'll do that inside of a folder called day08 in our FintechFocus2020 directory

# Before examining the code here, let's make sure it will run. There's enough code in the file where we should be able to see it go. 
flask run
# To "see" our app run, click the link in the console.

# Where in the code is this coming from? Let's dive in

# Our Flask app is handling receiving requests from the user and sending back a response.

# The first type of request we'll look at is a GET request. GET requests do exactly what you sound like. Your web browers makes a request of the server via the URL. The web server takes that URL and turns it into something to send back as a response.

# Let's write another get request.

## First, we need to define a function. This function is what the Flask app will run to turn the request into a response. What we put as the return of the function is what will get sent back to the web browser.

def secret():
  return "<h1>You found the secret!</h1>"

#But at this point, the Flask app doesn't know which URL should trigger this function to run. The flask app needs to build a lookup table that says URL_A goes to Function_A. 

# To do that, we add a line of code *before* the function definition. It's called a decorator
@app.route('/secret')

#What do we need to type in the URL bar to get to this route?

## Let's take ~5 minutes in breakout rooms to add at least 1 additional route


######### Templates ###########

# While we could write out an entire HTML page as a string to return from the function, it feels like there's gotta be a better way.

# Flask comes with a fuction that lets us use a template to do it

from flask import render_template

# and now we'll modify the index route to render the template called "index.html"

def index():
    return render_template('index.html')

# We can do even more by passing data to the render_template that we can access in the template.

# To do that, we'll package up some information into a dictionary. Let's make a user and a title to pass to the index.html template

data = {
  'user':{'first_name':'Anoopa'},
  'title':'Home'
}

# To get this data to the template,
def index():
  data = {
    'user':{'first_name':'Anoopa'},
    'title':'Home'
  }
  return render_template('index.html', data=data)

#And to access it in the index.html, we need to do tthe following
<html>
    <head>
      <title>{{ data.title }} - Microblog</title>
    </head>
    <body>
        <h1>Hello, {{ data.user.first_name }}!</h1>
    </body>
</html>

# The double curly braces is a fill inn tthte blank for render_template, sort of like a f-string we already know.

##### Playtime: Adding a resultsPage.html with route that renders at least one piece of new information.


####### Building out a form #######
# Right now our web app can use data we've hard coded and can use it to dynamically generate HTML files. But in most web apps we get info from the user. One way to do that is with a form.

# Let's put this form on the index.html page

<form method="POST" action="/sendBreakfast">
  <label for="nickname">What's your nickname?</label>
  <input type='text' name='nickname'>
  <label for="breakfast">What did you have for breakfast?</label>
  <input type='text' name='breakfast'>
  <input type='submit'>
</form>

# and let's try it out. What does this error mean?

# So we need to write a function to handle this.
@app.route('/sendBreakfast')
def handle_breakfast():
  return "Breakfast will appear here"

# Let's try this form again....uh oh, a new error. Method not allowed. But if we reload the page, it appears!

# Turns out this is because theer's another method your web browser can make a request of the web server. When the browser makes a request via by accessing a URL, that is a GET request. But through the form we can make a POST request. POST requests keep the information out of the URL  and is the preferred way to send information from a form to a web server.

# We need to update the route decorator to handle both GET and POST requests
@app.route('/sendBreakfast', methods=['GET', 'POST'])

## To access the information the user's web browser packaged up from the form and sent to the request, we need to import the request object from flask
from flask import request

#and then add some control flow to the handle_breakfast() function.

if request.method == 'GET':
  return "You're getting the breakfast page"
else:
  return "you're posting to the breakfast page"

#Now how about that data...to access the data froom the form, we do request.form
# Let's add these two lines of code and see what we get
form = request.form
print(form)

#To access the information, we can treat this object like a dict and access it like
# Store the nickname in a variable for easy reference
nickname = form['nickname']
# Store the breakfast in a variable for easy reference
breakfast = form['breakfast']

#And let's send this back to the user through the return
return f"Hello, {nickname}! I hear you had {breakfast} for breakfast"

## Of course we could package up this info into a data dict and pass it into a render_template().

## The last key concept we want to go over now is what we might refer to as business logic. Business logic is what your web app will do between getting a request (GET or POST) and what it sends back to the user response.

## Chatstorm: One example of business logic is when you enter a cuisine type in Yelp and it uses your current location to return a list of nearby relevent restaurants. What are other examples can you think of?

## Chat waterfall: So we just got the user's nickname and their breakfast (two strings)....what can we do with it? 

# A guiding principle of computer science is a separation of concerns. While it might sound impressive to write an app of 1000s of lines of code, it quickly becomes unwiedly to debug and to manage new features.

# So here's one way to do it....(1) write helper functions in model.py (2) import the model into app.py, and (3) use these helper functions to modify the user data before sending to the template

# Let's write a shout function together in model.py
def shout(word):
  return word.upper()+'!!'

# to import it we go to app.py
import model

## And to use it
model.shout()

# So let's change our code to say..
loud_name = model.shout(nickname)
return f"Hello, {loud_name}! I hear you had {breakfast} for breakfast"

#And let's test it out

## Whew. That was so intense and so cool! We'll spend the remainder of this pre-break time to continue to marinate in this initial flask web app we've created. Depending on your current comfort level,

# Create a results.html template that uses the name and breakfast values in the context of a larger HTML page.
# Write a model that does something more interesting.
# Modify the form so that it takes other inputs like how many servings they had.
# Add images and style to the results page.
# Bonus points if the images are dependent upon what breakfast the user entered.
# Add multiple templates and route to different ones depending on the user's answer.


### Post break...

# If you want to dive in to a semi-structured lab of creating a birthstone lab
# If you want to work through these steps with the instructors to create the birthstone lab


## Afternoon session
# Continue to work on the birthstone lab to get it just where you want it. 


# Copy down the flask template again and try out one of these other ideas.
# If a student pairing is mostly in their learning zone:

# Write an app that takes in a sentence and tells whether there are an even or an odd number of characters in it.
# Write an app that takes in two separate numbers, and then an operation name like "times" or "plus" and returns an answer.
# Write an app that takes in a restaurant bill and returns a long string explaining your different tipping options.

# If a student pairing is mostly in their comfort zone:

# Write an app that takes in a sentence, splits it into individual words, and then displays each word in a separate <p> tag - (requires either returning a string with lots of concatenated "
# " and "

# " substrings, or some code run between "{%" and "%}" tags)
# Write an app that takes in two words and renders them in some stylistic way - (requires styling written between style tags)
# Write an app that takes in a mathematical expression like "43 + 82" and returns the answer - (This answer scales in difficulty depending on how many terms the user puts in the expression and how well they account for it)
