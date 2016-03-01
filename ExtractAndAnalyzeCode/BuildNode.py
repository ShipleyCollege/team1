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
def doIt(buildMode, filename):	
	notRecognisedCount = 0
	print("Converting " + filename)	
	with open(filename) as f:
		lines = f.read().splitlines()
		if lines[0].startswith("Begin Object Class=K2Node_IfThenElse"):
			processBranch(lines, buildMode)
		elif lines[0].startswith("Begin Object Class=K2Node_CallFunction"):
			processFunction(lines, buildMode)
		elif lines[0].startswith("Begin Object Class=K2Node_Literal Name="):
			processVariable(lines, buildMode)
		elif lines[0].startswith("Begin Object Class=K2Node_VariableSet"):
				processVariable(lines, buildMode)
		elif lines[0].startswith("Begin Object Class=K2Node_VariableGet"):
				processVariable(lines, buildMode)
		elif lines[0].startswith("Begin Object Class=K2Node_InputKey"):
			processKey(lines, buildMode)
		else:
			print("\n======\nNode not recognised\n=====\n")
			notRecognisedCount += 1
		print(" ")
	return notRecognisedCount			
#doIt(FILENAME)



		

		
		