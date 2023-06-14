import json

def generate_combinations(text, *args):
    keyframes = []

    num_args = len(args)
    arg_count = num_args // 3

    # Generate the incremental combinations
    frame = 1
    for i in range(arg_count):
        arg_index = i * 3
        arg = args[arg_index]
        min_val = float(args[arg_index + 1])
        max_val = float(args[arg_index + 2])

        for j in range(int(min_val * 10), int(max_val * 10) + 1, 1):
            for k in range(arg_count):
                k_arg_index = k * 3
                k_arg = args[k_arg_index]
                k_min_val = float(args[k_arg_index + 1])
                k_max_val = float(args[k_arg_index + 2])

                for l in range(int(k_min_val * 10), int(k_max_val * 10) + 1, 1):
                    if i != k:
                        deforum_prompt = f"{text}, <lora:{arg}:{j / 10}>, <lora:{k_arg}:{l / 10}>, <lora:{k_arg}:{l / 10}>"
                        keyframe = {"frame": frame, "deforum_prompt": deforum_prompt}
                        keyframes.append(keyframe)
                        frame += 1

    # Output the combinations to a file
    with open("c://tmp//combinations.json", "w") as f:
        json.dump({"keyframes": keyframes}, f, indent=4)

# Example usage
generate_combinations(
    "a digital painting of a skull with a purple background and a purple background with a blue skull and a purple background with a purple background, Dan Mumford, josan gonzales and dan mumford, digital art, psychedelic art",
    "kewk-anime-lora",
        "0.1",
        "1.7",
    "add_detail",
        "0.1",
        "1.7",
    "epi_noiseoffset2",
        "0.1",
        "1.7"
    
)
