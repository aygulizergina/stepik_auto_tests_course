# Задание: поиск сокровища с помощью get_attribute

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "http://suninjuly.github.io/get_attribute.html"  
    browser = webdriver.Chrome()
    browser.get(link)      
	
    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))    
    
    #код
    x_element = browser.find_element(By.ID, "treasure")    
    x_elementt = x_element.get_attribute("valuex")
    x = x_elementt
    y = calc(x)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)  

    option1 = browser.find_element(By.ID, "robotCheckbox")   
    option1.click()
    option1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")   
    option1.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
