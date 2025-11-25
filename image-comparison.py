import os
from PIL import Image, ImageChops

def compare_images(image1_filepath, image2_filepath, destination_filepath):
    # Loads each image and ensures consistent color mode
    img1 = Image.open(image1_filepath).convert("RGB")
    img2 = Image.open(image2_filepath).convert("RGB")
    
    # Ensure both images are the same size
    if img1.size != img2.size:
        raise ValueError("Images must be the same size for comparison.")
    
    # Calculates the absolute diffence for each pixel
    # Identical pixels --> black, different pixels --> brighter greater difference
    difference_image = ImageChops.difference(img1, img2)
    difference_image.save(destination_filepath)
    print(f"Difference image saved as {destination_filepath}")

# Folder containing your images
folder_path = "images_folder"

# Get all image files in the folder
image_files = [f for f in os.listdir(folder_path) if f.lower().endswith((".jpg"))]

# Each image compared to every other image
for i, ref_file in enumerate(image_files):
    ref_name = os.path.splitext(ref_file)[0]  # reference name without extension
    ref_path = os.path.join(folder_path, ref_file)

    for j, other_file in enumerate(image_files):
        # Skip comparing the same file
        if i == j:
            continue

        other_name = os.path.splitext(other_file)[0]
        other_path = os.path.join(folder_path, other_file)

        # Output filename format: diff_reference_other.png
        output_filename = f"diff__{ref_name}__{other_name}.jpg"
        output_path = os.path.join(folder_path, output_filename)

        # Compare and save
        compare_images(ref_path, other_path, output_path)
        print(f"Saved difference: {output_filename}")