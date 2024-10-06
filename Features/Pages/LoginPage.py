from selenium.webdriver.common.by import By

from Features.Pages.AccountPage import AccountPage
from Features.Pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    email_id_field_xpath = "//input[@id='input-email']"
    password_field_xpath = "//input[@id='input-password']"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"

    def enter_email_id(self, email_text):
        self.type_on_element("email_id_field_xpath", self.email_id_field_xpath, email_text)
        # self.driver.find_element(By.XPATH, self.email_id_field_xpath).send_keys(email_text)

    def enter_password(self, password_text):
        self.type_on_element("password_field_xpath", self.password_field_xpath, password_text)
        # self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password_text)

    def click_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        # self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return AccountPage(self.driver)

    def display_warning_message(self, expected_war_msg):
        return self.elements_contain_text("warning_message_xpath", self.warning_message_xpath, expected_war_msg)
        # return self.driver.find_element(By.XPATH, self.warning_message_xpath).text.__contains__(expected_war_msg)


