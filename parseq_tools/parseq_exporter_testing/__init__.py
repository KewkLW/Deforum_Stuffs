bl_info = {
    "name": "Export to Parseq",
    "author": "Kewk",
    "version": (1, 0),
    "blender": (3, 5, 0),
    "location": "File > Import-Export",
    "description": "Export Blender animations to Parseq VR format",
    "category": "Import-Export",
}

import bpy
from . import operators, panels

def menu_func_export(self, context):
    self.layout.operator(operators.ExportToParseqVR.bl_idname, text="Export to Parseq VR")

def register():
    print("Registering addon")
    bpy.utils.register_class(operators.ExportToParseqVR)
    bpy.utils.register_class(panels.ExportToParseqPanel)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    print("Unregistering addon")
    bpy.utils.unregister_class(operators.ExportToParseqVR)
    bpy.utils.unregister_class(panels.ExportToParseqPanel)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
