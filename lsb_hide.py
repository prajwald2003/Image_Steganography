from PIL import Image

def hide_text_into_image(image, text):
    """
    Hides text into an image using the LSB (Least Significant Bit) technique.

    Parameters:
    - image (PIL.Image.Image): The input image.
    - text (str): The text to be hidden.

    Returns:
    - result_image (PIL.Image.Image): The image with the text embedded.
    """
    # Convert the text to binary representation
    binary_text = ''.join(format(ord(char), '08b') for char in text)

    # Get the pixel data of the image
    pixels = list(image.getdata())

    # Embed the text into the image
    new_pixels = []
    text_index = 0
    for pixel in pixels:
        if text_index < len(binary_text):
            # Get the RGB values of the pixel
            red, green, blue = pixel

            # Modify the least significant bit of each color component
            red = (red & 0xFE) | int(binary_text[text_index])
            text_index += 1
            if text_index < len(binary_text):
                green = (green & 0xFE) | int(binary_text[text_index])
                text_index += 1
            if text_index < len(binary_text):
                blue = (blue & 0xFE) | int(binary_text[text_index])
                text_index += 1

            # Create the new pixel with the modified color components
            new_pixel = (red, green, blue)
            new_pixels.append(new_pixel)
        else:
            # Append the remaining pixels as is
            new_pixels.append(pixel)

    # Create a new image with the modified pixel data
    result_image = Image.new(image.mode, image.size)
    result_image.putdata(new_pixels)

    return result_image

def hide(image_path, text):
    """
    Hides text into an image file using the LSB (Least Significant Bit) technique.

    Parameters:
    - image_path (str): The file path of the input image.
    - text (str): The text to be hidden.

    Returns:
    - result_image (PIL.Image.Image): The image with the text embedded.
    """
    # Open the image
    image = Image.open(image_path)

    # Hide the text and the image
    result_image = hide_text_into_image(image, text)

    return result_image
