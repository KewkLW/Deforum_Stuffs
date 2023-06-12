bl_info = {
    "name": "Deforum Parseq Exporter",
    "author": "https://twitter.com/kewkd",
    "version": (1, 0),
    "blender": (3, 5, 0),
    "location": "File > Export",
    "description": "Export camera motion to JSON",
    "warning": "",
    "wiki_url": "",
    "category": "Export",
}

import bpy
import json
from bpy_extras.io_utils import ExportHelper
from bpy.props import StringProperty, BoolProperty, FloatProperty

# Helper Functions

def roundZero(num, magnitude_thresh=0.00001):
    return num if abs(num) > magnitude_thresh else 0

# Write camera data

def write_camera_data(context, filepath, start, end, cams, output_config, scale_config, output_json, swap_translation_yz, round_to_single_decimal, swap_negative_translation_x, swap_negative_translation_y, swap_negative_translation_z, swap_negative_rotation_3d_x, swap_negative_rotation_3d_y, swap_negative_rotation_3d_z):
    camera_data = []
    previous_frame_data = None
    next_frame_data = None

    for cam in cams:
        if cam.animation_data and cam.animation_data.action:
            keyframes = set()
            fcurves = cam.animation_data.action.fcurves

            for fcurve in fcurves:
                if fcurve.data_path in {'location', 'rotation_euler'}:
                    for keyframe in fcurve.keyframe_points:
                        keyframes.add(int(keyframe.co[0]))

            sorted_keyframes = sorted(keyframes)

            for i in range(len(sorted_keyframes)):
                if start <= sorted_keyframes[i] <= end:
                    bpy.context.scene.frame_set(sorted_keyframes[i])
                    raw_location = cam.matrix_world.to_translation()
                    raw_rotation = cam.matrix_world.to_euler()

                    location = [roundZero(raw_location[j] * scale_config[f'translation_{axis}']) if scale_config[f'translation_{axis}'] != 0 else 0 for j, axis in enumerate('xyz')]
                    rotation = [roundZero(raw_rotation[j] * scale_config[f'rotation_3d_{axis}']) if scale_config[f'rotation_3d_{axis}'] != 0 else 0 for j, axis in enumerate('xyz')]

                    if round_to_single_decimal:
                        location = [round(val, 1) for val in location]
                        rotation = [round(val, 1) for val in rotation]

                    if swap_translation_yz:
                        location[1], location[2] = location[2], location[1]

                    if swap_negative_translation_x:
                        location[0] = -location[0]
                    if swap_negative_translation_y:
                        location[1] = -location[1]
                    if swap_negative_translation_z:
                        location[2] = -location[2]
                    if swap_negative_rotation_3d_x:
                        rotation[0] = -rotation[0]
                    if swap_negative_rotation_3d_y:
                        rotation[1] = -rotation[1]
                    if swap_negative_rotation_3d_z:
                        rotation[2] = -rotation[2]

                    frame_data = {
                        'frame': sorted_keyframes[i],
                        'translation_x': location[0] if output_config['translation_x'] else None,
                        'translation_y': location[1] if output_config['translation_y'] else None,
                        'translation_z': location[2] if output_config['translation_z'] else None,
                        'rotation_3d_x': rotation[0] if output_config['rotation_3d_x'] else None,
                        'rotation_3d_y': rotation[1] if output_config['rotation_3d_y'] else None,
                        'rotation_3d_z': rotation[2] if output_config['rotation_3d_z'] else None
                    }

                    # First frame or the value has changed
                    if previous_frame_data is None or frame_data != previous_frame_data:
                        camera_data.append(frame_data)
                        previous_frame_data = frame_data
                    # if the next frame is not the same as the current frame, append current frame data
                    elif i < len(sorted_keyframes) - 1:  # check we are not at the last frame
                        bpy.context.scene.frame_set(sorted_keyframes[i + 1])  # get next frame
                        next_raw_location = cam.matrix_world.to_translation()
                        next_raw_rotation = cam.matrix_world.to_euler()

                        next_location = [roundZero(next_raw_location[j] * scale_config[f'translation_{axis}']) if scale_config[f'translation_{axis}'] != 0 else 0 for j, axis in enumerate('xyz')]
                        next_rotation = [roundZero(next_raw_rotation[j] * scale_config[f'rotation_3d_{axis}']) if scale_config[f'rotation_3d_{axis}'] != 0 else 0 for j, axis in enumerate('xyz')]

                        next_frame_data = {
                            'frame': sorted_keyframes[i+1],
                            'translation_x': next_location[0] if output_config['translation_x'] else None,
                            'translation_y': next_location[1] if output_config['translation_y'] else None,
                            'translation_z': next_location[2] if output_config['translation_z'] else None,
                            'rotation_3d_x': next_rotation[0] if output_config['rotation_3d_x'] else None,
                            'rotation_3d_y': next_rotation[1] if output_config['rotation_3d_y'] else None,
                            'rotation_3d_z': next_rotation[2] if output_config['rotation_3d_z'] else None
                        }

                        if next_frame_data != frame_data:
                            camera_data.append(frame_data)

    if output_json:
        with open(filepath, 'w') as outfile:
            json.dump(camera_data, outfile, indent=4)



