from PIL import Image
import numpy as np
import glob
import argparse
import os


def diff(image1, image2):
    image = [None, None]
    for im1, im2 in enumerate([image1, image2]):
        image[im1] = (np.array(im2.resize((32, 32), resample=Image.BICUBIC).convert('L'))).astype(np.int)
    return np.abs(image[0] - image[1]).sum()


parser = argparse.ArgumentParser()
parser.add_argument('--path', required=True, help='folder with images')
args = vars(parser.parse_args())
img_format = '\\*.jpg'

images = []
for file in glob.glob(args['path'] + img_format):
    path, name = os.path.split(file)
    im = Image.open(file)
    im.filename = name
    images.append(im)

for i in range(len(images)):
    for j in range(i+1, len(images)):
        if i == j:
            continue
        if 0 <= diff(images[i], images[j]) < 30000:
            print(images[i].filename, images[j].filename)
