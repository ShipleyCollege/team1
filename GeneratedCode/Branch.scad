//include <../OpenSCAD/BPNode.scad>;
include <../../ViPteam2/OpenSCAD/BPNode.scad>;

numLines = 3;
longestLine = "Condition False";
drawBase("Branch");
executePinLeft(line2);
executePinRightWithText(line2, "True");
leftPin(line3, "Condition");
executePinRightWithText(line3, "False");
