## Morning Session

### Morning Routine --- 

## Stretch and Share ## 
# Question: What's the best piece of advice you've ever been given?


### Coding Game ###
#### In your Breakout rooms, you'll have 10 minutes to play through this CSS Diner - Sushi Selector Game https://flukeout.github.io/

### Microfeedback ###
## Everyone excited for project mode! We are too. And we're looking forward to exploring just how our projects can make the world a better place.

### Agenda For Today ###
# Github Collaboration
# Review Sessions
# Break
# Post-Break Flex Time
### You can ask additional questions or start working on your project. You'll let us know right before the break
# Lunch
# Project Mode Afternoon

### Git Collaboration ###
# In order to Deploy to Heroku, you need your project to be on Github (it's the easiest way to deploy)
# So we want to make sure that we are practicing our add/commit/push Git workflow and add a new workflow so we can collaborate.

# First, let's identify which partner will create the copy of the github repository. Message to eachother via the slack DM from yesterday. That person will template this repo https://github.com/upperlinecode/flaskproject

## Next, this partner needs to add the other partner as a collaborator via the Github website. You'll do that by going to settings -> manage access -> invite a collaborator. Type in your partner's git username. Your partner will need to log into their github account to accept the invitation.

## At this stage, both the repo owner and repo collaborators will be able to copy down the project using git clone <GitHubURL.git> in your FinTechFocus2020 folder (no more day subdirectory)

## Green Checkmark in participants window when you and your partner have the repo cloned to your cloudshell

## Next, we want to set up branches so we can work individually on the project without too many conflicts

# 1) Create your branch - Do this one time only
git checkout -b branch-name
# where branch-name is going to be your name

#2) Then you would do your coding like you normally would. To practice, let's each make a new file in the templates folder of "yourName.html"

#3) Next, we would do our typical add/commit workflow
git add filename
git commit -m "Create filed yourName.html"

#4) But now that we've created a branch, we don't just do git push. When we do git push, we will get back an error that we haven't specificed a remote branch on GitHub. So for the first time, we need to use
git push --set-upstream origin <branch-name>
#where you replace <branch-name> with your name

# The next time you need to use git push, it will assume what you just specified.

#5 ) Next, we need to merge the changes in. We do that by going to GitHub and creating a pull request. One person will create the pull request and the other person will merge teh pull request.

#6 ) Finally, for both partners to have teh same version each person will run
git pull origin master
## You might need to resolve some conflicts locally...you'll do that by editing the files with the conflicts to decide what you want to keep.

#7) And finally you'll do one last sync with a
git push

# We'll spend ~10 minute in breakout rooms to try out this workflow again. 
# This Glitch site has the directions laid out
https://voltaic-calico-fibre.glitch.me/

# 1) Create another new file in the templates folder
# 2) Edit the same line of code in app.py to see what a merge conflict looks like

##### Review Sessions #####
# We will have review sessions about
## Using APIs
## Bootstrap
## Flask + MongoDB
## Advanced Mongo

### Each session will be for ~30 minutes so you'll be able to attend two.

# PM via Zoom which Session You'd like to attend 1st

## Three of the sessions will be lead by your fellow classmates! Very exciting

## We'll also be able to do additional sessions next week if there's a feature you want to include as your project progresses


##### Off to Breakout Rooms ######

# PM via zoom which one you'd like to attend second