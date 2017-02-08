'''
	This script finds the negated context in the tweets. 
	In output file, each tweet represented in a single line:
		if tweet doesn't have negation there is an empty line.
		if there is negation, "C S1 E1 S2 E2 ... Sn En" is found in the corresponding line
				where 	C is the number of negated context
						S1 is the start index of the first negated context in the tweet
						E1 is the end index of the first negated context in the tweet
						S2 is the start index of the second negated context in the tweet
						E2 is the end index of the second negated context in the tweet
'''

#!/usr/bin/python
import sys, os, re

global inputFile
global outputFile

negativeWords = []
tweets = []
punctuations = [',', '.', ':', ';', '!', '?']

def loadNegativeWords():
	global negativeWords
	file = open("negativeWords.txt", encoding="utf-8")
	lines = file.readlines()
	negativeWords = lines[0].split("|")

def getTweets():
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
					tw = " ".join(tweet)
					tweets.append(tw)
					tweet = []
					isTweet = False
				else:
					tweet.append(sLine.split()[0])


def findNegatedContext():
	output = open(outputFile, "w+", encoding="utf-8")

	regEx1 = '.*[.?;:!,]+'
	#regEx2 = '[0-9]+[.?;:!,][0-9a-zA-Z"]+$'
	#regEx3 = '^http.*'
	#regEx4 = '.*@.*'

	for tweet in tweets:
		tokens = tweet.split()

		isNegated = False

		negStart = 0
		negStart2 = []

		negEnd = 0
		negEnd2 = []

		negContext = 0

		for i in range(0, len(tokens)):
			token = "".join(tokens[i].split("\'")).lower()
			#print(token)
	
			if token in negativeWords:
				isNegated = True
				negStart = i
				negStart2.append(negStart)
				#print("NEGATIVE")
			if isNegated:
				#print(token)
				if re.match(regEx1, token):
					negEnd = i - 1
					negEnd2.append(negEnd)
					isNegated = False
		
		if negEnd < negStart:
			negEnd = len(tokens) - 1
			negEnd2.append(negEnd)
			isNegated = False

		#print(negStart2)
		#print(negEnd2)
		for i in range(0, len(negEnd2)):
			negContext += negEnd2[i] - negStart2[i]

		#print(negContext)
		if negContext != 0:
			#output.write("%s %s " %(tokens[0], negContext))
			output.write("%s " %negContext)
			for i in range(0, len(negEnd2)):
				output.write("%s %s " %(negStart2[i], negEnd2[i]))

		output.write("\n")

	output.close()


if __name__ == '__main__':
	global inputFile
	global outputFile
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]
	loadNegativeWords()
	getTweets()
	findNegatedContext()
