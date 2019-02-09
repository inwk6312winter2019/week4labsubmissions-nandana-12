#TASK 1

import string

def remove_punctuations(book):
	new_words = [] 
	spl = string.punctuation
	for line in book:
		line = line.strip()
		word = line.split()
		for w in word:
			s = ''
			for letter in w:
				if letter not in spl:
					s+=letter
			if(s):
				new_words.append(s.lower())
	return new_words

f = open("./word_samp.txt")
print(remove_punctuations(f))
f.close()

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
word_count()
f.close()

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

def words_count():
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
words_count()
f.close()


#TASK 4 

def not_in_words(book,the_words):
	book_set = set(remove_punctuations(book))
	word_set = set()
	#for line in book:
		#line = line.strip()
		#word = line.split()
		#for w in word:
			#book_set.add(w)
	for wor in the_words:
		 wor = wor.strip()
		 wor = wor.split()
		 for wo in wor:
		 		word_set.add(wo)
	print(book_set)

b = open("book1.txt")
my_words = open("words.txt")
not_in_words(b,my_words)

#TASK 5
import matplotlib.pyplot as plt
from tabulate import tabulate
import math
import string

def freq(book):
	d = {}
	l = []
	for line in book:
		line = line.strip()
		word = line.split()
		for w in word:
			d[w] = d.get(w,0) + 1
	for i,j in d.items():
		l.append((j,i))
	l.sort(reverse = True)
	return l

def rank(b):
	rank_list = []
	log_r = []
	log_f = []
	freq_list = freq(b)
	for i,j in freq_list:
		log_f.append(math.log(i))
		ran = freq_list.index((i,j))+1
		log_r.append(math.log(ran))
		print(j,"   ",i,"   ",math.log(i),"   ",ran,"   ",math.log(ran))
	plot_ranks(log_r,log_f)
	
def plot_ranks(log_r,log_f):
		plt.plot(log_r,log_f)
		plt.savefig("./zipf.png")
		
f = open("book1.txt")
the_hist = rank(f)


#TASK 6

import os
for root, dirs, files in os.walk(".", topdown=False):
   for name in files:
      print(os.path.join(root, name))
   for name in dirs:
      print(os.path.join(root, name))

import os
def walk(dirname):    
	for name in os.listdir(dirname):        
		path = os.path.join(dirname, name)        
		if os.path.isfile(path):            
			print(path)        
		else:            
			walk(path)
walk(".")

#TASK 7

def sed(pattern,repl,f1,f2):
	for line in f1:
		line2 = line.replace(pattern,repl)
		f2.write(line2)
		#f2.write("    ")

try:
	file1 = open("sample.txt")
	file2 = open("new_file.txt")
	repl_str = input("Enter the replacement string : ")
	sed("the",repl_str,file1,file2)

except FileNotFoundError:
	print("No file found!! Exiting!!!")
	exit()

#TASK 8






