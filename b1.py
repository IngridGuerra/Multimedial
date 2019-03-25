import os
import cv2
import numpy as np
import pandas as pd
from PIL import Image

#Open the image from folder
path = os.chdir('/Users/Ingrid/Documents/UDLAP/6o SEMESTRE/MULTIMEDIAL/ProjectGroup1/B1')
for files in os.getcwd():
    img = cv2.imread('6.jpg',0)

#Applies a little bit of more blur to avoid particular edges
blurred = cv2.medianBlur(img,1)

#Applies the Canny algortihm to detect edges to the blurred image
#The parameters are the input image, the minVal and maxVal refering to the threshold
edges = cv2.Canny(blurred,7,20)

#Let's keep the edged image to compare later
cv2.imwrite('6_b1Edge.png', edges)

rows = edges.shape[0]
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1.05, 30,
                               param1=20, param2=20,
                               minRadius=10, maxRadius=20)

#Create a CSV file to save coordinates data
with open('6_B1coordinates.csv', 'w+') as f:
    f.write('x,y coordinates\n')
    if circles is not None:
        circles = np.uint16(np.around(circles))
        #Draws the circles and its centers
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(edges, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(edges, center, radius, (255, 0, 255), 3)
            cv2.putText(edges, str(i[0])+str(',')+str(i[1]), center, cv2.FONT_HERSHEY_SIMPLEX, 0.4,(255, 255, 255),1)
            f.write(str(center)+'\n')
            print("Coordinates1-6: ",center)

#Display results and save new circled image       
cv2.imshow("detected circles", edges)
cv2.imwrite('6_b1Circles.png', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
