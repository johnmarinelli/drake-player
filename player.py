#!/usr/bin/env python

import pygame
from pygame import mixer
import os
import threading
import time

SONG_END = pygame.USEREVENT + 1

class Player(threading.Thread):
	"""Main class for playing Drake AND ONLY DRAKE GODDAMNIT!!"""

	def __loadFiles(self):
		"""Adds all files in 'mp3' folder to our Files variable"""
		for (root, dirs, files) in os.walk('mp3'):
			for f in files:
				self.Files.append(root + "/" + f) #add each file to our list of Files
	
	def __printCurrentSong(self):
		print('Now playing: ' + self.Files[self.CurrentPosition])

	def __loop(self):
		while True:
			#if not self.isStopped and mixer.music.get_busy() == 0: #if user didn't stop player and mixer is not busy, a song ended
			#	self.next()
			#time.sleep(1)
			
			event =  pygame.event.wait()
		
			if event.type == SONG_END:
				self.next() 
			#time.sleep(1)

	def __init__(self):
		"""Initializes player in this order:
		   External libraries
		   Data attributes
		   Populating data attributes
		"""
		threading.Thread.__init__(self)
		pygame.init()
		mixer.pre_init(44100, -16, 2, 2048) 	#frequency, size, channels, buffersize
		mixer.music.set_endevent(SONG_END)	
		
		self.isPaused = False
		self.isStopped = False
		self.Files = []
		self.CurrentPosition = 0;

		self.__loadFiles()

		self.TotalFiles = len(self.Files)	
	
	def run(self):
		print 'starting player'	
		self.__loop()

	def checkSongEnd(self):
		for event in pygame.event.get():
			if event.type == SONG_END:
				self.next()

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
		if self.CurrentPosition > self.TotalFiles-1:	#check if we're in valid space
			self.CurrentPosition = 0

		self.load(self.Files[self.CurrentPosition])
		mixer.music.play() #play once
		self.isStopped = False
		self.__printCurrentSong()

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

