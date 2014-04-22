#!/usr/bin/env python

from player import Player
from asciititle import TitleArt
from pygame import mixer

import threading
import Queue
import time
import sys

import ConsoleManip

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
        sys.exit()

    else:
        sys.stdout.write(ConsoleManip.up_line())
        sys.stdout.write(ConsoleManip.up_line())
        sys.stdout.write(ConsoleManip.clear_line())     
        print 'YololPlayer cannot process ' + userinput + '\n'

def getInput():
	while True:
		cmd = raw_input('YololPlayer: ')
		handleInput(cmd)

		sys.stdout.write(ConsoleManip.up_line())
		sys.stdout.write(ConsoleManip.clear_line())

if __name__ == '__main__':
    print(TitleArt)
   
    inputThread = threading.Thread(target=getInput)

    inputThread.daemon = True
    p.daemon = True

    inputThread.start()
    p.start()

    inputThread.join()
    p.join()
