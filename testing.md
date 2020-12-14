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
</div>
<br>
<br>
- **Solved** When getting the data for the ingredients and preparation steps the text was formatted like following:
"['put on the tap,\r\nput the glass under the tap']"
To Solve this I decided to change the ingredients and prepsteps from displaying in array format into string format.
After that it was a lot easier to split the ingredients after each comma and present them on a row each.
I added a jinja for loop in the select_recipe html code to iterate through the ingredients and prepsteps. 
<br>
<br>
- **Solved** The categories would not display on the index page. Caused by a misunderstanding in the code from my side.
I thought I could just reuse the category code from the categories.html page, but I also had to put the categories variable in the home page
route for the categories to be able to show.
<br>
<br>
- **Not Solved** When searching for a recipe the categories disappear.
<br>
<br>
- **Not Solved** When a user don't have recipies added, profile page will not fill out completely.