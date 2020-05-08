Feature: Edit Tweet
  As a user,
  In want to be able to edit tweets

  Background: There is a registered user
    Given Exists a user logged {username} {name} {surname} {password}

  Scenario: Edit a Tweet
    Given I login as user "{username}" with password "{password}"
    When I create and edit a Tweet
      | text                     | hashtag    |
      | This is my first Tweet   | #create    |
      | This is my edited Tweet  | #edit      |
    Then I'm viewing 1 tweet created by {user}
      | text                     |
      | This is my edited Tweet  |
    And There are 1 Tweet's