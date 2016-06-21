//include <../OpenSCAD/BPNode.scad>;
include <../../ViPteam2/OpenSCAD/BPNode.scad>;

numLines = 3;
longestLine = "PrintString";
drawBase("PrintString");
executePinLeft(line2);
executePinRight(line2);
leftPin(line3, "Instring");
