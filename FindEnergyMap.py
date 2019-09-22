import numpy as np
import matplotlib.image as mpimage
import matplotlib.pyplot as plt
from scipy import signal

def FindEnergyMap(image):
    grayImage = rgb2gray(image)
    #plt.imshow(grayImage)
    #plt.show()  # Must add this for the image to show
                # Reference: https://stackoverflow.com/questions/42812230/why-plt-imshow-doesnt-display-the-image

    # Using Sobel Derivatives to find image derivatives
    p_u = np.array([[1, 2, 1],
                   [0, 0 ,0],
                   [-1, -2, -1]])

    p_v = np.array([[1, 0, -1],
                   [2, 0, -2],
                   [1, 0, -1]])

    energyMap = np.absolute(signal.convolve2d(grayImage, p_u)) + np.absolute(signal.convolve2d(grayImage, p_v))
    #plt.imshow(energyMap)
    #plt.show()
    return energyMap

def rgb2gray(image):
    return np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])

# Convert RGB to Grayscale: https://stackoverflow.com/questions/12201577/how-can-i-convert-an-rgb-image-into-grayscale-in-python