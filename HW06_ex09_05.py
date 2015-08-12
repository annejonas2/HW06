#!/usr/bin/env python
# HW06_ex09_05.py

# (1)
# Write a function named uses_all that takes a word and a string of required
# letters, and that returns True if the word uses all the required letters at
# least once.
#   - write uses_all
# (2)
# How many words are there that use all the vowels aeiou? How about
# aeiouy?
#   - write functions(s) to assist you
#   - # of words that use all aeiou:
#   - # of words that use all aeiouy:
##############################################################################
# Imports

# Body
def uses_all(word, letters):
	"""Fuction to test if a string contains all of the required letters"""
	for char in letters:
		if char not in word:
			return False
	return True

def how_many_words(fin, letters):
		count = 0
		for word in fin:	
			if uses_all(word, letters):
				count += 1
		return count

##############################################################################
def main():
      print "Words that use all aeiou: " + str(how_many_words(open("words.txt"),"aeiou"))
      print "Words that use all aeiouy: " + str(how_many_words(open("words.txt"),"aeiouy"))


if __name__ == '__main__':
    main()
