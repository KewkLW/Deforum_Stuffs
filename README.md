# Deforum Parseq Tools

## Scripts

### **blender_export_to_parseq.py**

This script provides a addon for Blender, allowing users to export camera motion data from their Blender projects into JSON format intended for [parseq](https://sd-parseq.web.app/). 

## Installation

1. Download the `blender_export_to_parseq.py` file from the repository.
2. Open Blender and go to `Edit > Preferences`.
3. In the Preferences window, switch to the `Add-ons` tab.
4. Click on the `Install...` button at the top of the window.
5. Navigate to the location where you downloaded the `blender_export_to_parseq.py` file, select it, and click `Install Add-on`.
6. The add-on should now appear in the add-on list. However, it might not be enabled yet. To enable it, find it in the list (you can use the search bar) and check the checkbox on the left side.

## Usage
To use it go to file > export > camera diffusion string. 

When exporting, on the right of the window, you will see the various options to swap parameters. You can also choose to not output specfic parameters, and you can increase the scale of the output, but right now it is balanced for use in deform. Most of these are just there for debugging.


### **convert_deforum_to_parseq.py**

This is used to take raw frames and convert it to JSON to be used in parseq. Helpful if you have old camera data and want to use it in parseq for ease of manipulation. 

##Instructions
1. Download the `convert_deforum_to_parseq.py` file from the repository.
2. Open the script in a Python environment. This could be in a Python IDE, a Jupyter notebook, or even from the command line.
3. At the bottom of the script, you'll see two variables: `input_file` and `output_file`. You need to replace the paths specified here with the path to your input file and the desired path for your output file. For example:

```python
input_file = 'path_to_your_input_file.txt'
output_file = 'path_to_your_output_file.json'
```


## Contact

For any questions or issues, please open an issue on the GitHub repository or hit me up on Twitter [@kewkd](https://twitter.com/kewkd)

## Disclaimer

Please note that these scripts are provided as-is, and you use them at your own risk. The author is not responsible for any issues or damages that may occur as a result of using the scripts.

## Credits 

Our Lord and Savior: OpenAI for GPT
Michael Walker <micwalk@gmail.com> Twitter: [@mwalk10](twitter.com/mwalk10) for writing the original Blender export code which was modified then re-written. 
[Robin Fernandes / REWBS](https://github.com/rewbs) for Parseq
The [Deforum](https://github.com/deforum-art/sd-webui-deforum) crew for Deforum. 
