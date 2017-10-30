import unittest
from lib.ui.youraccount import SignIn
from util.config.create_driver import CreateDriver
from selenium.webdriver.common.keys import Keys
import time

class SignIn_US110(unittest.TestCase):
    def setUp(self):
        self.driver = CreateDriver().instance()
        self.signin = SignIn(self.driver)
    def tearDown(self):
        self.driver.close()
    def test_signin_tc_220(self):
        self.signin.get_yourtrips_link().click()
        self.signin.get_signin_button().click()
        self.signin.get_switch_frame()
        self.signin.get_username_textbox().send_keys("asd")
        self.signin.get_password_textbox().send_keys("qwe")
        self.signin.get_login_button().click()
        self.signin.get_errormsg_text()
