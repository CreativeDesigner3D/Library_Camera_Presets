import bpy
import os

def get_scene_props(scene):
    return scene.camera_presets

def get_library_path():
    return os.path.join(os.path.dirname(__file__),"library")

def get_saved_view_paths():
    return os.path.join(os.path.dirname(__file__),"saved_views")

def get_current_view_matrix(context):
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    return space.region_3d.view_matrix    