import unittest
from selenium import webdriver
from locators import Common, Main, Product, Cart, User


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
        feature_product = browser.find_elements_by_css_selector(Main.featured.products['css'])[0]
        product_name = feature_product.find_element_by_css_selector(Main.featured.names['css']).text
        feature_product.click()
        # Click on the button on the Product page
        browser.find_element_by_css_selector(Product.add_to_wishlist['css']).click()
        # Click on the link in the alert-success block
        browser.find_element_by_css_selector(Common.alert.success.login['css']).click()
        # Login from the user authorization form
        browser.find_element_by_css_selector(Common.user_login.email_input['css']).send_keys("test2@mail.ru")
        browser.find_element_by_css_selector(Common.user_login.password_input['css']).send_keys("test")
        browser.find_element_by_css_selector(Common.user_login.login_button['css']).click()
        # Go to favorites section
        browser.find_element_by_css_selector(User.right_menu.wish_list['css']).click()
        # Checking the link with the text of the selected product
        browser.find_element_by_link_text(product_name)

    def test_add_to_cart(self):
        browser = self.driver
        browser.get('http://opencart/')
        # Click on the first element in the block featured
        feature_product = browser.find_elements_by_css_selector(Main.featured.products['css'])[0]
        product_name = feature_product.find_element_by_css_selector(Main.featured.names['css']).text
        feature_product.click()
        # Click on the button on the Product page
        browser.find_element_by_css_selector(Product.add_to_cart['css']).click()
        # Click on the link in the alert-success block
        browser.find_element_by_css_selector(Common.alert.success.to_cart['css']).click()
        # Checking the link with the text of the selected product
        browser.find_element_by_link_text(product_name)
        # Click on the Checkout button on the cart page
        browser.find_element_by_css_selector(Cart.bottom_btn.checkout['css']).click()
        # Login from the user authorization form
        browser.find_element_by_css_selector(Common.user_login.email_input['css']).send_keys("test2@mail.ru")
        browser.find_element_by_css_selector(Common.user_login.password_input['css']).send_keys("test")
        browser.find_element_by_css_selector(Common.user_login.login_button['css']).click()
        # Waiting for the payment registration form to be displayed
        browser.find_elements_by_css_selector(User.paymnet_form.it['css'])


if __name__ == "__main__":
    unittest.main()
