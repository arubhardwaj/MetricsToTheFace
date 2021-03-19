import tweepy
import time

# API Keys are removed!!
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()


for tweet in tweepy.Cursor(api.search, q='#metricstotheface').items():
    tweet.favorite()
    pass
