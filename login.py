import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestLogin(unittest.TestCase): # test scenario

    def setUp(self):
        self.browser = webdriver.Chrome(ChromeDriverManager().install())

    def test_success_login(self): #test cases 'Verifikasi Login Sukses'
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys("Admin")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        
    def test_failed_login_invalid_username(self): #test cases 'Verifikasi Login Gagal invalid username'
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys("test")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        error_message = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.oxd-alert-content-text").text
        self.assertIn("Invalid credentials", error_message)

    def test_failed_login_invalid_username(self): #test cases 'Verifikasi Login Gagal invalid username'
        driver = self.browser
        driver.implicitly_wait(10)
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(By.NAME, "username").send_keys("test")
        driver.find_element(By.NAME, "password").send_keys("admin123")
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        error_message = driver.find_element(By.CSS_SELECTOR, ".oxd-text.oxd-text--p.oxd-alert-content-text").text
        self.assertIn("Invalid credentials", error_message)    

if __name__ == '__main__':
    unittest.main()