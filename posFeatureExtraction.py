#!/usr/bin/python
import sys
from collections import Counter

postags = ['N', 'O', 'S', '^', 'Z', 'L', 'M', 'V', 'A', 'R', '!', 'D', 'P', '&', 'T', 'X', 'Y', '#', '@', '~', 'U', 'E', '$', ',', 'G']
global inputFile
global outputFile
tweets = []

def getTweetTags():
	global tweets 
	tweets = []
	tweet = []
	file = open(inputFile, encoding="utf-8")
	lines = file.readlines()
	isTweet = False
	for line in lines:
		sLine = line.strip()
		if sLine != "":
			if not isTweet:
				if sLine == "<ENDSENTIMENT>":
					isTweet = True
			else:
				if sLine == "<ENDTOKEN>":
					tweets.append(tweet)
					tweet = []
					isTweet = False
				else:
					tweet.append(sLine.split()[1])

def findPostags():	
	output = open(outputFile, "w+", encoding="utf-8")

	for tweet in tweets:
		tweettags = Counter(tweet)
		for pos in postags:
			if pos in tweet:
				output.write("%s " %tweettags[pos])
			else:
				output.write("0 ")
		output.write("\n")




if __name__ == '__main__':
	global inputFile
	global outputFile
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	getTweetTags()
	findPostags()