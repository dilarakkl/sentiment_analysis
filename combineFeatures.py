#!/usr/bin/python
import sys

global ngramFile
global posFile
global negFile
global lexFile
global outputFile

#this file gets the vector files created by seperate programs, combines them.
#Matlab program svm.m gets these feature vector files and classify test tweets.
def combine():
	ngramF = open(ngramFile, encoding="utf-8")
	posF = open(posFile, encoding="utf-8")
	negF = open(negFile, encoding="utf-8")
	lexF = open(lexFile, encoding="utf-8")

	outputF = open(outputFile, "w+", encoding="utf-8")

	ngramLines = ngramF.readlines()
	posLines = posF.readlines()
	negLines = negF.readlines()
	lexLines = lexF.readlines()

	length = len(ngramLines)

	for i in range(length):
		ngramLine = ngramLines[i].strip()
		posLine = posLines[i].strip()
		negLine = negLines[i].strip()
		lexLine = lexLines[i].strip()

		if negLine == "":
			neg = 0
		else:
			neg = negLine.split()[0]

		outputF.write("%s %s %s %s\n" %(ngramLine, posLine, neg, lexLine))

	outputF.close()


if __name__ == '__main__':
	global ngramFile
	global posFile
	global negFile
	global lexFile
	global outputFile
	ngramFile = sys.argv[1]
	posFile = sys.argv[2]
	negFile = sys.argv[3]
	lexFile = sys.argv[4]
	outputFile = sys.argv[5]

	combine()
