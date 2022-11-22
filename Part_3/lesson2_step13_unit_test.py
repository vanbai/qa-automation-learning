from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first[placeholder][required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".second[placeholder][required]")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".third[placeholder][required]")
        input3.send_keys("test@test.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        successful_text = "Congratulations! You have successfully registered!"
        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, successful_text, "Test wasn't accepted. Texts are not equal")

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Заполняем обязательные поля
        input1 = browser.find_element(By.CSS_SELECTOR, ".first[placeholder][required]")
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR, ".second[placeholder][required]")
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, ".third[placeholder][required]")
        input3.send_keys("test@test.com")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        successful_text = "Congratulations! You have successfully registered!"
        # проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, successful_text, "Test wasn't accepted. Texts are not equal")

        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()