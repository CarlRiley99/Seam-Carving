import ComputeSeams as compSeams
import FindEnergyMap as enMap
import numpy as np
import matplotlib.pyplot as plt

def reduceWidth(image, numPixels):
    # Assuming the image is in RGB
    row = image.shape[0]
    col = image.shape[1]

    newCol = col
    newImage = np.copy(image)
    seamPath = np.copy(image)
    redVal = 256

    for z in range(0, numPixels):
        energyMap = enMap.FindEnergyMap(newImage)
        energySums, energySumsCoords = compSeams.ComputeSeams(energyMap)
        #FIXME CHECK THIS LINE OF CODE
        coord = np.argmin(energySums[row, :])
        redVal = redVal - 1

        print(newImage.shape)

        for i in range(row - 1, 0, -1):
            coord = energySumsCoords[i, coord]
            coord = int(coord)
            newImage[i,coord,0] = 0
            newImage[i,coord,1] = 0
            newImage[i,coord,2] = 0

            seamPath[i,coord,0] = redVal
            seamPath[i,coord,1] = 0
            seamPath[i,coord,2] = 0
            for j in range(coord, newCol - 1):
                newImage[i,j,0] = newImage[i,j+1,0]
                newImage[i,j,1] = newImage[i,j+1,1]
                newImage[i,j,2] = newImage[i,j+1,2]
                newImage[i,j+1,0] = 0
                newImage[i,j+1,1] = 0
                newImage[i,j+1,2] = 0

        newCol = newCol - 1
        newImage = newImage[:, 0:newCol, :]

    plt.imshow(seamPath)
    plt.show()

    return newImage