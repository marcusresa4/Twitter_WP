Feature: Delete Tweet
  As a user,
  In want to be able to delete tweets

  Background: There is a registered user
    Given Exists a user logged {username} {name} {surname} {password}

  Scenario: Delete a Tweet
    Given I login as user "{username}" with password "{password}"
    Given I create a Tweet
      | text                    | hashtag   |
      | This is my first Tweet  | #first    |
    Then There are 1 Tweet's
    When I delete a Tweet(There are 1 tweets)
    Then There are 0 Tweet's
  
  Scenario: Delete some Tweets
    Given I login as user "{username}" with password "{password}"
    Given I create a Tweet
      | text                    | hashtag   |
      | This is my first Tweet  | #first    |
      | This is my second Tweet | #second   |
    Then There are 2 Tweet's
    When I delete a Tweet(There are 2 tweets)
    Then There are 1 Tweet's
    When I delete a Tweet(There are 1 tweets)
    Then There are 0 Tweet's
  
  Scenario: Delete without logging 
    Given I login as user "{username}" with password "{password}"
    Given I create a Tweet
      | text                    | hashtag   |
      | This is my first Tweet  | #first    |
    Then There are 1 Tweet's
    Given I'm not logged in
    When I delete a Tweet(There are 1 tweets)
    Then There are 1 Tweet's

  Scenario: Delete empty 
    Given I login as user "{username}" with password "{password}"
    Then There are 0 Tweet's
    When I delete a Tweet(There are 0 tweets)
    Then There are 0 Tweet's
    