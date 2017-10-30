from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class SignIn():
    def __init__(self, driver):
        self.driver = driver
    def get_yourtrips_link(self):
        try:
            return self.driver.find_element_by_id("userAccountLink")
        except:
            return None
    def get_signin_button(self):
        try:
            return self.driver.find_element_by_id("SignIn")
        except:
            return None
    def get_switch_frame(self):
        try:
            wait = WebDriverWait(self.driver, 30)
            element = self.driver.switch_to_frame("modal_window")
            wait.until(EC.frame_to_be_available_and_switch_to_it(element))

        except:
            return None

    def get_username_textbox(self):
        try:
            return self.driver.find_element_by_id("email")
        except:
            return None
    def get_password_textbox(self):
        try:
            self.driver.find_element_by_id("password")
        except:
            return None
    def get_login_button(self):
        try:
            self.driver.find_element_by_id("signInButton")
        except:
            return None
    def get_errormsg_text(self):
        wait =WebDriverWait(self.driver, 30)
        element =self.driver.find_element_by_tag_name("span")
        wait.until(EC.visibility_of(element))
        assert element.txt == "There were errors in your submission"
        self.driver.switch_to_default_content()




