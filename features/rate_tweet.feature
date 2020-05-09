Feature: Rate a Tweet
  In order to rate tweets,
  As a user,
  I want rate tweets

  Background: There is a registered user
    Given Exists a user logged {username} {name} {surname} {password}

  Scenario: Rate a Tweet
    Given I login as user "{username}" with password "{password}"
    When I create a Tweet and Rate It with 3 stars
      | text                    | hashtag   |
      | This is my first Tweet  | #first    |
    Then I'm viewing a tweet with 3 stars