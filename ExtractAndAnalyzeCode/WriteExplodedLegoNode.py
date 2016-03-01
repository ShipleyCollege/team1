

def writeNode(self, buildMode):

	self.leftPins = list(reversed(self.leftPins))   
	self.rightPins = list(reversed(self.rightPins))

	openSCAD = []
	openSCAD.append("//include <../OpenScad/TextAndBrailleLegoBlock.scad>\n")
	openSCAD.append("//include <../openSCADLibs/lego_brick_builder.scad> \n")
	openSCAD.append("//include <../openSCAD/BPNode.scad> \n")
	openSCAD.append("//include <../openSCADLibs/lego_brick_builder.scad> \n")
	openSCAD.append("//include <../openSCAD/Pin.scad> \n")

	openSCAD.append("include <../../ViPteam2/OpenSCAD/TextAndBrailleLegoBlock.scad>\n")
	openSCAD.append("include <../../ViPteam2/openSCADLibs/lego_brick_builder.scad> \n")
	openSCAD.append("include <../../ViPteam2/openSCAD/BPNode.scad> \n")
	openSCAD.append("include <../../ViPteam2/openSCADLibs/lego_brick_builder.scad> \n")
	openSCAD.append("include <../../ViPteam2/openSCAD/Pin.scad> \n")

	openSCAD.append("\n")
	
	if len(self.leftPins) > len(self.rightPins):
		longest = len(self.leftPins) 
	else:
		longest = len(self.rightPins)
		
	openSCAD.append("lineWidth = 15;\n")  
		
#	openSCAD.append("drawBase(\"" + self.title + "\");\n")
	openSCAD.append("translate([0, 0, 0])\n    brickAndText(\"" + self.title + "\");\n")


	for i in range(longest ):
		if i < len(self.leftPins):
			openSCAD.append(self.leftPins[i].writePin(i+2, "left", buildMode) + "\n")
		if i < len(self.rightPins):
			openSCAD.append(self.rightPins[i].writePin(i+2, "right", buildMode) + "\n")
		
	outFilename = "../GeneratedCode/" + self.title + ".scad"
	outFile = open(outFilename, "w")
	outFile.writelines( openSCAD )
	outFile.close()
	print(str(len(openSCAD)) + " lines written to " + outFilename)


