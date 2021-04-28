import bpy
import os
from .pc_lib import pc_utils
from . import camera_presets_utils

class CAMERA_PRESETS_PT_library_settings(bpy.types.Panel):
    bl_space_type = 'FILE_BROWSER'
    bl_label = "Library"
    bl_region_type = 'HEADER'
    bl_ui_units_x = 16

    def draw(self, context):
        layout = self.layout
        props = camera_presets_utils.get_scene_props(context.scene)
        props.draw_library_settings(layout, context)

classes = (
    CAMERA_PRESETS_PT_library_settings,
)

register, unregister = bpy.utils.register_classes_factory(classes)                