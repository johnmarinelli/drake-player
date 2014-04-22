#!/usr/bin/env python

def verifyDrake(songfile):
	isDrake = False
	
	f = file(songfile, 'rb') #read in as binary data
	f.seek(0)

	if 'Drake' in f.read():
		isDrake = True
	else:
		print('Nah')
		isDrake = False

	return isDrake
