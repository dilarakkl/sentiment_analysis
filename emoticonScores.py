#!/usr/bin/python
import sys
from collections import Counter

tweets = []
emoticons = []

#This file takes emoticon scores and sums these scores for every tweet.
#writes the score of it as a feature.
def getEmoticons():
	global emoticons
	emoticons = []

	file = open("emo2.txt", encoding="utf-8")

	lines = file.readlines()
	for line in lines:
		sLine = line.strip()
		tokens = sLine.split()

		emoticons.append((tokens[0], float(tokens[4])))



def getTweetTags():
	global tweets 

	tweets = []
	tweet = []

	file = open(inputFile, encoding="utf-8")
	lines = file.readlines()
	isTweet = False


	for i in range(len(lines)):
		sLine = lines[i].strip()

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
					if sLine.split()[1] == "E":
						tweet.append(sLine.split()[0])


def findScores():
	output = open(outputFile, "w+", encoding="utf-8")

	for tweet in tweets:
		if len(tweet) == 0:
			output.write("0\n")
		else:
			tot = 0
			for emo in tweet:
				score = [score for (emo2, score) in emoticons if emo2 == emo]
				tot += sum(score)
			
			output.write("%s\n" %tot)

	output.close()


if __name__ == '__main__':
	global inputFile
	global outputFile
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]

	getTweetTags()
	getEmoticons()
	findScores()
