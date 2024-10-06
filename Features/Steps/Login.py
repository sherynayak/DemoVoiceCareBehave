import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By

from Features.Pages.AccountPage import AccountPage
from Features.Pages.HomePage import HomePage
from Features.Pages.LoginPage import LoginPage


@when(u'I got navigated to the Login page')
def step_impl(context):

    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account_button()
    context.login_page = context.home_page.click_on_login_button()


@given(u'I entered valid username as "{email}" and password as "{password}"into the field')
def step_impl(context, email, password):

    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_id(email)
    context.login_page.enter_password(password)
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("sheriffnayak@gmail.com")
    # context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345")


@given(u'I clicked the login button')
def step_impl(context):
    context.account_page = context.login_page.click_login_button()
    # context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then(u'I should get logged in')
def step_impl(context):
    time.sleep(5)
    # account_page = AccountPage(context.driver)
    assert context.account_page.display_status_of_edit_your_account_information_option()
    # assert context.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
    print("Validated Successfully for valid login")


@given(u'I entered valid username and invalid password into the field')
def step_impl(context):
    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_id("sheriffnayak@gmail.com")
    context.login_page.enter_password("123456")

    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("sheriffnayak@gmail.com")
    # context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("123456")
    time.sleep(2)


@then(u'I should get a proper warning message')
def step_impl(context):
    time.sleep(5)
    expected_war_msg = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.display_warning_message(expected_war_msg)
    # z = context.driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']").text
    # assert z.__contains__(expected_war_msg)
    print("Validated Successfully for invalid Login")


@given(u'I entered valid invalid username and valid password into the field')
def step_impl(context):
    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_id("sheriffnayak111@gmail.com")
    context.login_page.enter_password("12345")
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("sheriffnayak111@gmail.com")
    # context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("12345")


@given(u'I entered invalid username and invalid password into the field')
def step_impl(context):
    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_id("sheriffnayak111@gmail.com")
    context.login_page.enter_password("123456")
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("sheriffnayak111@gmail.com")
    # context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("123456")


@given(u'I dont enter any username and password into the field')
def step_impl(context):
    # context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_id("")
    context.login_page.enter_password("")
    # context.driver.find_element(By.XPATH, "//input[@id='input-email']").send_keys("")
    # context.driver.find_element(By.XPATH, "//input[@id='input-password']").send_keys("")
