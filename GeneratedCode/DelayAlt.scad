//include <../OpenSCAD/BPNode.scad>  
//include <../OpenSCAD/Pin.scad>  
//include <../OpenSCAD/brailleAndText.scad> 
include <../../ViPteam2/openSCAD/BPNode.scad>  
include <../../ViPteam2/openSCAD/Pin.scad>  
include <../../ViPtest2/openSCAD/brailleAndText.scad> 

lineWidth = 15;
translate([0, lineWidth * 0, 0])
        rotate([180,180,90]) 
 printTextAndBraille("Delay");
 // Pin name : , pin side : left, pin line : 2, pin type : exec
translate([-12,  -lineWidth * 2, 0]) {
        executePin(4, 4);
}
 // Pin name : Completed, pin side : right, pin line : 2, pin type : exec
translate([0, +lineWidth * 1, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Completed");
translate([-12,  +lineWidth * 0, 0]) {
        executePin(4, 4);
}
 // Pin name : Duration, pin side : left, pin line : 3, pin type : float
translate([0, -lineWidth * 2, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Duration");
translate([-12,  -lineWidth * 3, 0]) {
        pin(4, 4, 0);
}
