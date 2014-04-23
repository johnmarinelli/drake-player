#!/usr/bin/env python

import ConsoleManip
import sys

from yololplayer import p

nextStrings = ['n', 'ne', 'next']
playStrings = ['pl', 'play']
stopStrings = ['s', 'st', 'stop']
pauseStrings = ['p', 'pa', 'pause']
quitStrings = ['q', 'quit']

isPlaying = True

def handleInput(userinput):
    """ Communicates input between input thread and player thread
    """
    if any(userinput in string for string in nextStrings):
        p.next()

    elif any(userinput in string for string in stopStrings):
        p.stop()

    elif any(userinput in string for string in pauseStrings):
        p.pause()

    elif any(userinput in string for string in quitStrings):
        p.stop()
        isPlaying = False
        sys.exit()

    elif any(userinput.split(' ', 1)[0] in string for string in playStrings):   #"play x"
        command = userinput.split(' ', 1)[0]                                    #split once at first space
        try:
            song = userinput.split(' ', 1)[1]

            if any(song in string for string in p.Files):                       #if song is in list of p.Files
                p.playSong([s for s in p.Files if (song in s)])                 #returns a list of songs that contain the same string as userinput
        except IndexError:
            p.play()                                                            #no song appended to the command. "play"

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

def introText():
	cmd = raw_input('Are you on your Drake today? (y/n): ')
	if cmd is 'y':
		p.isOnDrakeToday = True
	elif cmd is 'n':
		p.isOnDrakeToday = False
