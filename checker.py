import os
import shutil

# Define the source directories and the destination directory
txt_dir = r'C:\Users\Mahadi Saym\Desktop\imran\labels'
img_dir = r'C:\Users\Mahadi Saym\Desktop\imran\images'
mismatch_dir = r'C:\Users\Mahadi Saym\Desktop\imran\xmismatch'

# Get a list of all .txt files in the txt_dir
txt_files = [f.lower() for f in os.listdir(txt_dir) if f.lower().endswith('.txt')]

# Get a list of all .jpg and .JPG files in the img_dir
img_files = [f.lower() for f in os.listdir(img_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]

# Find the mismatched .txt files
mismatched_txt_files = [txt_file for txt_file in txt_files if txt_file.replace('.txt', '.jpg') not in img_files]

# Move the mismatched .txt files to the destination directory
for txt_file in mismatched_txt_files:
    source_path = os.path.join(txt_dir, txt_file)
    destination_path = os.path.join(mismatch_dir, txt_file)
    shutil.move(source_path, destination_path)
    print(f"Moved {txt_file} to {destination_path}")

print("Done!")
