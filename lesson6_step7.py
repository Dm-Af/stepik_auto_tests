import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print(__file__, '-> start work...')
link = "http://suninjuly.github.io/huge_form.html"
try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--remote-debugging-port=9222")
    browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
    browser.get(link)

    inputs = browser.find_elements(By.TAG_NAME, "input")
    for input in inputs:
        input.send_keys("Bla-Bla-Bla")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()
finally:
    time.sleep(20)
    browser.quit()
    print(__file__, '-> end work!!!')