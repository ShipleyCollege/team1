from Node import *
from Pin import *
from Utilities import getQuotedString

###
#  FUNCTION : Handle Function nodes
###
def processFunction(lines, buildMode, nodeNumber):
	node = Node("Function", buildMode)
	inObject = False
	pinName = ""
	pinType = ""
	pinSide = ""	
	for line in lines:
		line = line.strip(" ")
		if line.startswith("FunctionReference"):
			functionName = getQuotedString(line)
			node.title = functionName
		if line.startswith("Begin Object Class=K2Node_SpawnActorFromClass"):
			node.title = "Spawn Actor From Class"
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
		if line.startswith("Begin Object Class"):
			if line.find("FunctionResult") > 0:
				node.title = "Return Node"	
		if line.startswith("SignatureName"):
				node.title = getQuotedString(line)
				
		if line.startswith("PinToolTip="):
			x = line.find("PinToolTip=")
			y = line.find("\\n", x)
			pinName = line[x + 12 : y]		
				
		if line.startswith("MacroGraphReference"):
			x = line.find("StandardMacros:")
			if x > 0:
				y = line.find("'", x)
				node.title = line[x + 15 : y]
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
	node.writeNode(nodeNumber)