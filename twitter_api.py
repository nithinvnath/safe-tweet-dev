#! /usr/bin/python

import tweepy
from webbrowser import open as webopen

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

if api.me().name is not None:
	print "Successfully authenticated"
else:
	print "Authentication failed!"

pub = api.home_timeline()

for tweet in pub:
	print tweet.user.name + ":" + tweet.text