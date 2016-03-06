from Node import *
from Pin import *
from Utilities import getQuotedString

###
#  FUNCTION : Handle Branch nodes
###
def processBranch(lines, buildMode, nodeNumber):
	node = Node("Branch", buildMode)
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
	node.writeNode(nodeNumber)
