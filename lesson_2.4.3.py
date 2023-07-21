import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/wait1.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
    browser.get(link)
    indicator = False
    i = 0
    while not indicator:
        try:
            button = browser.find_element(By.ID, "verify")
            button.click()
            indicator = True
        except:
            i += 1
            print(i)
        time.sleep(0.2)
    message = browser.find_element(By.ID, "verify_message")

    assert "successful" in message.text

    time.sleep(3)

finally:
    browser.quit()