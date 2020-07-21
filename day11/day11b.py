Mid-Morning Session

### For the afternoon, we're going to create and deploy a Flask app that incorporates an API.

## We'll spend ~30 minutes incorporating the JService API and your code from the morning to display a jeopardy clue

## We'll also sign up for Heroku and deploy our app.

## After we deploy our basic jeopardy API, we'll be able to either continue to build out features or you can explore some other APIs


## We'll also add two new things to our Flask knowledge: Jinja2 templates & session variables. And we'll be able to incorporate the boootstrap that we learned last week.

# Let's use a modified version of the Flask Template https://github.com/dstamp1/flask-template

## First, let's look at this new file called "base.html". This file serves as a template that our other files will inherit. It includes two blocks: title and content. To fill in these blocks, we use the same syntax and then fill it in. You can see that in our index.html file. You'll also notice that our base.html includes Bootstrap.

## Second, let's look at the session variable. To use the session variable, we need to import it from flask and give the app a configuration attribute called secret_key. The flask app will use the secret_key to store information specific to the individual user accessing your website in a crypographically safe form. We can add to, modify, and remove that information just let it's a dictionary. We do that with session[key]  where key is a string that we set. This information is stored in the end user's browser and is available to our flask app business logic. We also can display it on the page.


### In your breakout rooms, 1) write a route called '/random' that display a random jeopardy clue using the Jservice API. As a stretch, begin to style it using a card.


#### So now we have an app that we want to deploy for others to access. Right now, we need to access via Cloudshelll in a  "local" way. Pushing to a service like heroku lets us send it to our friends and family!

# Heroku will provision a virtual machine that will install python and all the packages that we used and essentially do "flask run". There is alread information in the files runtime.txt, requirements.txt, and Procfile that makes this possible. The one place we need to update when we deploy web apps in this course is in requirements.txt where we update the list of packages to include any that we might have installed. To see what's installed in your cloudshell environment, we can run pip3 freeze. We don't need to include every single package that is installed, just the ones that we're using. For us, that would include requests requests==2.11.1

## Let's go to Heroku and sign up for an account. Green check once we're on the apps homepage

## To deploy the app, we'll click new => create new app. You'll give your app a unique (across heroku) name. Then on the deploy tab we'll select Connect to Github.

# WE'll connect to a particular github repo. and select Enable Automatic Deploys. finally we'll click deploy branch.

# We can click back to Overrview and then in the latest activity area we can click on the build log. Here well be able to see the progress and identify any deployment errors.

#Finally, we can view the live web app by clicking open App in the upper right corner.

## 99% of deployment issues are due to missing packages in requirements.txt
