import bpy

from bpy.types import Panel


class BlendUI_PT_Panel(Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_label = "Modifier operations"
    bl_category = "Timeriz Addon"

    def draw(self, context):
        layout = self.layout
        row = layout.row()
        col = row.column()
        col.operator("object.create_rendering_camera",
                     text="Create Camera")

        row = layout.row()
        col = row.column()
        col.operator("object.apply_smooth_shade", text="Apply smooth shade")

        row = layout.row()
        col = row.column()
        col.operator("object.apply_flat_shade", text="Apply flat shade")

        row = layout.row()
        col = row.column()
        col.operator("object.apply_all_mods", text="Apply all modifiers")

        row = layout.row()
        col = row.column()
        col.operator("object.cancel_all_mods", text="cancel all modifiers")

        row = layout.row()
        col = row.column()
        col.operator("object.add_bevel_preset", text="Add a preset bevel")

        row = layout.row()
        col = row.column()
        col.operator("object.add_decimate_preset", text="Add a decimate mod")

        row = layout.row()
        col = row.column()
        col.operator("object.add_remesh_preset", text="Add a remesh mod")

        row = layout.row()
        col = row.column()
        col.operator("object.add_mirror_mod", text="Add a mirror mod")

        row = layout.row()
        col = row.column()
        col.operator("object.add_color", text="Add a color")

        row = layout.row()
        col = row.column()
        col.operator("object.export_obj", text="Export object")

        row = layout.row()
        col = row.column()
        col.operator("object.choose_render_engine_cycles",
                     text="Change to Cycles")

        row = layout.row()
        col = row.column()
        col.operator("object.choose_render_engine_eevee",
                     text="Change to Eevee")

        row = layout.row()
        col = row.column()
        col.operator("object.create_better_sphere", text="meshmaker")
