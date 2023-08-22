import pytest
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math
import selenium

os.chdir('/home/dmitry/PycharmProjects/stepik_auto_tests_selenium/test_lesson_3_6/')

lnks = [#'https://stepik.org/lesson/236895/step/1'
        #,'https://stepik.org/lesson/236896/step/1'
        #,'https://stepik.org/lesson/236897/step/1'
        'https://stepik.org/lesson/236898/step/1'
        ,'https://stepik.org/lesson/236899/step/1'
        ,'https://stepik.org/lesson/236903/step/1'
        ,'https://stepik.org/lesson/236904/step/1'
        ,'https://stepik.org/lesson/236905/step/1']
@pytest.mark.parametrize('link', lnks)
def test_guest_should_see_login_link(browser, login_pass, link):
    # link = f"https://stepik.org/lesson/236895/step/1"
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

    # text_area = WebDriverWait(browser, 5).until(EC.element_to_be_clickable(By.CSS_SELECTOR, "#ember98"))
    # WebDriverWait(browser, 5).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#ember98"),"Напишите ваш ответ здесь..."))
    # text_area = WebDriverWait(browser, 5).until(EC.invisibility_of_element(By.CSS_SELECTOR, "#ember98"))
    # text_area = browser.find_element(By.CSS_SELECTOR, "#ember98")

    # Если уже решено, нужно нажать кнопку "решить заново"
    # try:
    #     btn_reload = WebDriverWait(browser, 4).until(EC.presence_of_element_located(By.XPATH, '//button[@class="again-btn white"]'))
    # btn_reload = browser.find_element(By.XPATH, '//button[@class="again-btn white"]')
    # btn_reload.click()
    # time.sleep(3)


    text_area = browser.find_element(By.CSS_SELECTOR, "textarea.ember-text-area")
    # text_area = WebDriverWait(browser, 3).until(EC.element_to_be_clickable(By.CSS_SELECTOR, "textarea.ember-text-area"))
    # text_area = WebDriverWait(browser, 3).until(EC.element_to_be_selected("textarea.ember-text-area"))
    answer = math.log(int(time.time()))
    text_area.send_keys(answer)
    send_btn = browser.find_element(By.CSS_SELECTOR, "div.attempt__actions button")
    send_btn.click()
    # assert browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"][text()="Correct!"]')
    assert browser.find_element(By.XPATH, '//p[@class="smart-hints__hint"]').text == "Correct!"
    time.sleep(5)
    # print(login_pass['login'], login_pass['pass'])
    # The owls are not what they seem!
