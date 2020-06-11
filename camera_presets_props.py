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

class Camera_Presets_Scene_Props(PropertyGroup):
    library_enum: EnumProperty(name="Library Tabs",
                               items=[('OPTION1',"Option 1","Example Enum"),
                                      ('OPTION2',"Option 2","Example Enum"),
                                      ('OPTION3',"Option 3","Example Enum")],
                               default='OPTION1')

    preset_path: StringProperty(name="Preset Path",subtype='DIR_PATH')

    lock_camera_to_view: BoolProperty(name="Lock Camera to View",update=update_lock_camera_to_view)

    def draw_library_settings(self,layout,context):
        col = layout.column(align=True)
        col.prop(self,'preset_path')
        col.separator()
        col.operator('camera_presets.temp',text="Export Presets",icon='EXPORT')
        col.separator()
        col.operator('camera_presets.temp',text="Import Presets",icon='IMPORT')

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
    Camera_Presets_Scene_Props,
)

register, unregister = bpy.utils.register_classes_factory(classes)        