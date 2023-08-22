import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

os.chdir('/home/dmitry/PycharmProjects/stepik_auto_tests_selenium/test_lesson_3_6/')

lnks = ['https://stepik.org/lesson/236895/step/1'
        ,'https://stepik.org/lesson/236896/step/1'
        ,'https://stepik.org/lesson/236897/step/1'
        ,'https://stepik.org/lesson/236898/step/1'
        ,'https://stepik.org/lesson/236899/step/1'
        ,'https://stepik.org/lesson/236903/step/1'
        ,'https://stepik.org/lesson/236904/step/1'
        ,'https://stepik.org/lesson/236905/step/1']
@pytest.mark.parametrize('link', lnks)
def test_guest_should_see_login_link(browser, login_pass, link):
    browser.get(link)
    enter_lnk = browser.find_element(By.CSS_SELECTOR, "a#ember33")
    enter_lnk.click()
    login_inp = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
    passw_inp = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    entr_btn = browser.find_element(By.CSS_SELECTOR, "#login_form button")
    login_inp.send_keys(login_pass['login'])
    passw_inp.send_keys(login_pass['pass'])
    entr_btn.click()

    time.sleep(4)

    text_area = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
    answer = math.log(int(time.time()))
    text_area.send_keys(answer)
    send_btn = browser.find_element(By.CSS_SELECTOR, "div.attempt__actions button")
    send_btn.click()
    assert browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text == "Correct!"
    time.sleep(5)

