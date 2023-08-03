import sys
from PIL import Image
import numpy as np

# Read the command line argument
image_path = sys.argv[1]

# Open the image
image = Image.open(image_path)

# Convert the image to a NumPy array
image_array = np.array(image)

# Get the red channel of the image (assuming it's an RGB image)
red_channel = image_array[:, :, 0]

# Retrieve the LSBs of each pixel value to reconstruct the message
binary_message = ""
for row in red_channel:
    for pixel in row:
        binary_message += bin(pixel)[-1]

# Convert the binary message to ASCII characters
message = ""
for i in range(0, len(binary_message), 8):
    byte = binary_message[i:i + 8]
    message += chr(int(byte, 2))

# Print the decrypted message
print("Decrypted Message:", message)
