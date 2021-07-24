

# Welcome to Share Plate

This site was set up by a passionate foodie for other passionate foodies. It is a casual and easy way to share and find unique and popular recipes. To use the app you need to first register. Once you become a member you will have a bevey of delicious recipes to choose from. Enjoy!


[The live website can be viewed here!](https://shareplate.herokuapp.com/)

![Am I responsive images](/static/images/responsive.png)

## Table of contents 

1. [User Experience](#user-experience)
   - [User Stories](#stories)
   - [The 5 Planes](#planes)
   - [Wireframes](#wireframes)
2. [Database Schema](#dbschema)
3. [Features](#features)
4. [Technologies Used](#technologies)
5. [Testing](#testing)
6. [Database Creation](#database)
7. [Deployment](#deployment)
8. [Resources](#resources)
9. [Credits](#credits)
    - [Media](#media)
    - [Code Snippets](#code)
    - [Acknowledgements](#acknowledgements)
10. [Technical Support](#technical)
______

<a name="user-experience"></a>
## User Experience (UX)

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




    
<a name="deployment"></a>
## Deployment

  1. Install all the requirements: In your development workspace open a terminal window and type: pip3 install -r requirements.txt.

  2. Create a database in MongoDB

     - Login to your MongoDB account.
     - Create a cluster and the database called shareplate.
     - Create the following collections in the db: categories, recipes, stars, & users.
     - Populate your database with some documents so that you have something to work with on the back end.

  3. Back in the IDE create the environment variables
     - 
     - Create the file env.py. This will contain all the envornment variables.
        - Import os
        - os.environ.setdefault("IP", "Added by developer")
        - os.environ.setdefault("PORT", "Added by developer")
        - os.environ.setdefault("SECRET_KEY", "Added by developer")
        - os.environ.setdefault("MONGO_URI", "Added by developer")
        - os.environ.setdefault("MONGO_DBNAME", "Added by developer")
      - Create a .gitignore file in the root directory of the project.
      - Add the env.py file in the .gitignore. 
  4. Run the app: Open your terminal window in your IDE. Type python3 app.py and run the app or right click on the app.py file and from the dropdown click on run file in terminal.
  
- ### Heroku Deployment
  1. Set up local workspace for Heroku. The requirements.txt file tell heroku which libraies/modules are needed for this application.
     - In terminal window of your IDE type: pip3 freeze -- local > requirements.txt.
     - In termial window of your IDE type: python app.py > Procfile 
  2. Set up Heroku: create a Heroku account and create a new app and select your region.
  3. Deployment method I used was 'Github'.
     - Click on the Connect to GitHub section in the deploy tab in Heroku.
       - Search for your repository and select it by clicking on connect.
     - Go to the settings app in Heroku and go to Config Vars. Click on Reveal Config Vars.
       - Enter the variables contained in your env.py file. IE: IP, PORT, SECRET_KEY, MONGO_URI, MONGO_DBNAME
  4. Push the requirements.txt and Procfile to repository.
     - $ git add requirements.txt
     - $ git commit -m "Add requirements.txt"
     - $ git add Procfile 
     - $ git commit -m "Add Procfile"
  5. Automatic deployment: Go to the deploy tab in Heroku and scroll down to Automatic deployments. Click on Enable Automatic Deploys. By Manual deploy click on Deploy Branch.

  Heroku will receive the code from Github. This will take a few minutes to build. Click on "Open app" in the bottom right corner of your Heroku account. The app will open and the live link is available from the address bar. 

- ### Forking
  
  1. Go to the GitHub website and log in.
  2. Locate the [Repository](https://github.com/Michele-C/SHAREPLATE-).
  3. On the right-hand side of the Repository name, you'll see the 'Fork' button. It's located next to the 'Star' and 'Watch' buttons.
  4. This will create a copy in your personal repository.
  5. Once you're finished making changes you can locate the 'New Pull Request' button just above the file listing in the original repository.

- ### Cloning 
  
  1. Go to the GitHub website and log in.
  2. Locate the [Repository](https://github.com/Michele-C/SHAREPLATE-).
  3. Under the Repository name locate 'Clone or Download' button in green.
  4. To clone the repository using HTTPS click the link under "Clone with HTTPS".
  5. Open your Terminal and go to a directory where you want the cloned directory to be copied in.
  6. Type Git Clone and paste the URL you copied from the GitHub.
  7. To create your local clone press Enter.