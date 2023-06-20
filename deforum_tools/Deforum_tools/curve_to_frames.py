import bpy
import mathutils
import math
import numpy as np


def execute_curve_to_frames():

    # Check if there is a curve object in the scene
    curve = None
    for obj in bpy.data.objects:
        if obj.type == 'CURVE':
            curve = obj
            break

    # If no curve object, print a message and exit
    if curve is None:
        print("No curve object found in the scene.")
        return

    # Check if there is a camera in the scene
    camera = None
    for obj in bpy.data.objects:
        if obj.type == 'CAMERA':
            camera = obj
            break

    # If no camera, add a new camera and name it 'deforum_cam'
    if camera is None:
        # Create a camera data-block
        camera_data = bpy.data.cameras.new(name='Camera')

        # Create an object and link it with the camera data-block
        camera = bpy.data.objects.new('deforum_cam', camera_data)

        # Add created camera-object to the scene
        bpy.context.scene.collection.objects.link(camera)

    # Get the first spline in the curve
    spline = curve.data.splines[0]
    points = spline.points  

    # Calculate the number of frames per point
    frames_per_point = bpy.context.scene.frame_end / len(points)

    # Loop through each control point and add a keyframe to the camera at that position
    for i, point in enumerate(points):
        # Set the camera's location to the control point's location
        camera.location = point.co.xyz

        # If this isn't the last point, calculate the direction to the next point
        # and rotate the camera to face that direction
        if i < len(points) - 1:
            direction = mathutils.Vector(points[i+1].co.xyz) - mathutils.Vector(point.co.xyz)
            rot_quat = direction.to_track_quat('-Z', 'Y')
            camera.rotation_euler = rot_quat.to_euler()

        # Insert a keyframe for the camera's location
        camera.keyframe_insert(data_path="location", frame=i*frames_per_point)

        # Insert a keyframe for the camera's rotation
        camera.keyframe_insert(data_path="rotation_euler", frame=i*frames_per_point)

    # Now remove all keyframes except min and max
    for fcurve in camera.animation_data.action.fcurves:
        # Copy all keyframe points
        keyframe_points = [point for point in fcurve.keyframe_points]

        # Create an array of the y values
        y_values = np.array([point.co[1] for point in keyframe_points])

        # Find the global maximum and minimum
        max_index = np.argmax(y_values)
        min_index = np.argmin(y_values)

        # Clear all keyframes
        fcurve.keyframe_points.clear()

        # Add back only the global maximum and minimum
        for index in (max_index, min_index):
            point = keyframe_points[index]
            fcurve.keyframe_points.insert(point.co[0], point.co[1])

        # Set keyframe handle types to AUTO to create Bezier curve
        for point in fcurve.keyframe_points:
            point.handle_left_type = 'AUTO'
            point.handle_right_type = 'AUTO'


execute_curve_to_frames()
