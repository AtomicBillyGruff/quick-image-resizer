# set folder argument 
import os
import sys
import argparse
import shutil
from PIL import Image

def resize_image(filename, width, height):
    # open image
    img = Image.open(filename)
    # resize image to width and height but keep aspect ratio (keep_aspect_ratio)
    img = img.resize((width, height), Image.ANTIALIAS)
    # save image
    img.save(filename)

def setup_environment():

    # set up argument parser
    parser = argparse.ArgumentParser(description='Resize images in a folder')
    parser.add_argument('-f', '--folder', help='Folder to resize', required=True)
    parser.add_argument('--width', type=int, help='Width to resize images to', required=True)
    parser.add_argument('--height', type=int, help='Height to resize images to', required=True)
    parser.add_argument('-O', '--output', help='Output folder', required=True)
    # filetype 
    parser.add_argument('-t', '--type', help='Filetype to resize', required=True)

    # parse arguments
    args = parser.parse_args()

    # print folder name
    print('Resizing images in folder: ' + args.folder)

    # print resizing dimentions to console
    print('Resizing to: ' + str(args.width) + 'x' + str(args.height))

    # print output folder name
    print('Output folder: ' + args.output)

    # for all files in arg.folder copy to arg.output
    for filename in os.listdir(args.folder):
        # copy to output folder
        shutil.copy(args.folder + '/' + filename, args.output)
        
        # increase the dimensions of the image with the resize function
        resize_image(args.output + '/' + filename, args.width, args.height)

      

        

        

    

if __name__ == "__main__":
    

    setup_environment()
