# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task1A
*  Filename: gridWrite.py
*  Version: 1.0.0  
*  Date: October 13, 2016
*  
*  Author: Jayant Solanki, e-Yantra Project, Department of Computer Science
*  and Engineering, Indian Institute of Technology Bombay.
*  
*  Software released under Creative Commons CC BY-NC-SA
*
*  For legal information refer to:
*        http://creativecommons.org/licenses/by-nc-sa/4.0/legalcode 
*     
*
*  This software is made available on an “AS IS WHERE IS BASIS”. 
*  Licensee/end user indemnifies and will keep e-Yantra indemnified from
*  any and all claim(s) that emanate from the use of the Software or 
*  breach of the terms of this agreement.
*  
*  e-Yantra - An MHRD project under National Mission on Education using 
*  ICT(NMEICT)
*
**************************************************************************
"""
# Read the gridImage.jpg and display it.
# Go through the below code, it will write the numeral with and without their signs
# on the gridImage
# At the end, output the resultant image as output.jpg and also save it.
#=============================================================
#					Task1A begins	
import cv2
import numpy as np
# Image size is of 600 by 600 pixels. 
# Total gridlines are 7 veticals lines and 7 Horizontals lines
grid_line_x = 7
grid_line_y = 7
m=600/(grid_line_x-1)
n=600/(grid_line_y-1)
# Read Image
img_rgb = cv2.imread('gridImage.jpg')
x,y=(50,50)
cv2.putText(img_rgb, '5', (x-m/4, y+n/4),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)
x,y=(350,150)
cv2.putText(img_rgb, '4', (x-m/4, y+n/4),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)
x,y=(550,250)
cv2.putText(img_rgb, '-7', (x-m/2, y+n/4),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)
x,y=(550,550)
cv2.putText(img_rgb, '9', (x-m/4, y+n/4),cv2.FONT_HERSHEY_PLAIN, 5, (0, 0, 255), 4)
# Show the image
cv2.imshow('output',img_rgb)
# Write the image
cv2.imwrite('output.jpg',img_rgb)
cv2.waitKey()
cv2.waitKey()
#=============================================================
# Your task1A ends here