from core.web_driver import WebDriverFactory
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



def check_login_credentials(username: str, password: str) -> bool:
    driver = WebDriverFactory.create_driver()
    try:
        driver.get("https://thinking-tester-contact-list.herokuapp.com/")
        sleep(3)
        username_field = driver.find_element(By.ID, "email")
        password_field = driver.find_element(By.ID, "password")

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = driver.find_element(By.ID, "submit")
        login_button.click()

        try:
            error_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.ID, "error"))
            )
            print("Error message found: Login failed.")
            driver.save_screenshot(f"screenshots/check_login_fail_{username}_{password}.png")
            return False
        except TimeoutException:
            print("No error message found: Login successful or error not displayed.")

        return True
    except Exception as e:
        print(e)
    finally:
        driver.quit()