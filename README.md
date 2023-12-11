# Final Project Report

* Student Name: Kavya Veeramony
* Github Username: KavyaVee00
* Semester: Fall 2023
* Course: CS 5001


[Project.py](../Project.py) - This is the main file you will be working on. It contains the functions you will be writing, along with already built docstrings. 
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
There will be a prompt welcoming you to to site. There will be 3 options 

L - Login 
A - Create a New account 
R - Reset password 

Whichever key you click, it will direct you to that accordingly. 

Here are the steps to run the project locally:

Download the Script:
Download the Python script (e.g., project.py) to your local machine.

Open a Terminal/Command Prompt:
Open a terminal or command prompt on your computer.

Navigate to the Script's Directory:
Use the cd command to navigate to the directory where the script is located. 

Since this script doesn't have external dependencies, you can run it without additional installations.









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

> Major Challenge:  
> When I initially had written this code, I kept having the problem where I would create an account with a username and password, and then when I went to login with the exact same username and password, it would tell me that the username was not found (even though it was the exact username I had signed up with). I eventually understood that the issue seemed to be related to the trailing space in the username when creating a new account. To fix this, I modified the code so that it would strip the leading and trailing spaces from the entered username.


### Login 

The login function handles the login process. It checks if the entered username exists in the user_accounts dictionary. If the username exists, it prompts the user for a password and checks if it matches the stored password. If the password is incorrect, it allows the user to retry or go back to the main menu by entering 'Q'.

    def login(username, password):
    """
    Log in a user with the provided username and password.

    Parameters:
    - username (str): The username for login.
    - password (str): The password for login.

    Returns:
    - None
    """
    print("Login:")

    # Check if the username exists
    cleaned_username = username.strip()
    if cleaned_username not in user_accounts:
        print("Username not found. Please create a new account.")
        return

    # Check if the entered password matches the stored password
    stored_password = user_accounts[cleaned_username]
    while stored_password != password:
        password = input("Incorrect password. Please try again. (or 'Q' to go back to the main menu): ").strip()

        if password.upper() == "Q":
            return

    print("Login successful!")

> Major Challenge:  
> When I had resetted a password and tried logging in again, it would say that the password was wrong. It seemed like there was an issue with the login function where it doesn't correctly handle the updated password after a successful reset. The problem was that the login function I had written didn't take the new password into account when checking for a match. So I had modified the code so that it ensured that the login function uses the cleaned username when checking for a match in the user_accounts dictionary.


### Resetting Password 

The reset_password function allows a user to reset their password. It checks if the username exists in the user_accounts dictionary. It prompts the user for a new password and ensures that it meets the strength criteria. The password is then updated in the dictionary.

    def reset_password(username, new_password):
    """
    Reset the password for a user.

    Parameters:
    - username (str): The username for which the password is reset.
    - new_password (str): The new password.

    Returns:
    - None
    """
    print("Reset Password:")

    # Check if the username exists (after stripping leading/trailing spaces)
    cleaned_username = username.strip()
    if cleaned_username not in user_accounts:
        print("Username not found. Please create a new account.")
        return

    # Check if the new password is strong
    while not is_password_strong(cleaned_username, new_password):
        print("Weak password. Make sure it meets the criteria:")
        print("- 8 to 16 characters")
        print("- At least one uppercase letter")
        print("- At least one lowercase letter")
        print("- At least one digit")
        print("- At least one special character (!@#$%^&*(),.?\":{}|<>)")
        print("- Should not contain the username")
        new_password = input("Enter a stronger password: ")

    # Update the password in the dictionary
    user_accounts[cleaned_username] = new_password
    print("Password reset successful!")

> Key takeaway:  
> When I had originally written the code, I had forgotton to update the password in the dictionary. Every time I tried to log in with the new password, it would say wrong password. I realized my mistake and wrote in the code to update the password. This really affirmed for me the usefulness of dictionaries in code.



### Main function 


