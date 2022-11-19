# -*- coding: utf-8 -*-
"""
This is main code
"""

import cv2
import matplotlib.pyplot as plt
image= cv2.imread('image.jpg')

#shape of image

(h, w, d) =image.shape
#cv2.imshow("image",image)
#cv2.WAITKEY(0)

#to display te image

plt.imshow(image)

#Command to extract pixel value from image
#(B, G, R)=image(600,1000)

#print("R={}, G={}, B={}".format(R, G, B))

#Extracting a 100*200 pixel extracted image
#extracted_region = image[300:500,50:650]
#plt.imshow(extracted_region)

#cv2.imshow("extracted REGION",extracted_region)
#cv2.waitKey(0)

#sketching on a image

output = image.copy()
cv2.rectangle(output,(610,450),(555,400),(0,0,255),5)
cv2.rectangle(output,(250,500),(50,370),(0,0,255),5)
cv2.imshow("rectangle on car", output)
plt.imshow(output)
cv2.waitKey(0)

#TEXT ON IMAGE
#output= image.copy()

cv2.putText(output,"RED SUV",(90,350),
    cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0),3)
cv2.putText(output,"WHITE CAR",(530,375),
    cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0 ), 1 )
cv2.imshow("TEXT",output)
cv2.waitKey(0)

#CODE TO DRAW LANE MARKING

cv2.line(output, (1040, 670), (690, 450), (0, 255, 0), 5)
cv2.line(output, (280, 670), (590, 450), (0, 255, 0), 5)
cv2.imshow("Assignment_rohan", output)

#bgr to rgb conversion
image_rgb=cv2.cvtColor(output,cv2.COLOR_BGRA2RGBA)
plt.imshow(image_rgb)

#Save imaage to local folder
status = cv2.iwrite("D:\Bits Pilani\Sem 2\Advanced Driver Assistance Systems\output.jpg")
print("image saved",status) 
cv2.waitKey(0)