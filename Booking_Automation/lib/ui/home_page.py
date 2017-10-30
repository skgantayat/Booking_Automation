from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage():
    def __init__(self,driver):
        self.driver = driver
    def get_hotels_button(self):
        try:
            return self.driver.find_element_by_partial_link_text("Hotels")
        except:
            return None
    def get_flight_button(self):
        try:
            return self.driver.find_element_by_partial_link_text("Flights")
        except:
            return None
    def get_yourtrips_link(self):
        try:
            return self.driver.find_element_by_id("userAccountLink")
        except:
            return None
    def wait_for_home_page(self):
        wait = WebDriverWait(self.driver, 30)
        wait.until(EC.title_is("Cleartrip - Flights, Hotels, Local, Trains, Packages"))
