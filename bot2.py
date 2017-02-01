import tweepy
from time import sleep

CONSUMER_KEY = 'M7Ar3FLjGiF04HXB9NjQov95m'
CONSUMER_SECRET = ''
ACCESS_TOKEN = '8034215579010129929i4Z6cAf0SHVTptPjMarWjkiBaDOziM'
ACCESS_TOKEN_SECRET = 'LuRM5ppgZ3Tn1vqN2j9MCGcwUMEYm3Vwu7PjIUuJhBeG3'

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
auth.secure = True
api = tweepy.API(auth)
print(str(api.get_user(screen_name = '@crimeparadox')))