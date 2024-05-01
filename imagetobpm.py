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
        #if your images are in different format simply replace the end switch
        if filename.endswith(".bmp"):
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".pbm"
            output_path = os.path.join(output_folder, output_filename)
            # Convert the image using ImageMagick
            subprocess.run(["magick", "convert", input_path, output_path])

# Specify the input and output folders
input_folder = "/users/alexa/documents/bh_images"
output_folder = "/users/alexa/documents/bh_pbm_converted"

# Convert BMP images in the input folder
convert_bmp_to_pbm(input_folder, output_folder)
