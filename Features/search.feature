Feature: Search Functionality

  @Search
  Scenario: Search for a valid product
    Given I got navigated to search page
    When I enter the valid product on the search field
    And I click on the search button
    Then Valid product should display on the search result page

  @Search
  Scenario: Search for an invalid product
    Given I got navigated to search page
    When I enter the invalid product on the search field
    And I click on the search button
    Then Proper message should display on the search result page

  @Search
  Scenario: Search without entering any product
    Given I got navigated to search page
    When I dont enter any product on the search field
    And I click on the search button
    Then Proper message should display on the search result page