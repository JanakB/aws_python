import numpy as np

# Input parameters

nTrials = int(10E4)

radius = 1

# Counter for thepoints inside the circle

nInside = 0

# Generate points in a square of side 2 units, from -1 to 1. 
XrandCoords = np.random.default_rng().uniform(-1, 1, (nTrials,))
YrandCoords = np.random.default_rng().uniform(-1, 1, (nTrials,))

for i in range(nTrials):

    x = XrandCoords[i]

    y = YrandCoords[i] 
    # Check if the points are inside the circle or not if x2 y2 <= radius**2:
    if x**2+y**2 <= radius**2:
       nInside = nInside + 1

       
area = 4*nInside/nTrials 
print("Value of Pi: ", area)