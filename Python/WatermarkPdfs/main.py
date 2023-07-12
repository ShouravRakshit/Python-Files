import requests

from PIL import Image

# Open the image
image = Image.open('C:/Work/Web-Deveopment/HTML & CSS/3.1 Nesting and Indentation/goal.png')

# Get the color of a pixel at (x, y) coordinates
pixel_color = image.getpixel((130, 0))

print(pixel_color)  # Output: (R, G, B) tuple

