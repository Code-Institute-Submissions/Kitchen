# Testing

## Content

## User Testing
1. **Get inspired into learning new recipes.**
    - This page was designed with an idea to look as realistic as possible (from a beginners point of view). 
    This to both encourage and inspire the user to scroll through all different kinds of recipies.
    - High quality images are used throughout the site to increase the user experience to the max.

2. **Browse different categories for easier navigation of what kind of recipe I want to cook.**
    - The different categories are displayed on the following pages for easy access for the user:
        - Home Page 
        - Recipies Page
    - The categories has their own category image that represents the content behind the category itself. 
    This to make it easy to identify the category before reading the name of it.
    - When clicking on each category the category image acts as the hero image, to also indicate which category is
    currently viewed.

3. **Be able to sign up and share my own recipies.**
    - When the user first visits the page he/she is prompted to press the blue button in the red section right under the hero image
    to sign up to the page.
    - The user can also sign up by pressing the 'Sign Up' button in the navigation bar at the top.
    - The appearance of the 'Sign Up' button is consistent throughout the site, with its blue color and white text.
    - When the user is signed in, the button text in the red section changes to 'Add Recipe' to encourage the user
    to share a recipe.
    - The user can also click on the link in the navigation bar with the text 'Add Recipe' to get to the page to add
    a recipe.

4. **Have a good overlook of my own recipies that I've made.**
    - On the users profile page, all the users recipies are listed right under the hero image of the page.
    - When the user don't have any recipies made the recipies section will fill out with a blue color to indicate
    that the list is empty.

5. **Be able to edit and delete recipies that I have made.**
    - On the each user recipe card there are two buttons displayed that only the logged in user can se:
        - A red 'Delete' button. 
        - A blue 'Edit' button.
    - The user can edit and delete their recipies on the following pages:
        - Profile Page:
            - On the profile page, the user has a better access over the recipies he/she has written. From here the
            user is able to both delete and edit each recipe.
        - Recipies Page:
            - The user is also able to delete and edit their recipies from the Recipies Page, however when a lot of
            recipies are displaying, and not only by the user in session, the user has to scroll through all of them
            in the order that the recipe was made and without any type of relevance.

## Automated Testing

## Manual Testing
All manual tests were done in the following browsers:
- Firefox
- Google Chrome
- Microsoft Edge

1. **Home Page/Index Page**
    - Navbar:
        - Make sure navbar covers the width of the viewport.
        - Click on 'Kitchen.' icon on the left to see that it links to the home page.
        - Click on the 'Home' link to see that it links to the home page.
        - Click on the 'Recipies' link to see that it links to the recipies page.
        - Click on the 'Sign Up' link to see that it links to the sign up page.
        - Click on the 'Sign In' link to see that it links to the sign in page.
        - **When Signed in as regular user:* Click on 'Add Recipe' link to see that it links to the add recipe page.
        - **When Signed in as regular user:* Click on 'Profile' link to see that it links to the profile page.
        - **When Signed in as regular user:* Click on 'Log Out' link to see that it removes the session user cookie
        and redirects the user to the 'Sign In' page.
        - **When Signed in as Admin user:* Click on 'Add Recipe' link to see that it links to the add recipe page.
        - **When Signed in as Admin user:* Click on 'Profile' link to see that it links to the profile page.
        - **When Signed in as Admin user:* Click on 'Manage Categories' link to see that it links to the manage 
        categories page.
        - **When Signed in as Admin user:* Click on 'Log Out' link to see that it removes the session user cookie
        and redirects the user to the 'Sign In' page.

    - Main Content:
        - Make sure that the main content fits the entire viewport without any white gaps, including:
            - Hero image
            - blue and red boxes
            - 'Pick a category' section

        - Click on 'Sign Up' button in the red box to see that it links to the sign up page.
        - Make sure every category image is displaying.
        - Click on the 'Chicken' category image to see that it links to the chicken category page.
        - Click on the 'Fish' category image to see that it links to the fish category page.
        - Click on the 'Meat' category image to see that it links to the meat category page.
        - Click on the 'Vegetarian' category image to see that it links to the vegetarian category page.

    - Footer:
        - Make sure footer is covering the width of the viewport.
        - Make sure copyright text is displaying
        - Click on 'Facebook' icon to see that it links to facebook.com
        - Click on 'Instagram' icon to see that it links to instagram.com
        - Click on 'Twitter' icon to see that it links to twitter.com
        - Click on 'Youtube' icon to see that it links to youtube.com

