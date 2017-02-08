#!/usr/bin/python

from pymongo import MongoClient
import traceback

def main():
	
	try:
		db = MongoClient("localhost", 27017)
	except Exception as detail:
		traceback.print_exc()

	tweets = db.semeval.Tweets.find()
	count = 0
	for tweet in tweets:
		
		if tweet['task']=='TrialA':
			count = count+1
			for a in tweet['sentiments']:
				print a
			print
			print tweet['tweet']
			print
		if count>5:
			break


#gets 5 tweets from trial A dataset just for example.





if __name__ == '__main__':
  main()