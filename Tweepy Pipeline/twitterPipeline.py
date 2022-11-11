import tweepy
import configparser
import pandas as pd

#read all of the credentialss

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

#Authenticate our account with the twitter API
authentication = tweepy.OAuthHandler(api_key, api_key_secret)

authentication.set_access_token(access_token, access_token_secret)

tweets_access_api = tweepy.API(authentication)

#we will use api to have access to twitter account
public_tweets = tweets_access_api.home_timeline()

#Searching tweets by hashtag
tweet_hashtag = '#TheWifeShowMax'
number_of_hashtag_tweets = 300

tweets = tweepy.Cursor(tweets_access_api.search_tweets, q = tweet_hashtag , count = 200, tweet_mode = 'extended').items(number_of_hashtag_tweets)

#Creating the dataframe with pandas
columns = ['Tweet']
data = []



#Adding tweets to the datafram
for tweet in tweets:
    data.append([tweet.full_text])

data_frame = pd.DataFrame(data, columns=columns)

#Displaying the tweets
print(data_frame)
