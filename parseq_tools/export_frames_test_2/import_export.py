import bpy
import json  # Added this import
from bpy_extras.io_utils import ExportHelper, ImportHelper  # Added ImportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, IntProperty, FloatProperty
from bpy.types import Operator
from .camera_operations import write_camera_data, cameras_to_string

class ExportDiffusionString(Operator, ExportHelper):
    
    # The bl_idname attribute represents the unique identifier for this operator.
    bl_idname = "export_scene.diffusion"
    
    # The bl_label attribute represents the name that will be displayed in the user interface for this operator.
    bl_label = "Export Diffusion"
    
    # The filename_ext attribute represents the default file extension for exported files.
    filename_ext = ".txt"
    
    # A string property that represents the type of files that can be selected in the file browser.
    # Default is set to "*.txt" and is hidden from the user interface.
    filter_glob: StringProperty(
        default="*.txt",
        options={'HIDDEN'},
        maxlen=255, 
    )
    # A boolean property to decide whether to output data in JSON format. Default is set to False.
    output_json: BoolProperty(name="Output JSON", default=False)
    
    # A boolean property to decide whether to output camera code. Default is set to False.
    output_cam_code: BoolProperty(name="Output cam_code", default=False)

    # A boolean property to decide whether to output raw frames. Default is set to True.
    output_raw_frames: BoolProperty(name="Output Raw Frames", default=True)    
    
    # An integer property representing the start frame for export. Default is set to -1.
    frame_start: IntProperty(name="Start", default=-1)
    
    # An integer property representing the end frame for export. Default is set to -1.
    frame_end: IntProperty(name="End", default=-1)    
    
    which_cams: EnumProperty(
        name="Which Cams",
        description="Which cameras to exprot",
        items=(
            ('ACTIVE', "Active", "Scene's active camera"),
            ('SELECTED', "Selected", "Selected cameras only"),
            ('ALL', "All", "All cameras in scene"),
        ),
        default='ACTIVE',
    )    
    translation_scale: FloatProperty(default=50, name="Translation Scale", description = "Conversion factor between blender units and Diffusion units")
# Create the user interface    
    def draw(self, context):
        layout = self.layout
        row = layout.row()
        row.label(text="Which Cameras")
        row = layout.row()
        row.props_enum(self, "which_cams")
        row = layout.row()
        row.label(text="Export Settings")                
        row = layout.row()
        row.label(text="Frames")
        if self.frame_start == -1:
            self.frame_start = bpy.context.scene.frame_start
        if self.frame_end == -1:
            self.frame_end = bpy.context.scene.frame_end
        row.prop(self, "frame_start")
        row.prop(self, "frame_end")
        row = layout.row()
        row.prop(self, "translation_scale")               
        row = layout.row()
        row.prop(self, "output_cam_code")
        row = layout.row()
        row.prop(self, "output_json")
        row = layout.row()
        row.prop(self, "output_raw_frames")

# Execute the main operation of the addon or script        
    def execute(self, context):
        export_cams = []
        if self.which_cams == "ACTIVE":
            export_cams = [context.scene.camera]
        elif self.which_cams == "SELECTED":
            export_cams = [cam for cam in context.selected_objects if cam.type == 'CAMERA']
        elif self.which_cams == "ALL":
            export_cams = [cam for cam in context.scene.objects if cam.type == 'CAMERA']
        return write_camera_data(context, self.filepath, self.frame_start, self.frame_end, export_cams, self.translation_scale, self.output_cam_code, self.output_json, self.output_raw_frames)


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

def menu_func_export(self, context):
    self.layout.operator(ExportDiffusionString.bl_idname, text="Diffusion (.txt)")

def register():
    bpy.utils.register_class(ImportDiffusionString)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

    bpy.utils.register_class(ExportDiffusionString)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ImportDiffusionString)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)

    bpy.utils.unregister_class(ExportDiffusionString)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
        
if __name__ == "__main__":
    register()
