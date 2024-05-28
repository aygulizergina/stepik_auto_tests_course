# Задание на execute_script

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://SunInJuly.github.io/execute_script.html"  
    browser = webdriver.Chrome()
    browser.get(link)     
	
    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))    
    
    #код
    x_element = browser.find_element(By.ID, 'input_value')    
    x = x_element.text
    y = calc(x)    

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)  

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

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
