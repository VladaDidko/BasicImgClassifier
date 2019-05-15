from PIL import Image
import numpy as np
import glob

PATH = input('Please input PATH of img folder:  ')


def diff(image1, image2):
    image = [None, None]
    for im1, im2 in enumerate([image1, image2]):
        image[im1] = (np.array(im2.resize((32, 32), resample=Image.BICUBIC).convert('L'))).astype(np.int)
    return np.abs(image[0] - image[1]).sum()


images = [Image.open(filename) for filename in glob.glob(PATH + '\\*.jpg')]
temp = []
for i in range(len(images)):
    if images[i] in temp:
        continue
    for j in range(len(images)):
        if i == j or images[j] in temp:
            continue
        elif 0 <= diff(images[i], images[j]) < 30000:
            print(images[i].filename, images[j].filename)
            temp.append(images[j])