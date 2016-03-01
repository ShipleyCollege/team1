
		
def writePin(self, line, side):
	response = " "
	
	sign = " "
	if side == "right":
		sign = "+"
	else:
		sign = "-"
		
	response += "// Pin name : " + self.name + ", pin side : " + side + ", pin line : " + str(line) + ", pin type : " + self.pinType + "\n"	
	if (self.name != "") :
		response += "translate([0, " + sign + "lineWidth * " + str(line-1) + ", 0])\n    rotate([180,180,90]) \n printTextAndBraille(\"" + self.name + "\");\n"

	if sign == "-":
		line += 2
	if self.pinType == "exec":
		response  +=  "translate([-12,  " + sign + "lineWidth * " +  str(line-2) +", 0]) {\n        executePin(4, 4);\n}"
	else:
		response  +=  "translate([-12,  " + sign + "lineWidth * " +  str(line-2) +", 0]) {\n        pin(4, 4, 0);\n}"


	return(response)
	
	
	