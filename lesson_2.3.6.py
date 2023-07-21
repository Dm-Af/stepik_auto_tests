import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
    browser.get(link)
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    new_window = browser.window_handles[-1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, "input_value").text
    rez = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(rez)
    button1 = browser.find_element(By.TAG_NAME, "button")
    button1.click()

    time.sleep(10)

finally:
    browser.quit()