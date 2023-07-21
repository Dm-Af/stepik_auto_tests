import selenium
from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from stepik_auto_tests_selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random

try:
    link = "http://suninjuly.github.io/registration2.html"
    # ---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    # -------------------------------------------------------------------
    # browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    inputs = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
    for element in inputs:
        element.send_keys(str(random.random()))
        time.sleep(2)

        # Добавляем проверку на количество обязательных полей
        required_fields = browser.find_elements(By.CSS_SELECTOR, 'input[required]')
        assert len(required_fields) == 3, f"Требуется заполнить {len(required_fields)} поля, вместо 3"

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(3)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()
