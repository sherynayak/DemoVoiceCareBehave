from selenium.webdriver.common.by import By

from Features.Pages.BasePage import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    valid_product_link_text = "HP LP3065"
    invalid_product_message_xpath = "//div[@id='content']/p[2]"

    def display_status_of_product(self):
        return self.display_status("valid_product_link_text", self.valid_product_link_text)
        # return self.driver.find_element(By.LINK_TEXT, self.valid_product_link_text).is_displayed()

    def display_invalid_product_message(self, expected_result):
        return self.verify_equals("invalid_product_message_xpath", self.invalid_product_message_xpath, expected_result)
        # return self.driver.find_element(By.XPATH, self.invalid_product_message_xpath).text.__eq__(expected_result)
