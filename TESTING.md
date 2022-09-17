# [Caitlin's Crafts](testing/caitlins_crafts_responsiveness.jpg)

# Testing for Caitlin's Crafts

## User Stories testing:
To view all userstories, go to [USERSTORIES.md](USERSTORIES.md)

## Browser Compatability
- Firefox
    - ![image](testing/profile.jpg)

- Microsoft Edge
    - ![image](testing/microsoft_edge.jpg)

- Google Chrome
    - ![image](testing/google_chrome.jpg)

## Responsiveness
- Desktop
     - ![image](testing/profile.jpg)

- Tablet
     - ![image](testing/tablet.jpg)

- Cell Phone
     - ![image](testing/google_chrome.jpg)

## Validator Testing

### Pep8 Testing
To view all Pep8 testing, go to [PEP.md](PEP.md)

## custom_storage.py Pep 8
-  Pep8 for custom_storage.py
     - ![image](testing/custom_storage.py.jpg)

### HTML Validation
- ![image](testing/html_testing.jpg)

### CSS Validation
- base.css
     - ![image](testing/base_css_validator.jpg)
- checkout.css
     - ![image](testing/checkout_css_validator.jpg)
- profiles.css
     - ![image](testing/checkout_css_validator.jpg)

## Remaining Bugs
- Gitpod is working properly when sending the email and listing totals but for some reason on the deployed site it is sending those as 0.
     -![image](testing/deployed_site_error.jpg)
     -![image](testing/gitpod_site_no_error.jpg)this picture is after doing on heroku site and shows the error

## Bugs
- Needed to add I solve it by removing s from function in crafts/views.py. My function was not called craft_detail instead it was crafts_detail.
     -![image](testing/attribute_error.jpg)
- Made crafts be craft where needed in code on crafts.html and craft_detail.html. 
     -![image](testing/no_reversematch_error.jpg)
     -![image](testing/lost_pictures.jpg)
- Corrected stripe_element.js and changed it to stripe_elements.js
     -![image](testing/payment_error.jpg)
- Procfile I had put an empty row at the end and shouldn't have done so.
     -![image](testing/error_procfile.jpg)
- Typo for allowed hosts. Found this after Procfile error.
     -![image](testing/typos_settings.jpg)
- Attribute Error at checkout. Added line of code that was missing.
     -![image](testing/attribute_error_checkout.jpg)
- Heroku had issue with pictures not coming up when entered on AWS. Come to find out when copying from zip file it was adding [1] after each photo number which I fixed by renaming before added to AWS again.
- webhooks had a 403 error under heroku because I forgot to add checkout/wh/
     -![image](testing/403errror.jpg)
- webhooks had a 404 error under gitpod because I needed to make it public
     -![image](testing/404errror.jpg)
- ModuleNotFoundError: No module named'crafts.widgets'. I just had to stop and then restart my server.
     -![image](testing/crafts_widgets.jpg)
- Heroku 500error in the end redid creating the app on google
     -![image](testing/heroku1.jpg)
     -![image](testing/heroku2.jpg)
     -![image](testing/heroku3.jpg)
     -![image](testing/heroku4.jpg)
- Gitpod is working properly when sending the email and listing totals but for some reason on the deployed site it is sending those as 0.
     -![image](testing/deployed_site_error.jpg)
     -![image](testing/gitpod_site_no_error.jpg)this picture is after doing on heroku site and shows the error
 

Return back to [README.md](README.md)