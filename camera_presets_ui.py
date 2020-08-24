import bpy
import os
from .pc_lib import pc_utils
from . import camera_presets_utils

class FILEBROWSER_PT_camera_presets_headers(bpy.types.Panel):
    bl_space_type = 'FILE_BROWSER'
    bl_region_type = 'UI'
    bl_label = "Library"
    bl_category = "Attributes"
    bl_options = {'HIDE_HEADER'}

    @classmethod
    def poll(cls, context):
        #Only display when active and File Browser is not open as separate window
        if len(context.area.spaces) > 1:
            pyclone = pc_utils.get_scene_props(context.scene)
            if pyclone.active_library_name == 'Camera Presets':
                return True   
        return False

    def draw(self, context):
        layout = self.layout
        props = camera_presets_utils.get_scene_props(context.scene)

        row = layout.row()
        row.scale_y = 1.3
        row.label(text="Camera Presets")
        row.popover(panel="CAMERA_PRESETS_PT_library_settings",text="",icon='SETTINGS')

        row = layout.row()
        row.scale_y = 1.3
        row.prop(props,'library_tabs',expand=True)

        if props.library_tabs == 'CAMERAS':
            row = layout.row()
            row.scale_y = 1.3
            row.operator('camera_presets.save_preset',icon='ADD')  

            if context.scene.camera:
                
                layout.prop(props,'lock_camera_to_view')
        
        if props.library_tabs == 'SAVED_VIEWS':
            row = layout.row()
            row.scale_y = 1.3
            row.operator('camera_presets.save_view',icon='ADD')              


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
    FILEBROWSER_PT_camera_presets_headers,
    CAMERA_PRESETS_PT_library_settings,
)

register, unregister = bpy.utils.register_classes_factory(classes)                