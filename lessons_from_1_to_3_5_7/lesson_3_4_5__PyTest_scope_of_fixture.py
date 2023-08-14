import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

#область покрытия фикстур:
@pytest.fixture(scope="class") #Допустимые значения: “function”, “class”, “module”, “session”.
def browser():
    print("\nstart browser for test..")
    # ---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    # -------------------------------------------------------------------
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()

class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")
        print("finish test2")

# Браузер открылся один раз и тесты последовательно выполнились в этом браузере.
# Но! Лучше открывать каждый раз новый браузер.
# Фикстуры, которые занимают много времени для запуска и ресурсов (обычно это работа с базами данных),
# можно вызывать и один раз за сессию запуска тестов.
