import bpy
import os
from bpy.types import (
        Operator,
        Panel,
        PropertyGroup,
        UIList,
        )
from bpy.props import (
        BoolProperty,
        FloatProperty,
        IntProperty,
        PointerProperty,
        StringProperty,
        CollectionProperty,
        EnumProperty,
        )

def update_lock_camera_to_view(self,context):
    pass #TODO:

def update_view(self,context):
    pass

class Saved_View(PropertyGroup):
    location: bpy.props.FloatVectorProperty(name="Location")
    rotation: bpy.props.FloatVectorProperty(name="Rotation",default=(0,0,0,0),size=4)
    zoom: bpy.props.FloatProperty(name="Zoom")


class Camera_Presets_Scene_Props(PropertyGroup):
    library_tabs: EnumProperty(name="Library Tabs",
                               items=[('CAMERAS',"Cameras","Cameras"),
                                      ('SAVED_VIEWS',"Saved Views","Saved Views")],
                               default='CAMERAS',
                               update=update_view)

    preset_path: StringProperty(name="Preset Path",subtype='DIR_PATH')

    saved_views: CollectionProperty(name="Saved Views",type=Saved_View)
    saved_views_folder_name: StringProperty(name="Saved Views Folder Name")
    
    lock_camera_to_view: BoolProperty(name="Lock Camera to View",update=update_lock_camera_to_view)

    def draw_library_settings(self,layout,context):
        col = layout.column(align=True)
        col.prop(self,'preset_path')
        col.separator()
        col.operator('camera_presets.temp',text="Export Presets",icon='EXPORT')
        col.separator()
        col.operator('camera_presets.temp',text="Import Presets",icon='IMPORT')

    def draw_filebrowser_header(self,layout,context):
        row = layout.row()
        row.scale_y = 1.3
        row.label(text="Camera Presets")
        row.popover(panel="CAMERA_PRESETS_PT_library_settings",text="",icon='SETTINGS')

        row = layout.row()
        row.scale_y = 1.3
        row.prop(self,'library_tabs',expand=True)

        if self.library_tabs == 'CAMERAS':
            row = layout.row()
            row.scale_y = 1.3
            row.operator('camera_presets.save_preset',icon='ADD')  

            if context.scene.camera:
                layout.prop(self,'lock_camera_to_view')
        
        if self.library_tabs == 'SAVED_VIEWS':
            row = layout.row()
            row.scale_y = 1.3
            row.operator('camera_presets.save_view',icon='ADD')         

    @classmethod
    def register(cls):
        bpy.types.Scene.camera_presets = PointerProperty(
            name="Camera Presets Props",
            description="Camera Presets Props",
            type=cls,
        )
        
    @classmethod
    def unregister(cls):
        del bpy.types.Scene.camera_presets

classes = (
    Saved_View,
    Camera_Presets_Scene_Props,
)

register, unregister = bpy.utils.register_classes_factory(classes)        