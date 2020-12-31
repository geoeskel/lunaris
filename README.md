![alt text](https://github.com/geoeskel/lunaris/blob/master/static/documentation/wireframes/end_effect.JPG?raw=true)

# Lunaris Library
Data Centric Development - Code Institute project

This project aims to create a database of movies and series. It allows user to add their favorite movies & series, rate, categorize, and specify the service where they can be watched


# Design 
I wanted the website to have a calm, cozy, and comfortable theme. It should resemble a library: delicate contrasts and toned colors. I used the below tool to create the website theme:
https://coolors.co/fbebd0-f79f45-0d1f1f-6c231d-cc9e7e 
1.	Colour Scheme
- The 5 colors used are: Papaya Whip, Deep Saffron, Dark Jungle Green, Persian Plum, and Antique Brass

2.	Typography
The Cinzel font is the main font used throughout the whole project. It is a simple-looking, all caps font that works well with the website’s design; it is both attractive and appropriate

3.	Imagery
The background image works well with the rest of the design and allow for good color contrast. It gives the website a calm, aesthetic look.


# UX
This database is designed for anyone who would wish to systematize their knowledge of various movies and series and access it from one location. It has plenty of room for improvement

## User stories

1.	First Time Visitor Goals
As a first-time visitor, I want to easily navigate through the website to be able to easily access all of its features
As a first-time visitor, I want to be able to immediately see what the website is about
As a first-time visitor, I want to be able to create an account
As a first-time visitor, I want to be able to log in with my new account
As a first-time visitor, I want to be able to explore the dashboard easily
As a first-time user, I want to be able to add a movie to the database
As a first-time user, I want to be able to search for movies 
As a first-time user, I want to be able to log out when I am done
As a first-time user, I want my personal details to be private and kept away from the reports

2.	Returning Visitors Goals
As a returning user, I want to be able to log in easily
As a returning user, I want to be able to do all the things as stated in a new user with the same ease
As a returning user, I want to see my own movies and series
As a returning user, I want to be able to add a movie to my collection
As a returning user, I want to be able to modify my movies
As a returning user, I want to be able to delete my movies

3.	Frequent Visitor Goals
As a frequent visitor, I would like to see if there are any new updates and features

 
# Wireframes

1.	Plan #1: https://github.com/geoeskel/lunaris/blob/master/static/documentation/wireframes/plan%231.jpg?raw=true
2.	Plan #2: https://github.com/geoeskel/lunaris/blob/master/static/documentation/wireframes/plan%232.jpg?raw=true
3.	Plan #3: https://github.com/geoeskel/lunaris/blob/master/static/documentation/wireframes/plan%233.jpg?raw=true
4.	End-effect: https://github.com/geoeskel/lunaris/blob/master/static/documentation/wireframes/end_effect.JPG?raw=true



# Features

## Navbar 
1.	Responsive navbar with a book icon ‘hamburger’ on devices with a screen width smaller than 992px 
2.	Each link will take the user to the designated pages
3.	There are links for the home page, login page, and signup page when the user is not logged in
4.	When the user logs in, the additional links appear: add a movie, my library, log out
5.	The ‘Lunaris Library’ link will take the user back to the home page

## Footer
1.	A copyright is added to the footer

## Home
1.	There is a welcome message on top of the Home page
2.	User can search the titles using title name, genre, title location, or the user ratings
3.	There is a list of all the movies added by all users below the search field

## Login
1.	A form to input user details that will allow them to log in
2.	A button that will submit the form.
3.	If the user inputs an incorrect email or password, then a message will flash underneath the heading giving the user feedback.
4.	After successful login, a flash message is displayed on the top of the page welcoming the user back
5.	There is a link to the signup page in case the user doesn't yet have an account

## Signup
1.	A form to fill in to register an account
2.	There is a link to the login page in case the user already has an account
3.	Once signed up, the user is redirected to their profile page

## Add movie
1.	A form to fill in to add the title to the user’s library: 
  a.	Title field 
  b.	Genre (pick from the drop-down menu)
  c.	Available on (pick from the drop-down menu, multiple choices)
  d.	User’s rating (pick from drop down menu)
2.	Once the title is added, the user is redirected to the home page where they can see the title they added on the bottom of the title list

## My Library
1.	A welcome message saying ‘users’ profile
2.	A list of all the titles the user has added
3.	User can edit/delete the titles they added
4.	Delete button has a confirm form (are you sure you want to delete). After the title is deleted, a flash message is displayed, confirming the action
5.	User can edit the title; the form looks identical to the one they used to add a title. Once they click on the Edit button, the flash message is displayed confirming that the movie has been edited. Once they click the Back button, they are redirected to the My Library page
6.	Under the movie list is the Fact Button. Once clicked, a randomly generated interesting fact is displayed 

## Log Out
1.	After the user logs out, a flash message is displayed, confirming the action



# Data Integration

I picked MongoDB for my project as it was the preferred database during the course and it can handle large quantities of data and I am expecting huge amounts of titles added 

In MongoDB my collections are: 
source
genre
movies
ratings
users
They store a mixture of strings and binaries. I hashed all of my passwords.

# Defensive Features

If the user tries to add a movie without a title, a message is displayed asking to add a title
If a user tries to delete a movie, a confirmation form is displayed, asking them to confirm
If a user tries to create an account whose username or password does not match the minimum criteria, a message is displayed asking match the format requested
A new user cannot use the same username as the existing user. If they try this, a flash message is displayed (username already exists)
If a user provides an incorrect password, a flash message is displayed (the username/password are incorrect. Please try again)
The passwords are hashed and a different salt is generated each time a password is made/changed. If anyone hacks into the database, they will not be able to see the passwords

# Technologies Used

## Front-end
1.	HTML
2.	CSS
3.	Javascript

## Back-end
1.	Python
2.	MongoDB Atlas

## Frameworks
1.	Materialize 1.0.0
2.	Flask
3.	Jinja
4.	jQuery

# Testing

JSHint Validator: https://github.com/geoeskel/lunaris/blob/master/static/documentation/validators/js_validator.JPG
W3C CSS Validator: https://github.com/geoeskel/lunaris/blob/master/static/documentation/validators/css_validator.JPG
PEP8 Validator: https://github.com/geoeskel/lunaris/blob/master/static/documentation/validators/pep8_validator.JPG
Google Lighthouse check: https://github.com/geoeskel/lunaris/blob/master/static/documentation/validators/lighthouse_check.JPG

## Basic test
1.	Nav has been fully tested
2.	I have checked that the collapsible open and close appropriately
3.	I have checked buttons enable and disable appropriately
4.	I have checked that the correct form options are unhidden based on the user's previous inputs
5.	All tests were done on PC and Mobile view

## Feedback from users
-	“I would change ‘Sign-In’ to ‘Register’ or it’s a bit confusing.”
Regarding this, I have changed the sign in to sign up to avoid confusion.

-	“There are 2 Hulus on the platform to watch on”
I have removed the duplicate source option from MongoDB

-	“I know this is meant to be a style but is coming across as blurry”
I have amended the styling to make it more visible and appealing to the eye. 

-	“can ‘Edit movie’ be changed to something like ‘confirm edit’ because I am already editing the movie by this point. “
I have amended the button to avoid confusion

-	“Is it possible to have any warning before I delete something just in case I click it by accident?”
I have added a confirm delete form 

-	“The buttons in mobile I think they are too close”
I have added a margin to the buttons for the view to be more clear and less clattered

-	“If you like to add to your features that option to add more than one streaming option and not just one”
I have amended the dropdown menu to allow multiple selections when choosing the title source


# User stories

First time user #1:
As a first-time user, I want to easily navigate through the website be able to easily access all of its features.	I expect all of the links to be working and in an intuitive position.	All the links take me to their destination and none are broken

First time user #2:
As a first-time user, I want to be able to immediately see what the website is about.	I expect information about the website to be ready available on the landing page without needed to click a button	The purpose is very close to the top and the home page gives me all the information I need

First time user #3:
As a first-time user, I want to be able to search titles.	I expect to click on the search form to fill in the details and find the title	I can search by movie title, genre, rating and source

First time user #1:
As a returning user, I want to be able to log in easily. I expect to find the login button easily and be able to fill in the form to login.	I could find the login button easily in the nav bar and the form is very quick to fill in. Once I have logged in I am taken to my profile page

First time user #2:
As a returning user, I want to be able to add a title to my collection.	I expect to add a movie and then find it in my profile page	When I click on the Add Movie link, it takes me to the form I can fill in to add a title. Once it is done, I can see the title on my profile page and in the Home page

First time user #3:
As a returning user, I want to be able to delete my titles	I expect to pick a movie, click delete and see a confirmation form	On my profile page I can see all the titles I added. Once I select one and click Delete I can see the confirmation form ‘are you sure you want to delete’. Once I confirm, my title is deleted

# Deployment

## Running app in Heroku.
Create a Heroku account. Click to start a new app. Pick your location based on the closest free version (or paid version) to your actual location. For this project it was Europe. Choose an appropriate name for the app and click to create.

Once your app has been created, then move to the ‘deploy’ tab. You can connect to GitHub through one of the tabs. I, however, have used the CLI. You can link to an existing repository by using the following command in your IDE:
$ heroku git:remote -a "enter-your-heroku-app-name"

Heroku has an excellent documentation on this and the full documentation can be found here under the ‘deploy’ tab in your Heroku account. There are several ways to connect your project to Heroku.

Then, head over to the ‘settings’ tab and click on the ‘reveal config vars’ button. Configure the following:
Key: value
IP: 0.0.0.0
PORT: 8080
MONGO_URI: "link to your MongoDB"

You can find your MongoDB link by going into your MongoDB Atlas account and clicking the ‘connect’ button. From there you have the option to choose to connect to your application and can select the correct language and version.

With the Heroku settings sorted, you can head back to your IDE. There a few things you now need to set up:
1.	A ‘procfile’ which will tell Heroku what kind of application it is and how it should be run.
2.	A ‘requirements.txt’ which will tell Heroku which dependencies it needs to install in order for the app to run. The command for ‘procfile’ is:
echo web: python run.py > Procfile

The command for requirements is:
pip3 freeze --local > requirements.txt

Please note that you need to re-run the requirements command if you add any dependencies mid-project. Otherwise, Heroku will not deploy the app correctly.

With those set up, you can now push your project to Heroku directly from your IDE.
$ heroku login -i

Enter your username and password. Push your commits to Heroku using this command:
$ git push -u Heroku master



# Credit

I mostly based my project on the tutorials provided by the Code Institute Data Centric Development Mini Project

Additional resources: 
-	https://pythonise.com/series/learning-flask/flask-session-object 
-	https://animate.style/ 
-	Wallpaper was downloaded from https://www.detroitlabs.com/wp-content/uploads/2018/02/alfons-morales-YLSwjSy7stw-unsplash.jpg 
-	https://www.w3schools.com/tags/att_input_pattern.asp#:~:text=The%20pattern%20attribute%20specifies%20a,pattern%20to%20help%20the%20user

# Acknowledgements

1. The initial inspiration came from my WhatsApp condeinstitute group for which I am very grateful! Also a bit thank you for assistance in testing and ideas on how to improve my project.	
2. My Mentor for continuous helpful feedback.