The function contains a ongoing loop which ensures that the program continues to run until the user decides to exit. The function begins by welcoming the user to the Northeastern Align networking app. Within the loop, it repeatedly displays a menu of options, including Login (L), Create a New Account (A), Reset Password (R), and Quit (Q). The user is prompted to input their choice and the function processes this choice to trigger the corresponding functionality.

    def main():
    """
    The main function for the Northeastern Align networking app.

    Returns:
    - None
    """
    print("Welcome to the Northeastern Align networking app!")

    while True:
        print("\nOptions:")
        print("L - Login")
        print("A - Create a New account")
        print("R - Reset password")
        print("Q - Quit")

        choice = input("Enter your choice: ").upper()

        if choice == 'L':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            login(username, password)
        elif choice == 'A':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            create_account(username, password)
        elif choice == 'R':
            username = input("Enter your username: ")
            new_password = input("Enter your new password: ")
            reset_password(username, new_password)
        elif choice == 'Q':
            print("Exiting the Northeastern Align networking app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

        if __name__ == "__main__":
            main()



## Example Runs

### Welcome prompt 
```text
Welcome to the Northeastern Align Networking app!

Options:
L - Login
A - Create a New account
R - Reset password
Q - Quit
Enter your choice: 
```

### Creating account
```text
Options:
L - Login
A - Create a New account
R - Reset password
Q - Quit
Enter your choice: A
Enter your username: KavyaV
Enter your password: AlignN.1212
Creating a new account:
Account created successfully!
 
```
### Login 
```text
Options:
L - Login
A - Create a New account
R - Reset password
Q - Quit
Enter your choice: L
Enter your username: KavyaV
Enter your password: AlignN.1212
Login:
Login successful!
 
```

### Username Checking 

```text
Options:
L - Login
A - Create a New account
R - Reset password
Q - Quit
Enter your choice: A
Enter your username: KavyaV 
Enter your password: qwdnhwkd
Creating a new account:
Username already exists. Please choose another.
 
```

### Password checking 

```text
Options:
L - Login
A - Create a New account
R - Reset password
Q - Quit
Enter your choice: A
Enter your username: KavyaVee
Enter your password: 1121ed323
Creating a new account:
Weak password. Make sure it meets the criteria:
- 8 to 16 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character (!@#$%^&*(),.?":{}|<>)
- Should not contain the username
Enter a stronger password: 
 
```
### Password Resetting 

```text
Options:
L - Login
A - Create a New account
R - Reset password
Q - Quit
Enter your choice: R
Enter your username: KavyaV
Enter your new password: North.E123
Reset Password:
Password reset successful!
 
```












## Testing
I tested this code by writing test cases for the functions: 


    def check(actual, expected) -> int:
    """
    Check for error, return 1 if error exists, 0 if it doesn't.

    Args:
        actual: Actual value
        expected: Expected value
    """
    if actual != expected:
        print(f"Actual: {actual} does not equal Expected: {expected}")
        return 1
    return 0

    def test_is_password_strong() -> int:
    """
    Tests is_password_strong function.

    Returns:
        int: The number of tests failed.
    """
    fail = 0

    # Test Case 1: Strong password
    result = is_password_strong("username", "Strong!Pass123")
    fail += check(result, True)

    # Test Case 2: Weak password, no uppercase
    result = is_password_strong("username", "weak!pass123")
    fail += check(result, False)

    # Test Case 3: Weak password, no special character
    result = is_password_strong("username", "WeakPass123")
    fail += check(result, False)

    return fail

    def test_create_account() -> int:
    """Test cases for create_account function.

    Returns:
        int: the number of tests failed.
    """
    fail = 0

    # Test case 1: Creating an account successfully
    username_1 = "user1"
    password_1 = "StrongPass1!"
    fail += check(create_account(username_1, password_1), None)

    # Test case 2: Attempting to create an account with an existing username
    username_2 = "user1"  # Use the same username as in test case 1
    password_2 = "AnotherStrongPass2!"
    fail += check(create_account(username_2, password_2), "Username already exists. Please choose another.")

    # Test case 3: Creating an account with a weak password (simulate user input)
    username_3 = "user3"
    weak_password_input = "WeakPass"
    strong_password_input = "StrongPass3!"
    
   
    return fail



## Missing Features / What's Next
In the future, I would implement these features: 
- Avoid Common Passwords: Check if the password is not too common or easily guessable.
- Password History: Keep a history of previous passwords to prevent users from reusing the same passwords.
- Account Lockout Policy: Implement a policy that locks an account after multiple failed login attempts.

## Final Reflection 

One of the key takeaways from this class has been understanding the basic concepts of programming, such as variables, data types, conditionals, loops, debugging, etc. I've also learned how to write simple programs and solve problems using code. The instructional videos have been essential in grasping these foundational concepts, and I appreciate the guidance provided by the instructor and the opportunity to practice coding during the video lectures as well. The class has been both useful and challenging. It's been rewarding to see how coding can be applied to real-world problem-solving, which I find highly valuable. However, the challenges have arisen when dealing with more complex coding tasks and debugging issues. One of the most challenging aspects for me has been mastering the syntax of programming languages and understanding how to translate my ideas into functional code. I feel like I understand the problem and that I know what I want the function to do, but when it comes to writing the code, it takes me a little bit more time being able to organize everything so that it runs smoothly. What I've enjoyed the most is the sense of accomplishment when I successfully write code that works as intended. Especially whenever I submit it, and then the autograder lets me know that I have something wrong with the code. Being able to go back and successfully figure out what went wrong using the knowledge that I learned makes me really feel a sense of accomplishment. I can see the direct application of what I've learned in this class in various fields, from automating repetitive tasks to developing simple software solutions. 
