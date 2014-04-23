#!/usr/bin/env python

import threading
import utils

from AsciiArt import TitleArt
from player import Player
from pygame import mixer

p = Player()

if __name__ == '__main__':
    print(TitleArt)
    utils.introText()  
 
    inputThread = threading.Thread(target=utils.getInput)
	
    p.daemon = True

    inputThread.start()
    p.start()

