import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import math

os.chdir('/home/dmitry/PycharmProjects/stepik_auto_tests_selenium/test_lesson_3_6/')

lnks = [
        'https://stepik.org/lesson/236895/step/1'
        ,'https://stepik.org/lesson/236896/step/1'
        ,'https://stepik.org/lesson/236897/step/1'
        ,'https://stepik.org/lesson/236898/step/1'
        ,'https://stepik.org/lesson/236899/step/1'
        ,'https://stepik.org/lesson/236903/step/1'
        ,'https://stepik.org/lesson/236904/step/1'
        ,'https://stepik.org/lesson/236905/step/1'
        ]
@pytest.mark.parametrize('link', lnks)
def test_guest_should_see_login_link(browser, login_pass, link):
    browser.get(link)
    enter_lnk = browser.find_element(By.CSS_SELECTOR, "a.navbar__auth_login")
    enter_lnk.click()
    login_inp = browser.find_element(By.CSS_SELECTOR, 'input[name="login"]')
    passw_inp = browser.find_element(By.CSS_SELECTOR, 'input[name="password"]')
    entr_btn = browser.find_element(By.CSS_SELECTOR, "#login_form button")
    login_inp.send_keys(login_pass['login'])
    passw_inp.send_keys(login_pass['pass'])
    entr_btn.click()

    # Если уже решено, нужно нажать кнопку "решить заново"
    try:
        btn_reload = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.again-btn"))
        )
        btn_reload.click()
    except TimeoutException:
        print("'решить заново' - отсутствует")
    finally:
        # Ждем пока поле textarea не очистится и станет активным(пропадет атрибут "disabled"),
        # при этом не используем time.sleep!
        WebDriverWait(browser, 10).until_not(
            EC.element_attribute_to_include((By.CSS_SELECTOR, 'textarea.ember-text-area'), 'disabled')
        )

        answer = math.log(int(time.time()))
        textarea = WebDriverWait(browser, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "textarea.ember-text-area"))
        )
        textarea.send_keys(answer)
        button_entr = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission"))
        )
        button_entr.click()
        site_response = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//p[@class="smart-hints__hint"]'))
        )
        assert site_response.text == "Correct!"
        time.sleep(2)
