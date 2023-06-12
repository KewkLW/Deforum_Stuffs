import bpy
from bpy_extras.io_utils import ExportHelper
from . import exporter

class ExportToParseqVR(bpy.types.Operator, ExportHelper):
    bl_idname = "export_scene.parseq_vr"
    bl_label = "Export to Parseq VR"
    bl_options = {'PRESET'}

    filename_ext = ".json"

    # Add custom properties for the operator
    rounding_precision: bpy.props.IntProperty(
        name="Rounding Precision",
        description="Number of decimal places to round the values",
        default=1,
        min=0,
        max=10
    )

    # Add more custom properties as needed for the proposed improvements and features

    def execute(self, context):
        # Pass the custom properties to the export_to_parseq_vr function
        return exporter.export_to_parseq_vr(context, self.filepath, self.rounding_precision)
