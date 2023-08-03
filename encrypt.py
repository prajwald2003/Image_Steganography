from stegano import lsb
import sys

# Read the command line arguments
image_path = sys.argv[1]
message = sys.argv[2]

# Encrypt the message into the image
encrypted_image = lsb.hide(image_path, message)
encrypted_image.save("encrypted_image.jpg")

