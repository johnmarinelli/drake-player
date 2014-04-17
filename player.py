#!/usr/bin/env python

import pygame
from pygame import mixer
import os

class DrakePlayer():
	"""Main class for playing Drake AND ONLY DRAKE GODDAMNIT!!"""

	def __init__(self):
		mixer.pre_init(44100, -16, 2, 2048) #frequency, size, channels, buffersize
		pygame.init()
		self.isPaused = False
	
	def load(self, filename):
		if isinstance(filename, str): #check if input is string
			if filename.split('.')[1] == 'mp3': #check if file type is mp3
				mixer.music.load(os.path.join('mp3', filename)) #cd mp3 & load file
			elif filename.split('.')[1] == 'wav':
				mixer.music.load(os.path.join('wav', filename))

		else:
			print "Can't find " + filename

	def play(self):
		mixer.music.play(0) #play once

	def pause(self):
		mixer.music.unpause() if self.isPaused else mixer.music.pause()	
		self.isPaused = not self.isPaused

	def stop(self):
		mixer.music.stop()
