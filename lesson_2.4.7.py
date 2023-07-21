import time, math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
    browser.implicitly_wait(5)
    browser.get(link)

    button1 = browser.find_element(By.ID, "book")
    text = WebDriverWait(browser, 10).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button1.click()

    x = browser.find_element(By.ID, "input_value").text
    rez = calc(x)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(rez)
    button2 = browser.find_element(By.ID, "solve")
    button2.click()

    time.sleep(10)

finally:
    browser.quit()