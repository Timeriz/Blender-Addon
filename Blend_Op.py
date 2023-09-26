import os
import random
from math import radians, sin, cos
import bpy
from bpy.types import Modifier, Operator
from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       EnumProperty,
                       PointerProperty,
                       )
from bpy.types import (Panel,
                       Operator,
                       PropertyGroup,
                       )



class Blend_OT_Flat_Shade_Op(Operator):
    bl_idname = "object.apply_flat_shade"
    bl_label = "Apply flat shade"
    bl_description = "Apply all flat shade for object"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None and obj.mode == "OBJECT":
            return True
        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        bpy.ops.object.shade_flat()
        return {'FINISHED'}


class Blend_OT_Smooth_Shade_Op(Operator):
    bl_idname = "object.apply_smooth_shade"
    bl_label = "Apply smooth shade"
    bl_description = "Apply all smooth shade for object"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None and obj.mode == "OBJECT":
            return True
        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        bpy.ops.object.shade_smooth()
        return {'FINISHED'}


class Blend_OT_Apply_All_Op(Operator):
    bl_idname = "object.apply_all_mods"
    bl_label = "Apply all"
    bl_description = "Apply all operators of active object"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if context.view_layer.objects.active.modifiers:
            if obj is not None and obj.mode == "OBJECT":
                return True

        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        print(active_obj.modifiers)
        for mod in active_obj.modifiers:
            bpy.ops.object.modifier_apply(modifier=mod.name)

        return {'FINISHED'}


class Blend_OT_Cancel_All_Op(Operator):
    bl_idname = "object.cancel_all_mods"
    bl_label = "Cancel all"
    bl_description = "Cancel all operators of active object"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if context.view_layer.objects.active.modifiers:
            if obj is not None and obj.mode == "OBJECT":
                return True

        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active

        active_obj.modifiers.clear()

        return {'FINISHED'}


class Blend_OT_Add_Bevel_Op(Operator):
    bl_idname = "object.add_bevel_preset"
    bl_label = "add bevel preset"
    bl_description = "Add a bevel preset"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None and obj.mode == "OBJECT":
            return True

        return False

    def execute(self, context):

        active_obj = context.view_layer.objects.active
        modifier = active_obj.modifiers.new(name="Bevel", type='BEVEL')
        modifier.segments = 4
        bpy.ops.object.dialog_operator_bevel('INVOKE_DEFAULT')
        return {'FINISHED'}


class DialogOperatorBevel(bpy.types.Operator):
    bl_idname = "object.dialog_operator_bevel"
    bl_label = "Dialog Operator Bevel"

    int: bpy.props.IntProperty(name="Bevel segments: ")

    def execute(self, context):
        modifier = context.object.modifiers['Bevel']
        modifier.segments = self.int
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class Blend_OT_Add_Decimate_Op(Operator):
    bl_idname = "object.add_decimate_preset"
    bl_label = "add decimate mod"
    bl_description = "adds a decimate mod with preset"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None and obj.mode == "OBJECT":
            return True

        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        modifier = active_obj.modifiers.new(name="Decimate", type='DECIMATE')
        modifier.ratio = 0.6
        bpy.ops.object.dialog_operator_decimate('INVOKE_DEFAULT')
        return {'FINISHED'}


class DialogOperatorDecimate(bpy.types.Operator):
    bl_idname = "object.dialog_operator_decimate"
    bl_label = "Dialog Operator Decimate"

    float: bpy.props.FloatProperty(name="Decimate Ratio: ")

    def execute(self, context):
        modifier = context.object.modifiers['Decimate']
        modifier.ratio = self.float
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class Blend_OT_Add_Remesh_Op(Operator):
    bl_idname = "object.add_remesh_preset"
    bl_label = "add remesh mod"
    bl_description = "adds a remesh mod with preset"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None and obj.mode == "OBJECT":
            return True

        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        modifier = active_obj.modifiers.new(name="Remesh", type='REMESH')
        modifier.voxel_size = 0.2
        bpy.ops.object.dialog_operator_remesh('INVOKE_DEFAULT')
        return {'FINISHED'}


class DialogOperatorRemesh(bpy.types.Operator):
    bl_idname = "object.dialog_operator_remesh"
    bl_label = "Dialog Operator Remesh"

    float: bpy.props.FloatProperty(name="Voxel Size: ")

    def execute(self, context):
        modifier = context.object.modifiers['Remesh']
        modifier.voxel_size = self.float
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class Blend_OT_Add_Mirror_Op(Operator):
    bl_idname = "object.add_mirror_mod"
    bl_label = "add mirror mod"
    bl_description = "adds a mirror mod with preset"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None and obj.mode == "OBJECT":
            return True

        return False

    def execute(self, context):
        active_obj = context.view_layer.objects.active
        modifier = active_obj.modifiers.new(name="Mirror", type='MIRROR')
        bpy.ops.object.dialog_operator_mirror('INVOKE_DEFAULT')
        return {'FINISHED'}


