#! /usr/bin/python

import tweepy

consumer_token = "pDeVZbNzK6HXocUuhwLqBg"
consumer_secret = "Itj45FWSmMr0VmrNPJuO2KIaIt3hzayY2ywVteh2M"

auth = tweepy.OAuthHandler(consumer_token,consumer_secret)
auth_url = auth.get_authorization_url()

print "Authorize: " + auth_url
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)

access_token = auth.access_token.key
access_secret = auth.access_token.secret
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

if api.me().name is not None:
	print "Successfully authenticated"
else:
	print "Authentication failed!"