import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://app.sharedaffairs.com/auth/sign-in")
        time.sleep(5)
        self.assertIn("Shared Affairs", driver.title)
        email = driver.find_element(By.NAME, "email")
        email.send_keys("testingkite6@gmail.com")
        password = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Password*']")
        password.send_keys("FMKTesting@123")
        submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        submit.is_displayed()
        submit.click()
        time.sleep(10)
        otp = driver.find_element(By.CSS_SELECTOR, "input[placeholder='OTP*']")
        otp.send_keys("123")
        otpSubmit = driver.find_element(By.CSS_SELECTOR, ".custom-btn-auth.justify-content-center.align-items-center"
                                                         ".my-2")
        otpSubmit.click()
        self.assertIn("Shared Affairs", driver.title)








    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()