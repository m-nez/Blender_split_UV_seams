bl_info = {
    "name": "Split UV seams",
    "author": "Michał Nieznański",
    "version": (1, 0, 0),
    "blender": (2, 77, 0),
    "description": "Split meshes along the UV seams.",
    "category": "UV",
}

import bpy

def splitUVSeams(context):
    objects = context.selected_objects
    active_obj = context.active_object

    bpy.ops.object.mode_set(mode='OBJECT')

    for obj in objects:
        for e in obj.data.edges:
            if e.use_seam:
                e.use_edge_sharp = True

        context.scene.objects.active = obj
        bpy.ops.object.modifier_add(type='EDGE_SPLIT')
        obj.modifiers[-1].use_edge_angle = False
        obj.modifiers[-1].use_edge_sharp = True

        bpy.ops.object.modifier_apply(
                apply_as='DATA', modifier=obj.modifiers[-1].name)

    context.scene.objects.active = active_obj

class UVSeamSplitter(bpy.types.Operator):
    """
    Split meshes along UV seams
    """
    bl_idname = "uv.split_seams"
    bl_label = "Split UV Seams"

    def execute(self, context):
        splitUVSeams(context)

        return {'FINISHED'}

def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
