//include <../OpenSCAD/BPNode.scad>;
include <../../ViPteam2/OpenSCAD/BPNode.scad>;

numLines = 3;
longestLine = "Condition  False";
drawBase("Branch");
leftPin(line2, "Condition");
executePinRightWithText(line2, "False");
executePinLeftWithText(line3,"");
executePinRightWithText(line3, "True");
