# Final Project Report

* Student Name: Kavya Veeramony
* Github Username: KavyaVee00
* Semester: Fall 2023
* Course: CS 5001



## Description 
I've taken on a project to develop a password checker which was insired by the widespread use of passwords in our everyday online activities. 

From emails and social media to shopping and gaming, passwords are a crucial aspect of our online experiences. My aim is to understand how we can ensure these passwords are strong and secure. It goes beyond just account logins; it encompasses all our online interactions, be it for work, school, healthcare, and more. This project is my way of delving into what factors contribute to the security of passwords across various aspects of our digital lives. It's an interesting journey to explore how we can make online activities safer through robust password practices. 



## Key Features
The objective here is to facilitate the creation of an account on the new Northeastern Align Networking app, providing a platform for connecting with fellow Align students. 

The primary focus of this project lies in establishing strict password requirements to ensure that users create secure passwords meeting specific criteria: 
- 8 to 16 characters
- at least one uppercase letter,
- one lowercase letter, one digit
- one special character.
- Must not contain the login name

The user experience will mirror an actual login scenario, requiring individuals without an existing account to create one. Subsequently, they will need to sign in with the correct username and password. In case of incorrect login attempts, users will have the option to reset their password. 


## Guide
How do we run your project? What should we do to see it in action? - Note this isn't installing, this is actual use of the project.. If it is a website, you can point towards the gui, use screenshots, etc talking about features. 


## Installation Instructions
If we wanted to run this project locally, what would we need to do?  If we need to get API key's include that information, and also command line startup commands to execute the project. If you have a lot of dependencies, you can also include a requirements.txt file, but make sure to include that we need to run `pip install -r requirements.txt` or something similar.

## Code Review
Go over key aspects of code in this section. Both link to the file, include snippets in this report (make sure to use the [coding blocks](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#code)).  Grading wise, we are looking for that you understand your code and what you did. 


### Password

The first function that I've written is the one that checks that the password fits the criteria. The is_password_strong function checks if a password is strong based on certain criteria.It takes two parameters: username and password.

The criteria for a strong password are as follows:
The password must be between 8 and 16 characters in length.
It must contain at least one uppercase letter ([A-Z]).
It must contain at least one lowercase letter ([a-z]).
It must contain at least one digit (\d).
It must contain at least one special character ([!@#$%^&*(),.?":{}|<>]).
The password should not contain the username (case-insensitive).

    def is_password_strong(username, password):
    """
    Check if a password is strong based on certain criteria.

    Parameters:
    - username (str): The username associated with the password.
    - password (str): The password to be checked.

    Returns:
    - bool: True if the password is strong, False otherwise.
    """
    if 8 <= len(password) <= 16 and re.search(r'[A-Z]', password) and re.search(r'[a-z]', password) \
            and re.search(r'\d', password) and re.search(r'[!@#$%^&*(),.?":{}|<>]', password) \
            and username.lower() not in password.lower():
        return True
    return False

Code Explanation:

- if 8 <= len(password) <= 16: Checks if the length of the password is between 8 and 16 characters (inclusive).
- re.search(r'[A-Z]', password): Checks if there is at least one uppercase letter in the password.
- re.search(r'[a-z]', password): Checks if there is at least one lowercase letter in the password.
- re.search(r'\d', password): Checks if there is at least one digit in the password.
- re.search(r'[!@#$%^&*(),.?":{}|<>]', password): Checks if there is at least one special character in the password.
- username.lower() not in password.lower(): Checks if the lowercase username is not part of the lowercase password.

### Creating an account 

The create_account function allows a user to create a new account. It prompts the user for a username and password. It checks if the username already exists in the user_accounts dictionary. It ensures that the password is strong by repeatedly prompting the user until a strong password is provided. The account details are then stored in the dictionary.


    def create_account(username, password):
    
    Create a new user account with a strong password.
    """
    Parameters:
    - username (str): The desired username.
    - password (str): The password for the new account.

    Returns:
    - None
    """
    print("Creating a new account:")

    # Check if the username already exists (after stripping leading/trailing spaces)
    cleaned_username = username.strip()
    if cleaned_username in user_accounts:
        print("Username already exists. Please choose another.")
        return

    # Check if the password is strong
    while not is_password_strong(cleaned_username, password):
        print("Weak password. Make sure it meets the criteria:")
        print("- 8 to 16 characters")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")
        print("- At least one digit")
        print("- At least one special character (!@#$%^&*(),.?\":{}|<>)")
        print("- Should not contain the username")
        password = input("Enter a stronger password: ")

    # Store the username and password in the dictionary
    user_accounts[cleaned_username] = password
    print("Account created successfully!")

> Major Challenge  
> When I initially had written this code, I kept having the problem where I would create an account with a username and password, and then when I went to login with the exact same username and password, it would tell me that the username was not found (even though it was the exact username I had signed up with). I eventually understood that the issue seemed to be related to the trailing space in the username when creating a new account. To fix this, I modified the code so that it would strip the leading and trailing spaces from the entered username.


### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.
