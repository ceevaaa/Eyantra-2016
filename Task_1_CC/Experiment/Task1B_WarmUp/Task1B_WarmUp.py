import cv2
import numpy as np
grid_line_x = 7
grid_line_y = 7
m=600/(grid_line_x-1)
n=600/(grid_line_y-1)

grid_map = [[0 for j in range(0,grid_line_x-1)]for j in range(0, grid_line_y-1)]
# grid_map is a 2D list to store the values that are read from given image

def assign_grid_map(num_template, num):
    '''
        takes the image template as input and matches it against the given image
    '''

    img = cv2.imread('demo.jpg')
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    result = cv2.matchTemplate(img_gray, num_template, cv2.TM_CCOEFF_NORMED)

    if num == 8 or num == 3:
        threshold = 0.57
    else:
        threshold = 0.52

    locations = np.where(result >= threshold)
    # locations is for storing the locations where templates are matched

    if num == 10:
        h = '-'
        # template[10] corresponds to '-'
    elif num == 11:
        h = '+'
        # template[11] corresponds to '+'
    else:
        h = num
        # template[i] corresponds to a value i except for i=10 and i=11

    for point in zip(*locations[::-1]):
        if point[0] % 100 != 0 or point[1] % 100 != 0:
            continue
            '''
                if either of x or y coordinate of the point is not a multiple of 100
                then the point is not required
            '''
        else:
            if point in zip(*locations[::-1]):
                x = int(point[0]/100)
                y = int(point[1]/100)
                grid_map[y][x] = h
            '''
                if both the x and y coordinates are multiple of 100
                then the template matching is successful and the value is assigned to the corresponding matrix element
                here x is the column number and y is the row number 
            '''

template = [
                cv2.imread('digits/0.jpg', 0), cv2.imread('digits/1.jpg', 0), cv2.imread('digits/2.jpg', 0),
                cv2.imread('digits/3.jpg', 0), cv2.imread('digits/4.jpg', 0), cv2.imread('digits/5.jpg', 0),
                cv2.imread('digits/6.jpg', 0), cv2.imread('digits/7.jpg', 0), cv2.imread('digits/8.jpg', 0),
                cv2.imread('digits/9.jpg', 0), cv2.imread('digits/minus.jpg', 0), cv2.imread('digits/plus.jpg', 0)
            ]
# template is list which stores the provided templates from the digits folder

for i in range(0,len(template)):
    assign_grid_map(template[i],i)
    '''
        every template is passed to the function assign_matrix()
        the number in template[i] corresponds to a value of i
        for example template[1] stores 1.jpg and hence corresponds to a value 1
        but template[10] corresponds to '-'
        and template[11] corresponds to '+' 
    '''

for i in range(0,6):
    print( grid_map[i] )

