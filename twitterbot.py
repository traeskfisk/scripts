#!/usr/bin/enc python
# -*- coding: utf-8 -*-

import tweepy
import time
import sys
import requests

#enter the corresponding information from your Twitter application:
CONSUMER_KEY = 'YOUR KEY HERE'
CONSUMER_SECRET = 'YOUR KEY HERE'
ACCESS_KEY = 'YOUR KEY HERE'
ACCESS_SECRET = 'YOUR KEY HERE'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def butkus():
        try:
	    print 'Sending request to website'
	    r = requests.get('https://butkus.xyz/api/quote')
	    citat = r.text
	    citat = citat.split('>')[1]
	    citat = citat.strip()
	    citat = citat.encode('UTF-8')
	    if citat in open('butkus.txt').read():
		    print "Citat found in textfile."
	    else:
		    print 'Updating twitter status'
		    api.update_status(citat)
		    print 'Saving to butkus.txt'
		    with open('butkus.txt', 'a') as f:
			    f.write(citat + '\n')
		    print 'Going to sleep'
		    time.sleep(5400) # sleep for 90 minutes
        except:
            print "Oops, something went wrong"
while(1):
	butkus()
