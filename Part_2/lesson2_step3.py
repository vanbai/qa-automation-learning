from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # находим значение выражения
    x = browser.find_element(By.ID, "num1").text
    y = browser.find_element(By.ID, "num2").text
    sum1 = str(int(x) + int(y))

    # находим полученное значение в списке и выбираем его
    browser.find_element(By.TAG_NAME, "select").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{sum1}'").click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # ждем загрузки страницы
    time.sleep(20)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