2. **Recipies Page**
    - Navbar:
        - Make sure navbar covers the width of the viewport.
        - Click on 'Kitchen.' icon on the left to see that it links to the home page.
        - Click on the 'Home' link to see that it links to the home page.
        - Click on the 'Recipies' link to see that it links to the recipies page.
        - Click on the 'Sign Up' link to see that it links to the sign up page.
        - Click on the 'Sign In' link to see that it links to the sign in page.
        - **When Signed in as regular user:* Click on 'Add Recipe' link to see that it links to the add recipe page.
        - **When Signed in as regular user:* Click on 'Profile' link to see that it links to the profile page.
        - **When Signed in as regular user:* Click on 'Log Out' link to see that it removes the session user cookie
        and redirects the user to the 'Sign In' page.
        - **When Signed in as Admin user:* Click on 'Add Recipe' link to see that it links to the add recipe page.
        - **When Signed in as Admin user:* Click on 'Profile' link to see that it links to the profile page.
        - **When Signed in as Admin user:* Click on 'Manage Categories' link to see that it links to the manage 
        categories page.
        - **When Signed in as Admin user:* Click on 'Log Out' link to see that it removes the session user cookie
        and redirects the user to the 'Sign In' page.
        
    - Main Content:
        - Make sure that the main content fits the entire viewport without any white gaps, including:
            - Hero image.
            - 'Pick a category' section.
            - 'All Recipies' section.
        - Make sure the search function is working by typing in a test word of 'Pasta'.
            - If recipe: The 'All Recipies' section displays all recipies that include the word pasta in either the
            ingredient list or the preparation steps.
        - Make sure the search function is working when no recipe is found by typing in the word 'Nej'.
            - No recipe during the testing of this site includes the word no, 
            so therefore the 'All recipies' section displays a red text saying
            ' No recipies found, try searching for something else'.
        - Click on 'Reset' button in the search section to see that it links back to all recipies displaying.
        - Click on the 'Chicken' category image to see that it links to the chicken category page.
        - Click on the 'Fish' category image to see that it links to the fish category page.
        - Click on the 'Meat' category image to see that it links to the meat category page.
        - Click on the 'Vegetarian' category image to see that it links to the vegetarian category page.
        - Make sure all recipies are showing when first visiting the page but also after clicking the 'Reset' button
        in the search function.
        - Make sure the following content is displaying in each recipe card:
            - Recipe image.
            - Name of recipe.
            - Category of the recipe.
            - The time to prepare the recipe.
            - Link to the recipe.
            - When image link is broken, a default image shows.
        - Click on recipe link to see that it links to the selected recipe page.

    - Footer:
        - Make sure footer is covering the width of the viewport.
        - Make sure copyright text is displaying
        - Click on 'Facebook' icon to see that it links to facebook.com
        - Click on 'Instagram' icon to see that it links to instagram.com
        - Click on 'Twitter' icon to see that it links to twitter.com
        - Click on 'Youtube' icon to see that it links to youtube.com

