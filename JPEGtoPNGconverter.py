import sys
import os
from PIL import Image
'''
MUST: You must have both the folder2_convert and the python file inside the project, else it wont work
SYS INFO: sys.argv's only accept the folder name with frontslash, no need for extras, like absolute path 
'''

# grab the first and second argument
folder_2convert = sys.argv[1]
folder_2store_converted_imgs = sys.argv[2]

# check if new/exists if not create it
if __name__ == "__main__":
    if os.path.exists(folder_2store_converted_imgs):
        pass
    else:
        os.makedirs(folder_2store_converted_imgs)

    files = os.listdir(folder_2convert)
    # loop through pokedex
    for file in files:
        filepath = f"./{folder_2convert}{file}"
        img = Image.open(filepath)
        # convert images to png
        # save to the new folder
        path = f"./{folder_2store_converted_imgs}{file.split('.')[0]}.png"
        img.save(path)
