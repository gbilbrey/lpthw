from sys import exit
from random import randint

class Scene(object):
	
	def enter(self):
		pass

class Engine(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
		self.start_scene_key = self.scene_map.start_scene_key

	def play(self):
		print "start scene is %s" %self.start_scene_key
		self.current_scene = self.scene_map.scenes.get(self.start_scene_key)
		while True:
			print "At start, current scene object is %r" %self.current_scene
			self.current_scene_key = self.current_scene.enter()
			print "After .enter() current_scene_key is %s" %self.current_scene_key
			self.current_scene =  self.scene_map.scenes.get(self.current_scene_key)
			print "After dict lookup, current scene object is %r" %self.current_scene 
		
			
		
		
		
class Death(Scene):

	def enter(self):
		print "So sad, you are dead."
		exit(1)

class CentralCorridor(Scene):

	def enter(self):
		print "You are in the central corridor."
		print "A nasty looking alien sits in front of you"
		print "What do you want to do?"
		print "Choices are: 'tell a joke' or 'attack'"
		
		answer = raw_input(">  ")
		
		if answer == "tell a joke":
			print "Gothons have a great sense of humor."
			print "You live!"
			return 'armory'
			
		elif answer == 'attack':
			print "Sorry, you cannot beat the Gothons.  You die"
			return 'death'
		else:
			print "Does not compute!"
			return 'central_corridor'
	

	

class LaserWeaponArmory(Scene):

	def enter(self):
		print "You are in the armory"
		return 'bridge'

class TheBridge(Scene):

	def enter(self):
		print "You are in the bridge"
		return 'escape_pod'
		

class EscapePod(Scene):

	def enter(self):
		print "You are in the escape pod"
		exit(1)

class Map(object):

	scenes = {
	"death": Death(),
	"central_corridor": CentralCorridor(),
	"armory": LaserWeaponArmory(),
	"bridge": TheBridge(),
	"escape_pod": EscapePod()
	}

	def __init__(self, start_scene_key):
		self.start_scene_key = start_scene_key
			
	def opening_scene_key(self):
		self.opening_scene_key = self.start_scene_key







