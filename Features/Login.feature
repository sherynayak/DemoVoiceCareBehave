Feature: Login Functionality

  @login @test
  Scenario Outline: Login with valid credentials
    When I got navigated to the Login page
    Given I entered valid username as "<email>" and password as "<password>"into the field
    And I clicked the login button
    Then I should get logged in
    Examples:
      | email                       | password  |
      | sheriffnayak@gmail.com      | 12345     |
      | amotoorisampleone@gmail.com | secondone |

  @login
  Scenario: Login with valid username and invalid password
    When I got navigated to the Login page
    Given I entered valid username and invalid password into the field
    And I clicked the login button
    Then I should get a proper warning message

  @login
  Scenario: Login with invalid username and valid password
    When I got navigated to the Login page
    Given I entered valid invalid username and valid password into the field
    And I clicked the login button
    Then I should get a proper warning message

  @login
  Scenario: Login with invalid credentials
    When I got navigated to the Login page
    Given I entered invalid username and invalid password into the field
    And I clicked the login button
    Then I should get a proper warning message

  @login
  Scenario: Login without entering any credentials
    When I got navigated to the Login page
    Given I dont enter any username and password into the field
    And I clicked the login button
    Then I should get a proper warning message
