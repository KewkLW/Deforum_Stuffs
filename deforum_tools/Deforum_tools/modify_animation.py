import bpy
import numpy as np

def modify_selected_keyframes(obj):
    # Ensure the object has animation data and action
    if obj.animation_data and obj.animation_data.action:
        action = obj.animation_data.action

        # Parse all the F-Curves in the action
        for fcurve in action.fcurves:
            # Copy only the selected keyframe points
            keyframe_points = [point for point in fcurve.keyframe_points if point.select_control_point]
            
            # Check if there are selected keyframes
            if keyframe_points:
                # Create an array of the y values
                y_values = np.array([point.co[1] for point in keyframe_points])
                
                # Find the local maxima and minima
                maxima = (np.diff(np.sign(np.diff(y_values))) < 0).nonzero()[0] + 1
                minima = (np.diff(np.sign(np.diff(y_values))) > 0).nonzero()[0] + 1

                # Combine the indices of the local maxima and minima
                extrema_indices = np.concatenate((maxima, minima))
                
                # Clear all keyframes
                fcurve.keyframe_points.clear()
                
                # Add back only the local maxima and minima
                for index in extrema_indices:
                    point = keyframe_points[index]
                    fcurve.keyframe_points.insert(point.co[0], point.co[1])

                # Set keyframe handle types to AUTO to create Bezier curve
                for point in fcurve.keyframe_points:
                    point.handle_left_type = 'AUTO'
                    point.handle_right_type = 'AUTO'
