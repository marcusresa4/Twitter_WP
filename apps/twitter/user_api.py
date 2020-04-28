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
        
        # 200 tweets to be extracted 
        number_of_tweets=2
        tweets = api.user_timeline(screen_name=username)
  
        # Empty Array 
        tmp=[]  
  
        # create array of tweet information: username,  
        # tweet id, date/time, text 
        tweet_text = tweets
        dictionary = {}
        #print(tweet_text[0])
        #print("Text:"+ tweet_text[0].text)
        #tmp.append("Text:"+ tweet_text[0].text)
        dictionary["Text"] = tweet_text[0].text
        #print("Name:"+ tweet_text[0].user.name)
        #tmp.append("Username:"+ tweet_text[0].user.name)
        dictionary["Real Name"] = tweet_text[0].user.name
        #print("Username:"+ tweet_text[0].user.screen_name)
        #tmp.append("Name:"+ tweet_text[0].user.screen_name)
        dictionary["Username"] = tweet_text[0].user.screen_name
        #print("User_id:"+ tweet_text[0].user.id_str)
        #tmp.append("Id:"+ tweet_text[0].user.id_str)
        dictionary["Id_Tweet"] = tweet_text[0].id_str
        dictionary["Id_User"] = str(tweet_text[0].user.id)
        #print("Hashtags:"+ str(tweet_text[0].entities["hashtags"]))
        #tmp.append("Hashtag:"+ str(tweet_text[0].entities["hashtags"]))
        dictionary["Hashtags"] = tweet_text[0].entities["hashtags"]
        #print("RT:"+ str(tweet_text[0].retweet_count))
        #tmp.append("RT:"+ str(tweet_text[0].retweet_count))
        dictionary["RT"] = str(tweet_text[0].retweet_count)
        #print("FAV:"+ str(tweet_text[0].favorite_count))
        #tmp.append("FAV:"+ str(tweet_text[0].favorite_count))
        dictionary["FAV"] = str(tweet_text[0].favorite_count)

        return dictionary
# Driver code 
if __name__ == '__main__': 
  
    # Here goes the twitter handle for the user 
    # whose tweets are to be extracted. 
    get_tweets("xtrullols35") 