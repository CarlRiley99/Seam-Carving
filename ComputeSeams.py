import numpy as np

def ComputeSeams(energyMap):
    # Finding the dimensions of a numpy matrix:
    # https://stackoverflow.com/questions/14847457/how-do-i-find-the-length-or-dimensions-size-of-a-numpy-matrix-in-python
    row = energyMap.shape[0]
    col = energyMap.shape[1]

    # IMPORTANT NOTE: If you only do energySums = energyMap, then energySums and energyMap point to the same array!
    # Use np.copy() to copy energyMap array and have it be separate to energySums array
    energySums = np.copy(energyMap)
    energySumsCoords = np.copy(energyMap)
    # Creating an empty array of m x 1 dimensions: https://www.geeksforgeeks.org/numpy-empty-python/
    minimumPath = np.empty([row, 1])

    for i in range(1, row):
        for j in range(0, col):
            # Case for when the pixel is at the first column.
            if (j == 0):
                minValue = min(energySums[i - 1, j:j+2])
                coord = np.argmin(energySums[i - 1, j:j+2])
            # Case for when the pixel is at the last column
            elif (j == col):
                minValue = min(energySums[i - 1, j-1:j+1])
                coord = np.argmin(energySums[i - 1, j-1:j+1])
                coord = coord + (j - 1)
            else:
                minValue = min(energySums[i - 1, j-1:j+2])
                coord = np.argmin(energySums[i - 1, j-1:j+2])
                coord = coord + (j - 1)
            energySums[i, j] = energySums[i, j] + minValue
            # print(energySums)
            # print(minValue, ' ', coord, ' ', i, ' ', j)
            energySumsCoords[i, j] = int(coord)

    minimumPath[row - 1, 0] = min(energySums[row - 1, :])
    coord = int(np.argmin(energySums[row - 1, :]))
    for i in range(row - 2, 0, -1):
        coord = int(energySumsCoords[i + 1, coord])
        minimumPath[i, 0] = energySums[i, coord]

    return energySums, energySumsCoords
