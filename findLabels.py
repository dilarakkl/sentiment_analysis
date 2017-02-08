#!/usr/bin/python
import sys

global inputFile
global outputFile

def findLabels():
	file = open(inputFile, encoding="utf-8")
	output = open(outputFile, "w+", encoding="utf-8")

	lines = file.readlines()

	isLabel = False
	for line in lines:
		sLine = line.strip()
		if sLine != "":
			if not isLabel:
				if sLine == "<ENDTWEET>":
					isLabel = True
			else:
				if sLine == "<ENDSENTIMENT>":
					isLabel = False
				else:
					if sLine == "positive":
						label = 1
					elif sLine == "neutral":
						label = 2
					elif sLine == "negative":
						label = 3
					elif sLine == "objective":
						label = 4
					else:
						label = 5

					output.write("%s\n" %label)

	output.close()



if __name__ == '__main__':
	global inputFile
	global outputFile
	inputFile = sys.argv[1]
	outputFile = sys.argv[2]

	findLabels()