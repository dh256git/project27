# Protected pages

I use a javascript to take a text input from user, and use it as a pin to unlock a protected page. This is how it works.

1. Create HTML form with text input and submit button.
2. Link submit button with onclick action triggering javascript function.
3. Script concatenates a string using path to protected file, the user input pin, and name of protected page. Then the script passes the string as the "href" attribute to an HTML link tag, identified through its ID.
4. The link only opens the protected page if the correct pin is entered, and submit button is pressed.