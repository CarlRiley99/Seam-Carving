# Seam Carving Algorithm

## Original Authors of the Seam Carving Algorithm
Authors: Shai Avidan (Mitsubishi Electric Research Labs) and Ariel Shamir (The Interdisciplinary Center & MERL)
Link to paper (PDF): http://graphics.cs.cmu.edu/courses/15-463/2012_fall/hw/proj3-seamcarving/imret.pdf

## Description
Seam Carving is a content-aware resizing technique for images based on a paper written by Shai Avidan (Mitsubishi Electric Research Labs) and Ariel Shamir (The Interdisciplinary Center & MERL). It reduces the dimensions of an image by figuring out what seams are the least important and deleting them. The paper mainly focuses on image reduction, but this algorithm can be also be modified to enlarge images. For this case, The algorithm would have to determine what seams are the least important and then copy them.

## Algorithm Overview

### 1.) Computing the Energy Map of the Image
The paper defines the energy map of an single pixel of the image to be:

[INSERT ENERGY IMAGE HERE]
Syntax for adding image: ![Energy Function defined by the paper](README_Assets/Energy_Function)

For each pixel, we have to sum the partial derivatives of that pixel with respect to x and y. We do this for every pixel in the image. Finding the image derivtaive can be done by using the sobel operator (more info on that here: https://en.wikipedia.org/wiki/Sobel_operator). If done successfully, the result should look similar to this:

[INSERT DERIVATIVE IMAGE HERE]
Syntax for adding image: ![Image description](link-to-image)

The higher the energy value, the brighter that pixel is. As you probably notice, the resulting image shows the outlines of a lot of the objects. This is because the image derivative are the largest at edges. This is due to the fact that for the most part, the edge of two objects can be defined by the area that pixel colors sharply change.

The energy map will be used to figure out what continuous line of pixels produces the least amount of change. This continuous line of pixels is a seam.

*NOTE: There are multiple ways of implementing this part. You can have 1 energy map for the entire duration of the algorithm or you can recalculate the energy map each time a seam is removed. I implemented the latter.*

### 2.) Computing Optimal Seams of the Image
The paper formally defines a seam to be:

[INSERT SEAM IMAGE HERE]
Syntax for adding image: ![Image description](link-to-image)

From the paper: "A vertical seam is an 8-connected path of pixels in the image from top to bottom, containing one, and only one, pixel in each row of the image". What this basically means that for any given pixel, the very next pixel could only be what is immediately diagonal to it, below it, above it, to the right of it, or to the left of it (i.e. it has a neighborhood of 8 pixels).

An optimal sean is deifned to be:

[INSERT OPTIMAL SEAM IMAGE HERE]
Syntax for adding image: ![Image description](link-to-image)

The optimal seam is basically the seam whose energy sum is the least. Calculating the minimum seam path:

[INSERT MIN SEAM PATH IMAGE HERE]
Syntax for adding image: ![Image description](link-to-image)

In programming terms, this is essentially a problem to find the minimum path between two points.

### 3.) Removing Optimal Seam of the Image
Once you find the optimal seam, you go back through the path and remove the pixels along that path. When removing the pixel, you must also shift the pixels along that row to fill in the missing pixel.

### 4.) Horizontal Seams
Finding and calculating optimal horizontal seams can be done with essentially the same steps as above, except that the algorithm has to go from the left of the image to the right (it can also go from right to left, it depends on implemtnation). One easy way of achieving this (and this is what I did for this implementation) is to rotate the image by 90 degrees before step 1. Then you would rotate the image back 90 degrees once the algorithm is finished.

## Regular Image Resizing vs. Resizing via Seam Carving

[INSERT REGULAR RESIZE IMAGE HERE]
Syntax for adding image: ![Image description](link-to-image)

[INSERT SEAM CARVE IMAGE HERE]
Syntax for adding image: ![Image description](link-to-image)

As you can see, regular image resizing techniques "squishes" (if reducing) or "stretches" (if enlarging) the objects in the image causing distortion. Despite this occuring, an advantage to regular resizing techniques is how all objects are still intact. No objects are being cut off.

[INSERT REGULAR RESIZE IMAGE HERE]
Syntax for adding image: ![Image description](link-to-image)

[INSERT BAD SEAM CARVE IMAGE HERE]
Syntax for adding image: ![Image description](link-to-image)

The two images above reveals what can happen if you want to reduce an image by too much. There are portions where objects in the image are being cut off and it produces less optimal image than the regular resizing technique.

## Conclusion
My implementation of the algorithm only reduces the height and width of the image. Enlarging the image is extremely similar except instead of removing minimum seams, you would copy minimum seams.

The performance of the Seam Carving Algorithm ultimately depends on the implementation. The paper explains how modifying the energy function could produce better results or maybe using a different method to find the shortest path of pixels. My implementation is not necessarily correct, but is merely a version of the algorithm.
