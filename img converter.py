from PIL import Image
import numpy as np

# Load image
image = Image.open("new.png")

#image=image.convert('L') #convert to gray scale

# Get dimensions
width, height = image.size

# Get pixel values as a 2D list
pixels = [[image.getpixel((x,y)) for y in range(height)] for x in range(width)]
#print(pixels)

# Convert pixel values to a NumPy array
pixels_np = np.array(pixels,dtype=np.uint8)

print(pixels_np)

# Create image from NumPy array
img = Image.fromarray(pixels_np)
img.save('image2.png')
