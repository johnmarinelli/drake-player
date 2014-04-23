#!/usr/bin/env python

import threading
import yplayer.utils

from yplayer.asciiart import titleArt
from yplayer.player import Player
from pygame import mixer

p = Player()

if __name__ == '__main__':
    print(titleArt)
    yplayer.utils.introText()  
 
    inputThread = threading.Thread(target=yplayer.utils.getInput)
	
    p.daemon = True

    inputThread.start()
    p.start()

