import bpy

obj = bpy.context.active_object

bpy.ops.object.mode_set(mode='OBJECT')

prev_state = []
for e in obj.data.edges:
    prev_state.append(e.use_edge_sharp)
    if e.use_seam:
        e.use_edge_sharp = True

bpy.ops.object.modifier_add(type='EDGE_SPLIT')
obj.modifiers[-1].use_edge_angle = False
obj.modifiers[-1].use_edge_sharp = True

bpy.ops.object.modifier_apply(apply_as='DATA', modifier=obj.modifiers[-1].name)

for p, e in zip(prev_state, obj.data.edges):
    e.use_edge_sharp = p
