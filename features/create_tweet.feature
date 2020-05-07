Feature: Create a Tweet
  In order to create possible tweets to post,
  As a user,
  I want to create a tweet with its hashtags

  Background: There is a registered user
    Given Exists a user logged {username} {name} {surname} {password}

  Scenario: Create a Tweet
    Given I login as user "{username}" with password "{password}"
    When I create a Tweet
      | text                    | hashtag   |
      | This is my first Tweet  | #first    |
    Then I'm viewing the tweet created by {user}
      | text                    |
      | This is my first Tweet  |
    And There are 1 Tweet's