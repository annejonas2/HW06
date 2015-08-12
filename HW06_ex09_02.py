#!/usr/bin/env python
# HW06_ex09_02.py

# (1)
# Write a function called has_no_e that returns True if the given word doesn't
# have the letter "e" in it.
#   - write has_no_e
# (2)
# Modify your program from 9.1 to print only the words that have no "e" and
# compute the percentage of the words in the list have no "e."
#   - print each approved word on new line, followed at the end by the %
##############################################################################
# Imports

# Body
def has_no_e(word):
	if 'e' in word:
		return False
	else:
		return True

def writing_no_e_words():
	with open("words.txt") as fin:
		count = 0
		no_e_count = 0
		no_e_words = ''
		for word in fin:
			count += 1
			if has_no_e(word) == True:
				no_e_count += 1
				no_e_words = no_e_words + word
		decimal = float(no_e_count -1) / count
		str_decimal = str(decimal)
		percent = str_decimal[2:4]
		print no_e_words
		print "Percentage of all words: " + percent + '%' + '\n'


##############################################################################
def main():
      # Call your function(s) here.
    
    # has_no_e('blue')
    writing_no_e_words()

if __name__ == '__main__':
    main()
