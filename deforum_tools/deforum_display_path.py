import bpy

bl_info = {
    "name": "Deforum Tools",
    "description": "Kewk's Deforum Tools",
    "author": "https://twitter.com/kewkd",
    "version": (2, 0),
    "blender": (3, 5, 0),
    "location": "View3D > Sidebar > MotionPath > Deforum Camera",
    "category": "Object",
}
class OBJECT_OT_CalculateMotionPath(bpy.types.Operator):
    bl_idname = "object.calculate_motion_path"
    bl_label = "Calculate MotionPath"
    bl_description = "Calculates the MotionPath of the selected object"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        obj = context.active_object
        anim_data = obj.animation_data

        if anim_data is not None and anim_data.action is not None:
            loc_fcurves = [fc for fc in anim_data.action.fcurves if fc.data_path.endswith("location")]

            if len(loc_fcurves) > 0:
                curve = bpy.data.curves.new("MotionPath", "CURVE")
                spline = curve.splines.new("NURBS")
                num_frames = int(anim_data.action.frame_range[-1]) + 1
                spline.points.add(num_frames)
                for frame in range(num_frames):
                    sample = [loc_fcurve.evaluate(frame) for loc_fcurve in loc_fcurves]
                    spline.points[frame].co = (sample[0], sample[1], sample[2], 1)
                # set curve to 3D
                curve.dimensions = '3D'
                # create object and link to scene
                curve_obj = bpy.data.objects.new("MotionPath", curve)
                bpy.context.scene.collection.objects.link(curve_obj)
                # select object
                bpy.context.view_layer.objects.active = curve_obj
                curve_obj.select_set(True)

        return {'FINISHED'}

class MotionPathPanel(bpy.types.Panel):
    bl_idname = "OBJECT_PT_motion_path_panel"
    bl_label = "Deforum Tools"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Deforum Tools"

    def draw(self, context):
        layout = self.layout
        layout.operator("object.calculate_motion_path", text="Display path")       

classes = (OBJECT_OT_CalculateMotionPath, MotionPathPanel)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()