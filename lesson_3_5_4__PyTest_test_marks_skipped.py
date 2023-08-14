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

    @pytest.mark.skip
    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

# @pytest.mark.skip - декоратор, которые создают маркировку позволяющую игнорировать тест,
