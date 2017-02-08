#!/usr/bin/python

import codecs

def main():
	tweet_file = codecs.open("test_tokens.txt",'r',encoding='utf8')
	feat_vector = codecs.open("feature_adj_test_new.txt",'w+',encoding='utf8')
	
	adj_file = codecs.open("adjectives.txt",'r',encoding='utf8')
	adj = {}
	for line in adj_file:
		l = line.strip()
		if l in adj.keys():
			count = adj[l]
			count = count + 1
			adj[l] = count
		else:
			adj[l] = 1	
	
	
	
	word='a'
	count = 0
	word = tweet_file.readline().strip()
	while word !='<ENDFILE>':
		count = count + 1
		
		tokens = []
		
		
		while word != '<ENDSENTENCE>':
			tokens.append(word)
			word = tweet_file.readline().strip()
			
		createVector(tokens,feat_vector,adj)
		print str(count)+'th sentence finished'		
		word = tweet_file.readline().strip()
	
def createVector(tokens,feat_vector,adj):
	
	
	
	unary = {}
	for index in range(0,len(tokens)):
		unary_w = tokens[index]
		if unary_w in unary.keys():
			count = unary[unary_w]
			count = count + 1
			unary[unary_w] = count
		else:
			unary[unary_w] = 1
	
			
			
	for item,value in adj.iteritems():
		if value <3:
			continue
		if item in unary.keys():
			feat_vector.write(str(unary[item])+' ')
		else:
			feat_vector.write(str(0)+' ')
	
	print 'done for unary'
	
	
	
	feat_vector.write('\n')
	
if __name__ == '__main__':
  main()