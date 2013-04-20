#! /usr/bin/python

import tweepy
from webbrowser import open as webopen
import pickle	#for writing and reading objects directly to files

#Consumer token and secret are specific to the application
#Can  be found in dev.twitter.com/apps
consumer_token = "pDeVZbNzK6HXocUuhwLqBg"
consumer_secret = "Itj45FWSmMr0VmrNPJuO2KIaIt3hzayY2ywVteh2M"
auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
auth_url = auth.get_authorization_url(signin_with_twitter=True)
access_token = "45142783-KrrjDjWf0M3OKuq1Ckb9Bi6WpNX9ZQnhurPM1wxDA"
access_secret = "b6a6OHD39u1GNJMfkTp5LGRWCk7WWgTZgPkE6sgp8wo"
auth.set_access_token(access_token,access_secret)
api = tweepy.API(auth)
print "Authenticated"
fusersfile = open('user-list.txt','r')		#User names list
fuserdetail = open('user-details.txt','a')	#details of user are stored in case we need it later
pickle.HIGHEST_PROTOCOL
frawtweets = open('raw-tweets.dat','a')		#the tweepy tweet object is directly saved into this file
count = 1
for user_name in fusersfile:
	try:
		user=api.get_user(user_name)
		pickle.dump(user,fuserdetail)
		status_list=api.user_timeline(user_name)
		pickle.dump(status_list,frawtweets)
		print str(count) + ". " + user_name
		count = count+1
	except tweepy.error.TweepError,e:
		print user_name + e.reason 
fusersfile.close()
frawtweets.close()
fuserdetail.close()
