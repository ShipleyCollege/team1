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
    brickAndText("Key Event : Z");
 // Pin name : Released, pin side : right, pin line : 2, pin type : exec
translate([0, +lineWidth * 1, 0])
    brickAndText("Released");
translate([-12,  +lineWidth * 1, 0]) {
    brick(1, 1, 1);
    translate([0, -2, 3])
        executePin(4, 4);
}
 // Pin name : Pressed, pin side : right, pin line : 3, pin type : exec
translate([0, +lineWidth * 2, 0])
    brickAndText("Pressed");
translate([-12,  +lineWidth * 2, 0]) {
    brick(1, 1, 1);
    translate([0, -2, 3])
        executePin(4, 4);
}
