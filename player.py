#!/usr/bin/env python

import pygame
from pygame import mixer
import os

class Player():
	"""Main class for playing Drake AND ONLY DRAKE GODDAMNIT!!"""

	def __loadFiles(self):
		"""Adds all files in 'mp3' folder to our Files variable"""
		for (root, dirs, files) in os.walk('mp3'):
			for f in files:
				self.Files.append(root + "/" + f) #add each file to our list of Files
	
	def __init__(self):
		"""Initializes player in this order:
		   External libraries
		   Data attributes
		   Populating data attributes
		"""
		mixer.pre_init(44100, -16, 2, 2048) 	#frequency, size, channels, buffersize
		pygame.init()
	
		self.isPaused = False
		self.isStopped = False
		self.Files = []
		self.CurrentPosition = 0;

		self.__loadFiles()

		self.TotalFiles = len(self.Files)
	
	def load(self, filename):
		"""Loads .mp3 or .wav files after making sure they're valid"""
		if isinstance(filename, str): 			#check if input is string
			if filename.split('.')[1] == 'mp3': #check if file type is mp3
				mixer.music.load(os.path.join('', filename)) #cd mp3 & load file
			elif filename.split('.')[1] == 'wav':
				mixer.music.load(os.path.join('wav', filename))

		else:
			print "Can't find " + filename

	def play(self):
		"""Plays the CURRENTLY LOADED file.  Note that this function doesn't call self.stop()"""
		if self.CurrentPosition > self.TotalFiles:	#check if we're in valid space
			self.CurrentPosition = 0

		self.load(self.Files[self.CurrentPosition])
		mixer.music.play() #play once
		self.isStopped = False

	def playSong(self, song):
		"""Plays a specific song"""
		#currently only plays one song; what if userinput returns 2 songs?  queue them up?
		self.stop()
		self.CurrentPosition = self.Files.index(song[0])
		self.play()

	def pause(self):
		mixer.music.unpause() if self.isPaused else mixer.music.pause()	
		self.isPaused = not self.isPaused

	def stop(self):
		mixer.music.stop()
		self.isStopped = True

	def next(self):
		"""Stops the currently playing music, loads up a new piece of music(set boolean rand value later!), 
		   sets CurrentPosition attribute, and plays music
		"""
		self.stop()
		self.load(self.Files[self.CurrentPosition])
		self.CurrentPosition = self.CurrentPosition + 1
		self.play()

p = Player()
nextStrings = ['n', 'ne', 'next']
playStrings = ['pl', 'play']
stopStrings = ['s', 'st', 'stop']
pauseStrings = ['p', 'pa', 'pause']
quitStrings = ['q', 'quit']

isPlaying = True

def handleInput(userinput):
	"""What if a song has 'quit' in it?
	   split string at ' '
	"""
	print userinput

	if any(userinput in string for string in nextStrings):
		p.next()
	
	elif any(userinput in string for string in stopStrings):
		p.stop()

	elif any(userinput in string for string in pauseStrings):
		p.pause()

	elif any(userinput.split(' ', 1)[0] in string for string in playStrings):	#"play x"
		command = userinput.split(' ', 1)[0]  						 		 	#split once at first space
		try:
			song = userinput.split(' ', 1)[1]

			if any(song in string for string in p.Files):				 		#if song is in list of p.Files
				p.playSong([s for s in p.Files if (song in s)])     			#returns a list of songs that contain the same string as userinput
		except IndexError:														 
			p.play() 															#no song appended to the command. "play"

	elif any(userinput in string for string in quitStrings):
		p.stop()
		isPlaying = False
			
	else:
		print 'DrakePlayer cannot process' + userinput +'.\n'
#debug
if __name__ == '__main__':
	p.play()

	while isPlaying:
		if not p.isStopped and mixer.music.get_busy() == 0: #if user didn't stop player and mixer is not busy, a song ended
			p.next()

		userinput = raw_input('DrakePlayer: ')
		handleInput(userinput)
