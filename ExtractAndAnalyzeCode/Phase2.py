# TODO - have blank exec pins


#FILENAME = "../Sample Blueprint code/Branch - code"
FILENAME = "../Sample Blueprint code/Print String - GameOver - Code"

###
#  CLASS : Contains extracted node information
###
class Node:
	title = "unknown"
	leftPins = []
	rightPins = []
	
	def __init__(self, title):
		self.title = title
		self.leftPins = []
		self.rightPins = []
		
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
		
		openSCAD.append("drawBase(\"" + self.title + "\");\n")
		for i in range(longest ):
			if i < len(self.leftPins):
				openSCAD.append(self.leftPins[i].writePin(i+2, "left") + "\n")
			if i < len(self.rightPins):
				openSCAD.append(self.rightPins[i].writePin(i+2, "right") + "\n")
			
		outFilename = "../GeneratedCode/" + self.title + ".scad"
		outFile = open(outFilename, "w")
		outFile.writelines( openSCAD )
		outFile.close()
		print(str(len(openSCAD)) + " lines written to " + outFilename)


		
		
class Pin:
	name = "?"
	type = "?"
	def __init__(self, name, type):
		if name == "execute" and type == "exec":
			self.name = ""
		elif name == "then" and type == "exec":
			self.name = ""
		else:
			self.name = name.title()
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
				response = "executePinLeftWithText(line" + str(line) + ",\"\");"
		
		if (self.type == 'exec') and (side == "right"):
			if self.name != "":
				response = "executePinRightWithText(line" + str(line) + ", \"" + self.name + "\");"
			else:
				response = "executePinRightWithText(line" + str(line) + ",\"\");"
		
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
		return(response)


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
#  FUNCTION : Handle Function nodes
###
def processFunction(lines):	
	node = Node("Function")
	inObject = False
	pinName = ""
	pinType = ""
	pinSide = ""	
	for line in lines:
		line = line.strip(" ")
		if line.startswith("FunctionReference"):
			functionName = getQuotedString(line)
			node.title = functionName
		if inObject:
			# need to handle defaultValue=?
			# handle advanced view better?
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
			if line.startswith("bHidden=True"):
				print("Pin is hidden : " + line)
				pinSide = "" 		
			if line.startswith("bAdvancedView=True"):
				print("Pin only on advanced view : " + line)
				pinSide = "" 	
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
#  FUNCTION : Handle Function nodes
###
def processVariable(lines):	
	node = Node("Variable")
	inObject = False
	pinName = ""
	pinType = ""
	pinSide = ""	
	for line in lines:
		line = line.strip(" ")
		if line.startswith("PinFriendlyName"):
			functionName = getQuotedString(line)
			node.title = functionName
	print(node)
	node.writeNode()



###
#  FUNCTION : Handle Branch nodes
###
def processKey(lines):	
	node = Node("Key Event ")	
	
	for line in lines:
		line = line.strip(" ")
		if line.startswith("InputKey="):
			keyName = line[line.index('InputKey=')+9]
			node.title = "Key Event : " + keyName
	
	pin1 = Pin('Pressed', 'exec')
	node.addPin(pin1, 'Right')
	pin2 = Pin('Released', 'exec')
	node.addPin(pin2, 'Right')	


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
def doIt(filename):	
	print("Converting " + filename)	
	with open(filename) as f:
		lines = f.read().splitlines()
		if lines[0].startswith("Begin Object Class=K2Node_IfThenElse"):
			processBranch(lines)
		elif lines[0].startswith("Begin Object Class=K2Node_CallFunction"):
			processFunction(lines)
		elif lines[0].startswith("Begin Object Class=K2Node_Literal Name="):
			processVariable(lines)
		elif lines[0].startswith("Begin Object Class=K2Node_VariableSet"):
				processVariable(lines)
		elif lines[0].startswith("Begin Object Class=K2Node_VariableGet"):
				processVariable(lines)
		elif lines[0].startswith("Begin Object Class=K2Node_InputKey"):
			processKey(lines)
		else:
			print("\n======\nNode not recognised\n=====\n")
		print(" ")
			
#doIt(FILENAME)



		

		
		