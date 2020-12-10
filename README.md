# Kitchen
## Content

## About
Kitchen is a website where food enthusiasts from all over the world can gather to share their best recipes.
With the simple functions, it is easy for everyone to create an account to get started sharing their best 
cooking tricks, and in the future we hope to be able to offer more functions to make the stay on the website 
even easier.
If you're not interested in signing up and share a recipe, you can ofcourse visit the site to brows through all
the fantastic recipies for some cooking inspiration.

## UX
### UX goals
The UX goals for this website are the following:
- Simple design with a fixed navigation bar at the top.
- Clear sections of the content of each page.
- The site is responsive to all devices.
- All text on the site is easy to read without any distacting backgrounds.


### User Stories
As a user I want to:
- Get inspired into learning new recipes.
- Browse different categories for easier navigation of what kind of recipe I want to cook.
- Be able to sign up and share my own recipies.
- Have a good overlook of my own recipies that I've made.
- Be able to edit and delete recipies that I have made.

### Design process
The **structure** of the site is based upon the data that is presented on the page. I wanted the first page to be simple
and clear for the visitor which then by deciding what content they want to visit navigates through the navigation
bar at the top to get to that specific content.

This recipe site has four collections in the MongoDB database where the main content presented on the paige is 
stored.

- Recipies
- Categories
- Preptime
- Users

### Wireframes
The **skeleton** plane is defined in the structure of the wireframes for this project.
The wireframes where made with the technology of Figma and can be viewed 
[here](https://www.figma.com/file/aCMvZLULq29HaO6xSANTzr/MS3?node-id=273669%3A448).

<div align="center">
    <img src="static/img/wireframe1.png" alt="wireframe 1" width="600px">
    <br>
    Home and Recipies pages.
</div>
<br>
<br>
<div align="center">
    <img src="static/img/wireframe2.png" alt="wireframe 2" width="600px">
    <br>
    Inside Category and Sign Up pages.
</div>
<br>
<br>
<div align="center">
    <img src="static/img/wireframe3.png" alt="wireframe 3" width="600px">
    <br>
    Inside Recipe and Profile pages.
</div>
<br>
<br>
<div align="center">
    <img src="static/img/wireframes-mobile.png" alt="wireframe 3" width="600px">
    <br>
    Wireframes for mobile devices.
</div>
<br>
<br>

## Features
The features of the site was defined during the scope plane stage and all but one features from the original idea
was applied to this project.

The features of this web site are:

### All Pages:
- Fixed Navigation bar at the top of all pages. Complete list of links in the navbar:
    - **Logo** - Linked to home page.
    - **Home** - Linked to home page.
    - **Recipies** - linked to recipe page.
    - **Add Recipe** - Linked to page where the user can add recipe.
    - **Manage Categories** - Linked to a page where admin can manage categories.
    - **Profile** - Linked to the profile page of the user.
    - **Sign In** - Linked to page where user can sign in.
    - **Sign Up** - Linked to page where new user can sign up.
    - **Log Out** - Logges user out of the site.

- Footer with copyright text and social links.

<div align="center">
    <img src="static/img/navbar.png" alt="Navbar feature" width="600px">
    <br>
    The Navbar with the different links depending on if you are logged in or not, an admin or not.
</div>
    
### Home Page:
- Hero image with a welcome text.
- A blue section with brief information about the page.
- A red box with a heading text that encourages the visitor to add a recipe and button 
(depending on if the user is logged in or not)
- A section with recipe categories that includes:
    - Image of the category.
    - Name of the category

<div align="center">
    <img src="static/img/infobox.png" alt="Info boxes" width="600px">
    <br>
    Navbar    
</div>

### Recipes Page:
- Hero image.
- A section with recipe categories that includes:
    - Image of the category.
    - Name of the category

- Section with all recipies

### Add Recipe Page:
- A form for the logged in user to add their recipe to. The form includes:
    - An input field to write the name of the recipe.
    - An option list to pick the category of the recipe.
    - An option list to pick the total preptime for the recipe.
    - A textarea to add all the ingredients of the recipe.
    - A textarea to add the preparation steps of the recipe.
    - An input field to add a image url for the recipe image that is to be used.
    - A button to submit the recipe.

### Manage Categories Page:
This page can only be viewed by the admin user.
- A button that leads to a form to add a new category to the page.
- A section with the existing recipe categories that includes:
    - Image of the category.
    - Name of the category
    - Delete button, that deletes the category.
    - Edit button, that makes it possible to edit the image url or the name of the category.

<div align="center">
    <img src="static/img/addcategory.png" alt="Add category form" width="600px">
    <br>
    The form that makes it possible for the admin user to add a new category.    
</div>


### Features left to implement
- Timer that automatically logges you out if ur not active on the site.
- Search function. (Was in the original idea, but left out due to lack of time)

## Technologies used
### Languages
- HTML 5
- CSS3
- JQuery
- Python

### Libraries
- MongoDB
- Flask
- Materialize
- Fontawesome

### Technologies

## Testing

## Deployment

## Cloning this project

## Credits
### Media
- Index hero image by [LUM3N](https://unsplash.com/photos/Ngy0B2YWalk)
- Sign Up/Log In image by [CHUTTERSNAP](https://unsplash.com/photos/R9DeG1PnE9U)
- Vegetarian category image [Louis Hansel](https://images.unsplash.com/photo-1559847844-b0915a3800c6?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=942&q=80)
- Chicken category image [The Fry Family Food Co.](https://images.unsplash.com/photo-1584949602334-4e99f98286a9?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80)
- Meat category image [Sam Loyd](https://images.unsplash.com/photo-1595777216528-071e0127ccbf?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=1050&q=80)
- Fish category image [Victoria Shes](https://images.unsplash.com/photo-1594804233323-786d5c2ed9fb?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=634&q=80)
- Recipies hero image [Anastasia Zhenina](https://images.unsplash.com/photo-1605709303005-0fdddfd73dc4?ixid=MXwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHw%3D&ixlib=rb-1.2.1&auto=format&fit=crop&w=967&q=80)


## Acknowledgements
### Pages used to find information
### Code
This project was made with guidance from Mini Project | Putting It All Together led by Tim
### Thank you

## Disclaimer
This website was created for educational use only.

