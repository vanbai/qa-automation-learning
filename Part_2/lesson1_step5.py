from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значение выражения
    x_element = browser.find_element(By.ID, "input_value")
    x = int(x_element.text)
    y = calc(x)

    # вводим полученное значение в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(y))

    # выбираем checkbox
    checkbox1 = browser.find_element(By.ID, "robotCheckbox")
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
