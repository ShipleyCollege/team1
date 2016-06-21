//include <../OpenSCAD/BPNode.scad>;
include <../../ViPteam2/OpenSCAD/BPNode.scad>;

numLines = 3;
longestLine = "Key Event : Z";
drawBase("Key Event : Z");
executePinRightWithText(line2, "Released");
executePinRightWithText(line3, "Pressed");
