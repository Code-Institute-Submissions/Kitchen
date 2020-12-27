# Testing
## Content
1. [User Testing](#user-testing)
2. [Validator testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python)
3. [Manual Testing](#manual-testing)
    - [Home Page/Index Page](#home-page)
    - [Recipes Page](#recipes-page)
    - [Selected Recipe Page](#selected-recipe-page)
    - [Sign Up Page](#sign-up-page)
    - [Sign In Page](#sign-in-page)
    - [Add Recipe Page (regular user and admin user)](#add-recipe-page)
    - [Profile Page (regular user and admin user)](#profile-page)
    - [Selected Category Page](#selected-category-page)
    - [Manage Categories Page](#manage-categories-page)
    - [Add category Page (admin user only)](#add-category-page)
    - [Edit category Page (admin user only)](#edit-category-page)
    - [Edit recipe Page](#edit-recipe-page)
    - [Error 404 Page](#error-404-page)
    - [Error 500 Page](#error-500-page)
    - [Testing on phone and tablet devices](#testing-on-phone-and-tablet-devices)
4. [Bugs Found](#bugs-found)

## User Testing
1. **Get inspired into learning new recipes.**
    - This page was designed with the idea to look as realistic as possible (from a beginner's point of view). 
    This, to both encourage and inspire the user to scroll through all different kinds of recipes.
    - High-quality images are used throughout the site to increase the user experience to the max.
    - All recipes are authentic. (All authors are credited in the [README.md](README.md) file)

2. **Browse different categories for easier navigation of what kind of recipe I want to cook.**
    - The different categories are displayed on the following pages for the user to navigate to:
        - Home Page 
        - Recipes Page
    - The categories hheve its own category image that represents the content behind the category itself. 
    This to make it easy to identify the category before reading the name of it.
    - When clicking on each category the category image acts as the hero image on the selected category page, 
    to also indicate which category is currently viewed.

3. **Be able to sign up and share my own recipes.**
    - When the user first visits the page he/she is prompted to press the blue button in the red section right under the hero image
    to sign up for the page.
    - The user can also sign up by pressing the 'Sign Up' button in the navigation bar at the top.
    - The appearance of the 'Sign Up' button is consistent throughout the site, with its blue color and white text.
    - When the user is signed in, the button text in the red section changes to 'Add Recipe' to encourage the user
    to share a recipe.
    - The user can also click on the link in the navigation bar with the text 'Add Recipe' to get to the page to add
    a recipe.

4. **Have a good overlook of my own recipes that I've made.**
    - On the user's profile page, all the user's recipes are listed right under the hero image of the page.
    - When the user doesn't have any recipes made the recipes section will fill out with a blue color to indicate
    that the list is empty.

5. **Be able to edit and delete recipes that I have made.**
    - On each user recipe card there are two buttons displayed that only the logged-in user can se:
        - A red 'Delete' button. 
        - A blue 'Edit' button.
    - The user can edit and delete their recipes on the following pages:
        - Profile Page:
            - On the profile page, the user has better access to the recipes he/she has written. From here the
            user can both delete and edit each recipe.
        - Recipes Page:
            - The user is also able to delete and edit their recipes from the Recipes Page, however, when a lot of
            recipes are displaying, and not only by the user in session, the user has to scroll through all of them
            in the order that the recipe was made and without any type of relevance.
        - Selected Category page.
            - The same rules apply on this page as on the Recipes page mentioned above.

6. **To be able to search for recipes with a specific name or ingredient in them.**
    - The search function on the 'Recipes' page makes it possible for the user to search for a recipe with a 
    specific ingredient in it or with a specific name. You can search for multiple search words at a time which makes
    it easier to find what you are looking for.

## Validator Testing
### HTML
All html templates (except for the 404.html, 500.html, profile.html and base.html) were tested using 
[W3C Markup Validation Service](https://validator.w3.org/) by Validate by URI. 
This, to not cause any errors by the Jinja templates that were used in this project, since that would be expected.
The errors that occurred was the following:
1. Alt attribute missing on recipe images in recipes.html.
    - This error was corrected by adding the alt attribute.
2. Alt attribute missing on recipe images in select_category.html.
    - This error was corrected by adding the alt attribute.
3. < hr > tag not allowed as a child of < ol > in select_recipe.html.
    - This error was corrected by putting the < hr > inside the list elements of the preparation steps instead.

The 404.html, 500.html, profile.html and base.html had to be tested with 'Validate by Direct Input'. 
The errors that occurred was 
caused by the Jinja templates that were used. These errors were expected to occur and did not lead to any 
changes in the code itself since it would break the site.

### CSS
The CSS was tested by using [Jigsaw CSS Validation Service](https://jigsaw.w3.org/css-validator/). The CSS passed the test
without any errors.

### JavaScript
The JavaScript was tested using [JSHint](https://jshint.com/). The error that occurred was the following:
- One undefined variable. ($)
    - This however could not lead to any change of the code, since it would break the jQuery.

### Python
The Python code was tested using [PEP8](http://pep8online.com/). When testing my **env.py** file the following error
occurred:
- E501 line too long (106 > 79 characters)
    - This was caused by the MONGO_URI line being too long. This however could not lead to any change of the code, 
    since it would break the MONGO_URI itself.
<br>
<br>

The **app.py** passed the test without any errors in it.

## Manual Testing
All manual tests were done in the following browsers:
- Firefox
- Google Chrome
- Microsoft Edge

### Home Page
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Sign Up' link to see that it links to the sign-up page.
    - Click on the 'Sign In' link to see that it links to the sign in page.
    - When Signed in as a regular user: Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - When Signed in as a regular user: Click on the 'Profile' link to see that it links to the profile page.
    - When Signed in as a regular user: Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
    - When Signed in as Admin user: Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - When Signed in as Admin user: Click on the 'Profile' link to see that it links to the profile page.
    - When Signed in as Admin user: Click on the 'Manage Categories' link to see that it links to the manage 
    categories page.
    - When Signed in as Admin user: Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.

- Main Content:
    - Make sure that the main content fits the entire viewport without any white gaps, including:
        - Hero image
        - blue and red boxes
        - 'Pick a category' section
    - Click on the 'Sign Up' button in the red box to see that it links to the sign-up page.
        - (Click on the 'Add Recipe' in the red box if a user is already signed in.)
    - Make sure every category image is displaying.
    - Click on the 'Chicken' category image to see that it links to the chicken category page.
    - Click on the 'Fish' category image to see that it links to the fish category page.
    - Click on the 'Meat' category image to see that it links to the meat category page.
    - Click on the 'Vegetarian' category image to see that it links to the vegetarian category page.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

### Recipes Page
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Sign Up' link to see that it links to the sign-up page.
    - Click on the 'Sign In' link to see that it links to the sign-in page.
    - When Signed in as a regular user: Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - When Signed in as a regular user: Click on the 'Profile' link to see that it links to the profile page.
    - When Signed in as a regular user: Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
    - When Signed in as Admin user: Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - When Signed in as Admin user: Click on the 'Profile' link to see that it links to the profile page.
    - When Signed in as Admin user: Click on the 'Manage Categories' link to see that it links to the manage 
    categories page.
    - When Signed in as Admin user: Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
        
- Main Content:
    - Make sure that the main content fits the entire viewport without any white gaps, including:
        - Hero image.
        - 'Pick a category' section.
        - 'All Recipes' section.
    - Make sure the search function is working by typing in a test word of 'Pasta'.
        - If recipe: The 'All Recipes' section displays all recipes that include the word pasta in either the
        ingredient list or the preparation steps.
    - Make sure the search function is working when no recipe is found by typing in the word 'Nej'.
        - No recipe during the testing of this site includes the word no, 
        so therefore the 'All recipes' section displays a red text saying
        'No recipes found, try searching for something else'.
    - Click on the 'Reset' button in the search section to see that it links back to all recipes displaying.
    - Click on the 'Chicken' category image to see that it links to the chicken category page.
    - Click on the 'Fish' category image to see that it links to the fish category page.
    - Click on the 'Meat' category image to see that it links to the meat category page.
    - Click on the 'Vegetarian' category image to see that it links to the vegetarian category page.
    - Make sure all recipes are showing when first visiting the page but also after clicking the 'Reset' button
    in the search function.
    - Make sure the following content is displaying in each recipe card:
        - Recipe image.
        - Name of the recipe.
        - Name of the user who made the recipe.
        - Category of the recipe.
        - The time to prepare the recipe.
        - Link to the recipe.
            - When clicked on the user is redirected to the selected recipes page.
        - When an image link is broken, a default image shows.
    - Click on the recipe link to see that it links to the selected recipe page.
    - If a user is logged in, make sure the 'Delete' and 'Edit' buttons are displaying in the recipe card over the recipe link.
        - Click on 'Delete' button and a modal pops up asking the user if they are sure about deleting the recipe.
            - Click 'No' and the user is redirected back to the recipes page.
            - Click 'Yes' and the recipe gets deleted, redirecting the user back to the recipes page with a flash
            message saying "Recipe Deleted!".
        - Click on the 'Edit' button and the user is redirected to the 'Edit Recipe' page.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

### Selected Recipe Page
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page. (When logged in as regular user or admin)
    - Click on the 'Profile' link to see that it links to the profile page. (When logged in as regular user or admin)
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page. (When logged in as regular user or admin)
    - Click on the 'Manage Categories' link to see that it links to the manage categories page. (When logged in as admin)
    - Click on the 'Sign Up' link to see that it links to the sign-up page. (When not logged in)
    - Click on the 'Sign In' link to see that it links to the sign-in page. (When not logged in)

- Main Content:
    - Make sure the recipe image is displayed to the left on the same row as the red section with all recipe descriptions.
        - Make sure if the recipe image link is broken, a default image will display.
    - Make sure the red section with recipe details are containing the following:
        - Name of the recipe.
        - Name of the user who added the recipe.
        - Recipe category.
        - Preparation time.
    - Make sure the ingredients section is displaying all ingredients in an unordered list beginning each item
    with a check icon.
    - Make sure the preparation section is displaying each preparation step in an ordered list, dividing each step
    with a horizontal rule.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

### Sign Up Page
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Sign Up' link to see that it links to the sign-up page.
    - Click on the 'Sign In' link to see that it links to the sign-in page.

- Main Content:
    - Make sure the background image covers the whole viewport without any white gaps.
    - Make sure the 'Sign Up' section is centered
    - Make sure the content inside the 'Sign Up' section is displaying and centered.
    - Click on the 'Username' input field to make sure the text you write displays.
    - Click on the 'Password' input field to make sure the text you write displays.
    - When writing less than 5 letters in the 'Username' input field the line under the input fields turns red.
    - When trying to write more than 15 letters in the 'Username' input field, the typing input stops.
    - When writing less than 5 letters in the 'Password' input field the line under the input fields turns red.
    - When trying to write more than 15 letters in the 'Password' input field, the typing input stops.
    - Click on the 'Sign Up' button when no input fields are typed in:
        - The page encourages the user to fill in the required fields.
    - Click on the 'Sign Up' button when the username already exists:
    - The page displays a flash message that says 'Username already exists!'.
    - Click on the 'Sign Up' button when a new username and password is typed in:
        - Page signes user in and redirects user to the profile page.
    - Click on the 'Click here to sign in!' text to see that it links to the sign-in page.        

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

- Further testing:
    - If an already signed in user tries to get to the 'Sign Up' page they will be displayed
    with a flash message displaying "Please log out before signin up again!"

### Sign In Page
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Sign Up' link to see that it links to the sign-up page.
    - Click on the 'Sign In' link to see that it links to the sign-in page.

- Main Content:
    - Make sure the background image covers the whole viewport without any white gaps.
    - Make sure the 'Sign In' section is centered
    - Make sure the content inside the 'Sign In' section is displaying and centered.
    - Click on the 'Username' input field to make sure the text you write displays.
    - Click on the 'Password' input field to make sure the text you write displays.
    - When writing less than 5 letters in the 'Username' input field the line under the input fields turns red.
    - When trying to write more than 15 letters in the 'Username' input field, the typing input stops.
    - When writing less than 5 letters in the 'Password' input field the line under the input fields turns red.
    - When trying to write more than 15 letters in the 'Password' input field, the typing input stops.
    - Click on the 'Sign In' button when no input fields are typed in:
        - The page encourages the user to fill in the required fields.
    - Click on the 'Sign In' button when the wrong username:
    - The page displays a flash message that says 'The username doesn't exist! Please try again'.
    - Click on the 'Sign In' button when the correct username but the wrong password is typed in:
        - The page displays a flash message that says 'The Username and/or Password is incorrect!'.
    - Click on the 'Sign In' button when correct username and password:
        - A flash message displays on the page saying 'Hi there, < username >' and redirects the user to the profile page.
    - Click on the 'Click here to sign-up!' text to see that it links to the sign-up page.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

- Further testing:
    - If an already signed in user tries to get to the 'Sign In' page they will be displayed
    with a flash message displaying "You are already signed in in!"

### Add Recipe Page
### (regular user and admin user)
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - Click on the 'Profile' link to see that it links to the profile page.
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
    - When Signed in as Admin user: Click on the 'Manage Categories' link to see that it links to the manage 
    categories page.

- Main Content:
    - Make sure the 'Add Recipe' section is centered on the page.
    - Make sure all content inside the 'Add Recipe' is displaying.
    - 'Recipe Name' input:
        - Make sure the icon is displaying.
        - Make sure input gets marked in red when filled out with less than 4 letters.
        - Make sure input stops typing when trying to write more than 25 letters.
    - 'Category' options:
        - Make sure the icon is displaying.
        - Click on 'Choose category' and Make sure all categories are displaying in the options list.
        - *Bug noted when not choosing an option in the list. Please see 'Bugs Found' section further down.*
    - 'Preptime' options:
        - Make sure the icon is displaying.
        - Click on 'How long will it take' and Make sure all preparation times are displaying in the options list.
        - *Bug noted when not choosing an option in the list. Please see 'Bugs Found' section further down.*
    - Ingredients text area:
        - Make sure the icon is displaying.
        - Make sure the browser points out if the text area input is not filled out when submitting the recipe.
        *Bug noted of colored line not working correctly. Please see 'Bugs Found' section further down.*
    - Preparation steps text area:
        - Make sure the icon is displaying.
        - Make sure the browser points out if the text area input is not filled out when submitting the recipe.
        *Bug noted of colored line not working correctly. Please se 'Bugs Found' section further down.*
    - Img URL input:
        - Make sure the icon is displaying.
        - Make sure the browser points out if the field is not filled out when submitting the recipe.
    - 'Add Recipe' button:
        - Make sure that when the form is filled out correctly and the 'Add Recipe' button is clicked the page redirects
        to the 'Recipes' page with all recipes displaying including the newly added one at the bottom.
    - Make sure red text about required fields is showing.
- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

- Further testing:
    - If a user is not signed in and tries to get to the 'Add Recipes' page they will be displayed
    with a 404 message."

### Profile Page
### (regular user and admin user)
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - Click on the 'Profile' link to see that it links to the profile page.
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
    - When Signed in as Admin user: Click on the 'Manage Categories' link to see that it links to the manage 
    categories page.

- Main Content:
    - Make sure the hero image covers the width of the viewport.
    - Make sure the users' name is displaying in the blue section under the hero image.
    - Make sure that the users' recipes are displaying in the blue section under the users name with the following:
        - Image of each recipe.
        - Name of each recipe.
        - The name of the user who added the recipe.
        - The category of each recipe.
        - The preparation time of each recipe.
        - A 'Delete' button.
        - An 'Edit' button
        - A link to the selected recipe page.
            - When clicked on the page redirects to the selected recipe page.
        - Make sure that if img link is broken of a recipe a default image will display as the recipes' image.
    - Make sure that if the user has no recipes added yet the blue section fills out the page with a min-height of the view height.
    - Click on the 'Delete' button and a modal pops up asking the user if they are sure about deleting the recipe.
        - Click 'No' and the user is redirected back to the profile page.
        - Click 'Yes' and the recipe gets deleted, redirecting the user back to the recipes page with a flash
        message saying "Recipe Deleted!".
    - Click on the 'Edit' button and the user gets redirected to the edit recipe page.


- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

### Selected Category Page
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page. (When logged in as regular user or admin)
    - Click on the 'Profile' link to see that it links to the profile page. (When logged in as regular user or admin)
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page. (When logged in as regular user or admin)
    - Click on the 'Manage Categories' link to see that it links to the manage categories page. (When logged in as admin)
    - Click on the 'Sign Up' link to see that it links to the sign-up page. (When not logged in)
    - Click on the 'Sign In' link to see that it links to the sign-in page. (When not logged in)

- Main Content:
    - Make sure the hero image covers the width of the viewport, displaying the image of the chosen category.
        - If the image URL is broken, a default image will display.
    - Make sure category section is displaying the following:
        - Heading text.
        - 'All Recipes' button.
        - Category images.
        - Category names.
    - Make sure the category name is displayed in the recipes section.
    - Make sure that the category recipes are displaying in the blue section (if there are recipes within that
        category) under the category name with the following:
        - Image of each recipe.
        - Name of each recipe.
        - The name of the user who added the recipe.
        - The category of each recipe.
        - The preparation time of each recipe.
        - A 'Delete' button. (If signed in as the maker of the recipe)
            - Click on the 'Delete' button and a modal pops up asking the user if they are sure about deleting the recipe.
            - Click 'No' and the user is redirected back to the selected category page.
            - Click 'Yes' and the recipe gets deleted, redirecting the user back to the recipes page with a flash
            message saying "Recipe Deleted!".
        - An 'Edit' button. (If signed in as the maker of the recipe)
            - Click on the 'Edit' button and the user is redirected to the 'Edit Recipe' page.
        - A link to the selected recipe page.
            - When clicked on, the page redirects to the selected recipe page.
        - Make sure that if the image link is broken of a certain recipe added by the user, a default image will display
        as the recipes' image.
    - If no recipes are created yet, the recipe section is covered with light blue color with the view height of the
        device.
        - *Bug noted if no recipes are displaying. Please see 'Bugs Found' section further down*

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

### Manage Categories Page
### (admin user only)
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - Click on the 'Profile' link to see that it links to the profile page.
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
    - Click on the 'Manage Categories' link to see that it links to the manage 
    categories page.

- Main Content:
    - Make sure the heading text is displaying.
    - Make sure the 'Add Category' button is displaying and when clicked redirects the user to the 'Add Category' page.
    - Make sure all categories are displayed on the page with the following:
        - Category image.
        - Category name.
        - 'Delete' button.
        - 'Edit' button.
    - Make sure that if the image link is broken, a default image will display as the category image.
    - Click on the 'Delete' button and a modal pops up asking the user if they are sure about deleting the category.
        - Click 'No' and the user is redirected back to the 'Manage Categories' page.
        - Click 'Yes' and the category gets deleted, redirecting the user back to the 'Manage Categories' page with a flash
        message saying "Category Deleted!".
    - Click on the 'Edit' button and the user is redirected to the 'Edit Category' page.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

- Further testing:
    - If an unauthorized user tries to get to the 'Manage Categories' page they will be displayed
    with a 404 message."

### Add category Page
### (admin user only)
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - Click on the 'Profile' link to see that it links to the profile page.
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
    - Click on the 'Manage Categories' link to see that it links to the manage 
    categories page.

- Main Content:
    - Make sure content is centered to the page horizontally.
    - Make sure content is displaying the following:
        - Heading text.
        - Category Name input field with the icon.
        - Image URL input field with the icon.
        - 'Add Category' button.
        - Red text about the required fields.
    - Make sure if Category Name field doesn't get filled out or gets filled out with less than 3 letters when
        submitting the new category:
        - The line under the input field turns red.
        - The browser points out to the user to fill out the form correctly.
    - Make sure if Image URL field doesn't get filled out when submitting the new category:
        - The line under the input field turns red.
        - The browser points out to the user to fill out the form correctly.
    - Click on the 'Add Category' button when the form is filled out correctly and the page redirects to the 'Manage
     Categories' page displaying the new category at the bottom of the page.


- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

- Further testing:
    - If an unauthorized user tries to get to the 'Add Category' page they will be displayed with
    a 404 message."

### Edit category Page
### (admin user only)
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - Click on the 'Profile' link to see that it links to the profile page.
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
    - Click on the 'Manage Categories' link to see that it links to the manage 
    categories page.

- Main Content:
    - Make sure content is centered on the page horizontally.
    - Make sure content is displaying the following:
        - Heading text.
        - Category Name input field with the icon.
            - The current category name is displayed within the input field for the user to edit.
        - Image URL input field with the icon.
            - The current image url is displayed within the input field for the user to edit.
        - 'Cancel' button.
            - Click on the 'Cancel' button and the page redirects to the 'Manage Categories' page without saving the changes
            that were made to the category.
        - 'Edit Category' button.
            - Click on the 'Edit Category' button and the page redirects to the 'Manage Categories' page and displays the changes
            to the category that was edited.
        - Red text about the required fields.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

- Further testing:
    - If an unauthorized user tries to get to the 'Edit Category' page they will be displayed
    with a 404 message."


### Edit recipe Page
- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page.
    - Click on the 'Profile' link to see that it links to the profile page.
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page.
    - *When Signed in as Admin user:* Click on the 'Manage Categories' link to see that it links to the manage 
    categories page.

- Main Content:
    - Make sure the 'Edit Recipe' section is centered on the page.
    - Make sure all content inside the 'Add Recipe' is displaying.
    - 'Recipe Name' input:
        - Make sure the icon is displaying.
        - Make sure the current Name of the recipe is displaying for the user to edit.
        - Make sure input gets marked in red when filled out with less than 4 letters.
        - Make sure input stops typing when trying to write more than 25 letters.
    - 'Category' options:
        - Make sure the icon is displaying.
        - Make sure the current Category is displaying for the user to edit by selecting a new option when clicked on.
        - Click on 'Choose category' and Make sure all categories are displaying in the option list.
        - Make sure option cannot be left empty.
    - 'Preptime' options:
        - Make sure the icon is displaying.
        - Make sure the current Preptime is displaying for the user to edit by selecting a new option when clicked on.
        - Click on the current preptime and make sure all preparation times are displaying in the option list.
        - Make sure the option cannot be left empty.
    - Ingredients text area:
        - Make sure the icon is displaying.
        - Make sure the current ingredient list is displaying for the user to edit.
        - Make sure the browser points out if the text area input is not filled out when submitting the recipe.
        *Bug noted of colored line not working correctly. Please see 'Bugs Found' section further down.*
    - Preparation steps text area:
        - Make sure icon is displaying.
        - Make sure current preparation list is displaying for the user to edit.
        - Make sure browser points out if the text area input is not filled out when submitting the recipe.
        *Bug noted of colored line not working correctly. Please see 'Bugs Found' section further down.*
    - Img URL input:
        - Make sure the icon is displaying.
        - Make sure the current img url is displaying for the user to edit.
        - Make sure the browser points out if the field is not filled out when submitting the recipe.
    - 'Cancel' button:
        - Click on the 'Cancel' button and the page redirects to the 'Recipes' page displaying all recipes but
        without saving the changes that were made to the recipe.
    - 'Save' button:
        - Click on the 'Save' button after the form is filled out correctly the page stays on the
        'Edit Recipe' page but with a flash message displaying at the top saying: "Recipe Edited!"
    - Make sure red text about required fields is showing.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

- Further testing:
    - If an unauthorized user tries to get to the 'Edit Recipe' page for a recipe they did not create
    they will be displayed with a 404 message."

### Error 404 Page
To test the 404 error page I simply added a random letter to the url for the page that I knew would not exist. This
method could be applied to all pages of the site to test the 404 error function.

- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link to see that it links to the recipes page.
    - Click on the 'Add Recipe' link to see that it links to the add recipe page. (When logged in as regular user or admin)
    - Click on the 'Profile' link to see that it links to the profile page. (When logged in as regular user or admin)
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page. (When logged in as regular user or admin)
    - Click on the 'Manage Categories' link to see that it links to the manage categories page. (When logged in as admin)
    - Click on the 'Sign Up' link to see that it links to the sign-up page. (When not logged in)
    - Click on the 'Sign In' link to see that it links to the sign-in page. (When not logged in)

- Main Content:
    - Make sure the background image covers the whole viewport without any white gaps.
    - Make sure the 'Oops' message section is centered.
    - Make sure the content inside the 'Oops' message section is displaying and centered including:
        - A description of what the error is about.
        - A link the user can click on to get back to the home page.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

### Error 500 Page
To test the 500 error page, when an internal service error occur, I did the following:
- Changed debug mode in the app.py to **False**.
- Changed the name of the 'recipes.html' page to 'recipess.html'
This would cause the 500 error page to appear every time I tried to reach the recipes page. This could be applied to
all pages of the site to test the 500 error function.
When on the 500 error page:

- Navbar:
    - Make sure the navbar covers the width of the viewport.
    - Click on the 'Kitchen.' icon on the left to see that it links to the home page.
    - Click on the 'Home' link to see that it links to the home page.
    - Click on the 'Recipes' link. *Due to the testing, the page would redirect to the same 500 error page*
    - Click on the 'Add Recipe' link to see that it links to the add recipe page. (When logged in as regular user or admin)
    - Click on the 'Profile' link to see that it links to the profile page. (When logged in as regular user or admin)
    - Click on the 'Log Out' link to see that it removes the session user cookie
    and redirects the user to the 'Sign In' page. (When logged in as regular user or admin)
    - Click on the 'Manage Categories' link to see that it links to the manage categories page. (When logged in as admin)
    - Click on the 'Sign Up' link to see that it links to the sign-up page. (When not logged in)
    - Click on the 'Sign In' link to see that it links to the sign-in page. (When not logged in)

- Main Content:
    - Make sure the background image covers the whole viewport without any white gaps.
    - Make sure the 'Oops' message section is centered.
    - Make sure the content inside the 'Oops' message section is displaying and centered including:
        - A description of what the error is about.
        - A link the user can click on to get back to the home page.

- Footer:
    - Make sure the footer is covering the width of the viewport.
    - Make sure the copyright text is displaying
    - Click on the 'Facebook' icon to see that it links to facebook.com
    - Click on the 'Instagram' icon to see that it links to instagram.com
    - Click on the 'Twitter' icon to see that it links to twitter.com
    - Click on the 'Youtube' icon to see that it links to youtube.com

To go back to the original state of the page I put the debug mode to **True** and changed back the 'recipess.html'
page to the original name of 'recipes.html'.
The first time this test was applied the page got stuck on the 500 error page despite doing a hard refresh of the page. 
To solve this issue I had to clear the cache and cookies for the site.

### Testing on phone and tablet devices
All of the tests mentioned above were also made on the following devices using the developer tool on Google Chrome:
- iPad
- iPad Pro
- iPhone 5/SE
- iPhone 6/7/8
- Galaxy S5

With additional testing on all the above devices:
- Make sure the menu collapse on phone and tablet devices (not on iPad PRO though).
- Make sure the side navigation menu appears to the left by clicking the trigger button to the left in the navigation bar.
- Make sure the copyright text and social icons in the footer get their own rows covering the whole 
width of the page on smaller devices.

Further testing was made on the following pages:

#### Home Page
- Make sure the content of the page fits the device nicely.
    - *Bug noted of a gap in category section. Please see 'Bugs Found' section further down.*
- Make sure the text gets smaller to fit the device better.
- Make sure the blue box and red box gets their own rows covering the whole width of the page.
- Make sure category images get smaller on smaller devices to fit the device nicely.
- Make sure categories are displayed with a maximum of two on each row in the category section on phone devices and
a maximum of three on the iPad device (not PRO).

#### Recipes page
- Make sure the hero image covers the width of the viewport.
- Make sure category images get smaller on smaller devices to fit the device nicely.
- Make sure categories are displayed with a maximum of two on each row in the category section on phone devices and
a maximum of three on iPad device (not PRO).
- Make sure recipes are displayed with a maximum of one on each row on phone devices, two on iPad and three 
on iPad PRO.
- Make sure the recipe section fills out the entire vh if no recipes/ or a few recipes are displayed when searching.
    - *Bug noted. Please see 'Bugs Found' section further down.*

#### Selected Recipe Page
- Make sure the recipe image gets its own row and covers the width of the viewport.
- Make sure the red section with the recipe description gets its own row and covers the width of the viewport.
- Make sure heading text size is adapted to phone devices.
- Make sure the ingredients list gets its own row.
- Make sure the preparation step list gets its own row presented after the ingredient list.

#### Profile Page (regular user and admin user)
- Make sure the hero image covers the width of the viewport.
- Make sure recipes are displayed with a maximum of one on each row on phone devices, two on iPad and three 
on iPad PRO. 
- Make sure the recipe section fills out the entire vh if no recipes/ or a few recipes are displayed.
    - *Bug noted. Please see 'Bugs Found' section further down.*

#### Selected Category Page
- Make sure the hero image covers the width of the viewport.
- Make sure heading text and button text gets smaller on phone devices.
- Make sure category images get smaller on smaller devices to fit the device nicely.
- Make sure categories are displayed with a maximum of two on each row in category section on phone devices and
a maximum of three on iPad device (not PRO).
- Make sure recipes are displayed with a maximum of one on each row on phone devices, two on iPad and three 
on iPad PRO.

#### Manage Categories Page (admin user only)
- Make sure categories are displayed with a maximum of two on each row in category section on phone devices and
a maximum of three on iPad devices.

## Bugs found
- **Not Solved** Not able to make select elements required in the forms when adding a recipe. 
Materialize applies a custom CSS on all select elements which makes the 'required' attributes not working on 
unordered lists. Even though this is covered in the Mini Project that this project is based upon, the code provided
there didn't work for me when I tried it out. I therefore decided to leave this bug to hopefully solve it in the
future, but for now I decided to put a red mark next to the fields I wanted to be required to
show the user that the fields are required after all. When a user wants to add a recipe or edit a recipe and the options
sections get left out empty, the browser does not point this out correctly.

- **Solved** When getting the data for the ingredients and preparation steps the text was formatted as following:
"['put on the tap,\r\nput the glass under the tap']"
To Solve this I decided to change the ingredients and prepsteps from displaying in array format into string format.
After that, it was a lot easier to split the ingredients after each comma and present them on a row each.
I added a jinja for loop in the select_recipe html code to iterate through the ingredients and prepsteps. 

- **Solved** The categories would not display on the index page. Caused by a misunderstanding in the code from my side.
I thought I could just reuse the category code from the categories.html page, but I also had to put the categories variable in the home page
route for the categories to be able to show.

- **Solved** When searching for a recipe the categories would disappear. I solved this one by deleting the search
function entirely and redo it to try to understand the logic of it better. It turned out I did not apply the 
variable for the categories, so therefore they would not display when searching. After adding the variable to the search
function worked without any issues.

- **Not Solved** When a user doesn't have recipes added, their profile page would not fill out completely causing a 
white gap within the recipe section until the footer area. Originally my
idea to solve this bug was to put in an else statement in my Jinja code for the profile page with a text displaying
"No recipes found!" when no recipes were to be found. 
However, this caused even more bugs when adding the else statement by looping the text endlessly all over the 
page even if there were recipes there or not.
As Explained by tutor support, this was apparently a limitation with Jinja templating, so to solve this problem I 
would have to do it from my python code. Because of my limitation of knowledge in python (and lack of time) it 
led me to do an emergency solution for this bug by adding a min-height of the recipe section that 
would automatically fill out the view height with the blue background color on all devices.
This however is causing a pretty large blue empty area at the page, but at least there are no white gaps on the page.
This is something I will have to try to solve in the future, when more knowledge in python is found.
The min view height does also affect when searching for a recipe on the 'Recipes' page and when visiting a 
selected category page that doesn't have any recipes yet. When no recipes are to
display, the blue background covers the page with a min of the view height for the device. 
The search function does however also provide a red text displaying when no recipes are found.

<div align="center">
    <img src="/readme-img/bug1.png" alt="Profile bug" width="600px">
    <br>
    Bug on Profile page when no user recipes.
    <br>
    <br>
</div>

- **Solved** Though it's required to add an image url when you add a recipe, the images would show a broken link if the
url was not from the correct source. To solve this bug I added an onerror attribute with a value that would automatically
replace the broken image link with a default image.

- **Not Solved** When deleting a recipe from the profile page, the user gets redirected to the 'get_recipes' page
instead of staying on the profile page after deleting. Due to lack of time this bug will have to remain to be solved
in the future.

- **Not Solved** When editing a recipe from the profile page, and the user clicks on the 'Cancel' button the user 
gets redirected to the 'get_recipes' page instead of staying on the profile page after clicking on 'Cancel'. 
Due to lack of time this bug will have to remain to be solved in the future.

- **Not Solved** When not filling out the text areas that are required when adding/editing a recipe the line under the
text input doesn't change to a red color due to a Materialize bug. However if not filling out the text area when submitting
a recipe still makes the browser point out to fill the required field in.

- **Not Solved** When a category gets edited, the recipes within that category will not automatically change to the
edited category. The recipes will still have the old category name displayed which makes it impossible to reach them within
the select category function. As soon as the name for the edited category got changed back or a new category with that
particular name was created, the recipes could be reached.

- **Not Solved** When inspecting the home page in the developer tool a gap under the category section when 
viewing the page from an iPad Pro perspective would appear. I guess this has to do with the fact that the iPad PRO 
vh is larger than what my site is designed for. To solve this I would have to add more content to the page
to fill the gap out. The best would be to be able to target only the iPad PRO perspective, but since that is out
of my knowledge the bug remains unsolved.

- **Not Solved** When inspecting the site from an iPad perspective the categories are displaying with a maximum of 
three on each row. When testing the site I had a total of four categories. This would cause the fourth category to take up
a new row, displayed to the left.
An ideal solution for this would be to make that fourth category display in the center of that row, for a better balance.
Another solution would be to implement some kind of pagination, to make the user scroll through the categories vertically
on the same row. This however is out of my knowledge at the moment, and due to lack of time I will have to solve this one
in the future.

<div align="center">
    <img src="/readme-img/bug2.png" alt="Profile bug" width="600px">
    <br>
    Bug in categories section when viewed on tablet device.
    <br>
    <br>
</div>

- **Not Solved** When viewing the 'Sign Up' page and 'Sign In' page from my iPhone, the background image doesn't cover 
the view height properly. However, when viewing the pages on my Google Chrome developer tool the background image
works properly. When trying to search for a solution on this bug it seems like iOS is not supporting fixed 
background images. Despite research I have not yet come up with a solution for this bug.

- **Not Solved** When selecting a preptime when editing or adding a recipe, the options do not display in 
the increasing logic order they should be. The '< 30' option is displaying right before the '> 60' option instead of
displaying as the first option. Due to lack of time, this bug remains.