Feature: Create a Tweet
  In order to create possible tweets to post,
  As a user,
  I want to create a tweet with its hashtags

  Background: There is a registered user
    Given Exists a user logged "username" "name" "surname" "password"
  Scenario: Create a Tweet
    Given That "username" is logged in
    When I create a Tweet
      | text                    |
      | This is my first Tweet  |
    Then I'm viewing the tweet created by user
      | text                    |
      | This is my first Tweet  |
    And There are 1 Tweet's

  Scenario: Try to create tweet but not logged in
  Given I'm not logged in
  When I create tweet
    | test        |
    | This is my first Tweet  |
  Then I'm redirected to the login form
  And There are 0 tweets