Feature: Edit Tweet
  In order to keep updated my previous created tweets before publishing them
  As a user
  I want to be able to edit tweets

  Background: There are registered users and a tweet by one of them
    Given Exists a user "user1" with password "password"
    And Exists a user "user2" with password "password"
    And Exists tweet created by "user1"
      | text            | hashtag_in_tweet|
      | A common tweet  | #Bartomeu       |

  Scenario: Edit owned tweet text
    Given I login as user "user1" with password "password"
    When I edit the restaurant with text "Laporta dimissio"
      | text             |
      | Laporta dimissio |
    Then I'm viewing the details page for restaurant by "user1"
      | text             | hashtag_in_tweet|
      | Laporta dimissio | #Bartomeu       |
    And There are 1 tweet

  Scenario: Try to edit tweet but not logged in
  Given I'm not logged in
  When I view the details for tweet "A common tweet"
  Then There is no "edit" link available

  Scenario: Try to edit tweet but not the owner no edit button
    Given I login as user "user2" with password "password"
    When I view the details for restaurant "A common tweet"
    Then There is no "edit" link available

  Scenario: Force edit tweet but not the owner permission exception
    Given I login as user "user2" with password "password"
    When I edit the restaurant with name "A common tweet"
      | text             |
      | Laporta dimissio |
    Then Server responds with page containing "403 Forbidden"
    When I view the details for restaurant "A common tweet"
    Then I'm viewing the details page for restaurant by "user1"
      | text            | hashtag_in_tweet|
      | A common tweet  | #Bartomeu       |