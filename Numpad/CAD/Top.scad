base = 4;
wall_height = 0.9;







module corner_base(){
    cube([25.4,25.4,base],center = false);
    rotate([0,0,270]){
        translate([0,0,0]){
            mirror([1,0,0]){
                difference(){
        union(){
            
            translate([0,25.4-wall_height,base])
                cube([25.4,0.9,9]);
            translate([0,17.4,base])
                    cube([7.1,7.1,4],center = false);
            
            difference(){
                translate([17.4,17.4,base])
                    cube([7.1,7.1,4],center = false);
                translate([20.4,20.4,base+2.5])
                    cylinder(h = 5, r = 1.6,center = true,$fn = 32  );
            }
        }
        translate([25.4/2 - 11/2,25.4-2,base+4])
            cube([11,5,10]);
        translate([3.6,24.9,base+2]){
            rotate([90,0,0])
            cylinder(h=3,r=1.6,center = true,$fn = 32);
    }
        translate([21.8,24.9,base+2]){
            rotate([90,0,0])
                cylinder(h=3,r=1.6,center = true,$fn = 32);
    }
    }   
                
            }
            
    }      
        
    }

    difference(){
        union(){
            
            translate([0,25.4-wall_height,base])
                cube([25.4,0.9,9]);
            translate([0,17.4,base])
                    cube([7.1,7.1,4],center = false);
            
            difference(){
                translate([17.4,17.4,base])
                    cube([7.1,7.1,4],center = false);
                translate([20.4,20.4,base+2.5])
                    cylinder(h = 5, r = 1.6,center = true,$fn = 32  );
            }
        }
        translate([25.4/2 - 11/2,25.4-2,base+4])
            cube([11,5,10]);
        translate([3.6,24.9,base+2]){
            rotate([90,0,0])
            cylinder(h=3,r=1.6,center = true,$fn = 32);
    }
        translate([21.8,24.9,base+2]){
            rotate([90,0,0])
                cylinder(h=3,r=1.6,center = true,$fn = 32);
    }
    }   
}
















module edge_base(){
    translate([-25.4,0,0]){

        cube([25.4,25.4,base],center = false);
        

        difference(){
            union(){
                
                translate([0,25.4-wall_height,base])
                    cube([25.4,0.9,9]);
                translate([0,17.4,base])
                        cube([7.1,7.1,4],center = false);
                
                difference(){
                    translate([17.4,17.4,base])
                        cube([7.1,7.1,4],center = false);
                    
                }
            }
            translate([25.4/2 - 11/2,25.4-2,base+4])
                cube([11,5,10]);
            translate([3.6,24.9,base+2]){
                rotate([90,0,0])
                cylinder(h=3,r=1.6,center = true,$fn = 32);
        }
            translate([21.8,24.9,base+2]){
                rotate([90,0,0])
                    cylinder(h=3,r=1.6,center = true,$fn = 32);
        }
        }
    }

}








module corner_top(){
    difference(){
        union(){
            translate([18.4,18.4,10]){
                cube([6.1,6.1,3]);
            }
            translate([0,0,9+base]){
                cube([25.4,25.4,2]);
            }
        }
        
        
        translate([20.4,20.4,12.5])
            cylinder(h = 15, r = 1.6,center = true,$fn = 32  );

    }
}
difference(){
    union(){
        translate([-25.4,-38.1,0]){
            rotate([0,0,180])   
                corner_top();


            translate([50.8,0,0])
                rotate([0,0,270])   
                    corner_top();


            translate([50.8,76.2,0])
                rotate([0,0,0])   
                    corner_top();
             
            translate([0,-25.4,9+base]){
                cube([50.8,127,2]);
                
            }
            translate([0,76.2,0])
                rotate([0,0,90])   
                    corner_top();



            translate([-25.4,0,9+base]){
                cube([101.6,76.4,2]);
            }
        }
    }
    linear_extrude(20)
        translate([-38.1,-47.7625])
            difference(){
                translate([1,1])
                    square([74.2,93.525]);
                translate([0,95.525])
                    import("plate.dxf");
                
            }
        }