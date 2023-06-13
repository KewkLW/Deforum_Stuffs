import bpy
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, EnumProperty, IntProperty, FloatProperty
from bpy.types import Operator
from .camera_operations import write_camera_data, cameras_to_string

class ExportDiffusionString(Operator, ExportHelper):
    bl_idname = "export_scene.diffusion"
    bl_label = "Export Diffusion"
    filename_ext = ".txt"

    filter_glob: StringProperty(
        default="*.txt",
        options={'HIDDEN'},
        maxlen=255, 
    )

    output_json: BoolProperty(name="Output JSON", default=False)
    output_cam_code: BoolProperty(name="Output cam_code", default=False)
    output_raw_frames: BoolProperty(name="Output Raw Frames", default=True)
    frame_start: IntProperty(name="Start", default=-1)
    frame_end: IntProperty(name="End", default=-1)

    which_cams: EnumProperty(
        name="Which Cams",
        description="Which cameras to export",
        items=(
            ('ACTIVE', "Active", "Scene's active camera"),
            ('SELECTED', "Selected", "Selected cameras only"),
            ('ALL', "All", "All cameras in scene"),
        ),
        default='ACTIVE',
    )

    translation_scale: FloatProperty(default=50, name="Translation Scale", description="Conversion factor between blender units and Diffusion units")

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

def menu_func_export(self, context):
    self.layout.operator(ExportDiffusionString.bl_idname, text="Diffusion (.txt)")

def register():
    bpy.utils.register_class(ExportDiffusionString)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportDiffusionString)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()

