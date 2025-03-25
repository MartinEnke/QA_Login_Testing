from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
Login test incl. 
- positive / negative login test
- screenshot if incorrect user login 
"""

# Choose the browser for automation (chrome or firefox)
browser = "chrome"

if browser == "chrome":
    driver = webdriver.Chrome()
elif browser == "firefox":
    driver = webdriver.Firefox()
else:
    raise ValueError("Unknown browser!")

# function for screenshots (in case wrong user data was entered)
def take_screenshot(driver, test_type):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f"{test_type}_screenshot_{timestamp}.png"
    driver.save_screenshot(screenshot_name)
    print(f"Screenshot gespeichert: {screenshot_name}")

# positive test (correct user data)
def test_successful_login():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("student")
    password_input.send_keys("Password123")
    password_input.send_keys(Keys.RETURN)

    time.sleep(30)

    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    if driver.current_url == expected_url:
        print("✅ Positiver Test bestanden!")
    else:
        print("❌ Positiver Test fehlgeschlagen!")
        take_screenshot(driver, "positive_test")

# negative test (incorrect user data)
def test_unsuccessful_login():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    username_input.send_keys("student")
    password_input.send_keys("WrongPassword")
    password_input.send_keys(Keys.RETURN)

    time.sleep(3)

    error_message = driver.find_element(By.ID, "error")
    if error_message.is_displayed():
        print("✅ Negativer Test bestanden (Fehlermeldung angezeigt)!")
    else:
        print("❌ Negativer Test fehlgeschlagen!")
        take_screenshot(driver, "negative_test")


test_successful_login()
test_unsuccessful_login()


driver.quit()
