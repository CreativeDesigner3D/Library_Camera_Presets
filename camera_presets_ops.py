import bpy,os,inspect

from bpy.types import (Header, 
                       Menu, 
                       Panel, 
                       Operator,
                       PropertyGroup)

from bpy.props import (StringProperty,
                       BoolProperty,
                       IntProperty,
                       FloatProperty,
                       FloatVectorProperty,
                       PointerProperty,
                       EnumProperty,
                       CollectionProperty)
from . import camera_presets_utils
from .pc_lib import pc_utils

class camera_presets_OT_activate(Operator):
    bl_idname = "camera_presets.activate"
    bl_label = "Activate Library"
    bl_options = {'UNDO'}
    
    library_name: StringProperty(name='Library Name')

    def execute(self, context):
        path = camera_presets_utils.get_library_path()
        pc_utils.update_file_browser_path(context,path)
        return {'FINISHED'}


class camera_presets_OT_drop(Operator):
    bl_idname = "camera_presets.drop"
    bl_label = "Drop File"
    bl_options = {'UNDO'}
    
    filepath: StringProperty(name='Library Name')

    def execute(self, context):
        if context.scene.camera:
            '''
            This is just placeholder code. 
            This will need to run the preset script.
            '''
            if 'Red' in self.filepath:
                context.scene.camera.data.sensor_width = 30.0
                context.scene.camera.data.sensor_height = 15.0
                context.scene.camera.data.sensor_fit = 'HORIZONTAL'
            if 'iPhone' in self.filepath:
                context.scene.camera.data.sensor_width = 4.54
                context.scene.camera.data.sensor_height = 3.42
                context.scene.camera.data.lens = 3.85
                context.scene.camera.data.sensor_fit = 'HORIZONTAL'
            if 'Cannon' in self.filepath:
                context.scene.camera.data.sensor_width = 22.2
                context.scene.camera.data.sensor_height = 14.7
                context.scene.camera.data.sensor_fit = 'HORIZONTAL'
        else:
            bpy.ops.object.camera_add(align='VIEW')
            camera = context.active_object
            bpy.ops.view3d.camera_to_view()
            camera.data.clip_start = .01
            camera.data.clip_end = 9999
            camera.data.ortho_scale = 200.0
        return {'FINISHED'}


class camera_presets_OT_save_preset(Operator):
    bl_idname = "camera_presets.save_preset"
    bl_label = "Save Preset"
    bl_options = {'UNDO'}
    
    filepath: StringProperty(name='Library Name')

    def execute(self, context):
        #TODO: Save Preset
        return {'FINISHED'}


class camera_presets_OT_temp(Operator):
    bl_idname = "camera_presets.temp"
    bl_label = "Temp"
    bl_options = {'UNDO'}
    
    filepath: StringProperty(name='Library Name')

    def execute(self, context):
        #TODO: Placeholder
        return {'FINISHED'}

classes = (
    camera_presets_OT_activate,
    camera_presets_OT_drop,
    camera_presets_OT_save_preset,
    camera_presets_OT_temp,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
