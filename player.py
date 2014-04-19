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
		"""Plays the CURRENTLY LOADED file"""
		if self.CurrentPosition > self.TotalFiles:	#check if we're in valid space
			self.CurrentPosition = 0

		self.load(self.Files[self.CurrentPosition])
		mixer.music.play() #play once

	def pause(self):
		mixer.music.unpause() if self.isPaused else mixer.music.pause()	
		self.isPaused = not self.isPaused

	def stop(self):
		mixer.music.stop()

	def next(self):
		"""Stops the currently playing music, loads up a new piece of music(set boolean rand value later!), 
		   sets CurrentPosition attribute, and plays music
		"""
		self.stop()
		self.load(self.Files[self.CurrentPosition])
		self.CurrentPosition = self.CurrentPosition + 1
		self.play()

#debug
if __name__ == '__main__':
	p = Player()
