from selenium import webdriver

"""
webdriver test
"""

def run_test(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        print("Unknown browser!")
        return

    driver.get("https://www.google.com")

    import time
    time.sleep(5)

    driver.quit()

# testing Chrome and Firefox
run_test("chrome")
run_test("firefox")