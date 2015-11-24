FILENAME = "../Sample Blueprint code/Branch - code"

###
#  CLASS : Contains extracted node information
###
class Node:
	title = "unknown"
	leftPins = []
	rightPins = []
	
	def __init__(self, title):
		self.title = title
		
	def __str__(self):
		response = "Node"
		response += "\n- Title : " + self.title
		response+= "\n Left Pins;\n"
		for pin in self.leftPins:
			response += str(pin) + "\n"
		response+= "\n Right Pins;\n"
		for pin in self.rightPins:
			response += str(pin) + "\n"			
		return response
		
	def addPin(self, pin, side):
		if side == "Left":
			self.leftPins.append(pin)
		else:
			self.rightPins.append(pin)
			
	def writeNode(self):
		print("include <../OpenSCAD/BPNode.scad>;")
		print()
		if len(self.leftPins) > len(self.rightPins):
			longest = len(self.leftPins) 
		else:
			longest = len(self.rightPins)
		print("numLines = " + str(longest+1) + ";")
		
		print("longestLine = \"abcdefghijklm\";")     #  *TODO*
		print("drawBase(\"" + self.title + "\")")
		for i in range(longest ):
			self.leftPins[i].writePin(i+2, "left")
			self.rightPins[i].writePin(i+2, "right")


		
		
class Pin:
	name = "?"
	type = "?"
	def __init__(self, name, type):
		self.name = name
		self.type = type
		
	def __str__(self):
		response = "Pin Name : " + self.name + ", type : " + self.type
		return response
		
	def writePin(self, line, side):
		response = "?"
		if (self.type == 'exec') and (side == "left"):
			if self.name != "":
				response = "executePinLeftWithText(line" + str(line) + ", \"" + self.name + "\");"
			else:
				response = "executePinLeft(line" + str(line) + ");"
		
		if (self.type == 'exec') and (side == "right"):
			if self.name != "":
				response = "executePinRightWithText(line" + str(line) + ", \"" + self.name + "\");"
			else:
				response = "executePinRight(line" + str(line) + ");"
		
		if (self.type != 'exec') and (side == "right"):
			if self.name != "":
				response = "rightPin(line" + str(line) + ", \"" + self.name + "\");"
			else:
				response = "rightPin(line" + str(line) + ");"
										
		if (self.type != 'exec') and (side == "left"):
			if self.name != "":
				response = "leftPin(line" + str(line) + ", \"" + self.name + "\");"
			else:
				response = "leftPin(line" + str(line) + ");"
		print(response)


###
#  FUNCTION : Handle Branch nodes
###
def processBranch(lines):	
	node = Node("Branch")
	inObject = False
	pinName = ""
	pinType = ""
	pinSide = ""	
	for line in lines:
		line = line.strip(" ")
		if inObject:
			if line.startswith("PinName="):
				print("-Name : " + line)
				pinName = getQuotedString(line)
			if line.startswith("PinType="):
				print("-Type : " + line)
				pinType = getQuotedString(line)
			if line.startswith("Direction=EGPD_Output"):
				print("-Direction : " + line)
				pinSide = "Right"
			if line.startswith("PinFriendlyName="):
				print("Pin freindly name : " + line)
				pinName = getQuotedString(line)
		if line.startswith("Begin Object Name="):
			inObject = True
			pinName = ""
			PinType = ""
			pinSide = "Left"			
			print("In Object")
		if line.startswith("End Object"):
			inObject = False
			if pinSide != "":
				pin = Pin(pinName, pinType)
				node.addPin(pin, pinSide)
			pinName = ""
			PinType = ""
			pinSide = ""			
#			print("Out Object")
#		print(">" + line + "<");
	print(node)
	node.writeNode()
		

###
#  FUNCTION : get string between quotes
###
def getQuotedString(string):
	return string.split('"')[1]
		
###
# Read in Blueprint code and extract information we need.
###		
		
with open(FILENAME) as f:
	lines = f.read().splitlines()
	if lines[0].startswith("Begin Object Class=K2Node_IfThenElse"):
		processBranch(lines)
	else:
		print()



		

		
		