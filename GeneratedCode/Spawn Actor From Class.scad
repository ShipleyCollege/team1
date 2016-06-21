//include <../OpenSCAD/BPNode.scad>  
//include <../OpenSCAD/Pin.scad>  
//include <../OpenSCAD/brailleAndText.scad> 
include <../../ViPteam2/openSCAD/BPNode.scad>  
include <../../ViPteam2/openSCAD/Pin.scad>  
include <../../ViPtest2/openSCAD/brailleAndText.scad> 

lineWidth = 15;
translate([0, lineWidth * 0, 0])
        rotate([180,180,90]) 
 printTextAndBraille("Spawn Actor From Class");


 // Pin name : Return Value, pin side : right, pin line : 2, pin type : object
translate([0, +lineWidth * 1, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Return Value");
translate([-12,  +lineWidth * 0, 0]) {
        pin(4, 4, 0);
}
 // Pin name : Collision Handling Override, pin side : left, pin line : 3, pin type : byte
translate([0, -lineWidth * 2, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Collision Handling Override");
translate([-12,  -lineWidth * 3, 0]) {
        pin(4, 4, 0);
}
 // Pin name : , pin side : right, pin line : 3, pin type : exec
translate([-12,  +lineWidth * 1, 0]) {
        executePin(4, 4);
}
 // Pin name : Spawn Transform, pin side : left, pin line : 4, pin type : struct
translate([0, -lineWidth * 3, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Spawn Transform");
translate([-12,  -lineWidth * 4, 0]) {
        pin(4, 4, 0);
}
 // Pin name : Class, pin side : left, pin line : 5, pin type : class
translate([0, -lineWidth * 4, 0])
    rotate([180,180,90]) 
 printTextAndBraille("Class");
translate([-12,  -lineWidth * 5, 0]) {
        pin(4, 4, 0);
}
 // Pin name : , pin side : left, pin line : 6, pin type : exec
translate([-12,  -lineWidth * 6, 0]) {
        executePin(4, 4);
}