3. **Sign Up Page**
    - Navbar:
        - Make sure navbar covers the width of the viewport.
        - Click on 'Kitchen.' icon on the left to see that it links to the home page.
        - Click on the 'Home' link to see that it links to the home page.
        - Click on the 'Recipies' link to see that it links to the recipies page.
        - Click on the 'Sign Up' link to see that it links to the sign up page.
        - Click on the 'Sign In' link to see that it links to the sign in page.
        - **When Signed in as regular user:* Click on 'Add Recipe' link to see that it links to the add recipe page.
        - **When Signed in as regular user:* Click on 'Profile' link to see that it links to the profile page.
        - **When Signed in as regular user:* Click on 'Log Out' link to see that it removes the session user cookie
        and redirects the user to the 'Sign In' page.
        - **When Signed in as Admin user:* Click on 'Add Recipe' link to see that it links to the add recipe page.
        - **When Signed in as Admin user:* Click on 'Profile' link to see that it links to the profile page.
        - **When Signed in as Admin user:* Click on 'Manage Categories' link to see that it links to the manage 
        categories page.
        - **When Signed in as Admin user:* Click on 'Log Out' link to see that it removes the session user cookie
        and redirects the user to the 'Sign In' page.

    - Main Content:
        - Make sure the background image covers the whole viewport without any white gaps.
        - Make sure the 'Sign Up' section is centered
        - Make sure the content inside the 'Sign Up' section is displaying and centered.
        - Click on the 'Username' input field to make sure the text you write diplays.
        - Click on the 'Password' input field to make sure the text you write diplays.
        - When writing less than 5 letters in the 'Username' input field the line under the input fields turns red.
        - When trying to write more than 15 letters in the 'Username' input field, the typing input stops.
        - When writing less than 5 letters in the 'Password' input field the line under the input fields turns red.
        - When trying to write more than 15 letters in the 'Password' input field, the typing input stops.
        - Click on the 'Sign Up' button when no input fields are typed in:
            - The page encourages the user to fill in the required fields.
        - Click on the 'Sign Up' button when username already exists:
        - The page displays a flash message that says 'Username already exists!'.
        - Click on the 'Sign Up' button when a new username and password is typed in:
            - Page signes user in and redirects user to the profile page.
        -Click on the 'Click here to sign in!' text to see that it links to the sign in page.        

    - Footer:
        - Make sure footer is covering the width of the viewport.
        - Make sure copyright text is displaying
        - Click on 'Facebook' icon to see that it links to facebook.com
        - Click on 'Instagram' icon to see that it links to instagram.com
        - Click on 'Twitter' icon to see that it links to twitter.com
        - Click on 'Youtube' icon to see that it links to youtube.com
    
 
## Bugs found
- **Not Solved** Not able to make select elements required in the forms when adding a recipe. 
Materialize applies a custom CSS on all select elements which makes the 'required' attributes not working on 
unordered lists. Even though this is covered in the Mini Project that this project is based upon, the code provided
there didn't work for me when I tried it out. I therefor decided to leave this bug to hopefully solve it in the
future, but for now I decided to put a red **'*'** mark next to the fields I wanted to be required to
show the user that the fields are required after all.
<div align="center">
    <img src="static/img/required.jpg" alt="Add category form" width="600px">
    <br>
    The red required mark next to the fields that are required.
    <br>
    <br>
</div>

- **Solved** When getting the data for the ingredients and preparation steps the text was formatted like following:
"['put on the tap,\r\nput the glass under the tap']"
To Solve this I decided to change the ingredients and prepsteps from displaying in array format into string format.
After that it was a lot easier to split the ingredients after each comma and present them on a row each.
I added a jinja for loop in the select_recipe html code to iterate through the ingredients and prepsteps. 

- **Solved** The categories would not display on the index page. Caused by a misunderstanding in the code from my side.
I thought I could just reuse the category code from the categories.html page, but I also had to put the categories variable in the home page
route for the categories to be able to show.

- **Solved** When searching for a recipe the categories would disappear. I solved this one by deleting the search
function entirely and redo it to try to understand the logic of it better. It turned out I did not apply the 
variable for the categories, so therefor they would not display when searching. After adding the variable the search
function worked without any issues.

- **Solved** When a user don't have recipies added, their profile page would not fill out completely causing a 
white gap between the recipe section and the footer. Originally my
idea to solve this bug was to put in an else statement in my jinja code for the profile page with a text displaying
when no recipies was to be found. However this caused even more bugs when adding the else statement due to the limitation
of jinja. I decided to change my solution and add a min-height of the recipe section that would automatically fill out the page
with the sections default background color to remove the white gap completely. 
Not the most ultimate solution, but it works for now.

- **Solved** Though it's required to add an img url when you add a recipe, the images would show a broken link if the
url was not from the correct source. To solve this bug I added an onerror attribute with a value that would automatically
replace the broken image link with a default image.

- **Not Solved** When deleting a recipe from the profile page, the user gets redirected to the 'get_recipies' page
instead of staying on the profile page after deleting. Due to lack of time this bug will have to remain to be solved
in the future.