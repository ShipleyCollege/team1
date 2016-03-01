# team1
Normalize and Extract data from UE4 BP editor and write to flat file.

Sample data for a UE4 Blueprint 'BRANCH' node is;


//--------------------START----------------------------<br>
include <BPNode.scad>;   // needed for OpenSCAD<br>
numLines = 3;                       // Used to deterimine depth<br>
longestLine = "Condition False";    // Used to deterimine width<br>
<br>
drawBase("Branch");                 // Title of node<br>
<br>
executePinLeft(line2);              // Draw an execute pin on the left, on line 2<br>
executePinRightWithText(line2, "True");  // Draw another on the right, with text<br>
<br>
leftPin(line3, "Condition");        // Draw a data pin, on the left, on line 3 with text<br>
executePinRightWithText(line3, "False");  // Draw another execute pin on right, with text<br>
//-----------------END---------------------------------<br>

<p>
When run through OpenSCAD, this will create an .stl file, which can then be printed on a 3D printer.

Sample commands are;
<table border="1">
<tr>
 <td>include<BPNode.scad>;</td>
</tr><tr>
 <td>numLines = n;</td>
</tr><tr>
 <td>longestLine = "   ";</td>
</tr><tr>
 <td>drawBase("Title");</td>
</tr><tr>
 <td>executePinLeft(lineNumber);</td>
</tr><tr>
 <td>executePinLeftWithText(lineNumber, text);</td>
</tr><tr>
 <td>executePinRight(lineNumber);</td>
</tr><tr>
 <td>executePinRightWithText(lineNumber, text);</td>
</tr><tr>
 <td>leftPin(lineNumber, text);</td>
</tr><tr>
 <td>rightPin(lineNumber, text);</td>
</tr>
<table>

tbc





