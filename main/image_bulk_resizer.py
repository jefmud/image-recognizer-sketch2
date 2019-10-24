import cv2
import os
import argparse

# construct the argument parser and parse the arguments
# since this is just a helper program, it is not particularly user friendly!
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--imagedir", required=True,
                help="path to input directory (i.e., directory of images)")
ap.add_argument("-o", "--outputdir", required=True,
                help="path to output directory (i.e., directory of images)")
ap.add_argument('-x', '--xdim', required=True,
                help="The x dimension")
ap.add_argument('-y', '--ydim', required=True,
                help="The y dimension")

args = vars(ap.parse_args())

# get required command line arguments
image_dir = args['imagedir']
out_dir = args['outputdir']
xdim = int(args['xdim'])
ydim = int(args['ydim'])

imagePath = image_dir

# processing loop
files = os.listdir(imagePath)
count = 0
for f in files:
    imagePath = os.path.join(image_dir, f)

    try:
        # brute force resize anything that loads as an image
        image = cv2.imread(imagePath)
        image = cv2.resize(image, (xdim, ydim))
        outPath = os.path.join(out_dir, f)
        cv2.imwrite(outPath, image)
        count += 1
    except Exception as e:
        # log error to the console
        print("Error: {} <{}>".format(str(e), imagePath))
        
print("Done. {} images resized.".format(count))