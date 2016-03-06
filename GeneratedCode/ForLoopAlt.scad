//include <../OpenSCAD/BPNode.scad>  
//include <../OpenSCAD/Pin.scad>  
//include <../OpenSCAD/brailleAndText.scad> 
include <../../ViPteam2/openSCAD/BPNode.scad>  
include <../../ViPteam2/openSCAD/Pin.scad>  
include <../../ViPtest2/openSCAD/brailleAndText.scad> 

lineWidth = 15;
translate([0, lineWidth * 0, 0])
        rotate([180,180,90]) 
 printTextAndBraille("For Loop");
 // Pin name : Lastindex, pin side : left, pin line : 2, pin type : int
translate([0, -lineWidth * 1, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Lastindex");
translate([-12,  -lineWidth * 2, 0]) {
        pin(4, 4, 0);
}
 // Pin name : Completed, pin side : right, pin line : 2, pin type : exec
translate([0, +lineWidth * 1, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Completed");
translate([-12,  +lineWidth * 0, 0]) {
        executePin(4, 4);
}
 // Pin name : Firstindex, pin side : left, pin line : 3, pin type : int
translate([0, -lineWidth * 2, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Firstindex");
translate([-12,  -lineWidth * 3, 0]) {
        pin(4, 4, 0);
}
 // Pin name : Index, pin side : right, pin line : 3, pin type : int
translate([0, +lineWidth * 2, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Index");
translate([-12,  +lineWidth * 1, 0]) {
        pin(4, 4, 0);
}
 // Pin name : , pin side : left, pin line : 4, pin type : exec
translate([-12,  -lineWidth * 4, 0]) {
        executePin(4, 4);
}
 // Pin name : Loopbody, pin side : right, pin line : 4, pin type : exec
translate([0, +lineWidth * 3, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Loopbody");
translate([-12,  +lineWidth * 2, 0]) {
        executePin(4, 4);
}
