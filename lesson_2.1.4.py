import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/math.html"
try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
    browser.get(link)
    time.sleep(1)
    x = browser.find_element(By.ID, "input_value").text
    rez = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(rez)
    check1 = browser.find_element(By.ID, "robotCheckbox")
    check1.click()
    radio1 = browser.find_element(By.ID, "robotsRule")
    radio1.click()
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    time.sleep(10)

finally:
    browser.quit()