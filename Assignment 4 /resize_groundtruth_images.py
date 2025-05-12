
from PIL import Image
import os

# Define input and output folders
original_folder = "/home/atharv/Assignment4/colmap/images"
rendered_folder = "/home/atharv/gaussianssplat/render/GaussianImages/test/rgb"
resized_output = "/home/atharv/gaussianssplat/renders/GaussianImages/test/groundtruthrgb"

os.makedirs(resized_output, exist_ok=True)

# Extract dimensions from any rendered image
sample_image = next((f for f in os.listdir(rendered_folder)
                     if f.lower().endswith(('.jpg', '.png'))), None)

if not sample_image:
    print("No rendered images found!")
    exit()

with Image.open(os.path.join(rendered_folder, sample_image)) as img:
    target_size = img.size  # (width, height)

# Resize and save each ground truth image
for filename in os.listdir(original_folder):
    if filename.lower().endswith(".jpg"):
        orig_path = os.path.join(original_folder, filename)
        new_path = os.path.join(resized_output, os.path.splitext(filename)[0] + ".png")

        with Image.open(orig_path) as orig_img:
            resized_img = orig_img.resize(target_size, Image.LANCZOS)
            resized_img.save(new_path)
            print(f"Resized: {filename} -> {new_path}")
