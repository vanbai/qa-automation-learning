from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # жмем "магическую" кнопку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # принимаем алерт
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(2)

    # находим значение выражения
    x_element = browser.find_element(By.ID, "input_value").text
    answer = calc(int(x_element))

    # вводим полученное значение в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(answer))

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    ans = browser.switch_to.alert
    congrats = ans.text
    time.sleep(2)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    print(congrats.split(': ')[-1])

