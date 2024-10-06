from selenium.webdriver.common.by import By

from Features.Pages.BasePage import BasePage
from Features.Pages.LoginPage import LoginPage
from Features.Pages.RegisterPage import RegisterPage
from Features.Pages.SearchPage import SearchPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    my_account_option_xpath = "//a[@title='My Account']"
    login_button_xpath = "//a[normalize-space()='Login']"
    search_box_field_xpath = "//input[@placeholder='Search']"
    search_button_xpath = "//button[@class='btn btn-default btn-lg']"
    register_button_xpath = "//a[normalize-space()='Register']"

    def click_on_my_account_button(self):
        self.click_on_element("my_account_option_xpath", self.my_account_option_xpath)
        # self.driver.find_element(By.XPATH, self.my_account_option_xpath).click()

    def click_on_register_button(self):
        self.click_on_element("register_button_xpath", self.register_button_xpath)
        # self.driver.find_element(By.XPATH, self.register_button_xpath).click()
        return RegisterPage(self.driver)

    def click_on_login_button(self):
        self.click_on_element("login_button_xpath", self.login_button_xpath)
        # self.driver.find_element(By.XPATH, self.login_button_xpath).click()
        return LoginPage(self.driver)

    def check_home_page_title(self, expected_title):
        self.verify_page_title(expected_title)
        # return self.driver.title.__eq__(expected_title)

    def enter_product_on_search_box(self, product_name):
        self.type_on_element("search_box_field_xpath", self.search_box_field_xpath, product_name)
        # self.driver.find_element(By.XPATH, self.search_box_field_xpath).send_keys(product_name)

    def click_on_search_button(self):
        self.click_on_element("search_button_xpath", self.search_button_xpath)
        # self.driver.find_element(By.XPATH, self.search_button_xpath).click()
        return SearchPage(self.driver)
