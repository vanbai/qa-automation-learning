from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    price = WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
    browser.find_element(By.ID, "book").click()

    # находим значение выражения
    x_element = browser.find_element(By.ID, "input_value").text
    answer = calc(int(x_element))

    # вводим полученное значение в поле
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(str(answer))

    # Отправляем заполненную форму
    browser.find_element(By.ID, "solve").click()

    # ждем загрузки страницы

    ans = browser.switch_to.alert
    congrats = ans.text
    time.sleep(1)

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
    print(congrats.split(': ')[-1])

