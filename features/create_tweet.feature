Feature: Create a Tweet
  In order to create possible tweets to post,
  As a user,
  I want to create a tweet with its hashtags

  Background: There is a registered user
    Given Exists a user logged

  Scenario: Create a Tweet
    Given I login as user with Google
    When I create a Tweet
      | text                    |
      | This is my first Tweet  |
    Then I'm viewing the tweet created by user
      | text                    |
      | This is my first Tweet  |
    And There are 1 Tweet's