class DialogOperatorMirror(bpy.types.Operator):
    bl_idname = "object.dialog_operator_mirror"
    bl_label = "Dialog Operator Mirror"

    xBool: bpy.props.BoolProperty(name="Axis X")
    yBool: bpy.props.BoolProperty(name="Axis Y")
    zBool: bpy.props.BoolProperty(name="Axis Z")

    def execute(self, context):
        modifier = context.object.modifiers['Mirror']
        modifier.use_axis[0] = self.xBool
        modifier.use_axis[1] = self.yBool
        modifier.use_axis[2] = self.zBool
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class Blend_OT_Add_Color_Op(Operator):
    bl_idname = "object.add_color"
    bl_label = "add color"
    bl_description = "adds a color"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None and obj.mode == "OBJECT":
            return True

        return False

    def execute(self, context):
        bpy.ops.object.dialog_operator_color('INVOKE_DEFAULT')
        return {'FINISHED'}


class DialogOperatorColor(bpy.types.Operator):
    bl_idname = "object.dialog_operator_color"
    bl_label = "Dialog Operator Color"

    col: bpy.props.FloatVectorProperty(name="Color: ", size=4, default=(0, 128, 0, 0))

    def execute(self, context):
        material_basic = bpy.data.materials.new(name="Basic")
        material_basic.use_nodes = True
        bpy.context.object.active_material = material_basic

        principled_node = material_basic.node_tree.nodes.get("Principled BSDF")

        principled_node.inputs[7].default_value = 0.08

        rgb_node = material_basic.node_tree.nodes.new("ShaderNodeRGB")
        rgb_node.location = (-250, 0)
        rgb_node.outputs[0].default_value = self.col

        link = material_basic.node_tree.links.new

        link(rgb_node.outputs[0], principled_node.inputs[0])



        bpy.context.space_data.shading.type = 'MATERIAL'

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)



class Blend_OT_Export_Obj_Op(Operator):
    bl_idname = "object.export_obj"
    bl_label = "export obj"
    bl_description = "exports obj"

    @classmethod
    def poll(cls, context):
        obj = context.object
        if obj is not None and obj.mode == "OBJECT":
            return True

        return False

    def execute(self, context):
        bpy.ops.object.dialog_operator_exporter('INVOKE_DEFAULT')
        return {'FINISHED'}

class DialogOperatorExport(bpy.types.Operator):
    bl_idname = "object.dialog_operator_exporter"
    bl_label = "Object exporter"

    selectedObjects: bpy.props.BoolProperty(name="Export selected objects")
    selectedAsIndividual: bpy.props.BoolProperty(name="Export selected as individual")
    activeCollection: bpy.props.BoolProperty(name="Export active collection")

    objSelection: bpy.props.BoolProperty(name="Wavefront (.obj)")
    fbxSelection: bpy.props.BoolProperty(name="FBX (.fbx)")
    x3dSelection: bpy.props.BoolProperty(name="X3D Extensible 3D (.x3d)")

    writeMaterials: bpy.props.BoolProperty(name="Write materials separately")


    path: bpy.props.StringProperty(
        name="Path: ", subtype="DIR_PATH", default="c:\\blender_exports")
    name: bpy.props.StringProperty(
        name="Filename:", default="Export_")
    
    lastActive = None
    def execute(self, context):
        selectedObjectsCache = bpy.context.selected_objects
        if(os.path.exists(self.path) == False):
            os.mkdir(self.path)

        if(self.selectedAsIndividual):
            self.selectedObjects = True
            for obj in selectedObjectsCache:
                bpy.ops.object.select_all(action='DESELECT')
                self.name = obj.name
                obj.select_set(True)
                self.exportSingle(context)
                self.lastActive = obj
        else:
            self.exportSingle(context)

        if(self.writeMaterials == False and self.name != None):
            os.remove(self.path + "\\" + self.name + ".mtl")
        #for file in os.listdir(self.path):
        #    if(file.endswith(".mtl")):
        #        print("removing:" + self.path + "\\" + file)
        #        os.remove(self.path + "\\" + file)

        return {'FINISHED'}
            
    def exportSingle(self, context):
        if self.objSelection:
            bpy.ops.export_scene.obj(
                filepath=self.path + "\\" + self.name + ".obj", use_selection=self.selectedObjects or self.activeCollection)
        if self.fbxSelection:
            bpy.ops.export_scene.fbx(
                filepath=self.path + "\\" + self.name + ".fbx", check_existing=True, use_selection=self.selectedObjects or self.activeCollection)
            if(self.writeMaterials == False and self.lastActive != None):
                os.remove(self.path + "\\" + self.lastActive.name + ".mtl")
        if self.x3dSelection:
            bpy.ops.export_scene.x3d(
                filepath=self.path + "\\" + self.name + ".x3d", check_existing=True, use_selection=self.selectedObjects or self.activeCollection)
        if self.selectedObjects:
            bpy.ops.export_scene.obj(
                filepath=self.path + "\\" + self.name + ".obj", check_existing=True, use_selection=self.selectedObjects or self.activeCollection)
        
    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)


