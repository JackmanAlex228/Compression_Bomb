from PIL import Image
import os, sys, imghdr

# scan all the photos in the same file as a script
# save the compressed images into a new filder

newFile = 'compressed_images'                           # constant for name of new file
os.makedirs(newFile)                                    # create new folder for comrpessed images
path = os.path.dirname(os.path.realpath(__file__))      # path = the current directory of the python script
dirs = os.listdir(path)                                 # list of items in path

# go through all jpeg and png files in the directory and then copy
# the compressed version of these files into a new folder
for item in dirs:
    # [Errno 13] Permission denied: 'compressed_images'
    # in some tests, it would compress some images but not all of them
    if imghdr.what(item) == "jpeg" or imghdr.what(item) == "png":
        image = Image.open(item)
        f, e = os.path.splitext(item)
        image.save(path + "/" + newFile + "/" + f + "_compressed.jpg", optimized = True, quality = 50)