import WriteCompactNode
import WriteExplodedNode
import WriteExplodedLegoNode

###
#  CLASS : Contains extracted node information
###
class Node:
	title = "unknown"
	leftPins = []
	rightPins = []
	
	def __init__(self, title, mode):
		self.title = title
		self.leftPins = []
		self.rightPins = []
		self.buildMode = mode	
	def __str__(self):
		response = "Node"
		response += "\n- Mode : " + self.buildMode
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
	
	def writeNode(self, nodeNumber):
		if self.buildMode == "Compact":	
			WriteCompactNode.writeNode(self, self.buildMode, nodeNumber)
		elif self.buildMode == "ExplodedLego":	
			WriteExplodedLegoNode.writeNode(self, self.buildMode, nodeNumber)
		else:
			WriteExplodedNode.writeNode(self, self.buildMode, nodeNumber)
				