class Blend_OT_Render_Engine_Cycles_Op(Operator):
    bl_idname = "object.choose_render_engine_cycles"
    bl_label = "Change Render Engine to Cycles"
    bl_description = "Changes the render engine to Cycles"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if bpy.context.scene.render.engine != 'CYCLES':
            return True
        return False

    def execute(self, context):
        bpy.context.scene.render.engine = 'CYCLES'
        bpy.context.scene.cycles.device = 'GPU'
        bpy.context.scene.cycles.samples = 256
        bpy.context.scene.cycles.preview_samples = 64
        return {'FINISHED'}


class Blend_OT_Render_Engine_Eevee_Op(Operator):
    bl_idname = "object.choose_render_engine_eevee"
    bl_label = "Change Render Engine to Eevee"
    bl_description = "Changes the render engine to Eevee"

    @classmethod
    def poll(cls, context):
        obj = context.object

        if bpy.context.scene.render.engine != 'BLENDER_EEVEE':
            return True
        return False

    def execute(self, context):
        bpy.context.scene.render.engine = 'BLENDER_EEVEE'
        bpy.context.scene.cycles.samples = 256
        bpy.context.scene.cycles.preview_samples = 64
        bpy.context.scene.eevee.use_ssr = True
        bpy.context.scene.eevee.use_bloom = True
        return {'FINISHED'}


class Blend_OT_Camera_Op(Operator):
    bl_idname = "object.create_rendering_camera"
    bl_label = "Create camera for rendering with preset"
    bl_description = "Creates a camera with reasonable preset"


    @classmethod
    def poll(cls, context):
        obj = context.object

        return True

    def execute(self, context):
        bpy.ops.object.camera_add(enter_editmode=False, align='VIEW',
                                  location=(0, 0, 0),
                                  rotation=(1.13198, 0.0125659, 0.652202),
                                  scale=(1, 1, 1),)
        bpy.context.object.data.type = 'PERSP'
        bpy.context.object.data.lens = 50
        bpy.context.object.data.clip_start = 0.1
        bpy.context.object.data.clip_end = 1000
        bpy.context.object.data.show_limits = True
        bpy.context.object.data.show_mist = False
        bpy.context.object.data.show_passepartout = True
        bpy.context.object.data.passepartout_alpha = 0.5
        return {'FINISHED'}



class Blend_OT_Mesh_Creator_Op(Operator):
    bl_idname = "object.create_better_sphere"
    bl_label = "Create sphere"
    bl_description = "Creates a sphere with better topography"


    segments: bpy.props.IntProperty(name="Segments: ", default=64)
    radius: bpy.props.FloatProperty(name="Radius: ", default=4.0)
    rings: bpy.props.IntProperty(name="Rings: ", default=64)

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        mesh = bpy.data.meshes.new("BetterSphere")
        obj = bpy.data.objects.new(mesh.name, mesh)
        col = bpy.data.collections.get("Collection")
        col.objects.link(obj)
        bpy.context.view_layer.objects.active = obj
        
        obj.select_set(True)

        
        vertices = []
        edges = []
        faces = []

        segments = self.segments
        rings = self.rings
        radius = self.radius

#verts = [(random.randint(-50, 50), random.randint(-50, 50),
#          random.randint(-50, 50)),
#
#                 (random.randint(-50, 50), random.randint(-50, 50),
#                  random.randint(-50, 50)),
#
#                 (random.randint(-50, 50), random.randint(-50, 50),
#                  random.randint(-50, 50)),
#
#                 (random.randint(-50, 50),  random.randint(-50, 50),
#                  random.randint(-50, 50)),
#                 ]
#        edges = []
#        faces = [[0, 1, 2, 3]]


        for ring in range(rings + 1):
            
            phi = ring * radians(180) / rings

            for segment in range(segments + 1):
                angle = segment * radians(360) / segments
                x = radius * cos(angle) * sin(phi)
                y = radius * sin(angle) * sin(phi)
                z = radius * cos(phi)
                vertices.append((x, y, z))

            if ring > 0:
                seg = segments + 1
                for segment in range(segments):
                    faces.append([

                        (ring - 1) * seg + segment,
                        (ring - 1) * seg + segment + 1,
                        ring * seg + segment + 1,
                        ring * seg + segment
                    
                    ])

        mesh.from_pydata(vertices, edges, faces)
        bpy.ops.object.mode_set(mode='EDIT')
        bpy.ops.mesh.select_all(action='SELECT')
        bpy.ops.uv.unwrap()
        bpy.ops.object.mode_set(mode='OBJECT')
        
        mesh.update()

        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)