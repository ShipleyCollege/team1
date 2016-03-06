# TODO - have blank exec pins


#FILENAME = "../Sample Blueprint code/Branch - code"
FILENAME = "../Sample Blueprint code/Print String - GameOver - Code"

from Node import *			
from Pin import *

from ProcessBranch import *
from ProcessFunction import *
from ProcessVariable import *
from ProcessKey import *





	
###
# Read in Blueprint code and extract information we need.
###		
def doIt(buildMode, filename, nodeNumber):	
	notRecognisedCount = 0
	print("Converting " + filename)	
	with open(filename) as f:
		lines = f.read().splitlines()
		if lines[0].startswith("Begin Object Class=K2Node_IfThenElse"):
			processBranch(lines, buildMode, nodeNumber)
		elif lines[0].startswith("Begin Object Class=K2Node_Commutative"):
			processFunction(lines, buildMode, nodeNumber)
		elif lines[0].startswith("Begin Object Class=K2Node_MacroInstance"):
			processFunction(lines, buildMode, nodeNumber)
		elif lines[0].startswith("Begin Object Class=K2Node_Literal Name="):
			processVariable(lines, buildMode, nodeNumber)
		elif lines[0].startswith("Begin Object Class=K2Node_VariableSet"):
				processVariable(lines, buildMode, nodeNumber)
		elif lines[0].startswith("Begin Object Class=K2Node_VariableGet"):
				processVariable(lines, buildMode, nodeNumber)
		elif lines[0].startswith("Begin Object Class=K2Node_InputKey"):
			processKey(lines, buildMode, nodeNumber)
		elif lines[0].startswith("Begin Object Class=K2Node_Function"):
			processFunction(lines, buildMode, nodeNumber)
		elif lines[0].startswith("Begin Object Class=K2Node"):  # was K2Node_CallFunction
			processFunction(lines, buildMode, nodeNumber)
		else:
			print("\n======\nNode not recognised\n=====\n")
			notRecognisedCount += 1
		print(" ")
	return notRecognisedCount			
#doIt(FILENAME)


		

		
		