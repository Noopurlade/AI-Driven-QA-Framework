
import pytest
from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    
    # Step 1: Open Website
    login_page.open()
    
    # Step 2: Perform Login
    login_page.login("tomsmith", "SuperSecretPassword!")
    
    # Step 3: Verify Success
    message = login_page.get_message()
    assert "You logged into a secure area!" in message
    print("\n[SUCCESS]: Valid login test passed.")

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    
    # Step 1: Open Website
    login_page.open()
    
    # Step 2: Perform Login with wrong credentials
    login_page.login("wrong_user", "wrong_pass")
    
    # Step 3: Verify Error Message
    message = login_page.get_message()
    assert "Your username is invalid!" in message
    print("\n[SUCCESS]: Invalid login error handled correctly.")