# Файл с фикстурами (функциями настроек PyTest)
# Фикстуры автоматически будут импортироваться из него в файлы с тестами
# При наличии файла conftest.py в поддиректориях могут возникать коллизии,
# связанные с переопределением фикстур!

import pytest
from selenium import webdriver
import json

@pytest.fixture(scope="function")
def browser():
    # ---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    # -------------------------------------------------------------------
    browser.implicitly_wait(20) # ожидаю максимум 20 сек для каждого элемента
    yield browser
    browser.quit()

@pytest.fixture(scope="function")
def login_pass():
    with open('../my_login.json', 'r', encoding='utf-8') as file:
        my_login = json.load(file)
    yield my_login
