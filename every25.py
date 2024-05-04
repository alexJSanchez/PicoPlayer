import os
import subprocess

def convert_bmp_to_pbm(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Initialize a counter to keep track of the number of files processed
    counter = 0

    # Iterate over files in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".bmp"):
            counter += 1
            # Skip files until the 25th file is reached
            if counter % 20 != 0:
                continue
            
            input_path = os.path.join(input_folder, filename)
            output_filename = os.path.splitext(filename)[0] + ".pbm"
            output_path = os.path.join(output_folder, output_filename)
            subprocess.run(["magick", "convert", input_path, output_path])

# Specify the input and output folders
input_folder = "/users/documents/input_folder_name"
output_folder = "/users/documents/output_folder_name"

# Convert every 25th BMP image in the input folder
convert_bmp_to_pbm(input_folder, output_folder)
