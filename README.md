# OPSWAT_test
Swaglabs Tests

Technologies: Selenium, Python - Visual Studio
Needed: python min. 3.9.13, selenium 4.15.2, webdriver-manager 4.0.1
I used visual studio's test explorer to run my tests. At the time of sending all tests worked as intended.

Idea: I have users that can do different things on the site.
I will do test suits for all the functions using standars user, which can be automated later using Selenium IDE.
I tought that I have 2 routes to separate the tests, by page or by functionality. I decieded I will do it by func. 

THIS IS NOT MY FINAL TAKE REGARDING THE TESTS. JUST A BASIC QUICK BRAINSTORM.
I am confident I have left out some improtant tests, these I would add later as I work on the project.
I am confident I can write an even better and cleaner code with digging deeper into selenium design patterns.

#Fundamental/Technical tests - tests which are testing the basic requirements to be able to run the page/IDE

- Check drivers (Separate tests for Opera/Chrome/Edge/Firefox, whatever are the supported browsers)
	- Install
	- Version (spec version check)
	- Chrome manager test
	- Connection test
	- validate response value (404/200)

#Basic functional tests 
tests that I would run to check the basic functionality "pre delivery"

- Login page works
- Menu works
- Main page works
	- Page name correct
	- Can open side menu
	- About takes to correct page
	- Sorting works
	- Logout works 
	- Reset App state works
	- Shopping works
		- Item in cart
		- Item can be removed
		- Continue shopping takes back to main page
			- while keeping stuff in cart
	- Can see all item
- Item page works
- Checkout page works
	- Name/Birth date can be added
-Checkout overview works
	- Added price correct
	- Finish button
	- Cart empties after stuff is bought

#Visual tests 
test that check the visual functinality of the page

- Alignment tests
	- Shop
	- Cart
	- Menu
- Aligns well so windows (Phone/Browser scaleing)
- Title/texts are correct
- Pictures are correct
	- pictures can be seen.
- Prices are correct

#Performance tests 
test that check the performance of the page

- Page response time
- Refresh rate
- Site kicks you out after 5mins of inactivity
- Stuff stays in cart after refresh

#User focused tests?? 
This one is asked for, so some tests for some user "problems" I discovered.

- locked_out_user can't log in, error message shows he is locked out.
- problem_user and error_user can't remove item on the main page, just at the cart
- performace_glitch user has problems with loading times -> performance test
- error user can't add to cart on the item page
- error_user has problems at the checkout page with the fields
- visual_user has tons of visual bugs, like cart icon moveing, showing badge when nothing in cart

