# Задание: кликаем по checkboxes и radiobuttons (капча для роботов)

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    #1 Открываем страницу https://suninjuly.github.io/math.html.
    link = "https://suninjuly.github.io/math.html"  
    browser = webdriver.Chrome()
    browser.get(link)   
	
    import math
    #3 Считаем математическую функцию от x.
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))    
    
    #2 код: считаем значение для переменной x.  
    x_element = browser.find_element(By.ID, 'input_value')    
    x = x_element.text
    y = calc(x)
    
    #4 Вводим ответ в текстовое поле.
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)  

    #5 Отмечаем checkbox "I'm the robot".
    option1 = browser.find_element(By.ID, "robotCheckbox")   
    option1.click()

    #6 Выбираем radiobutton "Robots rule!".
    option1 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")   
    option1.click()

    #7 Нажимаем на кнопку Submit.
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")    
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
