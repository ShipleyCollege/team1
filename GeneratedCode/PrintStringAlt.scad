//include <../OpenSCAD/BPNode.scad>;
include <../../ViPteam2/OpenSCAD/BPNode.scad>;

numLines = 3;
longestLine = "PrintString";
drawBase("Print String");
leftPin(line2, "In String");
executePinRightWithText(line2,"");
executePinLeftWithText(line3,"");
