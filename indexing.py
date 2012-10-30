#! /usr/bin/python

""" Reads tweets from a file and removes the stopwords
Assumes the tweets are of the form <username>: <tweet>"""

import re
from nltk.corpus import stopwords

#Function that takes as input a line and removes stopwords from it
def removeStopwords (line):
	words = re.findall(r'\w+', line,flags = re.UNICODE | re.LOCALE) 
	important_words = []
	for word in words:
		if word not in stopwords.words('english'):
			important_words.append(word)
	return important_words

#The following regular expression checks for three groups
#name followed by a colon, a tab and finally the tweet
p = re.compile('([a-z\ ]+\:)(\\t)(.*)',re.IGNORECASE)


f = open('test','rb')
for tweet in f:
	m = p.match(tweet)
	if m is not None:		#the file may contain invalid contents
		print tweet
		print removeStopwords(m.group(3))
		print '\n'
f.close()

