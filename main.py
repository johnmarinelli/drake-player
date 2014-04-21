#!/usr/bin/env python

from player import Player
from asciititle import TitleArt
from pygame import mixer

import threading
import Queue
import time

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
    print 'input is being handled'
	
    if any(userinput in string for string in nextStrings):
        p.next()

    elif any(userinput in string for string in stopStrings):
        p.stop()

    elif any(userinput in string for string in pauseStrings):
        p.pause()

    elif any(userinput.split(' ', 1)[0] in string for string in playStrings):   #"play x"
        command = userinput.split(' ', 1)[0]                                    #split once at first space
        try:
            song = userinput.split(' ', 1)[1]

            if any(song in string for string in p.Files):                       #if song is in list of p.Files
                p.playSong([s for s in p.Files if (song in s)])                 #returns a list of songs that contain the same string as userinput
        except IndexError:
            p.play()                                                            #no song appended to the command. "play"

    elif any(userinput in string for string in quitStrings):
        p.stop()
        isPlaying = False

    else:
        print 'YololPlayer cannot process' + userinput +'.\n'

"""
def checkSongEnd():
    if not p.isStopped and mixer.music.get_busy() == 0: #if user didn't stop player and mixer is not busy, a song ended
        p.next()
"""

def getInput(queue):
	while True:
		cmd = raw_input('YololPlayer: ')
		queue.put(cmd)
		print 'input received'

		handleInput(queue.get())

		#time.sleep(1)

#debug
if __name__ == '__main__':
    print(TitleArt)
   
    queue = Queue.Queue()
    p.play()
    thread = threading.Thread(target=getInput, args=(queue,))

    thread.start()
    p.start()

#    while isPlaying:
#        handleInput(queue.get())
        #p.checkSongEnd()

    thread.join()
