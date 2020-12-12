# Testing

## Content

## Automated Testing

## Manual Testing

## User Testing
    
## Bugs found
- **Not Solved** Not able to make required fields in form 
- **Solved** When getting the data for the ingredients and preparation steps the text was formatted like following:
"['put on the tap,\r\nput the glass under the tap']"
To Solve this I decided to change the ingredients and prepsteps from displaying in array format into string format.
After that it was a lot easier to split the ingredients after each comma and present them on a row each.
I added a jinja for loop in the select_recipe html code to iterate through the ingredients and prepsteps. 
- **Solved** The categories would not display on the index page. Caused by a misunderstanding in the code from my side.
I thought I could just reuse the category code from the categories.html page, but I also had to put the categories variable in the home page
route for the categories to be able to show.
- **Not Solved** When searching for a recipe the categories disappear.
- **Not Solved** When a user don't have recipies added, profile page will not fill out completely.