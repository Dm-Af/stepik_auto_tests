import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
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

    @pytest.mark.smoke
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    @pytest.mark.regression
    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# @pytest.mark.smoke и @pytest.mark.regression - декораторы, которые создают маркировку "mark" тестов,
# чтобы их можно было бы вызывать из консоли обособленно. Например, такой командой:
# pytest -svm smoke lesson_3_5_2__PyTest_test_marking.py
#
# или, наоборот, запустить все тесты, кроме маркированного:
# pytest -svm "not smoke" lesson_3_5_2__PyTest_test_marking.py
#
# за выбор теста по марке отвечает параметр -m
# чтобы не выходило предупреждение о незарегистрированной марке, нужно их добавить в pytest.ini
#
# Так же можно маркировать целый тестовый класс.
# В этом случае маркировка будет применена ко всем тестовым методам, входящим в класс.