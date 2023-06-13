import bpy
import json
from bpy.props import BoolProperty

class ExportFramesOperator(bpy.types.Operator):
    """Export frames to a file"""
    bl_idname = "export_frames.export"
    bl_label = "Export Frames"

    output_parseq: BoolProperty(name="Output Parseq", default=True)

    def execute(self, context):
        if self.output_parseq:
            frames = []
            for frame in range(context.scene.frame_start, context.scene.frame_end + 1):
                translation = context.scene.camera.matrix_world.to_translation()
                rotation = context.scene.camera.matrix_world.to_euler("XYZ")
                frames.append({
                    "frame": frame,
                    "translation": list(translation),
                    "rotation": list(rotation),
                })
            with open("frames.json", "w") as f:
                json.dump(frames, f, indent=4)
        else:
            pass
        return {'FINISHED'}

def menu_func_export(self, context):
    self.layout.operator(ExportFramesOperator.bl_idname, text="Export Frames")

def register():
    bpy.utils.register_class(ExportFramesOperator)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportFramesOperator)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
