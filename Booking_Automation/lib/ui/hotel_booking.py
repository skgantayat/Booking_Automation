from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class HotelBook():
    def __init__(self,driver):
        self.driver = driver
    def get_hotels_button(self):
        try:
            return self.driver.find_element_by_partial_link_text("Hotels")
        except:
            return None

    def get_where_textbox(self,text):
        try:
            element = self.driver.find_element_by_id("Tags")

            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.visibility_of(element)).send_keys(text)


            link = self.driver.find_element_by_link_text(text)

            wait.until(EC.visibility_of(link))
            link.send_keys(text, Keys.TAB)


        except:
            return None

    def get_checkin_button_button(self):
        try:
            return self.driver.find_element_by_id("CheckInDate")
        except:
            return None
    def get_checkout_button(self):
        try:
            return self.driver.find_element_by_id("CheckOutDate")
        except:
            return None
    def get_searchhotel_button(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            element = self.driver.find_element_by_id("SearchHotelsButton")
            wait.until(EC.visibility_of(element))
            return element
        except:
            return None
