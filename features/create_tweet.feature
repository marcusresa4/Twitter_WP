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
    Then I'm viewing 1 tweet created by {user}
      | text                    |
      | This is my first Tweet  |
    And There are 1 Tweet's

  Scenario: Create a Tweet without logging
    Given I'm not logged in
    When I create a Tweet 
      | text                    | hashtag   |
      | This is my first Tweet  | #first    |
    Then There are 0 Tweet's

  Scenario: Create more than one Tweet
    Given I login as user "{username}" with password "{password}"
    When I create a Tweet
      | text                    | hashtag   |
      | This is my first Tweet  | #first    |
      | This is my second Tweet | #second   |
    Then I'm viewing 2 tweet created by {user}
      | text                    |
      | This is my first Tweet  |
      | This is my second Tweet |
    And There are 2 Tweet's