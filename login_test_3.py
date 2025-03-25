from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

"""
Login test incl. 
- positive / negative login test
- screenshot if incorrect user login 
- test for various login combinations
- test for empty fields
- test email validation
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


# test for various login combinations
def test_multiple_users():
    test_cases = [
        ("student", "Password123", True),  # Korrekte Daten
        ("student", "WrongPassword", False),  # Falsches Passwort
        ("wronguser", "Password123", False),  # Falscher Benutzername
        ("wronguser", "WrongPassword", False),  # Beides falsch
    ]

    for username, password, should_pass in test_cases:
        driver.get("https://practicetestautomation.com/practice-test-login/")
        time.sleep(2)

        username_input = driver.find_element(By.ID, "username")
        password_input = driver.find_element(By.ID, "password")

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.RETURN)
        time.sleep(3)

        if should_pass:
            if driver.current_url == "https://practicetestautomation.com/logged-in-successfully/":
                print(f"✅ Login erfolgreich für {username}")
            else:
                print(f"❌ Fehler: Login sollte erfolgreich sein für {username}")
                take_screenshot(driver, f"failed_login_{username}")
        else:
            try:
                error_message = driver.find_element(By.ID, "error")
                if error_message.is_displayed():
                    print(f"✅ Fehlermeldung korrekt für {username}")
            except:
                print(f"❌ Fehler: Fehlermeldung wurde nicht angezeigt für {username}")
                take_screenshot(driver, f"missing_error_message_{username}")


# test for empty fields
def test_empty_fields():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(Keys.RETURN)
    time.sleep(3)

    try:
        error_message = driver.find_element(By.ID, "error")
        if error_message.is_displayed():
            print("✅ Fehlermeldung korrekt für leere Felder")
    except:
        print("❌ Fehler: Fehlermeldung wurde nicht angezeigt für leere Felder")
        take_screenshot(driver, "empty_fields_test")


# test for e-mail validation
def test_email_validation():
    driver.get("https://practicetestautomation.com/practice-test-login/")
    time.sleep(2)

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    invalid_emails = ["plainaddress", "@missingusername.com", "user@.com", "user@com"]
    for email in invalid_emails:
        username_input.clear()
        password_input.clear()
        username_input.send_keys(email)
        password_input.send_keys("Password123")
        password_input.send_keys(Keys.RETURN)
        time.sleep(2)

        try:
            error_message = driver.find_element(By.ID, "error")
            if error_message.is_displayed():
                print(f"✅ Fehlermeldung korrekt für ungültige E-Mail: {email}")
        except:
            print(f"❌ Fehler: Fehlermeldung wurde nicht angezeigt für ungültige E-Mail: {email}")
            take_screenshot(driver, f"invalid_email_{email}")



test_multiple_users()
test_empty_fields()
test_email_validation()


driver.quit()
