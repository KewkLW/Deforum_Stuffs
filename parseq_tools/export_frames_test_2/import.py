import bpy
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty
from bpy.types import Operator

class ImportDiffusionString(Operator, ImportHelper):
    bl_idname = "import_scene.diffusion"  
    bl_label = "Import Diffusion"
    filename_ext = ".txt"
    filter_glob: StringProperty(
        default="*.txt",
        options={'HIDDEN'},
        maxlen=255, 
    )

    def execute(self, context):
        print("Executing import operator...")
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        keyframe_data = json.loads(content)
        camera_obj = None
        for obj in context.scene.objects:
            if obj.type == 'CAMERA':
                camera_obj = obj
                break
        if camera_obj is None:
            bpy.ops.object.camera_add()
            camera_obj = bpy.context.active_object
        for frame, data in keyframe_data.items():
            camera_obj.location = data["location"]
            camera_obj.rotation_euler = data["rotation"]
            camera_obj.keyframe_insert(data_path="location", frame=frame)
            camera_obj.keyframe_insert(data_path="rotation_euler", frame=frame)
        return {'FINISHED'}
    
def menu_func_import(self, context):
    self.layout.operator(ImportDiffusionString.bl_idname, text="Diffusion (.txt)")

def register():
    bpy.utils.register_class(ImportDiffusionString)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ImportDiffusionString)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

if __name__ == "__main__":
    register()
