#TASK 1

'''import string
f = open("word_samp.txt")
spl = string.punctuation
for line in f:
	line = line.strip()
	word = line.split()
	for w in word:
		s = ''
		for letter in w:
			if letter not in spl:
				s+=letter
		if(s):
			print(s.lower())	
#TASK 2

import string
def book_details():
	spl = string.punctuation
	count = 0
	dic = {}
	for line in f:
		line = line.strip()
		word = line.split()
		for w in word:
			s = ''
			for letter in w:
				if letter not in spl:
					s+=letter
			if(s):
				count+=1
			if s not in dic:
				dic[s] = 1
			else:
				dic[s]+=1
	return count,dic

def word_count():
	c,d = book_details()
	print("No of words in the book is %d" %c)
	for key,val in d.items():
		print(key,val)
	
f = open("book1.txt")
word_count()'''


#TASK 3

import string
def book_details():
	spl = string.punctuation
	count = 0
	dic = {}
	for line in f:
		line = line.strip()
		word = line.split()
		for w in word:
			s = ''
			for letter in w:
				if letter not in spl:
					s+=letter
			if(s):
				count+=1
			if s not in dic:
				dic[s] = 1
			else:
				dic[s]+=1
	return count,dic

def word_count():
	l = []
	l_res = []
	c,d = book_details()
	print("No of words in the book is %d" %c)
	for key,val in d.items():
		l.append((val,key))
	l.sort(reverse=True)
	for i,j in l:
		l_res.append((j,i))
	for n in range(20):
		print(l_res[n])
	
			
f = open("book1.txt")
word_count()
