Morning Session

### Morning Routine
# Stretch + Share 
## Question: If you could instantly learn how to do something new, what would it be and why?

# Microfeedback - Lots of fun working through Flask. Students shared lots of growth from morning to afternoon session. We wanted to give a shoutout to Jaspreet, Alejandro, Alyssa, Tashfia, Anjali, Patrick, Angel for working on cool stuff during CYOA yesterday


### A game...Sean's list of people idea? Sure. I'll facilitate
#Students pick a person from history, DM you, you read those out loud one time, if you have a guess who submitted the name, send a message in the chat. 


###wink assassin?? Sure, i've never played via zoom you just PM "wink" and whoever you've winked at has to die dramatically + turn off cam...may be morbid for AM play

# Review of Design Manifesto
## On Tuesday we started class by talking about examples of good and not so good web design.
## Chat storm: What are some features of good web design? Send as many as you can think of

### Good web design is about putting the content at the center. The styling supports the content and doesn't distract.

# We have these key facets at our disposal: colors (text and background), font choice and size, and whitespace around elements (margins and padding)

#readbility, ease of focus, color scheme helps

## Bootstrap Code-A-Long

### Styling a page with CSS can be very tedious and often requires creating many classes and IDs.
### Sometimes this styling doesn't quite work out and can have some visual inconsistencies.
### To solve this problem, groups of people collaborate on design frameworks. These frameworks give you a wide range of CSS classes you can use to consistently style your site.

### We'll start off together this morning seeing how to incorporate Bootstrap into your site.
### Then we'll look through the Bootstrap documentation to pull out the essential features https://getbootstrap.com/docs/4.5/getting-started/introduction/

## Then we'll be able to explore aspects of the bootstrap library and bring it back to the whole group to demo the code.

## Then we'll look at the Bootstrap Grid together

## Finally, we'll be able to revist a previous HTML project you've worked on and you'll restyle it with Bootstrap.

## We'll close out the afternoon with a design challenge!



#### Using Bootstrap in our Website ####

## To use Bootstrap, we need to include a link to their CSS file & some JavaScript Files.

## Let's mkdir day09 and copy down this starter code: https://github.com/upperlinecode/bootstrap-code-along.git

# To add the CSS, we'll add
<link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">

#And then we'll add the JavaScript links
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>

## To view this page in cloudshell, we can right click on the file and select open with -> preview

## Let's start to add some content to our site!

### Take 3 minutes and add a list to your site with:
# An h1 header
# As many list items as you can


### To see how we use the Bootstrap classes, we're going to restyle the list using a List Group
# If we look at the documentation https://getbootstrap.com/docs/4.5/components/list-group/
# We see we need to add some classes
<ul class="list-group">
  <li class="list-group-item">Cras justo odio</li>
  <li class="list-group-item">Dapibus ac facilisis in</li>
  <li class="list-group-item">Morbi leo risus</li>
  <li class="list-group-item">Porta ac consectetur ac</li>
  <li class="list-group-item">Vestibulum at eros</li>
</ul>
# We also have some additional options to add .active or .disabled to change the appearance

## Take ~5 minutes in your breakout rooms to try out some more options of classes for list groups


### Showcase some code ###


# As you can see in the components section, there are alot of different components bootstrap pre-styled. Each breakout room will be designated to explore 1-2 of these components and to show it off for the group. 

Alerts & Badges
Buttons & Button Groups
Navbar x
Progress Bar
Dropdown x
Forms x
Card x
Modal x

#### 10 minutes in breakoout room with ~1 minute for each group to demo ####



#### Crash course to Bootstrap Grid ####
# A key feature of modern web design is the responsive page. Web sites are accessed on screens of many widths and we want our sites to look good on all of them.
## Bootstrap gives us the tools to make this happen.
# The fundamental concept is that the page is constructed of rows and columns.
## In our bootstrap index.html, let's add
<div class="row">
  Contents of row.
</div>

## Nested inside of this div we can add our columns
<div class="row">
  <div class="col-1">contents of column 1</div>
  <div class="col-1">contents of column 2</div>
</div>
# Let's preview this file.

# A question you might ask next is how many columns are possible. Let's experiment to find out
<div class="row">
  <div class="col-1">contents of column 1</div>
  <div class="col-1">contents of column 2</div>
  <div class="col-1">contents of column 3</div>
  <div class="col-1">contents of column 4</div>
  <div class="col-1">contents of column 5</div>
  <div class="col-1">contents of column 6</div>
  <div class="col-1">contents of column 7</div>
  <div class="col-1">contents of column 8</div>
  <div class="col-1">contents of column 9</div>
  <div class="col-1">contents of column 10</div>
  <div class="col-1">contents of column 11</div>
  <div class="col-1">contents of column 12</div>
  <div class="col-1">contents of column 13 - note that this 13th column will wrap to start a second row, since we've exceeded the maximum of 12.</div>
</div>

## Having 12 columns available to us is very exciring, but it does seem like its way too much content to have side-by-side.

## Bootstrap gives us the ability to have a column span more than 1 column. To do that, we include a -x where x is a whole number from 1 to 12. 
# To ensure that the row is complete, we'll make sure each row adds up to 12.


#### Recreating the Spotify Footer ####
# Let's use what we just saw to try to recreate the spotify footer

<div class="container">
  <div class="row">
    <div class="col-lg-2">Logo content</div>
    <div class="col-lg-2">Company content</div>
    <div class="col-lg-2">Communities content</div>
    <div class="col-lg-2">Useful links content</div>
    <div class="col-lg-4">Social icons - this one is twice as wide as the other four.</div>
  </div>
</div>

## To make this site responsive oon different viewports, we can specify the column sizes at different breakpoints.
