import bpy
from .pc_lib import pc_utils
from . import camera_presets_ops
from . import camera_presets_props
from . import camera_presets_ui
from bpy.app.handlers import persistent

#Standard bl_info for Blender Add-ons
bl_info = {
    "name": "Camera Presets",
    "author": "Andrew Peel",
    "version": (0, 0, 1),
    "blender": (2, 80, 0),
    "location": "Asset Library",
    "description": "This is an asset library that maintains presets for cameras",
    "warning": "",
    "wiki_url": "",
    "category": "Asset Library",
}

@persistent
def load_library_on_file_load(scene=None):
    pc_utils.register_library(name="Camera Presets",
                              activate_id='camera_presets.activate',
                              drop_id='camera_presets.drop',
                              namespace="camera_presets",
                              icon='OUTLINER_OB_CAMERA')

#Standard register/unregister Function for Blender Add-ons
def register():
    camera_presets_ops.register()
    camera_presets_props.register()
    camera_presets_ui.register()
    
    load_library_on_file_load()
    bpy.app.handlers.load_post.append(load_library_on_file_load)

def unregister():
    camera_presets_ops.unregister()
    camera_presets_props.unregister()
    camera_presets_ui.unregister()

    bpy.app.handlers.load_post.remove(load_library_on_file_load)  

    pc_utils.unregister_library("Camera Presets")

