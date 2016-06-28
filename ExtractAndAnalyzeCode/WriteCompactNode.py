from Utilities import addSpaces
import os.path

def writeNode(self, buildMode, OUTPUT_FOLDER, nodeNumber):
	self.leftPins = list(reversed(self.leftPins))   
	self.rightPins = list(reversed(self.rightPins))
		
	openSCAD = []
	openSCAD.append("//include <../OpenSCAD/BPNode.scad>;\n")
	openSCAD.append("include <../../ViPteam2/OpenSCAD/BPNode.scad>;\n")

	openSCAD.append("\n")
	if len(self.leftPins) > len(self.rightPins):
		longest = len(self.leftPins) 
	else:
		longest = len(self.rightPins)
	openSCAD.append("numLines = " + str(longest+1) + ";\n")
		
	longestLine = self.title
	print(self.title, len(self.leftPins), len(self.rightPins))
	for i in range(longest ):
		if i < len(self.leftPins) and i < len(self.rightPins):
			t = self.leftPins[i].name + "  " + self.rightPins[i].name
		elif len(self.leftPins) > 0 and i <= len(self.leftPins):
			t = self.leftPins[i].name
		elif i <= len(self.rightPins):
			t = self.rightPins[i].name
		else:
			print("logic error!")
		if len(longestLine) < len(t):
			longestLine = t
	openSCAD.append("longestLine = \"" + longestLine + "\";\n")    
				
	openSCAD.append("drawBase(\"" + addSpaces(self.title) + "\");\n")
	for i in range(longest ):
		if i < len(self.leftPins):
			openSCAD.append(self.leftPins[i].writePin(i+2, "left", buildMode) + "\n")
		if i < len(self.rightPins):
			openSCAD.append(self.rightPins[i].writePin(i+2, "right", buildMode) + "\n")
	
#	outFilename = "../GeneratedCode/" + nodeNumber + self.title + ".scad"
#	if (os.path.isfile(outFilename) ):
#		outFilename = "../GeneratedCode/" + nodeNumber + self.title + "Alt" + ".scad"
#	outFile = open(outFilename, "w")		
	
	outFilename = OUTPUT_FOLDER + "/" + nodeNumber + self.title + ".scad"
	if (os.path.isfile(outFilename) ):
		outFilename = OUTPUT_FOLDER + "/" + nodeNumber + self.title + "Alt" + ".scad"
	outFile = open(outFilename, "w")
	outFile.writelines( openSCAD )
	outFile.close()
	print(str(len(openSCAD)) + " lines written to " + outFilename)


