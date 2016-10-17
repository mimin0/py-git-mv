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

#createOldStructure()
#createNewStructure()

##Read list of file into array
oldPath = '/Users/vitalik/git/python/test'
newPath = '/Users/vitalik/git/python/testNew'
for root, directories, filenames in os.walk(oldPath):
	#for directory in directories:
		#print os.path.join(root, directory) 
		#print "root -- %s" %root
	for filename in filenames:
		#print os.path.join(root,filename)
		#print "PATH: %s NAME: %s" %(root, filename)
		oldFile = os.path.join(root, filename)
		##http://stackoverflow.com/questions/3964681/find-all-files-in-directory-with-extension-txt-in-python
		for newRoot, dirs, files in os.walk(newPath):
			if filename in files:
				#print "found coinsedence %s %s" %(newRoot, filename)
				newFile = os.path.join(newRoot, filename)
			else:
				newFile = "-"

		print oldFile, newFile
		#result.append(oldFile,newFile)
		#print "found coinsedence %s" %(newRoot, filename)

##Compare files and show result
## GIT move
## Show resul of movement 
