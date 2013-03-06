#! /usr/bin/python

import tweepy
import pickle	#for writing and reading objects directly to files

#Consumer token and secret are specific to the application
#Can  be found in dev.twitter.com/apps
consumer_token = "pDeVZbNzK6HXocUuhwLqBg"
consumer_secret = "Itj45FWSmMr0VmrNPJuO2KIaIt3hzayY2ywVteh2M"

#To get authorization from user using OAuth
auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
auth_url = auth.get_authorization_url(signin_with_twitter=True)

# print "Authorize: " + auth_url
webopen(auth_url)
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)

access_token = auth.access_token.key
access_secret = auth.access_token.secret
# access_token = "45142783-KrrjDjWf0M3OKuq1Ckb9Bi6WpNX9ZQnhurPM1wxDA"
# access_secret = "b6a6OHD39u1GNJMfkTp5LGRWCk7WWgTZgPkE6sgp8wo"

#Access the user's account using the OAuth credentials
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)	#authenticated api module
fusersfile = open('user-list.txt','r')
fuserdetail = open('user-details.txt','a')
pickle.HIGHEST_PROTOCOL
fcount = open('crawl_count.txt','rw+')	#keeps track of the count of users & tweets crawled

counts = fcount.readlines()

if counts is None:
	f.write('0\n0')
	user_count = 0
	tweet_count = 0
else:
	user_count = int(counts[0])
	tweet_count = int(count[1])

for user_name in fuserslist:
	user=api.get_user(user_name)
	pickle.dump(user,fuserdetail)
	status_list=api.get_user_timeline(user_name)
	pickle.dump(status_list)
	user_count = user_count + 1
	tweet_count = tweet_count + 1