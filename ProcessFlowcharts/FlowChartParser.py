# http://www.diveintopython3.net/xml.html

FILENAME = "TestData/Test Flowchart1.vdx"

import xml.etree.ElementTree as etree

class Node:

	def __init__(self, nodeId, nodeName):
		self.nodeId = nodeId
		self.nodeName = nodeName
		self.addType(nodeName)
		self.nodeText = "?"
		self.fromLinks = []
		self.toLinks = []	
		
	def __str__(self):
		response = "ID : " + self.nodeId + ", type : " + self.nodeType + ", [" + self.nodeText + "]"
		response += "  from(" 
		for connector in self.fromLinks:
			response += connector.fromNode + " "
		response += "), to(" 
		for connector in self.toLinks:
			response += connector.toNode + " "	
		response += ")." 
		return response

	def addText(self, nodeText):
		self.nodeText = nodeText
	def addType(self, nodeType):
		if nodeType == "com.lucidchart.ProcessBlock":
			self.nodeType = "process"
		elif nodeType == "com.lucidchart.DecisionBlock":
			self.nodeType = "decision"
		elif nodeType == "com.lucidchart.Line":
			self.nodeType = "line"	
		else:
			self.nodeType = nodeType
	def addFromLink(self, connector):
		self.fromLinks.append(connector)
	def addToLink(self, connector):
		self.toLinks.append(connector)
	def writeNode(self):
		outFilename = "../GeneratedCode/" + self.nodeType + self.nodeId + ".scad"
		openSCAD = []

		openSCAD.append("// Node built from " + outFilename + "\n")
		if self.nodeType == "process":
			outFile = open(outFilename, "w")
			openSCAD.append("//include <../OpenSCAD/FCProcess.scad>;\n")
			openSCAD.append("include <../../ViPteam2/OpenSCAD/FCProcess.scad>;\n")
		elif self.nodeType == "decision":
			outFile = open(outFilename, "w")
			openSCAD.append("//include <../OpenSCAD/FCDecision.scad>;\n")
			openSCAD.append("include <../../ViPteam2/OpenSCAD/FCDecision.scad>;\n")
		else:
			print("Node " + self.nodeId + " is a line and a model for it has not been generated")
			return
			
		openSCAD.append("printValue(\"" + self.nodeText +"\");\n")
		outFile.writelines( openSCAD )
		outFile.close()
		print("Model created and written to " + outFilename)

class Connector:
	fromNode = "?"
	toNode = "?"
	def __init__(self, fromNode, toNode):
		self.fromNode = fromNode
		self.toNode = toNode
	def __str__(self):
		return "Conector : " + self.fromNode + "->" + self.toNode

###
#  Start of Code
###
tree = etree.parse(FILENAME) 
root = tree.getroot()                 
lines = []
nodes = []
connectors = []

# build node objects from shapes
shapes = root.findall(".//Shape")
for shape in shapes:
	if "Name" in shape.attrib:
		node = Node(shape.attrib["ID"],shape.attrib["Name"])
		item = shape.findall(".//cp", namespaces=None)
		if item != None:
			for x in item:
				node.addText(x.tail)
		nodes.append(node)

#texts = root.findall(".//cp")
#for text1 in texts:
#	print(text1.tail)
#	lines.append(text1.tail)

# build connector objects from connects	
arrows = root.findall(".//Connect")
for arrow in arrows:
	connector = Connector(arrow.attrib["ToSheet"],  arrow.attrib["FromSheet"])
	connectors.append(connector)

nodeDict = {}
for node in nodes:
	nodeDict[node.nodeId] = node
		
for connector in connectors:
	print(connector)
	node = nodeDict[connector.fromNode]
	node.addToLink(connector)
	node.addFromLink(connector)
	node = nodeDict[connector.toNode]
	node.addToLink(connector)
	node.addFromLink(connector)

	
for node in nodes:
	node.writeNode();






	
	