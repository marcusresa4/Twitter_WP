import tweepy 

# Fill the X's with the credentials obtained by  
# following the above mentioned procedure. 
consumer_key = "yr504H9CTJKurY9VscygcB9YY" 
consumer_secret = "48CUa7jtvtqM6d0XqaQKuLp9PHJBf3CL9FUmm2Kuv56qaxoh5f"
access_key = "1239239848197849095-3ubmNIWQK8KBw295hiH22Eps6eZ4OI"
access_secret = "5hu7PlXSlxxZ3lUmWmPCXzVKnrgWhs00YA6QLsV7oakva"
  
# Function to extract tweets 
def get_tweets(username): 

        # Authorization to consumer key and consumer secret 
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
        # Access to user's access key and access secret 
        auth.set_access_token(access_key, access_secret) 
  
        # Calling api 
        api = tweepy.API(auth) 

        tweets = api.user_timeline(screen_name=username, count=1)

  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweet_text = tweets
        dictionary = {}
        dictionary["Text"] = tweet_text[0].text
        dictionary["Real Name"] = tweet_text[0].user.name
        dictionary["Username"] = tweet_text[0].user.screen_name
        dictionary["Id_Tweet"] = tweet_text[0].id_str
        dictionary["Id_User"] = str(tweet_text[0].user.id)
        dictionary["Hashtags"] = tweet_text[0].entities["hashtags"]
        dictionary["RT"] = str(tweet_text[0].retweet_count)
        dictionary["FAV"] = str(tweet_text[0].favorite_count)

        return dictionary