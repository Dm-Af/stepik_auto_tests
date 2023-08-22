from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument("--profile-root")
browser = webdriver.Firefox(options=firefox_options)
# browser = webdriver.Firefox()

browser.get("https://stepik.org/lesson/25969/step/8")