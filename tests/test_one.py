import unittest
from selenium import webdriver
from page_objects import MainPage, UserPage, ProductPage, CartPage
from page_objects.common import Alert


class TestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.implicitly_wait(10)

    def tearDown(self):
        driver = self.driver
        driver.close()

    def test_add_to_wish_list(self):
        browser = self.driver
        browser.get('http://opencart/')
        product_name = MainPage(browser).click_featured_product(1)
        ProductPage(browser).add_to_wishlist()
        Alert(browser).click_login()
        UserPage(browser).login_user(email="turchikz@gmail.com", password="0000")
        UserPage(browser).open_wishlist()
        UserPage(browser).verify_product(product_name)

    def test_add_to_cart(self):
        browser = self.driver
        browser.get('http://opencart/')
        product_name = MainPage(browser).click_featured_product(1)
        ProductPage(browser).add_to_cart()
        Alert(browser).click_to_cart()
        CartPage(browser).verify_product(product_name)
        CartPage(browser).checkout()
        UserPage(browser).login_user(email="turchikz@gmail.com", password="0000")
        UserPage(browser).verify_payment_form()


if __name__ == "__main__":
    unittest.main()
