import bpy
from math import radians

#Create Cube
bpy.ops.mesh.primitive_cube_add()
so = bpy.context.active_object

#move Object
#so.location[0] = 5

#Rotate Object 
so.rotation_euler[0] +=  radians(45)

#Create Modifier
mod_subsurf = so.modifiers.new('My Modifier', 'SUBSURF')

#Change modifier value
mod_subsurf.levels = 3

bpy.ops.object.shade_smooth()