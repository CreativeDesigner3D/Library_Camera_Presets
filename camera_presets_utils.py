import bpy
import os

def get_scene_props(scene):
    return scene.camera_presets

def get_library_path():
    return os.path.join(os.path.dirname(__file__),"library")
