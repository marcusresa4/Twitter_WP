Feature: Create a Tweet
  In order to create possible tweets to post,
  As a user,
  I want to create a tweet with its hashtags

  Background: There is a registered user
    Given Exists a user logged {username} {name} {surname} {password}

  Scenario: Get a Tweet from Twitter
    Given I login as user "{username}" with password "{password}"
    When I get a Tweet from API
      |user   |
      |Twitter|
    Then There are 1 Tweet's

  #Scenario: Get multiple Tweets from Twitter
   # Given I login as user "{username}" with password "{password}"
    #When I get a Tweet from API
  #    |user   |
  #    |Twitter|
  #    |TwitterEspana|
  #  Then There are 2 Tweet's

    #Scenario: Get a Tweet from a private Twitter user
   # Given I login as user "{username}" with password "{password}"
    #When I get a Tweet from API
  #    |user   |
  #    |marcusresa4|
  #  Then There are 0 Tweet's


        #Scenario: Get a Tweet without being logged
   # Given I'm not logged in
    #When I get a Tweet from API
  #    |user   |
  #    |marcusresa4|
  #  Then There are 0 Tweet's