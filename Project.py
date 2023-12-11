import re

# Dictionary to store user accounts and passwords
user_accounts = {}

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

def create_account(username, password):
    """
    Create a new user account with a strong password.

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

def main():
    """
    The main function for the Northeastern Align Networking app.

    Returns:
    - None
    """
    print("Welcome to the Northeastern Align Networking app!")

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
            print("Exiting the Northeastern Align Networking app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

