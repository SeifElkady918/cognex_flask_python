from PIL import Image
import os

def convert_bmp(input_file, output_format='png'):
    """
    Converts a BMP image to PNG or JPG format.

    Args:
        input_file (str): Path to the .bmp file.
        output_format (str): Target format ('png' or 'jpg').

    Returns:
        str: Path to the converted image file.
    """
    if output_format.lower() not in ['png', 'jpg', 'jpeg']:
        raise ValueError("Output format must be 'png' or 'jpg'.")

    # Load the BMP image
    with Image.open(input_file) as img:
        # Prepare output filename
        base_name = os.path.splitext(input_file)[0]
        output_file = f"{base_name}.{output_format.lower()}"

        # For JPG, convert to RGB if needed (to avoid saving with alpha channel)
        if output_format.lower() in ['jpg', 'jpeg'] and img.mode in ('RGBA', 'LA'):
            img = img.convert("RGB")

        img.save(output_file)
        print(f"Image saved as {output_file}")
        return output_file


if __name__ == "__main__":
    convert_bmp("Images\image.bmp", "png")

# Example usage:
# convert_bmp("example.bmp", "png")
# convert_bmp("example.bmp", "jpg")
