import time
from behave import *
from Features.Pages.HomePage import HomePage
from Features.Pages.SearchPage import SearchPage


@given(u'I got navigated to search page')
def step_impl(context):
    context.home_page = HomePage(context.driver)
    expected_title = "Your Store"
    context.home_page.check_home_page_title(expected_title)
    assert context.driver.title.__eq__(expected_title)


@when(u'I enter the valid product on the search field')
def step_impl(context):
    product_name = "HP"
    context.home_page.enter_product_on_search_box(product_name)
    # context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("HP")


@when(u'I click on the search button')
def step_impl(context):
    context.search_page = context.home_page.click_on_search_button()
    # context.driver.find_element(By.XPATH, "//button[@class='btn btn-default btn-lg']").click()


@then(u'Valid product should display on the search result page')
def step_impl(context):
    time.sleep(2)
    # product_name = "HP LP3065"
    # search_page = SearchPage(context.driver)
    assert context.search_page.display_status_of_product()

    # assert context.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()
    print("Validated Successfully for valid product")


@when(u'I enter the invalid product on the search field')
def step_impl(context):
    product_name = "Honda"
    context.home_page.enter_product_on_search_box(product_name)
    # context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("Honda")


@then(u'Proper message should display on the search result page')
def step_impl(context):
    time.sleep(2)
    expected_result = "There is no product that matches the search criteria.abc"
    # search_page = SearchPage(context.driver)
    assert context.search_page.display_invalid_product_message(expected_result)

    # actual_result = context.driver.find_element(By.XPATH, "//div[@id='content']/p[2]").text
    # assert expected_result.__eq__(actual_result)
    print("Validated Successfully for invalid product")


@when(u'I dont enter any product on the search field')
def step_impl(context):
    product_name = ""
    context.home_page.enter_product_on_search_box(product_name)
    # context.driver.find_element(By.XPATH, "//input[@placeholder='Search']").send_keys("")
