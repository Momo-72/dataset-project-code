from PIL import Image
import random
import os

def stitch_image(input_path, output_path, copies=10, mode="default"):
    img = Image.open(input_path)
    width, height = img.size

    if mode == "default":
        new_img = Image.new("RGB", (width * copies, height * copies))
        for i in range(copies):
            for j in range(copies):
                new_img.paste(img, (i * width, j * height))

    elif mode == "horizontal":
        new_img = Image.new("RGB", (width * copies, height))
        for i in range(copies):
            new_img.paste(img, (i * width, 0))

    elif mode == "vertical":
        new_img = Image.new("RGB", (width, height * copies))
        for i in range(copies):
            new_img.paste(img, (0, i * height))

    else:
        raise ValueError("Invalid mode provided.")

    new_img.save(output_path)
    return new_img  # return stitched image for further use


def random_crop(img, crop_width, crop_height):
    width, height = img.size

    if crop_width > width or crop_height > height:
        raise ValueError("Crop size larger than image dimensions.")

    left = random.randint(0, width - crop_width)
    top = random.randint(0, height - crop_height)
    right = left + crop_width
    bottom = top + crop_height

    return img.crop((left, top, right, bottom))


if __name__ == "__main__":
    folder = "Image_Folder"  # change this to working folder
    output_folder = "Output"  # change this to where you want to save
    os.makedirs(output_folder, exist_ok=True)

    for filename in os.listdir(folder):
        if filename.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(folder, filename)

            # Step 1: Stitch image
            stitched_path = os.path.join(output_folder, f"stitched_{filename}")
            stitched_img = stitch_image(input_path, stitched_path, copies=10, mode="default")

            # Step 2: Crop stitched image 10 times
            for i in range(10):
                random_crop_img = random_crop(stitched_img, crop_width=100, crop_height=100)
                random_path = os.path.join(output_folder, f"random_crop_{i+1}_{filename}")
                random_crop_img.save(random_path)
