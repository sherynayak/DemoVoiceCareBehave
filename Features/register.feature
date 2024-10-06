Feature: Register Account Functionality

  @register
  Scenario: Register with mandatory fields
    Given Navigate to register page
    When I enter details into mandatory fields
    And I click on continue button
    Then Account should get created


  @register
  Scenario: Register with a duplicate email address
    Given Navigate to register page
    When I enter details into all fields except email fields
    And I enter existing email accounts into email field
    And I click on continue button
    Then Proper warning message for informing about duplicate account should be displayed

  @register
  Scenario: Register without providing any details
    Given Navigate to register page
    When I dont enter anything into the fields
    And I click on continue button
    Then Proper warning message for every mandatory fields should be displayed



