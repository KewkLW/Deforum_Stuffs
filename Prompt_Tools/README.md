# Text Generator Script

This script allows you to generate a text file based on inputs for main text, additional text, prefix, suffix, and an output directory. The script uses the Gradio library to create a simple user interface for inputting these parameters.

## Dependencies

- Python 3.x
- Gradio

You can install Gradio using pip:

```bash
pip install gradio
```

## How to Use

1. **Run the script**: You can run the script using any Python IDE or from the command line using the command `python append_script.py`.

2. **Input the parameters**: The script will open a Gradio interface in your default web browser. Here, you can input the following parameters:

   - **Main Text**: The main body of text that you want to include in the output file. You can input multiple lines of text.

   - **Additional Text**: Any additional text that you want to append to the main text. You can input multiple lines of text.

   - **Prefix**: Any text that you want to prepend to each line of the main and additional text. You can input multiple lines of text.

   - **Suffix**: Any text that you want to append to each line of the main and additional text. You can input multiple lines of text.

   - **Output Directory**: The directory where you want the output text file to be saved.

3. **Generate the text file**: After inputting the parameters, click on the "Submit" button. The script will generate the text file and save it in the specified output directory. The path to the output file will be displayed in the interface.
