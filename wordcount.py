# put your code here.
import string

def get_word_count(filename):
	""" Read text file and return dictionary of word count 
		
		The function gets a text file as an input, and makes a dictionary of 
		the words in the file with their count as their value.
	"""	

	poem = open(filename)
	word_count={}

	for line in poem:
		line = line.strip()
		words = line.split(" ")
		
		for word in words:
			word = word.strip(string.punctuation)
			word_count[word.lower()] = word_count.get(word.lower(),0) + 1

	for k,v in word_count.items():
	 	print("{} {}".format(k,v))


	#return word_count

get_word_count("test.txt")
#get_word_count("twain.txt")