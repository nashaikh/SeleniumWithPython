from lib2to3.pgen2 import driver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Assuming you have already imported necessary modules and set up the WebDriver instance (driver)

# Wait for the element to be visible
wait = WebDriverWait(driver, 10)
username = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "custom-input ng-pristine ng-invalid ng-touched")))

# Check if the element is displayed
if username.is_displayed():
    # Perform actions on the element
    username.send_keys("example_username")
