#!/usr/bin/python

import codecs
import random

def main():
	
	ignore = [',','$','U','@']
	adj = 'A'
	negation_file = codecs.open("negated_train.txt",'r',encoding='utf8')
	#negation_test = codecs.open("negated_test.txt",'r',encoding='utf8')
	tweet_file = codecs.open("tweet_train.txt",'r',encoding='utf8')
	#dict_file = codecs.open("dictionary.txt",'w+',encoding='utf8')
	#adj_file= codecs.open("adjectives.txt",'w+',encoding='utf8')
	train_tokens= codecs.open("train_tokens.txt",'w+',encoding='utf8')
	#test_tokens= codecs.open("test_tokens.txt",'w+',encoding='utf8')
	
	for line in negation_file:
		word = tweet_file.readline().strip()
		while word != '<ENDSENTIMENT>':
			word = tweet_file.readline().strip()
		tokens = []		
		pos = []
		word = tweet_file.readline().strip()
		while word != '<ENDTOKEN>':
			w = word.split(' ')[0]
			tokens.append(w)
			pos.append(word.split(' ')[1])
			word = tweet_file.readline().strip()
			
		
		if line.strip() == 'NONE':
			for t,p in zip(tokens, pos):
				train_tokens.write("%s\n" %t)
				'''if p not in ignore:
					dict_file.write("%s\n" %t)
				if p == adj:
					adj_file.write("%s\n" %t)'''
			train_tokens.write("<ENDSENTENCE>\n")
		else:
			numbers = line.strip().split(" ")
			
			count = 0
			for item,p in zip(tokens, pos):
				
				if count<=int(numbers[1]):
					train_tokens.write("%s\n" %item)
					'''if p not in ignore:
						dict_file.write("%s\n" %item)
						if p == adj:
							adj_file.write("%s\n" %item)'''
				elif count<=int(numbers[2]):
					train_tokens.write("%s_NEG\n" %item)
					'''if p not in ignore:
						neg_w = item+'_NEG'						
						dict_file.write("%s\n" %neg_w)
						if p == adj:
							adj_file.write("%s\n" %neg_w)'''
				else:
					train_tokens.write("%s\n" %item)
					'''if p not in ignore:
						dict_file.write("%s\n" %neg_w )
						if p == adj:
							adj_file.write("%s\n" %neg_w)'''
				count = count + 1;
			train_tokens.write("<ENDSENTENCE>\n")
	train_tokens.write("<ENDFILE>\n")
	
	negation_file.close()
	tweet_file.close()
	
	train_tokens.close()
if __name__ == '__main__':
  main()