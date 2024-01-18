# Import the required modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import unittest

# Define the URL of the web project
URL = "http://verseifylance.ahmadyaz.my.id/"

# Define the test data for the authentication feature
test_data = {
    "valid_email": "test@example.com",
    "valid_password": "Test@1234",
    "invalid_email": "test@invalid.com",
    "invalid_password": "test",
    "new_email": "new@example.com",
    "new_password": "New@1234",
    "new_name": "New User"
}

# Define the locators for the web elements
locators = {
    "login_link": (By.LINK_TEXT, "Login"),
    "register_link": (By.LINK_TEXT, "Register"),
    "email_input": (By.ID, "email"),
    "password_input": (By.ID, "password"),
    "password_confirmation_input": (By.ID, "password_confirmation"),
    "name_input": (By.ID, "name"),
    "login_button": (By.ID, "login_button"),
    "register_button": (By.ID, "register_button"),
    "logout_link": (By.LINK_TEXT, "Logout"),
    "forgot_password_link": (By.LINK_TEXT, "Forgot password?"),
    "reset_password_button": (By.ID, "reset_password_button"),
    "stay_logged_in_checkbox": (By.ID, "stay_logged_in"),
    "error_message": (By.CLASS_NAME, "error"),
    "success_message": (By.CLASS_NAME, "success"),
    "home_page_title": (By.TAG_NAME, "h1"),
    "profile_link": (By.LINK_TEXT, "Profile")
}

# Define the expected messages for the authentication feature
expected_messages = {
    "login_success": "You have successfully logged in.",
    "login_error": "Invalid email or password.",
    "registration_success": "You have successfully registered. Please check your email for confirmation.",
    "registration_error": "The email is already taken or invalid. The password and password confirmation do not match or do not meet the requirements.",
    "password_reset_success": "You have successfully reset your password. Please login with your new password.",
    "password_reset_error": "The email is not registered or the new password and password confirmation do not match or do not meet the requirements."
}

# Define a base class for the test cases
class BaseTest(unittest.TestCase):

    # Set up the test environment
    def setUp(self):
        # Create a Chrome driver instance
        self.driver = webdriver.Chrome()
        # Maximize the browser window
        self.driver.maximize_window()
        # Navigate to the web project URL
        self.driver.get(URL)
        # Wait for the page to load
        self.wait = WebDriverWait(self.driver, 10)

    # Tear down the test environment
    def tearDown(self):
        # Close the browser window
        self.driver.quit()

# Define a test class for the login function
class LoginTest(BaseTest):

    # Define a test case for a successful login
    def test_login_success(self):
        # Click on the login link
        self.driver.find_element(*locators["login_link"]).click()
        # Wait for the login page to load
        self.wait.until(EC.visibility_of_element_located(locators["login_button"]))
        # Enter the valid email and password
        self.driver.find_element(*locators["email_input"]).send_keys(test_data["valid_email"])
        self.driver.find_element(*locators["password_input"]).send_keys(test_data["valid_password"])
        # Click on the login button
        self.driver.find_element(*locators["login_button"]).click()
        # Wait for the home page to load
        self.wait.until(EC.visibility_of_element_located(locators["home_page_title"]))
        # Verify that the success message is displayed
        self.assertEqual(self.driver.find_element(*locators["success_message"]).text, expected_messages["login_success"])
        # Verify that the user is redirected to the home page
        self.assertEqual(self.driver.find_element(*locators["home_page_title"]).text, "Welcome to the blog site")
        # Verify that the logout and profile links are displayed
        self.assertTrue(self.driver.find_element(*locators["logout_link"]).is_displayed())
        self.assertTrue(self.driver.find_element(*locators["profile_link"]).is_displayed())

    # Define a test case for an unsuccessful login
    def test_login_error(self):
        # Click on the login link
        self.driver.find_element(*locators["login_link"]).click()
        # Wait for the login page to load
        self.wait.until(EC.visibility_of_element_located(locators["login_button"]))
        # Enter the invalid email and password
        self.driver.find_element(*locators["email_input"]).send_keys(test_data["invalid_email"])
        self.driver.find_element(*locators["password_input"]).send_keys(test_data["invalid_password"])
        # Click on the login button
        self.driver.find_element(*locators["login_button"]).click()
        # Wait for the error message to be displayed
        self.wait.until(EC.visibility_of_element_located(locators["error_message"]))
        # Verify that the error message is displayed
        self.assertEqual(self.driver.find_element(*locators["error_message"]).text, expected_messages["login_error"])
        # Verify that the user is not redirected to the home page
        self.assertNotEqual(self.driver.current_url, URL)
        # Verify that the login and register links are displayed
        self.assertTrue(self.driver.find_element(*locators["login_link"]).is_displayed())
        self.assertTrue(self.driver.find_element(*locators["register_link"]).is_displayed())

    # Define a test case for the stay logged in option
    def test_stay_logged_in(self):
        # Click on the login link
        self.driver.find_element(*locators["login_link"]).click()
        # Wait for the login page to load
        self.wait.until(EC.visibility_of_element_located(locators["login_button"]))
        # Enter the valid email and password
        self.driver.find_element(*locators["email_input"]).send_keys(test_data["valid_email"])
        self.driver.find_element(*locators["password_input"]).send_keys(test_data["valid_password"])
        # Check the stay logged in checkbox
        self.driver.find_element(*locators["stay_logged_in_checkbox"]).click()
        # Click on the login button
        self.driver.find_element(*locators["login_button"]).click()
        # Wait for the home page to load
        self.wait.until(EC.visibility_of_element_located(locators["home_page_title"]))
        # Verify that the success message is displayed
        self.assertEqual(self.driver.find_element(*locators["success_message"]).text, expected_messages["login_success"])
        # Verify that the user is redirected to the home page
        self.assertEqual(self.driver.find_element(*locators["home_page_title"]).text, "Welcome to the blog site")
        # Verify that the logout and profile links are displayed
        self.assertTrue(self.driver.find_element(*locators["logout_link"]).is_displayed())
        self.assertTrue(self.driver.find_element(*locators["profile_link"]).is_displayed())
        # Close the browser window
        self.driver.quit()
        # Create a new Chrome driver instance
        self.driver = webdriver.Chrome()
        # Maximize the browser window
        self.driver.maximize_window()
        # Navigate to the web project URL
        self.driver.get(URL)
        # Wait for the page to load
        self.wait = WebDriverWait(self.driver, 10)
        # Verify that the user is still logged in