from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class Flightbook():
    def __init__(self, driver):
        self.driver = driver

    def get_flight_button(self):
        try:
            return self.driver.find_element_by_partial_link_text("Flights")
        except:
            return None

    def get_from_textbox(self,text):
        try:
            element = self.driver.find_element_by_id("FromTag")
            wait = WebDriverWait(self.driver,30)

            wait.until(EC.visibility_of(element)).send_keys(text)

            link = self.driver.find_element_by_partial_link_text("Bangalore, IN -")
            wait.until(EC.visibility_of(link))
            time.sleep(5)
            link.send_keys(text, Keys.ARROW_DOWN + Keys.ENTER)
        except:
            return None

    def get_to_textbox(self, text):
        try:
            element = self.driver.find_element_by_id("ToTag")
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.visibility_of(element)).send_keys(text)

            link = self.driver.find_element_by_partial_link_text("New Delhi, IN -")
            wait.until(EC.visibility_of(link))
            time.sleep(5)
            link.send_keys(text, Keys.ARROW_DOWN + Keys.ENTER)
        except:
            return None

    def get_depart_button(self):
        try:
            self.driver.find_element_by_id("DepartDate").click()
            self.driver.find_element_by_xpath("html/body/div[1]/div[2]/table/tbody/tr[1]/td[3]/a").click()

        except:
            return None
    def get_searchflight_button(self):
        try:
            return self.driver.find_element_by_id("SearchBtn")
        except:
            return None

