from Node import *
from Pin import *
from Utilities import getQuotedString


###
#  FUNCTION : Handle Branch nodes
###
def processKey(lines, buildMode, nodeNumber, OUTPUT_FOLDER):	
	node = Node("Key Event ", buildMode)	
	
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
	node.writeNode(nodeNumber, OUTPUT_FOLDER)
