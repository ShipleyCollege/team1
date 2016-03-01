from Node import *
from Pin import *
from Utilities import getQuotedString


###
#  FUNCTION : Handle Variable nodes
###
def processVariable(lines, buildMode):	
	node = Node("Variable", buildMode)
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

