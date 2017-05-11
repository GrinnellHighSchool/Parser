import os
#import subprocess for running commands
import subprocess

def Searcher(Name):
	Name = Name.lower()
	nameList = []
	nameList.append(Name)
	nameList.append("." + Name)
	for letter in range(len(Name)-1):
		if Name[letter] == ".":
			thingToAppend = Name[letter:]
			break
		else:
			thingToAppend = Name
	nameList.append(thingToAppend)

	subprocess.run("cd ~",shell = True)
	rootDir = '.'
	fileLocations = []
	for dirName, subdirList, fileList in os.walk(rootDir):
		for fname in fileList:
			if fname.lower() in nameList:
				fileLocations.append("~"+(dirName + "/" + fname)[1:])
	return fileLocations

print(Searcher("hello"))