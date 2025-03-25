from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
simple login test
"""

# Choose the browser for automation (chrome or firefox)
browser = "chrome"


if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
else:
    raise ValueError("Unknown browser!")

# Navigate to the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# Wait briefly to ensure the page has fully loaded
time.sleep(10)

# Find the username and password input fields and enter login credentials
username_input = driver.find_element(By.ID, "username")
password_input = driver.find_element(By.ID, "password")

username_input.send_keys("student")
password_input.send_keys("Password123")
password_input.send_keys(Keys.RETURN)  # Simulate pressing the Enter key to submit the form

# Wait for the page to redirect after login
time.sleep(10)

# Check if the URL matches the expected logged-in URL to confirm a successful login
expected_url = "https://practicetestautomation.com/logged-in-successfully/"
if driver.current_url == expected_url:
    print("✅ Login Test Passed!")
else:
    print("❌ Login Test Failed!")


driver.quit()
