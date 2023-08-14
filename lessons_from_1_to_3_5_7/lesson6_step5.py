import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
    browser.get(link)
    txt = str(math.ceil(math.pow(math.pi, math.e)*10000))
    searched_link = browser.find_element(By.LINK_TEXT, txt)
    searched_link.click()

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(20)
    browser.quit()