#!/usr/bin/python

#from subprocess import call
import os

##Create list of files and folders
def createOldStructure():
	os.system('mkdir -pv test/A/A1 test/B/B1 test/C/C1')
	print "INFO :: folders created"
	os.system('touch test/A/a.aa test/B/b.bb test/C/c.cc test/A/A1/a1.aa test/B/B1/b1.bb test/C/C1/c1.cc test/A/A1/a2.aa test/B/B1/b2.bb test/C/C1/c2.cc')
	print "INFO :: files created"

def createNewStructure():
	os.system('mkdir -pv testNew/AN/A1N testNew/BN/B1N testNew/CN/C1N')
	print "INFO :: folders created - NEW"

createOldStructure()
createNewStructure()

##Read list of file into array


##Compare files and show result


## GIT move


## Show resul of movement 