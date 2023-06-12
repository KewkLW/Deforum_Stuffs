import json

def parse_input_line(line):
    frame_data = {}
    for entry in line.strip().split(','):
        if ':' in entry:
            frame, value = entry.split(':')
            frame = int(frame)
            value = float(value.strip('()'))
            frame_data[frame] = value
    return frame_data

def convert_to_json_format(input_file, output_file):
    axis_map = {
        0: 'translation_x',
        1: 'translation_y',
        2: 'translation_z',
        3: 'rotation_3d_x',
        4: 'rotation_3d_y',
        5: 'rotation_3d_z',
    }

    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    camera_data = {}
    for i, line in enumerate(lines):
        axis = i % 6
        if axis in axis_map:
            axis_data = parse_input_line(line)
            for frame, value in axis_data.items():
                if frame not in camera_data:
                    camera_data[frame] = {'frame': frame}
                camera_data[frame][axis_map[axis]] = value

    camera_data_list = list(camera_data.values())

    with open(output_file, 'w') as outfile:
        json.dump(camera_data_list, outfile)

input_file = 'E:\\scripts\\blender\\convert deform frames to json for parseq\\test_input2.txt'
output_file = 'output-test.json'

# Check if the input file extension is .txt or .csv
file_extension = input_file.split('.')[-1]
if file_extension in ['txt', 'csv']:
    convert_to_json_format(input_file, output_file)
else:
    print(f"Unsupported file format: .{file_extension}")
