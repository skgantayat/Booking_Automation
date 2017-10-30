import unittest
from lib.ui.flight_booking import Flightbook
from util.config.create_driver import CreateDriver
from selenium.webdriver.common.keys import Keys
import time

class FlightBooking_US109(unittest.TestCase):
    def setUp(self):
        self.driver = CreateDriver().instance()
        self.flight_book = Flightbook(self.driver)
    def tearDown(self):
        self.driver.close()
    def test_flightbook_tc_219(self):
        self.flight_book.get_flight_button().click()
        self.flight_book.get_from_textbox("Bangalore")
        self.flight_book.get_to_textbox("New Delhi")
        self.flight_book.get_depart_button()
        self.flight_book.get_searchflight_button().click()