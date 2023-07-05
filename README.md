## Deforum Tools

This is a simple Blender addon that provides additional functionality. To use it, follow the steps below:

1. Download the ZIP file containing the addon.
2. Install the addon in Blender.
   - Open Blender and navigate to Edit > Preferences > Add-ons.
   - Click on the "Install" button.
   - Locate the downloaded ZIP file and select it for installation.

After installing the addon, a new menu will appear on the right side of the Blender interface, containing two buttons:

### Display Path:
This feature takes the animation data and converts it into a curve.
To use this feature:
1. Select the camera object in your scene.
2. Click on the "Display Path" button in the addon's menu.

### Clean Selected Keyframes:
This feature allows you to clean up selected keyframes in the Graph Editor. To use it:
1. Switch to the Graph Editor in Blender.
2. Ensure that the camera object is selected.
3. Select the keyframes you want to clean.
4. Click on the "Clean Selected Keyframes" button in the addon's menu.

### Curve to Frames
1. Draw a cuve, place a curve, throw a curve up whatever, select the curve 
2. Click curve to frames and now you have frame data from a curve that can be export to deforum.

The cleaning process involves analyzing the selected keyframes and removing any intermediate keyframes between high and low value changes. Additionally, the addon will attempt to fit a Bezier curve to maintain the shape of the animation. While this process is generally accurate, please note that it may not be perfect. However, for Deforum purposes, it is perfectly suitable.


## Contact

For any questions or issues, please open an issue on the GitHub repository or hit me up on Twitter [@kewkd](https://twitter.com/kewkd)

## Disclaimer

Please note that these scripts are provided as-is, and you use them at your own risk. The author is not responsible for any issues or damages that may occur as a result of using the scripts.

## Credits 

Our Lord and Savior: OpenAI for GPT
Michael Walker <micwalk@gmail.com> Twitter: [@mwalk10](twitter.com/mwalk10) for writing the original Blender export code which was modified then re-written. 
[Robin Fernandes / REWBS](https://github.com/rewbs) for Parseq
The [Deforum](https://github.com/deforum-art/sd-webui-deforum) crew for Deforum. 
