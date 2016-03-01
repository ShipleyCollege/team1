import WriteCompactPin
import WriteExplodedPin
import WriteExplodedLegoPin

class Pin:
	name = "?"
	pinType = "?"
	def __init__(self, name, pinType):
		if name == "execute" and pinType == "exec":
			self.name = ""
		elif name == "then" and pinType == "exec":
			self.name = ""
		else:
			self.name = name.title()
		self.pinType = pinType
		
	def __str__(self):
		response = "Pin Name : " + self.name + ", type : " + self.pinType
		return response
		
	def writePin(self, line, side, buildMode):
		if buildMode == "Compact":	
			return WriteCompactPin.writePin(self, line, side)
		elif buildMode == "ExplodedLego":	
			return WriteExplodedLegoPin.writePin(self, line, side)
		else:
			return WriteExplodedPin.writePin(self, line, side)		

