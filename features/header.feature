Feature: Header Navigation

  Background:
    Given Main page is opened
    Then  Main page header is displayed

  Scenario Outline: Verify top-level navigation links
    When Click header navigation button "<button_name>"
    Then <page_name> page is displayed


    Examples:
      | button_name   | page_name     |
      | Downloads     | Downloads     |
      | Documentation | Documentation |
      | Projects      | Projects      |
      | Support       | Support       |
      | Blog          | Blog          |

  Scenario Outline: Verify About dropdown navigation
    When Click header navigation button "About"
    And  Click header navigation button "<sub_button>"
    Then <sub_page> page is displayed


    Examples:
      | sub_button               | sub_page                 |
      | About Selenium           | About Selenium           |
      | Structure and Governance | Structure and Governance |
      | Events                   | Events                   |
      | Ecosystem                | Ecosystem                |
      | History                  | History                  |
      | Get Involved             | Get Involved             |
      | Sponsors                 | Sponsors                 |
      | Sponsor Us               | Sponsor Us               |

  Scenario: Verify logo returns user to Main page
    When Click header navigation button "Projects"
    Then Projects page is displayed
    When Click header logo
    Then Main page is fully displayed
