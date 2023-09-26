# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

from . BlendUI import BlendUI_PT_Panel
from . Blend_Op import Blend_OT_Apply_All_Op, Blend_OT_Cancel_All_Op, Blend_OT_Add_Bevel_Op, Blend_OT_Add_Decimate_Op, Blend_OT_Add_Remesh_Op, Blend_OT_Add_Mirror_Op, DialogOperatorBevel, DialogOperatorDecimate, DialogOperatorRemesh, DialogOperatorMirror, Blend_OT_Add_Color_Op, DialogOperatorColor, Blend_OT_Export_Obj_Op, DialogOperatorExport, Blend_OT_Smooth_Shade_Op, Blend_OT_Flat_Shade_Op, Blend_OT_Render_Engine_Cycles_Op, Blend_OT_Render_Engine_Eevee_Op, Blend_OT_Camera_Op, Blend_OT_Mesh_Creator_Op
import bpy
bl_info = {
    "name": "Timeriz Custom Addon",
    "author": "Timeriz",
    "description": "",
    "blender": (2, 80, 0),
    "version": (0, 0, 1),
    "location": "View3D",
    "warning": "",
    "category": "Object"
}


classes = (Blend_OT_Apply_All_Op, BlendUI_PT_Panel,
           Blend_OT_Cancel_All_Op, Blend_OT_Add_Bevel_Op,
           Blend_OT_Add_Decimate_Op, Blend_OT_Add_Remesh_Op,
           Blend_OT_Add_Mirror_Op, DialogOperatorBevel,
           DialogOperatorDecimate, DialogOperatorRemesh,
           DialogOperatorMirror, Blend_OT_Add_Color_Op,
           DialogOperatorColor, Blend_OT_Export_Obj_Op,
           DialogOperatorExport, Blend_OT_Smooth_Shade_Op,
           Blend_OT_Flat_Shade_Op, Blend_OT_Render_Engine_Cycles_Op,
           Blend_OT_Render_Engine_Eevee_Op, Blend_OT_Camera_Op,
           Blend_OT_Mesh_Creator_Op)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in classes:
        bpy.utils.unregister_class(cls)
