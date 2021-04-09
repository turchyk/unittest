import unittest
from selenium import webdriver
from locators import Common, Product, Cart, User
from page_objects import MainPage, UserPage


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
        # Click on the first element in the block featured
        product_name = MainPage(browser).click_featured_product(1)
        # Click on the button on the Product page
        browser.find_element_by_css_selector(Product.add_to_wishlist['css']).click()
        # Click on the link in the alert-success block
        browser.find_element_by_css_selector(Common.alert.success.login['css']).click()
        # Login from the user authorization form
        UserPage(browser).login_user(email="turchikz@gmail.com", password="0000")
        # Go to favorites section
        browser.find_element_by_css_selector(User.right_menu.wish_list['css']).click()
        # Checking the link with the text of the selected product
        browser.find_element_by_link_text(product_name)

    def test_add_to_cart(self):
        browser = self.driver
        browser.get('http://opencart/')
        # Click on the first element in the block featured
        product_name = MainPage(browser).click_featured_product(1)
        # Click on the button on the Product page
        browser.find_element_by_css_selector(Product.add_to_cart['css']).click()
        # Click on the link in the alert-success block
        browser.find_element_by_css_selector(Common.alert.success.to_cart['css']).click()
        # Checking the link with the text of the selected product
        browser.find_element_by_link_text(product_name)
        # Click on the Checkout button on the cart page
        browser.find_element_by_css_selector(Cart.bottom_btn.checkout['css']).click()
        # Login from the user authorization form
        UserPage(browser).login_user(email="turchikz@gmail.com", password="0000")
        # Waiting for the payment registration form to be displayed
        browser.find_elements_by_css_selector(User.paymnet_form.it['css'])


if __name__ == "__main__":
    unittest.main()
