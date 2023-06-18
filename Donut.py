import bpy
from mathutils import Vector

# Clear existing objects
bpy.ops.object.select_all(action='DESELECT')
bpy.ops.object.select_by_type(type='MESH')
bpy.ops.object.delete()

# Create the donut
bpy.ops.mesh.primitive_torus_add(
    align='WORLD',
    location=(0, 0, 0),
    rotation=(0, 0, 0),
    major_radius=1.0,
    minor_radius=0.375,
    major_segments=128,
    minor_segments=12
)
donut = bpy.context.object

# Create the icing
bpy.ops.object.select_all(action='DESELECT')
donut.select_set(True)
bpy.context.view_layer.objects.active = donut
bpy.ops.object.modifier_add(type='BEVEL')
bpy.context.object.modifiers["Bevel"].width = 0.05
bpy.ops.object.modifier_apply(modifier="Bevel")

icing = donut.copy()
icing.data = donut.data.copy()
icing.name = "Icing"
bpy.context.collection.objects.link(icing)
icing.location += Vector((0, 0, 0.02))

# Create the sprinkles
bpy.ops.object.select_all(action='DESELECT')
icing.select_set(True)
bpy.context.view_layer.objects.active = icing
bpy.ops.object.modifier_add(type='SUBSURF')
bpy.context.object.modifiers["Subdivision"].levels = 2
bpy.ops.object.modifier_apply(modifier="Subdivision")

sprinkles = icing.copy()
sprinkles.data = icing.data.copy()
sprinkles.name = "Sprinkles"
bpy.context.collection.objects.link(sprinkles)

# Create the plate
bpy.ops.mesh.primitive_cylinder_add(
    align='WORLD',
    location=(0, 0, -0.015),
    rotation=(0, 0, 0),
    radius=1.5,
    depth=0.03,
    end_fill_type='NOTHING'
)
plate = bpy.context.object
plate.name = "Plate"

# Set up materials
donut_material = bpy.data.materials.new(name="Donut Material")
donut.data.materials.append(donut_material)

icing_material = bpy.data.materials.new(name="Icing Material")
icing.data.materials.append(icing_material)

sprinkles_material = bpy.data.materials.new(name="Sprinkles Material")
sprinkles.data.materials.append(sprinkles_material)

plate_material = bpy.data.materials.new(name="Plate Material")
plate.data.materials.append(plate_material)

# Print the name of the created objects
print("Donut created with the name:", donut.name)
print("Icing created with the name:", icing.name)
print("Sprinkles created with the name:", sprinkles.name)
print("Plate created with the name:", plate.name)
