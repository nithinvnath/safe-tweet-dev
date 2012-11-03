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

def urlCheck (line):
	u=re.compile('http\:\/\/t\.co\/[a-zA-Z0-9]+')
	return u.findall(line)
#---------------------------------------------------------------------#
#function to find emphasis on words by repetition of
#letters

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
#The following regular expression checks for three groups
#name followed by a colon, a tab and finally the tweet
p = re.compile('([a-z\ ]+\:)(\\t)(.*)',re.IGNORECASE)
f = open('test','rb')
for tweet in f:
	m = p.match(tweet)
	if m is not None:		#the file may contain invalid contents
		print tweet
		print removeStopwords(m.group(3))
f.close()

