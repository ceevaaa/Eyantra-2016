# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  IMAGE PROCESSING (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task1C
*  Filename: task1-main.py
*  Version: 1.5.0  
*  Date: November 10, 2016
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
##################You are not allowed to add any external library here################## 
import sys
import cv2
import numpy as np
import pickle
from getCellVal import *
########################################################################################
# This file will test your getCellVal.py with different test cases
# To compile the file, on the console type 
# python task1-main.py N
# where N is the total number of images to be read, 7 in your case
# At the end, you will see the results of the test cases verified.
#=============================================================
#					Task1C begins			

#User providing the number of images files to be tested
N_images=int(sys.argv[1])
grid_line_x = 7
grid_line_y = 7
m=600/(grid_line_x-1)
n=600/(grid_line_y-1)
###Stores the numbers detected for all the tested images, maximum images 7 only
grid_map_result = [ [ [0 for i in range(grid_line_y-1)] for j in range(grid_line_x-1) ] for k in range(7) ]

######################Test case verification######################
############Do not edit this part of the code####################
def testCases(grid_map_result):
	grid_map_solution = pickle.load( open( "grid_map_solution.p", "rb" ) )
	error=0
	for l in range(0, N_images):
		print( 'Testing task1_img_',l+1,'.jpg' )
		for i in range(0, grid_line_y-1):
			if(grid_map_solution[l][i]==grid_map_result[l][i]):
				print( "Row ",i+1,"is correct" )
			else:
				print( "Row ",i+1,"is wrong" )
				error=error+1
	if(error>0):
		print( "Test Cases verification completed with ",error,"errors" )
	else:
		print( "Test Cases verification completed successfully. \n You can upload your submissions now" )
######################end of method###############################

#########################Test images are passed here#########################
for k in range(1,N_images+1):
	grid_map = [ [ 0 for i in range(grid_line_y-1) ] for j in range(grid_line_x-1) ]
	imgpath='task1sets/task1_img_'+str(k)+'.jpg'
	img_rgb = cv2.imread(imgpath)
	grid_map=detectCellVal(img_rgb,grid_map)
	#print the grid_map
	print( grid_map )
	grid_map_result[k-1]=grid_map## store it in the 3 dimensional array
	######################your code here###################################
	for i in range(0,6,1):
                cv2.putText(img_rgb, str(grid_map[i][5]), (505, i*100 + 55), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
           
	#print the output of the each expression on the input image, similar to what shown in the output.jpg image
	cv2.imshow('task1_img_'+str(k),img_rgb)
	cv2.imwrite('output/task1_img_'+str(k)+'.jpg',img_rgb)
	cv2.waitKey()
########################Test Cases are verified here, do not edit this code#########################
print( "<--------------Starting Test Cases verification-------------->" )
testCases(grid_map_result)
#=============================================================
# Your task1C ends here
