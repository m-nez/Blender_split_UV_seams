import bpy

objects = bpy.context.selected_objects
active_obj = bpy.context.active_object

bpy.ops.object.mode_set(mode='OBJECT')

for obj in objects:
    for e in obj.data.edges:
        if e.use_seam:
            e.use_edge_sharp = True

    bpy.context.scene.objects.active = obj
    bpy.ops.object.modifier_add(type='EDGE_SPLIT')
    obj.modifiers[-1].use_edge_angle = False
    obj.modifiers[-1].use_edge_sharp = True

    bpy.ops.object.modifier_apply(apply_as='DATA', modifier=obj.modifiers[-1].name)

bpy.context.scene.objects.active = active_obj
