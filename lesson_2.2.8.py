import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'txt_file_for_send.txt')
link = "http://suninjuly.github.io/file_input.html"
try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
    browser.get(link)
    name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    name.send_keys("Dm")
    lastname = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    lastname.send_keys("Af")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    email.send_keys("e@mail.ru")
    file_btn = browser.find_element(By.ID, "file")
    file_btn.send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(10)

finally:
    browser.quit()