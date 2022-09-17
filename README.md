# Caitlin's Crafts
- ![image](testing/caitlins_crafts_responsiveness.jpg)
## Visit the live Website : **[Caitlin's Crafts :arrow_right:](https://caitlins-crafts.herokuapp.com/)**
- Caitlin's Crafts is a website for users to find and purchase quality hand made items for themselves or for gifts.
- Users will be able to register for a newsletter on crafts available and any specials that are curently available.

## Existing Features
- Interactive Elements:
  - Home page
    - ![image](testing/home_page.jpg)
  - Login/Logout
    - ![image](testing/log_in.jpg)
    - ![image](testing/log_out.jpg)
  - Register
    - ![image](testing/register.jpg)
  - Choice of Crafts by Price, Category or All Crafts
    - ![image](testing/all_crafts.jpg)
  - Choice of Crafts from baby of blankets or accessories or All Baby
    - ![image](testing/baby.jpg)
  - Choice of Crafts from Kids/Adults of clothes, hats, scarfs or All Kids/Adults
    - ![image](testing/kids.jpg)
  - Choice of Crafts from Special Offers of Deals, Clearance or All Special Offers
    - ![image](testing/offers.jpg)

## Languages Used:

- Python
- Django
- HTML
- CSS
- JavaScript

## Relational Database used:

- Postgres

## Frameworks, Libraries & Programs Used:

- [Git](https://git-scm.com): used to utilize the Gitpod terminal to commit to Git and Push to GitHub
- [GitHub](https://github.com/): used to store project code after being pushed from Git
- [GitPod](https://gitpod.io/): used as cloud based IDE for writing code
- [Balsamiq Wireframes](https://balsamiq.com/):  used to draw wireframes of pages of project
- [Am I Responsive?](http://ami.responsivedesign.is/) used to give a visual of what the project looks like on various devices
- [Heroku](https://heroku.com): used to deploy the Our Family Recipes app
- [Cloudinary](https://cloudinary.com/): used to import my Cloudinary field for the featured image
- [Diffchecker](https://www.diffchecker.com/): used to compare code when I had an error
- [Stripe](https://stripe.com/): used to add the ability to charge consumer for crafts purchased
- [Pexels](https://pexels.com/): used to obtain photo for home page
- [AWS](https://aws.amazon.com/): used for database of media used to be stored for heroku


## Deployment

The live deployed application can be found at []().

### Heroku Deployment

This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.

Deployment steps are as follows, after account setup:

- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Your app name must be unique, and then choose a region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the following key/value pairs:
  - `CLOUDINARY_URL` (insert your own Cloudinary API key here)
  - `DATABASE_URL` (this comes from the **Resources** tab, you can get your own Postgres Database using the Free Hobby Tier)
  - `SECRET_KEY` (this can be any random secret key)

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: gunicorn family_recipes.wsgi > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:

Either:
- Select "Automatic Deployment" from the Heroku app.

Or:
- In the Terminal/CLI, connect to Heroku using this command: `heroku login -i`
- Set the remote for Heroku: `heroku git:remote -a <app_name>` (replace app_name with your app, without the angle-brackets)
- After performing the standard Git `add`, `commit`, and `push` to GitHub, you can now type: `git push heroku main`

The frontend terminal should now be connected and deployed to Heroku.

### Local Deployment

*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://github.com/FamilyRecipes.git`

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://github.com/pattytonyoneill/caitlins_crafts)

## Future Additions to page
- Ratings for crafts that are on this site

## Credits
-  [Selling Crafts Online](https://wellkeptwallet.com/selling-crafts-online/)
-  [Design & Crafts Council Ireland](https://www.dcci.ie/about/media/press-releases/new-global-online-platform-launched-for-the-very-best-of-irelands-design-an)
-  [Design Ireland](https://www.designireland.ie/)
-  [Smart Touch](https://www.smarttouch.me/)
-  [The 6 Best Social Media Platforms for your Business 2022](https://www.lyfemarketing.com/blog/best-social-media-platforms/)

### Code
- _Readme used sample readme from code institute as a model. [Github](https://github.com/Code-Institute-Solutions/readme-template/blob/master/README.md)_

### Content
- _All content written by the developer._

### Acknowlegements
- _My Mentor for his help and feedback._
- _Tutor support at Code Institute_
- _Family for help with help and feedback on website as a user_
- _Caitlin my daughter for being the inspiration for this particular website_

#### Data Schema
To view all Data Schema, go to [DATASCHEMA.md](DATASCHEMA.md)

#### Testing
To view all testing, go to [TESTING.md](TESTING.md)

#### SEO and Marketing Research
To view all SEO and Marketing Research, got to [SEO.md](SEO.md)

#### Wireframes
To view all wireframes, go to [WIREFRAMES.md](WIREFRAMES.md)
