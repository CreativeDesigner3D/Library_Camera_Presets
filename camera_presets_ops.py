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

import uuid

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
        props = camera_presets_utils.get_scene_props(context.scene)
        if props.library_tabs == 'SAVED_VIEWS':
            bpy.ops.camera_presets.load_preset(filepath=self.filepath)

        if props.library_tabs == '':

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


class camera_presets_OT_save_view(Operator):
    bl_idname = "camera_presets.save_view"
    bl_label = "Save View"
    bl_options = {'UNDO'}
    
    filepath: StringProperty(name='Library Name')

    def execute(self, context):
        #IF SAVED FOLDER DOESN"T EXSIST CREATE IT AND SAVE NAME
        props = camera_presets_utils.get_scene_props(context.scene)
        path = camera_presets_utils.get_saved_view_paths()
        if props.saved_views_folder_name == "":
            props.saved_views_folder_name = str(uuid.uuid4())
        active_folder_path = os.path.join(path,props.saved_views_folder_name)
        if not os.path.exists(active_folder_path):
            os.makedirs(active_folder_path)

        pc_utils.update_file_browser_path(context,active_folder_path)

        #CREATE SCREEN SHOT SAVE TO LOCATION
        filename = "View " + str(len(props.saved_views) + 1) + ".png"
        loc = (0,0,0)
        rot = (0,0,0,0)
        zoom = 0
        for window in context.window_manager.windows:
            screen = window.screen

            for area in screen.areas:
                if area.type == 'VIEW_3D':
                    override = {'window': window, 'screen': screen, 'area': area}
                    for space in area.spaces:
                        if space.type == 'VIEW_3D':
                            loc = space.region_3d.view_location
                            rot = space.region_3d.view_rotation
                            zoom = space.region_3d.view_distance
                    bpy.ops.screen.screenshot(override,filepath=os.path.join(active_folder_path,filename),hide_props_region=True,full=False)
                    break        

        #ADD SAVED VIEW DATA
        view = props.saved_views.add()
        view.name = filename
        view.location = loc
        view.rotation = rot
        view.zoom = zoom

        #REFRESH FILEBROWSER
        for window in context.window_manager.windows:
            screen = window.screen        
            for area in screen.areas:
                if area.type == 'FILE_BROWSER':
                    override = {'window': window, 'screen': screen, 'area': area}      
                    bpy.ops.file.refresh(override)
                    break
        return {'FINISHED'}


class camera_presets_OT_load_view(Operator):
    bl_idname = "camera_presets.load_preset"
    bl_label = "Load View"
    bl_options = {'UNDO'}
    
    filepath: StringProperty(name='Library Name')

    def execute(self, context):
        #TODO: Save Preset
        #GET SAVED VIEW DATA
        directory, file = os.path.split(self.filepath)
        filename, ext = os.path.splitext(file)

        location = (0,0,0)
        rotation = (0,0,0,0)
        zoom = 0

        props = camera_presets_utils.get_scene_props(context.scene)
        for view in props.saved_views:
            if view.name == file:
                location = view.location
                rotation = view.rotation
                zoom = view.zoom

        context.region_data.view_location = location
        context.region_data.view_rotation = rotation
        context.region_data.view_distance = zoom
        #SET VIEW
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
    camera_presets_OT_save_view,
    camera_presets_OT_load_view,
    camera_presets_OT_temp,
)

register, unregister = bpy.utils.register_classes_factory(classes)

if __name__ == "__main__":
    register()
