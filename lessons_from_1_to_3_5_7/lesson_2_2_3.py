import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

links = ["http://suninjuly.github.io/selects1.html"
         ,"http://suninjuly.github.io/selects2.html"]
for link in links:
    try:
        #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--remote-debugging-port=9222")
        browser = webdriver.Chrome(options=chrome_options)
        #-------------------------------------------------------------------
        browser.get(link)
        num1 = int(browser.find_element(By.ID, "num1").text)
        num2 = int(browser.find_element(By.ID, "num2").text)

        slct = Select(browser.find_element(By.ID, "dropdown"))
        slct.select_by_visible_text(str(num1 + num2))

        button = browser.find_element(By.TAG_NAME, "button")
        button.click()

        time.sleep(10)

    finally:
        browser.quit()