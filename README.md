

# Welcome to Share Plate

This site was set up by a passionate foodie for other passionate foodies. It is a casual and easy way to share and find unique and popular recipes. To use the app you need to first register. Once you become a member you will have a bevey of delicious recipes to choose from. Enjoy!


[The live website can be viewed here!](https://shareplate.herokuapp.com/)

![Am I responsive images](/static/images/responsive.png)

## Table of contents 


1. [User Experience (UX)](#UX)
2. [Features](#features)
3. [Design](#design)
4. [Technologies Used](#technology)
5. [Testing](#testing)
6. [Deployment](#deployment)
7. [Known Bugs](#bugs)
8. [Credits](#credits)

______

<a name="user-experience"></a>
## User Experience (UX)

<a name="stories"></a>
### User Stories

This website is a membership only site which provides information about different recipes provided by other members. It is directed at the novice cook. It allows you to also contribute your own recipes, edit them and remove them if you don't want to share them anymore. The ingredents, method, cuisine, star-rating and tools required are provided by site owner and other users. Foodies will without doubt find "gems" of tasty recipes form all over the world.


- ####  User
    1. I want a visual appealing site to appear when I click on the url.
    2. I want a quick description of what the site is about and its purpose.
    3. I want to easily navigate through the site to browse the content from other people.
    4. I want to easily log in and out of the site.
    5. I want my own area, personal to me, so that I can see the recipes that I contributed.
    6. I want to be able to create, update and delete my own content. 
    7. I want the site is responsive on all devices.
    8. I want to easily search for an ingredient, for example eggs, and a list of recipes containing eggs appear for me to select from.
    9. I want a star rating so that I pick the best recipe to try.
    9. I want my previous searches to be still available when I log back in.

- ####  Admin (AKA SITE-OWNER)
    1. As admin I want to read all the recipes.
    1. As admin I want to add, edit and delete my recipes.
    1. As admin I want to add new categories that have been requested by users.
    1. As admin I want to manage categories of recipes. As well as adding them, I want to also edit and delete the category.
    1. As admin I want to be able to see all users that have contributed to the site.
    1. As admin I want to gather a database of emails so that in the future we can sell kitchen utensils etc to the members.
    
- #### User who wants to get recipe
    1. I want this site to be exclusive - like a club - and so LOGin is required everytime.
    2. I want to be able to quickly delete my recipes and edit them.
    1. I want to get recipe by search option.
    1. I want to be able to email and phone the site owner with querys and suggestions. 
    

- #### User who wants to post recipe
    1. I want to create my profile by sign up.
    1. I want to easliy login and check my page.
    1. I want to add new recipe on my page and available to all users of site.
    1. I want to edit and delete my recipe only.
    1. I want to contact the site owner.
    1. I want easy access to social media at any time I am on the site.


<a name="design"></a> 

    # DESIGN

From the project goals the following features were included in the scope of the project.

### Colours

1. Colours were carefully selected to be bright and welcoming while sticking to pinks and greys. 

They include:
     
       1. #e91e63 pink
       2. #000000
       3. #ffffff
       4. #ad1457 pink darken-3
       5. #c51162 pink accent-4
       6. #e0e0e0 grey lighten-2
       7. #bdbdbd grey lighten-1
       8. #eeeeee grey lighten-3
       9. #455a64 blue-grey darken-2

### Typography

- #### The main font used is cursive

<a name="features"></a>
## Features


- ### Common Features Across All Pages

    - Nav bar allows user to easily navigate across all pages and it is available on all pages
      - The brand logo is positioned on the left and is visible on all pages.
      - Navigation links are to the right and clear and easy to read and access.
      - Navigation links collapse in a Shareplate menu and slides in from the left when viewed on mobile device.

    - Footer is available on all pages - it contains contact details and social media links  
     
    - Flash messages:

      - Messages displayed at the top of the page to provide the user confirmation of actions like sign out, adding or editing category.
    
    - Buttons/Links
      - All buttons are styled more of less in the way to provide consistency across the page.
      - All links work correctly
      - All external links open in a new tab to allow the user to easily navigate back to the page. 


### Specific to Pages
* Home Page
- This page has header, footer and a welcome card that invites you to either login or register. The nav bar has home, login or sign up only. To see more on this site you have to register. Its exclusive. The footer has contact details and social media links.


* Login Page 
    - This page simple displays a clean card looking for your log in name, password and submit button. The footer has contact details and social media links. 

* Sign Up Page
    - This page has sign up form. It is a clear card again and looks for your username, email and password, It has a submit button and the uniform nav bar.

* Profile page 
    - When you successfully log in this page displays all your recipes. It allows you to edit and deleted recipes. From this page you can see on the nav bar Home, All recipes, You profile, Add Recipe, logout

* Category Page
    - Only admin can access this page. In this page admin can manage categories - add, delete etc.

* Alls Recipes
    - This page displays all recipes - they are in an accordian format and drop down when you click on them. Here the recipe owners can edit and delete their recipes but can read other peoples recipes.


### Future Features
  - We are currently gathering emails from users. We hope to provide an online store for artisan cooking utensils and spices. 


## Wireframes

[PDF of all wireframes for this project](links/wireframes/wireframe.pdf) 


## Surface

The look and feel of the website should be one of exclusivity but with a welcoming tone. Colors are vibrant, fun and colorful. The colour and themes are complementary and complementary 
throughout. Its clear and easy to find what information you need from the website.

<a name="technology"></a>
## Technologies Used

### Languages Used

  - [HTML5](https://en.wikipedia.org/wiki/HTML5)
  - [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
  - [Python3](https://en.wikipedia.org/wiki/Python_(programming_language))
  - [JavaScript](https://en.wikipedia.org/wiki/Javascript)
  - [Jquery](https://en.wikipedia.org/wiki/JQuery)

  ### Frameworks & Libraries

  - [MaterializeCSS ](https://materializecss.com) - A modern responsive front-end framework based on Material Design.
  - [Font Awesome](https://fontawesome.com/) - Font Awesome icons were used throughout.
  - [Git](https://git-scm.com/) - Git is used to allow for version control.
  - [GitPod](https://www.gitpod.io/) - GitPod my IDE
  - [Github](https://github.com/) - GitHub is used to host the project files and publish the live website by using Git Pages.
  - [Heroku](https://www.heroku.com/) - Heroku is the cloud platform to deploying the app.
  - [Flask](https://flask.palletsprojects.com/en/1.1.x/) - Flask is the web framework for the app.
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja is used for Python template.
  - [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/) - Werkzeug is used for password hashing and authentication and autohorization.
  
### Database

  - [MongoDB](https://www.mongodb.com/) - MongoDB a cloud database service used for the project.
  - The project has 4 collections in the database. All fields are string data type.The database structure in MongoDB is as follows:

 [PDF of database structure for this project](static/links/DATABASE.pdf) 



## Validated
- All html files were sent through the html, CSS and PYTHON validators. Any errors were fixed and here are screen shots of validation.
[PDF of validated files](static/validate/pep8test.txt)
[PDF of validated files](static/validate/CSSVALIDATOR.pdf)
[PDF of validated files](static/validate/HTMLVALID.pdf)

<a name="testing"></a>
## Testing

* Throughout the writing and styling of the document I ran Devtools  [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) from google crome each and every time in an effort to make sure my website was responsive across all devices.

* The code was put through W3C Validators for HTML, pep8 and CSS3 with no issues found.

* Every inch of the website was checked - all the links and interactive buttons and click were check numberous times. Everytime a user or recipe was added the MONGODB was checked.

I have documented testing in this pdf. I have shown  design bugs that were found and proof that they were fixed:

[PDF of validated files](static/validate/responsive.pdf)


### Usability Testing
  - This website is shared and tested with colleagues, family  with friends to check on different devices and accessbility.

### Compatibility Testing
  - #### Browser Compatibility
    - Tested on Chrome, Firefox, Microsoft Edge, Safari.
  - #### OS Compatibility
    - Tested on iOS , Android 10 and Windows 365.

#### Other users

Feed back from friends and family I asked to test the site was as follows:

* That the site was easy to use.  
* Interesting and nicely interactive.
* The nav bar and footer were always available to allow for easy navigation.
* It was easy to get back to the home page by clicking on the home buttons and the logo throughout the site.
* It was easy to find the social media links at the bottom of every page
* Contact details were clear and easy to find.
* It was nice to click on the recipes and for the dropdown to reveal the recipes.
* It was simple to add a recipe, edit and delete a recipe.
* Different type of devices were used and the user found that the site was managable on mobiles & tables also.


One example of testing went as follows:

Test: To make sure that when the admin adds a category that if it is there already then a message will flash onto the screen. 

1. Log on to the website as admin. 
2. Click on Add category on the nav bar.
3. The Category page opens and there is a option to add a category. Click on this and add the category that is their already.
4. The error message that appears is : THIS CATEGORY ALREADY EXISTS.

TEST2: 

1. Log on to the website as any user. 
2. Click on recipes on the nav bar.
3. Make sure the buttons for edit and delete are not available to you if you don't own that recipe.
4. Test the edit and delete buttons that are there - worked perfectly.

<a name="bugs"></a>
## BUGS: 

1) On extra Small devices I found the Share Plate logo moved down onto visuals below it. FIX: I resized the font in styles.css file.

2) The add category function was not working properly - it allowed me to add a category that was already there. I fixed it by removing the .lower() code and then it worked perfectly.

3) The buttons on the small devices - could look better - they are too big - they need to be resized

<a name="deployment"></a>
## Deployment


GitHub Pages was used to deploy this website.


* From your broswer log into GitHub with you login account. 
* Locate the specific project's GitHub Repository. It will be in a list on your left hand side.
* In the repository, click on the Settings tab at the top right hand corner of the middle panel. It 
has a cog wheel beside it.
* After clicking on settings scroll down about halfway where it says GitHub Pages.
* Select "master branch" from the drop-down under Source, then click save. It'll then give a URL, which is the live deployment page to use.
(note it may take a couple minutes and a hard refresh Ctrl+F5 to fully load your project the first time)
* Then go back to the top, click Code tab to go back to the main repository, and at the very top to the very right there's a place to paste the live deployment link. You are live!
* Your readme file will be located under it.

To run the code locally do the following:

When you clone a repository, you copy the repository from GitHub to your local machine.

* Log onto github.
* Go to the main page of the repository.
* Over the list of files, click on the word Code.
* We want to clone the repository using HTTPS so click on HTTPS and copy the link provided.
* In your own IDE open GIT bash.
* Change to the directory where you want the clone directory and files to go into.
* In the terminal type in "git clone" and paste in the URL that you just copied form Github.
* Hit enter and you have your local clone. 



## Media

- All photos came from google images.

<a name="credits"></a>
## Acknowledgements

*TIM NELSON - CODE INSTITUDE - This app is based on his task manager app but applied to my project
*Tutor - Johann for helping me with the validation of the HTML file with JINJA
*Google 
*w3schools
*slack ci community


 