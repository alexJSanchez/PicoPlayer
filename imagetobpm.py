import os
#subprocess is built into python 3.5
import subprocess

# this function takes in images from input_folder and outputs them into output_folder in the format of bpm
# destination of folders is up to you. if you do not decide one will be created in the os folder


def convert_bmp_to_pbm(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate over files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".png"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".pbm"
            output_path = os.path.join(output_folder, output_filename)
            # Convert and resize the image using ImageMagick
            subprocess.run(["magick", "convert", input_path, "-resize", "128x64", output_path])

# Specify the input and output folders
input_folder = "/users/my_user/documents/input_folder"
output_folder = "/users/my_user/documents/output_folder"

# Convert BMP images in the input folder
convert_bmp_to_pbm(input_folder, output_folder)
