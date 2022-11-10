import tweepy
import configparser

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

#print all accessible home tweets
print(public_tweets)