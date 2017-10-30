import json
from selenium import webdriver

class CreateDriver():
    def instance(self):
        data = json.load(open('./test_config/config.json'))
        browser_info = data['browser']
        url = data['url']
        if browser_info == "chrome":
            chrome_path = './broweser_exe/chromedriver.exe'
            driver = webdriver.Chrome(chrome_path)
        else:
            print('invalid browser selection')
        driver.maximize_window()
        driver.implicitly_wait(30)
        driver.get("https://www.cleartrip.com")
        return driver
