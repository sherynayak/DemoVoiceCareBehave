from selenium.webdriver.common.by import By

from Features.Pages.AccountSuccessPage import AccountSuccessPage
from Features.Pages.BasePage import BasePage


class RegisterPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    first_name_field_xpath = "//input[@id='input-firstname']"
    last_name_field_xpath = "//input[@id='input-lastname']"
    email_field_xpath = "//input[@id='input-email']"
    telephone_field_xpath = "//input[@id='input-telephone']"
    password_field_xpath = "//input[@id='input-password']"
    confirm_password_field_xpath = "//input[@id='input-confirm']"
    agree_checkbox_xpath = "//input[@name='agree']"
    continue_button_xpath = "//input[@value='Continue']"
    alert_email_message_xpath = "//div[@class='alert alert-danger alert-dismissible']"
    warning_message_xpath = "//div[@class='text-danger']"

    def enter_first_name(self, first_name):
        self.type_on_element("first_name_field_xpath", self.first_name_field_xpath, first_name)
        # self.driver.find_element(By.XPATH, self.first_name_field_xpath).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.type_on_element("last_name_field_xpath", self.last_name_field_xpath, last_name)
        # self.driver.find_element(By.XPATH, self.last_name_field_xpath).send_keys(last_name)

    def enter_email_address(self, email_id):
        self.type_on_element("email_field_xpath", self.email_field_xpath, email_id)
        # self.driver.find_element(By.XPATH, self.email_field_xpath).send_keys(email_id)

    def enter_telephone_number(self, telephone_number):
        self.type_on_element("telephone_field_xpath", self.telephone_field_xpath, telephone_number)
        # self.driver.find_element(By.XPATH, self.telephone_field_xpath).send_keys(telephone_number)

    def enter_password(self, password):
        self.type_on_element("password_field_xpath", self.password_field_xpath, password)
        # self.driver.find_element(By.XPATH, self.password_field_xpath).send_keys(password)

    def enter_confirm_password(self, confirm_password):
        self.type_on_element("confirm_password_field_xpath", self.confirm_password_field_xpath, confirm_password)
        # self.driver.find_element(By.XPATH, self.confirm_password_field_xpath).send_keys(confirm_password)

    def choose_agree_checkbox(self):
        self.click_on_element("agree_checkbox_xpath", self.agree_checkbox_xpath)
        # self.driver.find_element(By.XPATH, self.agree_checkbox_xpath).click()

    def click_continue_button(self):
        self.click_on_element("continue_button_xpath", self.continue_button_xpath)
        # self.driver.find_element(By.XPATH, self.continue_button_xpath).click()
        return AccountSuccessPage(self.driver)

    def display_alert_email_message(self, expected_warning_message):
        return self.elements_contain_text("alert_email_message_xpath", self.alert_email_message_xpath, expected_warning_message)
        # return self.driver.find_element(By.XPATH, self.alert_email_message_xpath).text.__contains__(expected_warning_message)

    def display_warning_message(self, expected_warning_message):
        return self.elements_contain_text("warning_message_xpath", self.warning_message_xpath, expected_warning_message)
        # return self.driver.find_element(By.XPATH, self.warning_message_xpath).text.__contains__(expected_warning_message)
