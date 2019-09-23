# Seam Carving Algorithm

## Original Authors of the Seam Carving Algorithm
Authors: Shai Avidan (Mitsubishi Electric Research Labs) and Ariel Shamir (The Interdisciplinary Center & MERL)
Link to paper (PDF): http://graphics.cs.cmu.edu/courses/15-463/2012_fall/hw/proj3-seamcarving/imret.pdf

## Description
Seam Carving is a content-aware resizing technique for images based on a paper written by Shai Avidan (Mitsubishi Electric Research Labs) and Ariel Shamir (The Interdisciplinary Center & MERL). It reduces the dimensions of an image by figuring out what seams are the least important and deleting them. The paper mainly focuses on image reduction, but this algorithm can be also be modified to enlarge images. For this case, The algorithm would have to determine what seams are the least important and then copy them.

## Concepts I learned
- What is the an image's derivative and how to calculate it
- How to detect the edges of an image
- How to calculate an algorithm that computes the minimum cost path between two points
- How to find the convolution of an image (or matrix).
- How quickly an algorithm becomes inefficient as the size of a matrix increases. 
  - This algorithm can take very long sometimes in the order of hours depending on the size of the image.
  - I found images with farily small dimensions (mostly around 500 in width and height)
  - This can be fixed by reading more through possible python libraries instead of manually creating functions to perform certain tasks.
    - For example python's scipy library has a convolution function that will perform faster than if I were to create my own convolution function.

## Future Ideas for this Project
- Implement image enlarging using Seam Carving
- Could this be used to efficiently store images?
  - Reduce the image by removing minimum seams and put in storage
  - Enlarge image to original size when brought out of storage
  - Could be inefficient in terms of speed depending on implementation method.
- Incorporate this into a web app for other people to use.

## Algorithm Overview

### 1.) Computing the Energy Map of the Image
The paper defines the energy map of an single pixel of the image to be:

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/Energy_Function.JPG)

For each pixel, we have to sum the partial derivatives of that pixel with respect to x and y. We do this for every pixel in the image. Finding the image derivtaive can be done by using the sobel operator (more info on that here: https://en.wikipedia.org/wiki/Sobel_operator). If done successfully, the result should look similar to this:

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/CenturyTower_EnergyMap.JPG)

The higher the energy value, the brighter that pixel is. As you probably notice, the resulting image shows the outlines of a lot of the objects. This is because the image derivative are the largest at edges. This is due to the fact that for the most part, the edge of two objects can be defined by the area that pixel colors sharply change.

The energy map will be used to figure out what continuous line of pixels produces the least amount of change. This continuous line of pixels is a seam.

*NOTE: There are multiple ways of implementing this part. You can have 1 energy map for the entire duration of the algorithm or you can recalculate the energy map each time a seam is removed. I implemented the latter.*

### 2.) Computing Optimal Seams of the Image
The paper formally defines a seam to be:

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/Vertical_Seam_Definition.JPG)

From the paper: "A vertical seam is an 8-connected path of pixels in the image from top to bottom, containing one, and only one, pixel in each row of the image". What this basically means that for any given pixel, the very next pixel could only be what is immediately diagonal to it, below it, above it, to the right of it, or to the left of it (i.e. it has a neighborhood of 8 pixels).

An optimal sean is deifned to be:

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/Optimal_Seam_Definition.JPG)

The optimal seam is basically the seam whose energy sum is the least. Calculating the minimum seam path:

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/Calculating_Optimal_Seam.JPG)

In programming terms, this is essentially a problem to find the minimum path between two points.

### 3.) Removing Optimal Seam of the Image
Once you find the optimal seam, you go back through the path and remove the pixels along that path. When removing the pixel, you must also shift the pixels along that row to fill in the missing pixel.

### 4.) Horizontal Seams
Finding and calculating optimal horizontal seams can be done with essentially the same steps as above, except that the algorithm has to go from the left of the image to the right (it can also go from right to left, it depends on implemtnation). One easy way of achieving this (and this is what I did for this implementation) is to rotate the image by 90 degrees before step 1. Then you would rotate the image back 90 degrees once the algorithm is finished.

## Regular Image Resizing vs. Resizing via Seam Carving

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/SnowyMountains_Original.JPG)

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/SnowyMountains_Matlab_resize.JPG)

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/SnowyMountains_Reduce_150pixels_Height.JPG)

The first image is the original, the second image is what happens when you regularly resize it, and the third image is what happens when you resize it using Seam Carving. It is reduced by 150 pixels in height.

As you can see, regular image resizing techniques "squishes" (if reducing) or "stretches" (if enlarging) the objects in the image causing distortion. Despite this occuring, an advantage to regular resizing techniques is how all objects are still intact. No objects are being cut off.

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/ForrestGump_Original.JPG)

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/ForrestGump_Matlab_resize.JPG)

![](https://github.com/CarlRiley99/Seam-Carving/blob/master/README_Assets/ForrestGump_Reduced_200pixels_Width.JPG)

The first image is the original, the second image is what happens when you regularly resize it, and the third image is what happens when you resize it using Seam Carving. It is reduced by 200 pixels in width.

The two images above reveals what can happen if you want to reduce an image by too much. There are portions where objects in the image are being cut off and it produces less optimal image than the regular resizing technique.

## Conclusion
My implementation of the algorithm only reduces the height and width of the image. Enlarging the image is extremely similar except instead of removing minimum seams, you would copy minimum seams.

The performance of the Seam Carving Algorithm ultimately depends on the implementation. The paper explains how modifying the energy function could produce better results or maybe using a different method to find the shortest path of pixels. My implementation is not necessarily correct, but is merely a version of the algorithm.
