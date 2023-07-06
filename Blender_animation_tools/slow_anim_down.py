import bpy

# Factor to slow down the animation
scale_factor = 4

# Iterate over all objects in the current scene
for obj in bpy.context.scene.objects:
    # Check if the object has animation data and an action
    if obj.animation_data and obj.animation_data.action:
        # Iterate over all action's fcurves
        for fcurve in obj.animation_data.action.fcurves:
            # Iterate over all keyframes in the fcurve
            for keyframe in fcurve.keyframe_points:
                # Multiply the frame number by the scale factor
                keyframe.co.x *= scale_factor
                keyframe.handle_left.x *= scale_factor
                keyframe.handle_right.x *= scale_factor

# Adjust scene's end frame
bpy.context.scene.frame_end *= scale_factor
