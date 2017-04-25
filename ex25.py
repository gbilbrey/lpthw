def break_words(stuff):
	"""This function will breka up words for us."""
	words = stuff.split()
	return words
	
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)
	
def print_first_word(words):
	""" Print the first word. Popping it off """
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Prints the last word.  Popping it off"""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	""" Takes a full sentence and returns the sorted words. """
	words = break_words(sentence)
	return sort_words(words)
	
def print_first_and_last_sentence(sentence):
	""" Prints the first and last words fo the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)
	
	





	
	

	




