from selenium.webdriver.common.by import By

from Features.Pages.BasePage import BasePage


class AccountSuccessPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    confirm_message_xpath = "//div[@id='content']/h1"

    def display_confirm_message(self, expected_result):
        return self.verify_equals("confirm_message_xpath", self.confirm_message_xpath, expected_result)
        # return self.driver.find_element(By.XPATH, self.confirm_message_xpath).text.__eq__(expected_result)


