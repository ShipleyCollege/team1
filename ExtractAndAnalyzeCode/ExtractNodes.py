import os
import glob
import BuildNode


INPUT_FILENAME = "../Sample Blueprint code/SimpleMoveToActor-Network - Code.txt";
WORK_FOLDERNAME = "../Sample Blueprint code/Temp";

# function to remove temporary nodes extracted from network
def removeTempNodes():
    files = glob.glob(WORK_FOLDERNAME + '/node*.txt')
    for f in files:
        os.remove(f)


def DoIt(buildMode):
# make sure we start with an empty directory
    removeTempNodes()

# break network into individual nodes
# - each node starts end ends with 'Begin' and 'End' in column 0
    nodeNumber = 0	
    with open(INPUT_FILENAME) as f:
        content = f.readlines()
        for line in content:
            if (line[0:5] == "Begin"):
                text_file = open(WORK_FOLDERNAME + "/node" + str(nodeNumber) + ".txt", "w")
            text_file.write(line)
            if (line[0:3] == "End"):
                text_file.close()
                nodeNumber += 1

#  nodes to do : 6, 9 

    nrc = 0
    files = glob.glob(WORK_FOLDERNAME + '/node*.txt')
    for f in files:
        print("Calling BuildNode with [" + buildMode + ", " + f + "]")
        nrc += BuildNode.doIt(buildMode, f)

    print("Nodes Extracted : " + str(nodeNumber))
    print("Nodes not recognized : " + str(nrc))

    removeTempNodes()





	
