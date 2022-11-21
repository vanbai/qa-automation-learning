from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значение выражения
    x_element = browser.find_element(By.ID, "input_value").text
    answer = calc(int(x_element))

    # вводим полученное значение в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(answer))

    # скроллим страницу и выбираем checkbox
    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox1)
    checkbox1.click()

    # выбираем radiobutton
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(20)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
