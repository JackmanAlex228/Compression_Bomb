from PIL import Image
import os, sys, imghdr

# scan all the photos in the same file as a script
# save the compressed images into a new filder

os.makedirs('compressed_images')
path = os.path.dirname(os.path.realpath(__file__))
dirs = os.listdir(path)
for item in dirs:
    # [Errno 13] Permission denied: 'compressed_images'
    # in some tests, it would compress some images but not all of them
    if imghdr.what(item) == "jpeg" or imghdr.what(item) == "png":
        image = Image.open(item)
        f, e = os.path.splitext(item)
        image.save(path + "/compressed_images/" + f + "_optimized.jpg", optimized = True, quality = 50)