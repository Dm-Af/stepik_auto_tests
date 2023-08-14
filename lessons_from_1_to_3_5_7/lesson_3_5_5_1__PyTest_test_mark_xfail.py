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

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")

# @pytest.mark.xfail - декоратор, которые создают маркировку позволяющую проверять заведомо непроходящий тест,
# упавший тест теперь отмечен как xfail, но результат прогона тестов помечен как успешный
# Когда баг починят, мы это узнаем, так как теперь тест будет отмечен как XPASS
# (“unexpectedly passing” — неожиданно проходит)
# Если маркировка xfail имеет параметр: reason="something", то можно использовать ключ -r при запуске,
# чтобы увидеть причину падения теста:
# pytest -rx -v