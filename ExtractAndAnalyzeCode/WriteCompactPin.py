
def writePin(self, line, side):
	response = "?"
	if (self.pinType == 'exec') and (side == "left"):
		if self.name != "":
			response = "executePinLeftWithText(line" + str(line) + ", \"" + self.name + "\");"
		else:
			response = "executePinLeftWithText(line" + str(line) + ",\"\");"

	if (self.pinType == 'exec') and (side == "right"):
		if self.name != "":
			response = "executePinRightWithText(line" + str(line) + ", \"" + self.name + "\");"
		else:
			response = "executePinRightWithText(line" + str(line) + ",\"\");"

	if (self.pinType != 'exec') and (side == "right"):
		if self.name != "":
			response = "rightPin(line" + str(line) + ", \"" + self.name + "\");"
		else:
			response = "rightPin(line" + str(line) + ");"
									
	if (self.pinType != 'exec') and (side == "left"):
		if self.name != "":
			response = "leftPin(line" + str(line) + ", \"" + self.name + "\");"
		else:
			response = "leftPin(line" + str(line) + ");"
	return(response)
