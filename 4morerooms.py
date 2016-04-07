# 4 Rooms
from sys import exit
from random import randint



class Scene(object):

	def enter(self):
		print "This scene is not yet configured. Subclass it and implement enter()."

class Engine(object):

	def __init__(self, scene_map):
		self.scene_map = scene_map

	def play(self):
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')

		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		#be sure to print out the last scene
		current_scene.enter()

class Death(Scene):

	quips = [
		"You died. \nYou kinda suck at this.",
		"You died. \nSuch a loser. Lol.",
		"You died. \nI have a small cat that's better than you.",
		"You died. \nMy unborn child could do better than this."
	]

	def enter(self):
		print Death.quips[randint(0, len(self.quips)-1)]
		print "Wanna play again?"

		action = raw_input("[Type 'yes' to play again]> ")

		if action == "yes":
			return 'castle'
		else:
			exit(1)

class BadRoom(Scene):

	events = [
		"There was a trap in here, and a big boulder fell on your head.",
		"You awoke the spider queen!"
		"\nShe did not like that."
		"\nShe wrapped you in spider web and piereced your heart with her fang."
	]

	def enter(self):
		print BadRoom.events[randint(0, len(self.events)-1)]
		return 'death'


class Castle(Scene):

	def enter(self):
		print "You're running through the woods from evil."
		print "In order to escape you run into a castle."
		print "You're safe from the evil here."
		print "You come into the castle and hear the door lock. Typical.."
		print "You have no choice but to continue forward."
		print "You can see there are 4 rooms in this castle."

		action = raw_input("[Which room do you go to?]> ")

		if action == "room 1":
			return 'room1'
		if action == "room 2":
			return 'room2'
		if action == "room 3":
			return 'room3'
		if action == "room 4":
			return 'room4'

		else:
			print "Choose with room #"
			return 'castle'

class Room1(Scene):

	def enter(self):
		print "You've entered room 1."
		print "When you entered the room, the door locked itself."
		print "Typical for old castles."
		print "In this room you will find 3 escape hatches."


		action = raw_input("[Which hatch do you choose?]> ")

		if action == "hatch 1":
			print "When you jumped into escape hatch 1 you landed on spikes."
			return 'death'
		if action == "hatch 2":
			print "You fell 200 feet and are now a pancake on the ground."
			return 'death'
		if action == "hatch 3":
			print "This escape hatch was full of water and you don't know how to swim."
			return 'death'

		else:
			print "Choose with hatch #"
			return 'room1'

class Room2(Scene):

	def enter(self):
		print "You've entered room 2."
		print "When you entered the room, the door locked itself."
		print "Typical for old castles."
		print "Here you run into hungry rats."
		print "There is no escape."
		print "You were eaten by hungry, diseased ridden rats,"
		return 'death'

class Room3(Scene):

	def enter(self):
		print "You've entered room 3"
		print "When you entered the room, the door locked itself."
		print "Typical for old castles."
		print "In this room you will find 3 doors."
		print "Which door do you open?"

		good_room = randint(1,3)
		
		action = raw_input("[Which door? Choose with 1, 2 or 3.]> ")

		if int(action) == good_room:
			print "As you open the door you can smell fresh air."
			print "You can feel the warm sun on your face."
			print "You've escaped this castle."
			return 'finished'
		else:
			return 'badroom'
			

class Room4(Scene):

	def enter(self):
		print "You enter room 4."
		print "When you enter the room, the door locked itself."
		print "Typical for old castles."
		print "In this room you will only find 1 door."
		print "You open the door and walk into the next place."
		print "You've entered hell."
		print "You can't go back and you can hear hell hounds bark."
		print "\noOoooOooOOoooooOOOOoo"
		print "\nYou were consumed by insanity and darkness."
		print "The hell hounds came and ate you, not even bone are left behind."
		return 'death'


class Finished(Scene):

    def enter(self):
        print "You won! Good job."
        return 'finished'



class Map(object):

	scenes = {
		'castle': Castle(),
        'room1': Room1(),
        'room2': Room2(),
        'room3': Room3(),
        'room4': Room4(),
        'death': Death(),
        'badroom': BadRoom(),
        'finished': Finished(),
    }


	def __init__(self, start_scene):
		self.start_scene = start_scene

	def next_scene(self, scene_name):
		val = Map.scenes.get(scene_name)
		return val

	def opening_scene(self):
		return self.next_scene(self.start_scene)


a_map = Map('castle')
a_game = Engine(a_map)
a_game.play()
