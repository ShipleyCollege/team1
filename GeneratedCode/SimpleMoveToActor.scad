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
    brickAndText("SimpleMoveToActor");
 // Pin name : , pin side : left, pin line : 2, pin type : exec
translate([-12,  -lineWidth * 1, 0]) {
    brick(1, 1, 1);
    translate([0, -2, 3])
        executePin(4, 4);
}
 // Pin name : , pin side : right, pin line : 2, pin type : exec
translate([-12,  +lineWidth * 1, 0]) {
    brick(1, 1, 1);
    translate([0, -2, 3])
        executePin(4, 4);
}
 // Pin name : Controller, pin side : left, pin line : 3, pin type : object
translate([0, -lineWidth * 2, 0])
    brickAndText("Controller");
translate([-12,  -lineWidth * 2, 0]) {
    brick(1, 1, 1);
     pin(4, 4, 3);
}
 // Pin name : Goal, pin side : left, pin line : 4, pin type : object
translate([0, -lineWidth * 3, 0])
    brickAndText("Goal");
translate([-12,  -lineWidth * 3, 0]) {
    brick(1, 1, 1);
     pin(4, 4, 3);
}
