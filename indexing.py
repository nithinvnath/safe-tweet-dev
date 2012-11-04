#! /usr/bin/python

""" Reads tweets from a file and removes the stopwords
Assumes the tweets are of the form <username>: <tweet>"""

import re
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer

wnl = WordNetLemmatizer()
#---------------------------------------------------------------------#
#Function that takes as input a line and removes stopwords from it
def removeStopwords (line):
	words = re.findall(r'\w+', line,flags = re.UNICODE | re.LOCALE) 
	important_words = []
	for word in words:
		if word not in stopwords.words('english'):
			word = wnl.lemmatize(word)
			important_words.append(word)
	return important_words

#---------------------------------------------------------------------#
#Twitter converts all urls to http://t.co/<something>
#this regular expression checks for all urls in a ling
#and return them as a list

def hasUrl (line):
	u=re.compile('http\:\/\/t\.co\/[a-zA-Z0-9]+')
	return u.findall(line)
#---------------------------------------------------------------------#
#function to chech the presence of a usename in the 
#tweet

def hasUsernames(line):
	u=re.compile('\@[a-zA-Z0-9\_]+')
	return u.findall(line)


#---------------------------------------------------------------------#
#function to find emphasis on words by repetition of
#letters

def emphExist(line):
	presence = 0
	emp_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
	words = line.split()
	for word in words:
		if emp_regexp.match(word) is not None:
			if wordnet.synsets(word):
				continue
			else:
				presence = presence +1
	return presence


#replaces the word after removing repeated letters
def emphReplace(word):
	emp_regexp = re.compile(r'(\w*)(\w)\2(\w*)')
	if wordnet.synsets(word):
		return word
	matched = emp_regexp.match(word)
	if r is None:
		return word
	word = matched.group(1)+matched.group(2)+matched.group(3)
	return emphReplace(word)

#---------------------------------------------------------------------#
#checks if the tweet is a retweet
#takes as input the raw tweet
def isRetweet(tweet):
	p = re.compile('([A-Za-z\ ]+\:)(\\t)(.*)')
	t = m.group(3)
	if (t[0]=='R' and t[1]=='T' and t[2]==' '):
		return 1
	else:
		return 0

#---------------------------------------------------------------------#
#The following regular expression checks for three groups
#name followed by a colon, a tab and finally the tweet
p = re.compile('([a-z\ ]+\:)(\\t)(.*)',re.IGNORECASE)
f = open('test','rb')
for tweet in f:
	m = p.match(tweet)
	if m is not None:		#the file may contain invalid contents
		print tweet
		print hasUsernames(tweet)
		#print removeStopwords(m.group(3))
f.close()

