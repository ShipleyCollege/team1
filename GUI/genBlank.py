import sys

sys.path.append('../ExtractAndAnalyzeCode')
import Node
import Pin


'''
Inputs
p1 - output Folder
p2 - Build mode (compact, exploded, explodedLego)
p3 - Title
p4 - Row 1 Col 1 : pinType (exec, data)
p5 - Row 1 Col 1 : text (pin title or "")
p6 - Row 1 Col 2 : pinType
p7 - Row 1 Col 2 : text
p8 - Row 2 Col 1 : pinType
p9 - Row 2 Col 1 : text
p10- Row 2 Col 2 : pinType
p11- Row 2 Col 2 : text
etc.

'''

print( 'Number of arguments:', len(sys.argv), 'arguments.')
print( 'Argument List:', str(sys.argv))
print(" ")

if len(sys.argv) < 4:
	print("Error, insuficient parameters. These are expected;\nP1 : Output Folder Name\nP2 : Build Mode\nP3 : Title\nP4-n : [Pin Type, Pin Name] * n")
	sys.exit(0)

outputFolder = sys.argv[1]

node = Node.Node(sys.argv[3], sys.argv[2])

pins = []
for c in range(4, len(sys.argv), 2):
	if c >= len(sys.argv):
		continue
	if sys.argv[c] == 0:
		continue
	if (c+1) == len(sys.argv):
		continue
	pin = Pin.Pin(sys.argv[c+1], sys.argv[c])  # name , type
	print("Pin : " + str(pin))
	pins.append(pin)
	
pins.reverse() # make sure the pins are the correct way round
	
for c in range(len(pins)):
	if c % 2:
		node.addPin(pins[c], "Left")
	else:
		node.addPin(pins[c], "Right")

print(node)

node.writeNode("0", outputFolder)

