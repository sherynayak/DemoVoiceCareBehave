import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime

from Features.Pages.AccountSuccessPage import AccountSuccessPage
from Features.Pages.HomePage import HomePage
from Features.Pages.RegisterPage import RegisterPage


@given(u'Navigate to register page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_button()
    context.register_page = context.home_page.click_on_register_button()

    # context.driver.find_element(By.XPATH, "//a[@title='My Account']").click()
    # context.driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()


@when(u'I enter details into mandatory fields')
def step_impl(context):
    # Separate variables for each part of the date and time
    now = datetime.now()
    year = str(now.year)
    # print(year)
    month = str(now.month)
    day = str(now.day)
    hour = str(now.hour)
    minute = str(now.minute)
    second = str(now.second)
    email_new = str(year + month + day + hour + minute + second)
    email_new = "abc" + email_new + "@gmail.com"

    # context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name('abc')
    context.register_page.enter_last_name('efg')
    context.register_page.enter_email_address(email_new)
    context.register_page.enter_telephone_number('22222')
    context.register_page.enter_password('123456')
    context.register_page.enter_confirm_password('123456')
    context.register_page.choose_agree_checkbox()

    # context.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys('abc')
    # context.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys('efg')
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(email_new)
    # print("Email address: ", email_new)
    # context.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys('1111')
    # context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('12345')
    # context.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys('12345')
    # context.driver.find_element(By.XPATH, "//input[@name='agree']").click()
    time.sleep(3)


@when(u'I click on continue button')
def step_impl(context):
    context.account_success_page = context.register_page.click_continue_button()
    # context.driver.find_element(By.XPATH, "//input[@value='Continue']").click()


@then(u'Account should get created')
def step_impl(context):
    expected_result = "Your Account Has Been Created!"
    # account_success_page = AccountSuccessPage(context.driver)
    assert context.account_success_page.display_confirm_message(expected_result)

    # actual_result = context.driver.find_element(By.XPATH, "//div[@id='content']/h1").text
    # print("actual_result: "+actual_result)
    # print("expected_result: "+expected_result)
    # time.sleep(3)
    # assert expected_result.__eq__(actual_result)
    time.sleep(3)


@when(u'I enter details into all fields except email fields')
def step_impl(context):

    # context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name('abc')
    context.register_page.enter_last_name('efg')
    # context.register_page.enter_email_address(email_new)
    context.register_page.enter_telephone_number('22222')
    context.register_page.enter_password('123456')
    context.register_page.enter_confirm_password('123456')
    context.register_page.choose_agree_checkbox()

    # context.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys('abc')
    # context.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys('efg')
    # # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys(email_new)
    # # print("Email address: ", email_new)
    # context.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys('11111')
    # context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('12345')
    # context.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys('12345')
    # context.driver.find_element(By.XPATH, "//input[@name='agree']").click()


@when(u'I enter existing email accounts into email field')
def step_impl(context):
    context.register_page.enter_email_address("aaa@gmail.com")
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("aaa@gmail.com")


@then(u'Proper warning message for informing about duplicate account should be displayed')
def step_impl(context):
    expected_warning_message = "Warning: E-Mail Address is already registered!"
    assert context.register_page.display_alert_email_message(expected_warning_message)
    # z = context.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
    # print("expected_warning_message: " + expected_warning_message)
    # print("z: " + z)
    # time.sleep(3)
    # assert z.__contains__(expected_warning_message)
    print("Validated Successfully for duplicate account")


@when(u'I dont enter anything into the fields')
def step_impl(context):

    # context.register_page = RegisterPage(context.driver)
    context.register_page.enter_first_name('')
    context.register_page.enter_last_name('')
    context.register_page.enter_email_address('')
    context.register_page.enter_telephone_number('')
    context.register_page.enter_password('')
    context.register_page.enter_confirm_password('')

    # context.driver.find_element(By.XPATH, "//input[@id='input-firstname']").send_keys('')
    # context.driver.find_element(By.XPATH, "//input[@id='input-lastname']").send_keys('')
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys('')
    # context.driver.find_element(By.XPATH, "//input[@id='input-telephone']").send_keys('')
    # context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys('')
    # context.driver.find_element(By.XPATH, "//input[@id='input-confirm']").send_keys('')


@then(u'Proper warning message for every mandatory fields should be displayed')
def step_impl(context):
    expected_warning_message = "First Name must be between 1 and 32 characters!"
    assert context.register_page.display_warning_message(expected_warning_message)
    # z = context.driver.find_element(By.XPATH, "//div[@class='text-danger']").text
    # print("z: ", z)
    # assert z.__contains__(expected_warning_message)
    print("Validated Successfully for mandatory fields should be displayed")
