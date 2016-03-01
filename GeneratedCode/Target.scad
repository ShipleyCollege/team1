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
    brickAndText("Target");
