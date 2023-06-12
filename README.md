# Deforum Parseq Tools

## Scripts

### blender_export_to_parseq.py

This script provides a addon for Blender, allowing users to export camera motion data from their Blender projects into JSON format intended for [parseq](https://sd-parseq.web.app/). 

## Installation

1. Download the `blender_export_to_parseq.py` file from the repository.

2. Open Blender and go to `Edit > Preferences`.

3. In the Preferences window, switch to the `Add-ons` tab.

4. Click on the `Install...` button at the top of the window.

5. Navigate to the location where you downloaded the `blender_export_to_parseq.py` file, select it, and click `Install Add-on`.

6. The add-on should now appear in the add-on list. However, it might not be enabled yet. To enable it, find it in the list (you can use the search bar) and check the checkbox on the left side.

To use it go to file > export > camera diffusion string. 

When exporting, on the right of the window, you will see the various options to swap parameters. You can also choose to not output specfic parameters, and you can increase the scale of the output, but right now it is balanced for use in deform. Most of these are just there for debugging. But 

## Usage

To use these scripts, you need to have Blender installed on your system. You can then run the scripts inside Blender's scripting environment. The `blender_export_to_parseq.py` script adds a new option to Blender's export menu, allowing you to export camera motion data as a JSON file.

## Contribution

If you have any suggestions or improvements, feel free to fork the repository and submit a pull request. All contributions are welcome!

## License

This project is open-source, but the license terms have not been specified. Please contact the repository owner for more information.

## Contact

For any questions or issues, please open an issue on the GitHub repository or contact the repository owner directly.

## Disclaimer

Please note that these scripts are provided as-is, and you use them at your own risk. The author is not responsible for any issues or damages that may occur as a result of using the scripts.
