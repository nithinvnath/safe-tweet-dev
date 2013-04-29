#! /usr/bin/python

import tweepy
import cPickle as pickle

frawtweets=open('./Raw-Tweets/raw-tweets1.dat','r')
fsplit1=open('./Raw-Tweets/raw-tweets11.dat','a')
fsplit2=open('./Raw-Tweets/raw-tweets12.dat','a')
fsplit3=open('./Raw-Tweets/raw-tweets13.dat','a')
fsplit4=open('./Raw-Tweets/raw-tweets14.dat','a')
fsplit5=open('./Raw-Tweets/raw-tweets15.dat','a')

count = 1

statuses = pickle.load(frawtweets)
while statuses is not None:
	print count
	if count<=15:
		pickle.dump(statuses,fsplit1)
	else:
		if count<=30:
			pickle.dump(statuses,fsplit2)
		else:
			if count<=45:
				pickle.dump(statuses,fsplit3)
			else:
				if count<=60:
					pickle.dump(statuses,fsplit4)
				else:
					pickle.dump(statuses,fsplit5)
	statuses=pickle.load(frawtweets)
	count = count+1;

frawtweets.close()
fsplit1.close()
fsplit2.close()
fsplit3.close()
fsplit4.close()
fsplit5.close()