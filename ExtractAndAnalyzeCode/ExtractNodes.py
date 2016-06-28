import os
import glob
import BuildNode


#INPUT_FILENAME = "../Sample Blueprint code/SimpleMoveToActor-Network - Code.txt";
#INPUT_FILENAME = "../Sample Blueprint code/SpawnObjectsWithForLoop - Code.txt";
#INPUT_FILENAME = "../Sample Blueprint code/SpawnRoundTargetPoint - Code.txt";
#INPUT_FILENAME = "../Sample Blueprint code/SpawnRoundTargetPointV2 - Code.txt";
#INPUT_FILENAME = "../Sample Blueprint code/SpawnRoundTargetPointV3 - Code.txt";
#INPUT_FILENAME = "../Sample Blueprint code/JISCTest1.txt";
#INPUT_FILENAME = "../Sample Blueprint code/ResetLevelAfterTimeout.txt";
INPUT_FILENAME = "../Sample Blueprint code/Randomly Spawn Sound Objects - Code.txt";

OUTPUT_FOLDER = "../GeneratedCode"


WORK_FOLDERNAME = "../GeneratedCode/Temp";

# function to remove temporary nodes extracted from network
def removeTempNodes():
	if not os.path.exists(WORK_FOLDERNAME):
		os.makedirs(WORK_FOLDERNAME)
	files = glob.glob(WORK_FOLDERNAME + '/node*.txt')
	for f in files:
		os.remove(f)

def DoItNow(buildMode, filename, output_folder, debug=False):
	global INPUT_FILENAME
	INPUT_FILENAME = filename
	global OUTPUT_FOLDER
	OUTPUT_FOLDER = output_folder
	global WORK_FOLDERNAME
	WORK_FOLDERNAME = OUTPUT_FOLDER + "/Temp"
	DoIt(buildMode, debug=debug)


def DoIt(buildMode, debug=False):
# make sure we start with an empty directory
	removeTempNodes()

# break network into individual nodes
# - each node starts end ends with 'Begin' and 'End' in column 0
	nodeNumber = 0	
	print("Reading network from " + INPUT_FILENAME)

	if (not os.path.isfile(INPUT_FILENAME)) or (not os.path.exists(INPUT_FILENAME)):
		print("======> Input File Not Found <======")
	else:
		print("======> Input File Found <=======")

	with open(INPUT_FILENAME) as f:
		content = f.readlines()
		for line in content:
			if (line[0:5] == "Begin"):
				text_file = open(WORK_FOLDERNAME + "/node" + str(nodeNumber) + ".txt", "w")
			text_file.write(line)
			if (line[0:3] == "End"):
				text_file.close()
				nodeNumber += 1

	nrc = 0
	nodeNumber = 0
	files = glob.glob(WORK_FOLDERNAME + '/node*.txt')
	for f in files:
		print("Calling BuildNode with [" + buildMode + ", " + f + "]")
		if debug:
			nrc += BuildNode.doIt(OUTPUT_FOLDER, buildMode, f, str(nodeNumber))
		else:
			nrc += BuildNode.doIt(OUTPUT_FOLDER, buildMode, f, "")

		nodeNumber += 1

	print("Nodes Extracted : " + str(nodeNumber))
	print("Nodes not recognized : " + str(nrc))

#    removeTempNodes()





	
