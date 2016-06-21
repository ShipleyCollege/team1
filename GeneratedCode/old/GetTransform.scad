//include <../OpenSCAD/BPNode.scad>;
include <../../ViPteam2/OpenSCAD/BPNode.scad>;

numLines = 2;
longestLine = "Target  Return Value";
drawBase("Get Transform");
leftPin(line2, "Target");
rightPin(line2, "Return Value");
