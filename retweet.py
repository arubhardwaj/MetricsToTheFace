import tweepy
import time

# Keys are Removed
CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_KEY = ''
ACCESS_SECRET = ''

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

user = api.me()


for tweet in tweepy.Cursor(api.search, q='#metricstotheface').items():
    try:
        print('\nRetweet Bot found tweet by @' + tweet.user.screen_name + '. ' + 'Attempting to retweet.')

        tweet.retweet()
        print('Retweet published successfully.')



    except tweepy.TweepError as error:
        print('\nError. Retweet not successful. Because: ')
        print(error.reason)

    except StopIteration:
        break





#for tweet in tweepy.Cursor(api.search, q='#metricstotheface').items():
#    tweet.favorite()
#    pass
