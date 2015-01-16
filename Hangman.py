import sys
import json
from random import randint


hangman_value = ["    0000000000000",
"    0           0",
"    0           1",
"    0         1   1",
"    0           1",
"    0          234",
"    0         2 3 4",
"    0        2  3  4",
"    0          5 6",
"    0         5   6",
"    0        5     6",
"    0       5       6",
"    0",
"    0",
"    0"]

def drawing(value):
	for out_index, col_value in enumerate(hangman_value):
		for in_index, main_value in enumerate(col_value):
			if main_value == ' ':
					print ' ',
			if main_value < str(value):
				if main_value == '0':
					print '|',
				elif main_value == '1':
					print '|',
				elif main_value == '2':
					print '/',
				elif main_value == '3':
					print '|',
				elif main_value == '4':
					print '\\',	
				elif main_value == '5':
					print '/',
				elif main_value == '6':
					print '\\',	
		print '\n'


def find_random_word(mylist):
	random_value = randint(0,len(mylist[0])-1)
	random_word = mylist[0][random_value] = mylist[0][random_value].upper()
	return random_word;


def update_file_list(datafile, mylist, random_word):
	mylist[0].remove(random_word)
	mylist[1].append(random_word)
	datafile.seek(0)
	datafile.truncate()
	json.dump(mylist,datafile)
	datafile.close()


def main():
	attempts_allowed = 7
	PressedCharacters = []
	print '\t\t\t===============================================================';
	print '\t\t\tWelcome to Hangman..Guess the letters in the word in 8 attempts.'
	print '\t\t\t===============================================================';
	raw_input('\t\t\tPress any key to enter')
	

	datafile = open("hangman.dat","r+")
	mylist = json.load(datafile)
	random_word = find_random_word(mylist)
	#print '\n\t' + random_word + '\n';
	word_length = len(random_word)
	print '\nThe word has ' + str(word_length) + ' letters\n'
	for i in range(0,word_length):
			print '_ ',
	drawing_value = 0
	while (attempts_allowed > 0):
		flag = 0
		print '\tGuess any letter: ',
		character = raw_input()
		character = character.upper()
		j = 0
		while (j < word_length):
			if random_word[j] == character:
				flag = 1
				print '\nCORRECT\n--------------------------------------------'
				PressedCharacters.append(character)
				break
			else:
				j = j + 1
		if flag==0:
			attempts_allowed = attempts_allowed - 1
			drawing_value = drawing_value + 1
			drawing(drawing_value)
		IsWinValue = 1
		for j in range(0, word_length):
			if random_word[j] == character or random_word[j] in PressedCharacters:
				print '%s ' % random_word[j],
			else:
				print '_ ',
				IsWinValue = 0
		sys.stdin.flush()	
		if IsWinValue == 1:
			print '\nHurray!!! You won'
			update_file_list(datafile,mylist,random_word)
			break
	if IsWinValue != 1:
		print '\nSORRY, You din\'t guess the word, The answer is \"%s\"' % random_word

if __name__ == '__main__':
	main()


		


