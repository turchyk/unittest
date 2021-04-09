from locators import Common


class UserPage:

    def __init__(self, driver):
        self.driver = driver

    def login_user(self, email, password):
        browser = self.driver
        browser.find_element_by_css_selector(Common.user_login.email_input['css']).send_keys(email)
        browser.find_element_by_css_selector(Common.user_login.password_input['css']).send_keys(password)
        browser.find_element_by_css_selector(Common.user_login.login_button['css']).click()