#! /usr/bin/python

import tweepy
import cPickle as pickle

frawtweets=open('raw-tweets3.dat','r')
statuses = pickle.load(frawtweets)
count = 1
while statuses is not None:
	for tweet in statuses:
		print count, tweet.text
		count = count+1;
	try:
		statuses = pickle.load(frawtweets)
	except EOFError:
		print "\n\tCOUNT: ",count-1
		break
frawtweets.close()