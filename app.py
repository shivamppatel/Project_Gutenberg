import collections
import string

FILE_PATH = "../Pride-and-Prejudice_1342/1342.txt"

def getTotalNumberOfWords():
	num_words = 0
	
	with open(FILE_PATH, 'r') as f:
	    for line in f:
	    	num_words += len(line.split())
	print(num_words)


def getTotalUniqueWords():
	s = set()
	with open(file, 'r') as f:	
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
	print(lis[:20])

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
			output.append(lis[index])
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
	print(lis[:20])


# def getFrequencyOfWord():
	


if __name__ == '__main__':
    get20LeastFrequentWords()