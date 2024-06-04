# Задание: оформляем тесты в стиле unittest 

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
links = ["http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html"]


class TestReg(unittest.TestCase):
    for i in links:
        browser.get(i)
        
        def test_registration_form(self):

            input1 = browser.find_element(By.CSS_SELECTOR, ".first_block .first")
            input1.send_keys("Ivan")
            input2 = browser.find_element(By.CSS_SELECTOR, ".first_block .second")
            input2.send_keys("Petrov")
            input3 = browser.find_element(By.CSS_SELECTOR, ".first_block .third")
            input3.send_keys("Petrov@test.ru")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()
            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


if __name__ == "__main__":
    unittest.main()

