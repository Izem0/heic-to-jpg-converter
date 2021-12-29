import os
import glob
import re
from wand.image import Image

# user inputs
source_folder = r"G:\My Drive\heic_files"
target_folder = r"G:\My Drive\jpg_files"

# check if source_folder exists
if not os.path.exists(source_folder):
    raise NotADirectoryError(
        f"Source folder '{source_folder}' does not exist! Please put your .heic files in an existing folder."
    )
else:  # if exists, check if contains .heic files
    files_paths = glob.glob(os.path.join(source_folder, '*.heic'))
    if not files_paths:  # if no file in the source directory
        raise FileNotFoundError(f"No files to convert found in the directory '{target_folder}'.")

# create target folder is not exists
if not os.path.exists(target_folder):
    os.mkdir(target_folder)
    print(f"Target folder {target_folder} did not exist. It has been created.")

# loop through all .heic files and convert them
for file_path in files_paths:
    file_name = os.path.basename(file_path)

    new_file_name = re.sub("\.heic", ".jpg", file_name, flags=re.IGNORECASE)
    new_file_path = os.path.join(target_folder, new_file_name)

    # convert image
    img = Image(filename=file_path)
    img.format = 'jpg'
    img.save(filename=new_file_path)
    img.close()

    print(f"Image {file_name} converted to {new_file_name}")

print(f"\nAll {len(files_paths)} images were converted to jpg and saved to '{target_folder}'!")
