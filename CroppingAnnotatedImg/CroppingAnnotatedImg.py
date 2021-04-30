import os
from PIL import Image
import xml.etree.ElementTree as ET
import sys

# Crop Image Out of Annotated File
# Code Ref: https://stackoverflow.com/questions/61480425/automatic-image-cropping-from-bounding-boxes-annotation-python
for filename in os.listdir("kaggle/images"):
    img_counter = 0
    basename =  os.path.splitext(filename)[0]
    # print(basename)
    tree = ET.parse("kaggle/annotations/{}.xml".format(basename))
    root = tree.getroot()
    objects = root.findall('object')
    for o in objects:
        img_counter += 1
        temp_object_name = o.find('name').text
        bndbox = o.find('bndbox')  # reading bound box
        xmin = int(bndbox.find('xmin').text)
        ymin = int(bndbox.find('ymin').text)
        xmax = int(bndbox.find('xmax').text)
        ymax = int(bndbox.find('ymax').text)
        im = Image.open("kaggle/images/{}.png".format(basename))
        cropped = im.crop((xmin, ymin, xmax, ymax))
        temp_img_name = basename+"_"+str(img_counter)
        cropped.save('cropped_img/{}/{}.png'.format(temp_object_name, temp_img_name))
        im.close()