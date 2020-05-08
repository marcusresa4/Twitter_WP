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

      Scenario: Create 3 Tweets edit one
    Given I login as user "{username}" with password "{password}"
    When I create a Tweet
      | text                     | hashtag    |
      | This is my first Tweet   | #create    |
      | This is my second Tweet  | #create    |
      | This is my third Tweet   | #create    |
    When I edit the tweet
      | text                     | hashtag    |
      | This is my first Tweet   | #create    |
      | This is my edited Tweet  | #edited    |
    Then I'm viewing 3 tweet created by {user}
      | text                     |
      | This is my edited Tweet  |
      | This is my second Tweet  |
      | This is my third Tweet   |
    And There are 3 Tweet's

  Scenario: Edit without logging
    Given I login as user "{username}" with password "{password}"
    Given I create a Tweet
      | text                    | hashtag   |
      | This is my first Tweet  | #first    |
    Then There are 1 Tweet's
    Given I'm not logged in
    When I edit the Tweet
      | text                     | hashtag    |
      | This is my first Tweet   | #create    |
      | This is my edited Tweet  | #edited    |
    Then I'm viewing 1 tweet created by {user}
      | text                     |
      | This is my first Tweet  |
    Then There are 1 Tweet's