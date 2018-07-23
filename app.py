import collections
import string
import re
import random


FILE_PATH = "../Pride-and-Prejudice_1342/1342.txt"

def getTotalNumberOfWords():
	num_words = 0
	
	with open(FILE_PATH, 'r') as f:
	    for line in f:
	    	num_words += len(line.split())
	print(num_words)


def getTotalUniqueWords():
	s = set()
	with open(FILE_PATH, 'r') as f:	
		for line in f:
			clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
			for w in clean_line.split():
				s.add(w)
	print(len(s))

def get20MostFrequentWords():
	m = collections.defaultdict(int)
	with open(FILE_PATH, 'r') as f:	
		for line in f:
			clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
			for w in clean_line.split():
				m[w] += 1
	lis = sorted(m.items(), key=lambda x: x[1], reverse=True)
	lis = [x[0] for x in lis[:20]]
	print(lis)

def get20MostInterestingFrequentWords():
	common_words = get_common_set("common.txt", 1000)
	m = collections.defaultdict(int)
	with open(FILE_PATH, 'r') as f:	
		for line in f:
			clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
			for w in clean_line.split():
				m[w] += 1
	lis = sorted(m.items(), key=lambda x: x[1], reverse=True)
	i = 0
	index = 0
	output = []
	while i < 20:
		if lis[index][0] not in common_words:
			output.append(lis[index][0])
			i += 1
			index += 1
		else:
			index += 1
	print(output)


def get_common_set(path, limit):
	s = set()
	counter = 0
	with open(path, 'r') as f:	
		for line in f:
			clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
			for w in clean_line.split():
				if counter >= limit:
					break
				s.add(w)
				counter += 1
				
	return s

def get20LeastFrequentWords():
	m = collections.defaultdict(int)
	with open(FILE_PATH, 'r') as f:	
		for line in f:
			clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
			for w in clean_line.split():
				m[w] += 1
	lis = sorted(m.items(), key=lambda x: x[1], reverse=False)
	lis = [x[0] for x in lis[:20]]
	print(lis)

def getFrequencyOfWord(word):
	word_of_interest = word.lower()
	output = []
	arr = splitter()
	for i in range(0, len(arr)):
		cur_chap = arr[i].split("\n")
		cur_occur = 0
		for line in cur_chap:
			clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
			for w in clean_line.split():
				if w == word_of_interest:
					cur_occur += 1
		output.append(cur_occur)
	print(output)

def getChapterQuoteAppears(quote):
	quote_of_interest = quote.lower()
	quote_of_interest = ''.join([c for c in quote_of_interest if c not in string.punctuation]).lower()
	arr = splitter()
	for i in range(0, len(arr)):
		cur_chap = arr[i].split("\n")
		cur_occur = 0
		cur_str = ""
		for line in cur_chap:
			clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
			cur_str += clean_line + " "
			if quote_of_interest in cur_str:
				return i
	return -1

def generateSentence():
	m = build_mapping()
	word = random.choice(list(m.keys()))
	index = random.randint(0, len(m[word]) - 1)
	word = m[word][index]
	output = ""
	output += str(word)
	i = 1
	while i < 20:
		word = random.choice(list(m[word]))
		output += str(" " + word)
		i += 1
	print(output)

def build_mapping():
	m = collections.defaultdict(list)
	arr = splitter()
	for i in range(0, len(arr)):
		cur_chap = arr[i].split("\n")
		cur_occur = 0
		cur_str = ""
		for line in cur_chap:
			clean_line = ''.join([c for c in line if c not in string.punctuation]).lower()
			cur_str += clean_line + " "
		
		cur_str = cur_str.split(" ")
		
		for i in range(0, len(cur_str) - 1):
			m[cur_str[i]].append(cur_str[i + 1])
	return m

def splitter():
	with open(FILE_PATH, 'r') as f:	
		arr = re.split("Chapter [0-9]+\n", f.read(), flags=re.IGNORECASE)
	return arr


if __name__ == '__main__':
	getTotalNumberOfWords()
	getTotalUniqueWords()
	get20MostFrequentWords()
	get20MostInterestingFrequentWords()
	get20LeastFrequentWords()
	getFrequencyOfWord("Frankenstein")
	generateSentence()
