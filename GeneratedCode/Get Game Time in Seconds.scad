//include <../OpenSCAD/BPNode.scad>  
//include <../OpenSCAD/Pin.scad>  
//include <../OpenSCAD/brailleAndText.scad> 
include <../../ViPteam2/openSCAD/BPNode.scad>  
include <../../ViPteam2/openSCAD/Pin.scad>  
include <../../ViPtest2/openSCAD/brailleAndText.scad> 

lineWidth = 15;
translate([0, lineWidth * 0, 0])
        rotate([180,180,90]) 
 printTextAndBraille("Get Game Time in Seconds");
 // Pin name : Delta Seconds, pin side : right, pin line : 2, pin type : float
translate([0, +lineWidth * 1, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Delta Seconds");
translate([-12,  +lineWidth * 0, 0]) {
        pin(4, 4, 0);
}
 // Pin name : , pin side : right, pin line : 3, pin type : exec
translate([-12,  +lineWidth * 1, 0]) {
        executePin(4, 4);
}

