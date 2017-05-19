import os
#improt qwd to find the user file
import pwd

def Searcher(Name):
	#This searches for different versions of the names
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

	os.chdir("/Users/" + pwd.getpwuid( os.getuid() )[ 0 ])
	fileLocations = []
	for dirName, subdirList, fileList in os.walk("."):
		for fname in fileList:
			if fname.lower() in nameList:
				Location = "~"+(dirName + "/" + fname)[1:]
				Location = list(Location)
				#This makes sure that the spaces have a \ before them
				k = 0
				for letter in range(len(Location)-1):
					currentLetter = Location[letter]
					if currentLetter == " ":
						i = letter
						k += 1
					elif currentLetter != " ":
						k = 0
					if k == 1:
						Location.insert(i, "\\")
				fileLocations.append("".join(Location))
				
	if len(fileLocations) > 1:
		for x in range(len(fileLocations)):
			print(str(x+1) + ". " + fileLocations[x])
		local = input("Hey there is more that one file with that name please type the number of the file you want\n")
		
		try:
			local = int(local)
		except:
			try:
				local = input("Hey that wasn't a number\n")
				local = int(local)
				break
			except:
				pass
		
		fileLocation = fileLocations[int(local)-1]
	elif fileLocations == []:
		print("Hey there is no file found with that name")
		return False
	else:
		fileLocation = fileLocations[0]

	return fileLocation
#You can import this as a module but if you just run the file it will look for "helo there.txt"
if __name__ == "__main__":
	print(Searcher("helo there.txt"))
