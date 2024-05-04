# Video to Image Conversion for Raspberry Pi Pico SSD1306 OLED Display

## Overview

This project aims to provide a solution for displaying videos on the SSD1306 OLED display connected to a Raspberry Pi Pico. Since the display has limitations in playing videos directly, we use DaVinci Resolve to convert the video into a sequence of images. These images are then converted to PBM format using ImageMagick and displayed on the SSD1306 OLED screen using Python and the `framebuf` module.

## Requirements

- Python 3.5 or later
- ImageMagick
- DaVinci Resolve

## Steps

1. **Download all required tools.**
2. **Use DaVinci Resolve to save the video as multiple images.**
   - Upload your video file to DaVinci Resolve.
   - Click the render tab at the bottom right of the screen.
   - Navigate to the individual clip option on the left and note the export format you chose.
   - Choose your export folder and click render at the bottom.
3. **Use the provided Python script to convert BMP images to PBM format using ImageMagick.**
   - Open the `imagetobpm.py` file.
   - Replace the destination of `input_folder` with the folder where you saved the files from DaVinci Resolve.
   - Replace the destination of `output_folder` with where you want converted images to be saved.
   - Run the script in the terminal to convert the images to PBM format in the `output_folder`.
4. **Display the converted images on your SSD1306 OLED display using framebuf.**
   - Store the images on an SD drive connected to the Raspberry Pi Pico.
   - Copy the `main.py` file to your Thonny IDE.
   - Change the path to your folder with your PBM images.
   - Run the Thonny program.

## Tips and Considerations

- **Image Size:** Keep the image size at 128 x 64, as it's the native resolution of the SSD1306 OLED screen.
- **Color Invert:** You can adjust the color invert to better display your image if needed.
- **File Memory:** The file memory on Raspberry Pi Pico is minimal. Expanding to an SD card would give the ability for larger files.

---

Please replace placeholders like `"/users/documents/input_folder"` and `"/users/documents/output_folder"` with the actual paths in your system. Also, make sure to include the images referenced in your README (`screen_one.png`, `screen_two.png`, `screen_three.png`) in the correct path relative to your README file.
