# My little game. 4 rooms.
from sys import exit

def start():

	print "You're running through the woods from evil."
	print "In order to escape you run into a castle."
	print "You're safe from evil here."
	print "You come into the castle and hear the door lock. Typical.."
	print "You have no choice but to continue forward."
	print "You can see that there are 4 rooms in this castle."
	print "Which one do you go to?"

	choice = raw_input("> ")

	if choice == 'room 1':
		room_1()
	elif choice == 'room 2':
		room_2()
	elif choice == 'room 3':
		room_3()
	elif choice == 'room 4':
		room_4()
	else:
		start_again()

def start_again():

	print "You have to make a decision with 'room #'"

	choice = raw_input("> ")

	if choice == 'room 1':
		room_1()
	elif choice == 'room 2':
		room_2()
	elif choice == 'room 3':
		room_3()
	elif choice == 'room 4':
		room_4()
	else:
		start_again()

def room_1():

	print "This is room 1."
	print "When you entered the room, the door locked itself."
	print "Typical for old castles."
	print "In this room you will find 3 escape hatches."
	print "Which one do you choose?"

	choice = raw_input("> ")

	if choice == 'hatch 1':
		dead("When you jumped into escape hatch 1 you landed on spikes, and died.")
	if choice == 'hatch 2':
		dead("You fell 200 feet and are now a pancake on the ground.")
	if choice == 'hatch 3':
		dead("This escape hatch was full of water and you don't know how to swim, you drowned.")
	else:
		room_1_choice()

def room_1_choice():

	print "Make a decision with 'hatch #'"
	choice = raw_input("> ")

	if choice == 'hatch 1':
		dead("When you jumped into escape hatch 1 you landed on spikes, and died.")
	if choice == 'hatch 2':
		dead("You fell 200 feet and are now a pancake on the ground.")
	if choice == 'hatch 3':
		dead("This escape hatch was full of water and you don't know how to swim, you drowned.")
	else:
		room_1_choice()

def room_2():

	print "You've entered room 2."
	print "When you entered the room, the door locked itself."
	print "Typical for old castles."
	print "Here you into hungry rats."
	print "There is no escape."
	dead("You were eaten by hungry, diseased ridden rats.")

def room_3():

	print "Room number 3."
	print "When you entered the room, the door locked itself."
	print "Typical for old castles."
	print "In this room you will find 3 doors."
	print "What door do you open?"

	choice = raw_input("> ")

	if choice == 'door 1':
		dead("There was a trap in here, and a big boulder fell on your head.")
	elif choice == 'door 2':
		print "As you open the door you can smell fresh air."
		print "You can feel the warm sun on your face."
		print "You've escaped."
		print "Good job!"
		exit(0)
	elif choice == 'door 3':
		print "You awoke the spider queen!"
		print "She did not like that."
		dead("She wrapped you in spider web and piereced your heart with her fang.")
	else:
		room_3_choice()

def room_3_choice():

	print "You have to make a decision with 'door #'"

	choice = raw_input("> ")

	if choice == 'door 1':
		dead("There was a trap in here, and a big boulder fell on your head.")
	elif choice == 'door 2':
		print "As you open the door you can smell fresh air."
		print "You can feel the warm sun on your face."
		print "You've escaped."
		print "Good job!"
		exit(0)

	elif choice == 'door 3':
		print "You awoke the spider queen!"
		print "She did not like that."

		dead("She wrapped you in spider web and piereced your heart with her fang.")
	else:
		room_3_choice()

def room_4():

	print "You enter room 4."
	print "When you entered the room, the door locked itself."
	print "Typical for old castles."
	print "In this room you will only find 1 door."
	print "You open the door and walk into the next place."
	print "You've entered hell."
	print "You can't go back and you can hear hell hounds bark."
	print "\noOOooooOooOooooOooooo"
	print "\nYou were consumed by insanity and darkness."

	dead("The hell hounds came and ate you, not even bones are left behind.")

def dead(why):

	print why, "Good job!"
	exit(0)

start()