class ExportDiffusionString(bpy.types.Operator, ExportHelper):
    bl_idname = "export_camera.diffusion_string"
    bl_label = "Export Camera Diffusion String"
    filename_ext = ".json"

    # Properties
    output_json: BoolProperty(
        name="Output JSON",
        description="Export camera data as JSON",
        default=True,
    )

    swap_translation_yz: BoolProperty(
        name="Swap Translation Y and Z",
        default=True,
    )

    round_to_single_decimal: BoolProperty(
        name="Round to Single Decimal",
        default=True,
    )

    swap_negative_translation_x: BoolProperty(
        name="Swap Negative Translation X",
        default=False,
    )

    swap_negative_translation_y: BoolProperty(
        name="Swap Negative Translation Y",
        default=False,
    )

    swap_negative_translation_z: BoolProperty(
        name="Swap Negative Translation Z",
        default=False,
    )

    swap_negative_rotation_3d_x: BoolProperty(
        name="Swap Negative Rotation X",
        default=False,
    )

    swap_negative_rotation_3d_y: BoolProperty(
        name="Swap Negative Rotation Y",
        default=False,
    )

    swap_negative_rotation_3d_z: BoolProperty(
        name="Swap Negative Rotation Z",
        default=False,
    )

    # Checkboxes for output
    output_translation_x: BoolProperty(
        name="Output Translation X",
        default=True,
    )

    output_translation_y: BoolProperty(
        name="Output Translation Y",
        default=True,
    )

    output_translation_z: BoolProperty(
        name="Output Translation Z",
        default=True,
    )

    output_rotation_3d_x: BoolProperty(
        name="Output Rotation X",
        default=True,
    )

    output_rotation_3d_y: BoolProperty(
        name="Output Rotation Y",
        default=True,
    )

    output_rotation_3d_z: BoolProperty(
        name="Output Rotation Z",
        default=True,
    )

    # Scale for each axis
    scale_translation_x: FloatProperty(
        name="Scale Translation X",
        default=1.0,
    )

    scale_translation_y: FloatProperty(
        name="Scale Translation Y",
        default=1.0,
    )

    scale_translation_z: FloatProperty(
        name="Scale Translation Z",
        default=1.0,
    )

    scale_rotation_3d_x: FloatProperty(
        name="Scale Rotation X",
        default=1.0,
    )

    scale_rotation_3d_y: FloatProperty(
        name="Scale Rotation Y",
        default=1.0,
    )

    scale_rotation_3d_z: FloatProperty(
        name="Scale Rotation Z",
        default=1.0,
    )

    def execute(self, context):
        output_config = {
            'translation_x': self.output_translation_x,
            'translation_y': self.output_translation_y,
            'translation_z': self.output_translation_z,
            'rotation_3d_x': self.output_rotation_3d_x,
            'rotation_3d_y': self.output_rotation_3d_y,
            'rotation_3d_z': self.output_rotation_3d_z
        }

        scale_config = {
            'translation_x': self.scale_translation_x,
            'translation_y': self.scale_translation_y,
            'translation_z': self.scale_translation_z,
            'rotation_3d_x': self.scale_rotation_3d_x,
            'rotation_3d_y': self.scale_rotation_3d_y,
            'rotation_3d_z': self.scale_rotation_3d_z
        }

        write_camera_data(context, self.filepath, context.scene.frame_start, context.scene.frame_end, context.scene.objects, output_config, scale_config, self.output_json, self.swap_translation_yz, self.round_to_single_decimal, self.swap_negative_translation_x, self.swap_negative_translation_y, self.swap_negative_translation_z, self.swap_negative_rotation_3d_x, self.swap_negative_rotation_3d_y, self.swap_negative_rotation_3d_z)

        return {'FINISHED'}

    def draw(self, context):
        layout = self.layout

        # Output Config
        box = layout.box()
        box.label(text="Output Config")
        box.prop(self, "output_json")

        # Swap Config
        box = layout.box()
        box.label(text="Swap Config")
        box.prop(self, "swap_translation_yz")
        box.prop(self, "round_to_single_decimal")
        box.prop(self, "swap_negative_translation_x")
        box.prop(self, "swap_negative_translation_y")
        box.prop(self, "swap_negative_translation_z")
        box.prop(self, "swap_negative_rotation_3d_x")
        box.prop(self, "swap_negative_rotation_3d_y")
        box.prop(self, "swap_negative_rotation_3d_z")

        # Output selection
        box = layout.box()
        box.label(text="Output Selection")
        box.prop(self, "output_translation_x")
        box.prop(self, "output_translation_y")
        box.prop(self, "output_translation_z")
        box.prop(self, "output_rotation_3d_x")
        box.prop(self, "output_rotation_3d_y")
        box.prop(self, "output_rotation_3d_z")

        # Scale for each axis
        box = layout.box()
        box.label(text="Scale Config")
        box.prop(self, "scale_translation_x")
        box.prop(self, "scale_translation_y")
        box.prop(self, "scale_translation_z")
        box.prop(self, "scale_rotation_3d_x")
        box.prop(self, "scale_rotation_3d_y")
        box.prop(self, "scale_rotation_3d_z")


def menu_func_export(self, context):
    self.layout.operator(ExportDiffusionString.bl_idname, text="Camera Diffusion String (.json)")

def register():
    bpy.utils.register_class(ExportDiffusionString)
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    bpy.utils.unregister_class(ExportDiffusionString)
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)

if __name__ == "__main__":
    register()
