import tweepy, time, sys
 
argfile = str(sys.argv[1])
 

CONSUMER_KEY = 'K7kwwQL3s72MLlZhXxwLQt6Ct'
CONSUMER_SECRET = '1fidDXQhWvzb0uzI5LJ1i1nxB6X4JrBv3kv7WXZIrVngfn1jg1Z'
ACCESS_KEY = '803421557901012992-aPxXoND12tsUsWSWHKy0MnKpNoWl9Ju'
ACCESS_SECRET = '4EZYnNbvPAOfkYpR5endi5lp6ingYHvZ7fiRynteood4Y'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines()
filename.close()
 
for line in f:
    apis = api.update_status(line)
    apis.update_status(status=line)
    time.sleep(900)#Tweet every 15 minutes