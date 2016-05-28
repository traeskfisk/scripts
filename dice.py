from sys import exit
from random import randint

def dice():

	print "The dice shows"
	print randint(1,6)
	print "Wanna throw again?"
	choice = raw_input("> ")
	if choice == 'yes':
		dice()
	else:
		exit(1)

def throw():

	print "Wanna throw the dice?"
	choice = raw_input("> ")
	if choice == 'yes':
		dice()
	if choice == 'no':
		print "Oh, okay."
		exit(1)
	if choice == 'exit':
		exit(1)
	else:
		print "Choose by typing yes or no."
		throw()

throw()
