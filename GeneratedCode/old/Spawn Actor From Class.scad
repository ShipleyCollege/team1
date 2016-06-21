//include <../OpenSCAD/BPNode.scad>;
include <../../ViPteam2/OpenSCAD/BPNode.scad>;

numLines = 6;
longestLine = "Collision Handling Override";
drawBase("Spawn Actor From Class");
executePinLeftWithText(line2,"");
executePinRightWithText(line2,"");
leftPin(line3, "Class");
rightPin(line3, "Return Value");
leftPin(line4, "Spawn Transform");
leftPin(line5, "Collision Handling Override");
leftPin(line6, "Instigator");
