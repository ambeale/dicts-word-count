# put your code here.
import string
import sys

def get_word_count(filename):
	""" Read text file and print word counts
		
		The function gets a text file as an input, and makes a dictionary of 
		the words in the file with their count as their value.
	"""	

	poem = open(filename)
	word_count={}

	for line in poem:
		words = line.strip().split(" ")
		
		for word in words:
			word = word.strip(string.punctuation).lower()
			word_count[word] = word_count.get(word,0) + 1

	for k,v in word_count.items():
	 	print("{} {}".format(k,v))


	#return word_count

get_word_count(sys.argv[1])
#get_word_count("twain.txt")