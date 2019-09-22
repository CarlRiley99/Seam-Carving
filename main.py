import FindEnergyMap as enMap
import ComputeSeams as compSeam
import ReduceWidth
import sys
from imageio import imread
import numpy as np
import matplotlib.pyplot as plt


image = imread(sys.argv[1])

newImage = ReduceWidth.reduceWidth(image, 150)

# How to show multiple images in 1 figure:
# https://gist.github.com/mstankie/71e49f628beac320953e0460b8ee78c2
f = plt.figure()
f.add_subplot(1,2, 1)
plt.imshow(image)
f.add_subplot(1,2, 2)
plt.imshow(newImage)
plt.show(block=True)

print(image.shape)
print(newImage.shape)

# NOTES
# Using numpy.array: https://www.programiz.com/python-programming/matrix