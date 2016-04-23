#  ***** GPL LICENSE BLOCK *****
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.
#  All rights reserved.
#  ***** GPL LICENSE BLOCK *****

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
