# Задание: запуск автотестов для разных языков интерфейса
# lesson3_6_step10

import time
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    add_to_basket_button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert add_to_basket_button.is_displayed(), "Add to basket button is unvisible" 



 

