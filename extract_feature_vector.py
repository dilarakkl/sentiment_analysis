#!/usr/bin/python

import codecs

def main():
	unary_file = codecs.open("unary.txt",'r',encoding='utf8')
	binary_file = codecs.open("binary.txt",'r',encoding='utf8')
	triary_file = codecs.open("triary.txt",'r',encoding='utf8')
	tweet_file = codecs.open("test_tokens.txt",'r',encoding='utf8')
	feat_vector = codecs.open("feature_test.txt",'w+',encoding='utf8')
	
	
	
	word='a'
	count = 0
	word = tweet_file.readline().strip()
	while word !='<ENDFILE>':
		count = count + 1
		
		tokens = []
		
		
		while word != '<ENDSENTENCE>':
			tokens.append(word)
			word = tweet_file.readline().strip()
			
		createVector(tokens,feat_vector)
		print str(count)+'th sentence finished'		
		word = tweet_file.readline().strip()
	
def createVector(tokens,feat_vector):
	
	unary_file = codecs.open("unary.txt",'r',encoding='utf8')
	binary_file = codecs.open("binary.txt",'r',encoding='utf8')
	triary_file = codecs.open("triary.txt",'r',encoding='utf8')
	unary = {}
	for index in range(0,len(tokens)):
		unary_w = tokens[index]
		if unary_w in unary.keys():
			count = unary[unary_w]
			count = count + 1
			unary[unary_w] = count
		else:
			unary[unary_w] = 1
	binary = {}
	for index in range(0,len(tokens)-1):
		binary_w = tokens[index]+' '+tokens[index+1]
		if binary_w in binary.keys():
			count = binary[binary_w]
			count = count + 1
			binary[binary_w] = count
		else:
			binary[binary_w] = 1
			
	triary = {}
	for index in range(0,len(tokens)-2):
		triary_w = tokens[index]+' '+tokens[index+1]+' '+tokens[index+2]
		if triary_w in triary.keys():
			count = triary[triary_w]
			count = count + 1
			triary[triary_w] = count
		else:
			triary[triary_w] = 1
			
			
	for line in unary_file:
		w = line.strip()
		if w in unary.keys():
			feat_vector.write(str(unary[w])+' ')
		else:
			feat_vector.write(str(0)+' ')
	
	print 'done for unary'
	
	for line in binary_file:
		w = line.strip()
		if w in binary.keys():
			feat_vector.write(str(binary[w])+' ')
		else:
			feat_vector.write(str(0)+' ')
	
	print 'done for binary'
	
	
	for line in triary_file:
		w = line.strip()
		if w in triary.keys():
			feat_vector.write(str(triary[w])+' ')
		else:
			feat_vector.write(str(0)+' ')
	
	print 'done for triary'
	
	feat_vector.write('\n')
	
if __name__ == '__main__':
  main()