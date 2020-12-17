# Testing

## Content

## Automated Testing

## Manual Testing

## User Testing
    
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