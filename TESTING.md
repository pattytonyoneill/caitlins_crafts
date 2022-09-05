# Testing for Caitlin's Crafts

## User Stories testing:
- 1. As a shopper I can select something to purchase.
- ![image](testing/userstory1.jpg)
- 2. As a shopper I can view individual knitted product details.
- ![image](testing/userstory2.jpg)
- 3. As a shopper I can take advantage of any specials on any crafts that I want to purchase.
- ![image](testing/userstory3.jpg)
- 4. As a shopper I can avoid spending to much money by seeing the total of the purchases made.
- ![image](testing/userstory4.jpg)
- 5. As a site user I can have a personal account and be able to view my profile whenever I wish to.
- ![image](testing/profile.jpg)
- 6. As a site user I can access my account and the information that it contains
- ![image](testing/profile.jpg)
- 7. As a site user I can view my order history and order confirmations, and save the payment history
- ![image](testing/profile.jpg)
- 8. As a site user I can easily recover my password in case it is forgotten
- ![image](testing/password_reset.jpg)
- 9. As a site user I can confirm that my account registered successfully and receive an email after registration.
- ![image](testing/userstory9.jpg)
- 10. As a shopper I can easily find the best priced and sort products by category in a list of available crafts.
- ![image](testing/crafts_by_price.jpg)
- 11. As a shopper I can find the best priced product in a specific category by name.
- ![image](testing/userstory11.jpg)
- 12. As a shopper I can make sure that I don't accidently select the wrong product
- ![image](testing/userstory12.jpg)
- 13. As a shopper I can sort categories of products simultaneously.
- ![image](testing/userstory16.jpg)
- 14. As a shopper I can find a product that can be purchased
- ![image](testing/userstory14.jpg)
- 15. As a shopper I can quickly decide if the knitted item I want is available
- ![image](testing/userstory16.jpg)
- 16. As a shopper I can quickly find product that I am interested in without having to search through all of the products
- ![image](testing/userstory16.jpg)
- 17. As a shopper I can quickly find craft that I am interested in without having to search through all of the crafts so that I can easily identify the total cost of my purchase.
- ![image](testing/userstory17.jpg)
- 18. As a shopper I want to adjust the quantity of individual items that are in my bag so that *I can easily make changes to my purchase before I check out.
- ![image](testing/userstory12.jpg)
- 19. As a shopper I can quickly and easily enter my payment information so that I can quickly and easily check out with little or no hassle
- ![image](testing/userstory19.jpg)
- 20. As a shopper I can feel that my personal/payment information is safe and secure so that I can confidently provide the needed information for the purchase.
- ![image](testing/userstory19.jpg)
- 21. As a shopper I can view an order confirmation after checkout so that I can make sure that there are no errors in my order.
- ![image](testing/success_message_purchase.jpg)
- 22. As a shopper I can receive an email upon checkout confirming the purchase so that I can keep the confirmation of what has been purchased for my records.
- ![image](testing/order_confirmation.jpg)
- ![image](testing/confirmation_order2.jpg)

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

### Pep8
-  Pep8 for models.py
     - ![image](testing/models.py.jpg)

### HTML Validation
- ![image](testing/html_testing.jpg)

### CSS Validation
- ![image](testing/css_testing.jpg)

## Remaining Bugs
- 

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
     -![image]()
 

Return back to [README.md](README.md)