import time
from selenium import webdriver
from selenium.webdriver.common.by import By

print(__file__, '-> start work...')
links = ("http://suninjuly.github.io/registration1.html", "http://suninjuly.github.io/registration2.html")
for link in links:
    print("Try to processing", link)
    try:
    #---------UBUNTU 22.04 - PyCharm - Don't work without this!---------
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--remote-debugging-port=9222")
        browser = webdriver.Chrome(options=chrome_options)
    #-------------------------------------------------------------------
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control first"]')
        input1.send_keys("MyName")
        input2 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control second"]')
        input2.send_keys("MyLastName")
        input3 = browser.find_element(By.XPATH, '//div[@class="first_block"]//input[@class="form-control third"]')
        input3.send_keys("MyEmail@email.email")

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
    finally:
        time.sleep(10)
        browser.quit()

print(__file__, '-> end work!!!')

