"""This class gets passed no paramaters but it has a function run that takes either one or two parameters
these paramaters will specify the name and then the location of the file. the class also has a method
called Help that can be called to return a string that can help explain the overall idea of the usage of
the create keyword."""

class Create():
	def keywords(self):
		return(["New","Create","Make","Forge"])
	def help(self):
		return "this command will create a file in the current users documents folder if the user \
specifies somewhere else for the the file to be placed in this manner \
\"create hello.txt in Desktop\""
	def run(name, fileloc = "Documents/"):
		filextention = ".txt"
		for letter in range(len(name)-1):
			if name[letter] == ".":
				filextention = name[letter+1:]
				name = name[:letter+1]
				break
		try:
			file = open(fileloc+name+filextention, "x")
		except:	
			file = open("Documents/"+name+filextention,'x')
