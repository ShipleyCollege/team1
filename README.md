# team1
Normalize and Extract data from UE4 BP editor and write to flat file.

Sample data for a UE4 Blueprint 'BRANCH' node is;

//--------------------START----------------------------
include <BPNode.scad>;   // needed for OpenSCAD
numLines = 3;                       // Used to deterimine depth
longestLine = "Condition False";    // Used to deterimine width

drawBase("Branch");                 // Title of node

executePinLeft(line2);              // Draw an execute pin on the left, on line 2
executePinRightWithText(line2, "True");  // Draw another on the right, with text

leftPin(line3, "Condition");        // Draw a data pin, on the left, on line 3 with text
executePinRightWithText(line3, "False");  // Draw another execute pin on right, with text
//-----------------END---------------------------------

When run through OpenSCAD, this will create an .stl file, which can then be printed on a 3D printer.

Sample commands are;

include<BPNode.scad>;
numLines = n;
longestLine = "   ";
drawBase("Title");
executePinLeft(lineNumber);
executePinLeftWithText(lineNumber, text);
executePinRight(lineNumber);
executePinRightWithText(lineNumber, text);
leftPin(lineNumber, text);
rightPin(lineNumber, text);

tbc





