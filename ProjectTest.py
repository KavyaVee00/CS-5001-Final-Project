from Project import (

    is_password_strong, create_account, login, reset_password

    )

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




def main() -> None:
    fail = 0
    fail += test_is_password_strong()
    fail += test_create_account()
   

    print(f"Failed {fail} tests.")

if __name__ == "__main__":
    main()
