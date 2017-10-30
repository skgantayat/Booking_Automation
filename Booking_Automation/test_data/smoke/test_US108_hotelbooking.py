import unittest
from lib.ui.hotel_booking import HotelBook
from util.config.create_driver import CreateDriver
from selenium.webdriver.common.keys import Keys
import time

class HotelBooking_US108(unittest.TestCase):
    def setUp(self):
        self.driver = CreateDriver().instance()
        self.hotel_book = HotelBook(self.driver)
    def tearDown(self):
        time.sleep(10)
        self.driver.close()
    def test_hotelbook_tc_218(self):
        self.hotel_book.get_hotels_button().click()
        self.hotel_book.get_where_textbox("Indiranagar, Bangalore")
        #time.sleep(60)
        self.hotel_book.get_checkin_button_button().send_keys(Keys.ARROW_RIGHT + Keys.ENTER)
        self.hotel_book.get_checkout_button().send_keys(Keys.ARROW_RIGHT + Keys.ENTER)
        self.hotel_book.get_searchhotel_button().click()
