
		
def writePin(self, line, side):
	response = " "
	
	sign = " "
	if side == "right":
		sign = "+"
	else:
		sign = "-"
		
	response += "// Pin name : " + self.name + ", pin side : " + side + ", pin line : " + str(line) + ", pin type : " + self.pinType + "\n"	
	if (self.name != "") :
		response += "translate([0, " + sign + "lineWidth * " + str(line-1) + ", 0])\n    brickAndText(\"" + self.name + "\");\n"

	if self.pinType == "exec":
		response  +=  "translate([-12,  " + sign + "lineWidth * " +  str(line-1) +", 0]) {\n    brick(1, 1, 1);\n    translate([0, -2, 3])\n        executePin(4, 4);\n}"
	else:
		response  +=  "translate([-12,  " + sign + "lineWidth * " +  str(line-1) +", 0]) {\n    brick(1, 1, 1);\n     pin(4, 4, 3);\n}"


	return(response)
