# Testing

## Table of contents:

- [Validator Testing](#validator-testing)
    - [Lighthouse](#lighthouse)
    - [W3C](#w3c-html)
    - [Jigsaw](#jigsaw-css)
- [Responsiveness](#responsiveness)

## Validator Testing

### Lighthouse Testing

- Landing page testing
![index](DOCS/testing/lighthouse/hometest.png)
<br>

- Categories page testing
![categories](DOCS/testing/lighthouse/categoriestest.png)
<br>

- Blog page testing
![blog](DOCS/testing/lighthouse/blogtest.png)
<br>

- Recipe page testing
![Recipe](DOCS/testing/lighthouse/recipetest.png)
<br>

- Create Recipe page testing
![create page](DOCS/testing/lighthouse/createtest.png)
<br>

- About page testing
![About](DOCS/testing/lighthouse/abouttest.png)
<br>

- Contact page testing
![Contact](DOCS/testing/lighthouse/contactest.png)
<br>

- Login page testing
![Login](DOCS/testing/lighthouse/logintest.png)
<br>

### W3C HTML validator

- A total of 7 html errors were found on the website which were quickly fixed

![HTML Validator](DOCS/testing/validation/W3C-htmlvalidation.png)

### W3C Jigsaw validator

- After trying to run CSS validator by the website URL the validator crashed three times. By direct upload of CSS code 2 errors were found and fixed.

![CSS Validator](DOCS/testing/validation/cssval.png)

### JS Validation

- As I didn't write much JavaScript code for this project, only used it for the navbar and alert messages. Consequently, our testing process went smoothly, and validator didn't encounter any errors. By keeping our JavaScript code to a minimum and focusing on its specific functionality, I was able to streamline the testing efforts and ensure that the code I did write was thoroughly tested and bug-free.

![JSHint](DOCS/testing/validation/jshint.png)

### PEP8 Validation

- To ensure code consistency and readability, we followed the Pep8 guidelines and used packages for tracking errors and warnings. One of the most frequent issues I encountered was lines that were too long, which I addressed by breaking them up into smaller segments. Also fixed a few trailing spaces warnings that came across during the review process. Overall, these efforts helped to produce high-quality code that is easy to read, understand, and maintain.

![PEP](DOCS/testing/validation/pep8.png)

