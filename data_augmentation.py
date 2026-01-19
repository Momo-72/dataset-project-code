from PIL import Image
import random
import os

def stitch_image(input_path, output_path, copies=10, mode="default"):
    img = Image.open(input_path)
    width, height = img.size

    if (mode == "default"):
        new_img = Image.new("RGB", (width * copies, height * copies))
        for i in range(copies):
            for j in range(copies):
                new_img.paste(img, (i * width, j * height))

    elif (mode == "horizontal"):
        new_img = Image.new("RGB", (width * copies, height))
        for i in range(copies):
            new_img.paste(img, (i * width, 0))

    elif (mode == "vetical"):
        new_img = Image.new("RGB", (width, height * copies))
        for i in range(copies):
            new_img.paste(img, (0, i * height))

    else:
        raise ValueError("Invalid mode provided.")

    
    new_img.save(output_path)

def random_crop(input_path, output_path, crop_width, crop_height):
    img = Image.open(input_path)
    width, height = img.size

    left = random.randint(0, width - crop_width)
    top = random.randint(0, height - crop_height)
    right = left + crop_width
    bottom = top + crop_height
    
    new_img = img.crop((left, top, right, bottom))

    new_img.save(output_path)

if __name__ == "__main__":
    folder = "Image_Folder" # change this to working folder
    output_folder = "Output" # Change this to where want to save
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder):
        if filename.lower.endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(folder, filename)

            stitched_path = os.path.join(output_folder, f"stitched_{filename}")
            stitch_image(input_path, stitched_path, copies=10, mode="default")

            random_path = os.path.join(output_folder, f"random_crop_{filename}")
            random_crop(input_path, random_path, crop_width=100, crop_height=100)

