#!/usr/bin/python

import codecs
import random

def main():
	
	f = codecs.open("frequent_words.txt",'r',encoding='utf8')
	freq_w = []
	for line in f:
		freq_w.append(line.strip())
	dict_file = codecs.open("dictionary.txt",'r',encoding='utf8')
	unary_file = codecs.open("unary.txt",'w+',encoding='utf8')
	binary_file = codecs.open("binary.txt",'w+',encoding='utf8')
	triary_file = codecs.open("triary.txt",'w+',encoding='utf8')
	#fourgram_file = codecs.open("fourgram.txt",'w+',encoding='utf8')
	
	dictionary = []
	for line in dict_file:
		word = line.strip()
		dictionary.append(word)
	
	
	print 'finished dictionary loading'
	print str(len(dictionary))	
	unary_words = {}
	binary_words = {}	
	triary_words = {}
	for index in range(0,len(dictionary)-2):
		print str(index)
		unary_w = dictionary[index]
		binary_w = dictionary[index]+' '+dictionary[index+1]
		triary_w = dictionary[index]+' '+dictionary[index+1]+' '+dictionary[index+2]
		
		
		w = unary_w.split('_')[0]
		
		if unary_w in unary_words.keys():
			count = unary_words[unary_w]
			count = count + 1
			unary_words[unary_w] = count
		elif w not in freq_w:
			unary_words[unary_w] = 1
			
		if binary_w in binary_words.keys():
			count = binary_words[binary_w]
			count = count + 1
			binary_words[binary_w] = count
		else:
			binary_words[binary_w] = 1
			
		if triary_w in triary_words.keys():
			count = triary_words[triary_w]
			count = count + 1
			triary_words[triary_w] = count
		else:
			triary_words[triary_w] = 1
			
	for index in range(len(dictionary)-2,len(dictionary)):
		unary_w = dictionary[index]
		w = unary_w.split('_')[0]
		
		if unary_w in unary_words.keys():
			count = unary_words[unary_w]
			count = count + 1
			unary_words[unary_w] = count
		elif w not in freq_w:
			unary_words[unary_w] = 1
	
	binary_w = dictionary[-2]+' '+dictionary[-1]
	if binary_w in binary_words.keys():
		count = binary_words[binary_w]
		count = count + 1
		binary_words[binary_w] = count
	else:
		binary_words[binary_w] = 1
	
	for k,v in unary_words.iteritems():
		if v>3:
			unary_file.write(k+'\n')
	
	for k,v in binary_words.iteritems():
		if v>5:
			binary_file.write(k+'\n')
	
	for k,v in triary_words.iteritems():
		if v>7:
			triary_file.write(k+'\n')
	
	
	
	
if __name__ == '__main__':
  main()