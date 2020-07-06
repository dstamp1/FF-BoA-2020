# Intro to Cloudshell
## A virtual computer you get access to for free with a google account
## You get files and a terminal
### Do a quick tour of the parts

# Terminal - Bash
## The programming language of the terminal is called `bash` and most of its commands are abbreviations or acronyms.

# PWD - first command print working directory
## This command tells us where we are in the file system. It's called the working directory

# CHATSTORM - What are the ways you interact with the files and folders on a computer? open folders, files, make files, make folders, click inside of folders, etc.

#LS - abbreviation for list
## WATERFALLL - How can you tell difference between a file and a folder when looking at output of ls

#Making a directory (do this first so students can then cd into it and then make files there in an organized way)
## mkdir <directory_name>
## Let's make a directory called FintechFocus2020

#Change directory - cd <directory_path>
## Let's change into this new directory cd FintechFocus2020 and check the new working directory
## Waterfall - Copy and paste the output of pwd after cd'ing to FintechFocus2020 (if all students have the correct output, we are good to go!)

#Let's make another directory inside of the folder. Each day we will make a new directory for that day and include the day number.
## Make a new directory called 'day01' and CD into it. (take 30 seconds)

#Making files
## We'll use the command touch to create new files. We can list multiple file names w/ file extensions and make them simultaneously. 
## Mini-challenge in breakout rooms: In your day01 folder, make a folder called "myFirstWebsite" and create a index.html style.css and script.js inside that new folder. Use ls and pwd to verify your work.

### Opening files
#### To open files available in your current working directory (use ls to see whats available) you'll use the command cloudshell open <file>. 

### Check for time....removing and moving files and folders might be more beneficial as a full stretch where students look up how to do on their own. https://www.learnenough.com/command-line-tutorial/manipulating_files#sec-renaming_copying_deleting

## Possibly state that we can also move, delete, and rename files and folders.
# cp (copy) rm (remove/delete) mv (move) 

##First Lab
### Framing: We're going to work on our first lab now. Labs is where the *real* learning happens where you will work closely with your classmates to reinforce concepts and solve challenges. 
### To get the lab in your cloudshell, we will use git. We'll talk in more detail later on what git is and how we will use it for our own, original code, but for our purposes right now we will use this workflow. You'll cd into the directory of the day (in this case, day01) and you will run shared code that looks like 'git clone <url>' and then cd into that newly copied directory. Labs will include a readme file with directions and code for you to work with.
### During class, labs will take place in breakout rooms in pairs. When you get into the breakout room, decide who will be the driver (does the typing) and who will be the navigator (tells the driver what to type). Both students can contribute ideas on how to solve the challenge at hand. During labs, you will use a slack DM to exchange code back and forth for when you swap driver/navigator. Swapping driver/navigator should happen every 4-5 minutes (about two songs worth). 
### In your breakout room, you can click a button to ask for help and one of us will be able to pop into your room. We can also broadcast messages to all of the rooms too. When we're in breakout rooms, use slack to send us messages. 
### Most of the labs are designed in a way where there will always be more fun to be had in challenges than we will have the time for. The goal for no lab if for you to complete it! But if you do happen to complete a lab, we will always have extra fun additional labs for you to work. 

### Okay, so here's the code for our first lab 'git clone https://github.com/upperlinecode/command-line-hidden-treasure.git'

### When you get to your breakout room, introduce yourself again, tell your partner your favorite color, give them a digital high five and have fun coding!