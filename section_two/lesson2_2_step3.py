# Задание: работа с выпадающим списком

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/selects1.html"  
    browser = webdriver.Chrome()
    browser.get(link)      
	
    def calc(x,y):
        return str((int(x))+(int(y)))    

    #код
    x_element = browser.find_element(By.ID, "num1")
    x = x_element.text    
    y_element = browser.find_element(By.ID, "num2")
    y = y_element.text
    z = calc(x,y)
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(z) 
        
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
