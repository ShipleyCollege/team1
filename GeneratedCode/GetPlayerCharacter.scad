//include <../OpenScad/TextAndBrailleLegoBlock.scad>
//include <../openSCADLibs/lego_brick_builder.scad> 
//include <../openSCAD/BPNode.scad> 
//include <../openSCADLibs/lego_brick_builder.scad> 
//include <../openSCAD/Pin.scad> 
include <../../ViPteam2/OpenSCAD/TextAndBrailleLegoBlock.scad>
include <../../ViPteam2/openSCADLibs/lego_brick_builder.scad> 
include <../../ViPteam2/openSCAD/BPNode.scad> 
include <../../ViPteam2/openSCADLibs/lego_brick_builder.scad> 
include <../../ViPteam2/openSCAD/Pin.scad> 

lineWidth = 15;
translate([0, 0, 0])
    brickAndText("GetPlayerCharacter");
 // Pin name : Playerindex, pin side : left, pin line : 2, pin type : int
translate([0, -lineWidth * 1, 0])
    brickAndText("Playerindex");
translate([-12,  -lineWidth * 1, 0]) {
    brick(1, 1, 1);
     pin(4, 4, 3);
}
 // Pin name : Returnvalue, pin side : right, pin line : 2, pin type : object
translate([0, +lineWidth * 1, 0])
    brickAndText("Returnvalue");
translate([-12,  +lineWidth * 1, 0]) {
    brick(1, 1, 1);
     pin(4, 4, 3);
}
