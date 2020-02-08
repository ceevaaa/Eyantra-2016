# -*- coding: utf-8 -*-
"""
**************************************************************************
*                  Cross_A_Crater (e-Yantra 2016)
*                  ================================
*  This software is intended to teach image processing concepts
*
*  MODULE: Task2
*  Filename: imgLib.py
*  Version: 1.5.0  
*  Date: November 21, 2016
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

"""
* Team Id : eYRC-CC#4227
* Author List : RUTURAJ R. SHITOLE(TEAM LEADER), ANURAG PANDEY, SHIVA PUNDIR , SUBHAM BHARDWAJ
* Filename: imgLib.py
* Theme: CROSS A CRATER
* Functions:detectCellVal,solveGrid,around,Trace_path,Concurrent,create_grid
* Global Variables:NONE
"""


#Complete the both function mentioned below, and return the desired outputs
#Additionally you may add your own methods here to help both methods mentioned below
###################Do not add any external libraries#######################
import cv2
import numpy as np

# detectCellVal detects the numbers/operatorsm,
# perform respective expression evaluation
# and stores them into the grid_map 
# detectCellVal(img,grid_map)
# Find the number/operators, perform the calculations and store the result into the grid_map
# Return the resultant grid_map
"""
    FUNCTION NAME:detectCellVal

    INPUT: 1)img_gray
           2)grid_map

    OUTPUT:
            grid_map: grid map is the matrix representation of the given image

    LOGIC: we use the image templates provided and try matching it with the given image
            and store the values in corresponding cells of the matrix grid_map

    EXAMPLE CALL: detectCellVal(img_gray,grid_map)
"""
def detectCellVal(img_gray,grid_map):
    #your code here
    templates = cv2.imread('digits/1.jpg') 
    # templates is a variable to store the template which is to be compared in the task image

    # since there are only two numbers in the task image we compare only the image template 1.jpg and assign the corresponding elements of grid_map
    #the rest elements are assigned to zero

    gray_template = cv2.cvtColor(templates, cv2.COLOR_BGR2GRAY) 
    #gray_template is to store the gray image of the given template
    # so that it can be compared in the task image

    result = cv2.matchTemplate(img_gray, gray_template, cv2.TM_CCOEFF_NORMED)
    #result is a numpy.nd array which stores the extent of template matching
    #Expected range : no

    threshold = 0.40 
    #threshold is a value above which the extent of matching is to be considered

    locations = np.where(result >= threshold) 
    #locations is list to store the points where the result is greater than threshold

    for point in zip(*locations[::-1]): 
        #point stores the x and y coordinates of the point where the template is matched
        if point[0] % 50 == 0 and point[1] % 50 == 0: 
            #point[0] is the x coordinate and point[1] is the y coordinate of the matched point
            # we want only those points where the x and y coordinates are multiples of 50
            x = int(point[1] / 50) # x is the row number
            y = int(point[0] / 50) # y is the column number
            grid_map[x][y] = 1 #the corresponding element of grid_map is assigned to '1'
    
    return grid_map
############################################################################################
# solveGrid finds the shortest path,
# between valid grid cell in the start row 
# and valid grid cell in the destination row 
# solveGrid(grid_map)
# Return the route_path and route_length
"""
ALGORITHM OF THE CODE:

THE CODE BELOW IS BASED ON   "CONCURRENT ALGORITHM"
HERE WE CONSIDER ONE STARTING POINT AND ALL THE ENDING POINTS
THEN WE GENERATE A WAVE FROM THE STARTING POINT
THE CELLS AROUND THE STARTING POINT HAVING VALUE '1' ARE CONSIDERED, CALLED AS CHILDREN
THESE CELLS ARE CONSIDERED TO BE PART OF A WAVE AND ARE CALLED SQUARES
NOW THESE SQUARES HAVE THE STARTING POINT AS THEIR PARENT
THEN WE CONSIDER ALL THE SQUARES IN THE WAVES AND FIND THEIR CHILDREN
( HERE ONE CHILD SQUARE CAN  HAVE ONLY ONE PARENT, BUT ONE PARENT SQUARE CAN HAVE MANY CHILDREN SQUARES )
WE KEEP DOING THIS TILL A SQUARE IS ENCOUNTERED WHICH IS A MEMBER OF THE ENDING LINE
WE CALL THIS SQUARE AS END-POINT
THEN WE FIND THE PARENT OF THE END POINT
AFTER THIS WE FIND THE PARENT OF THE PARENT OF THE END POINT
WE KEEP ON DOING THIS TILL THE STARTING POINT IS ENCOUNTERED
THE PATH SO FORMED WILL BE THE SHORTEST PATH
WE THEN CONSIDER ANOTHER STARTING POINT AND FOLLOW THE SAME PROCEDURE
IF ITS PATH LENGTH IS SHORTER THAN PATH LENGTH OF PREVIOUS STARTING POINT WE OVERWRITE THE SHORTEST PATH
"""


'''
    CLASS NAME: Square

    DESCRIPTION OF THE CLASS:
                Each cell belonging to the wave is considered to be a Square
                EVERY SQUARE HAS ONLY ONE PARENT BUT A PARENT SQUARE CAN HAVE MORE THAN ONE CHILDREN SQUARES
                A square has following properties:
                    1)Its own row number (r) which corresponds to the row number of the cell in the matrix which we are considering Square here
                    2)Its own column number (r) which corresponds to the column number of the cell in the matrix which we are considering Square here
                    3)Row number of the parent Square(parent_sq_r)
                    4)Column number of the parent square(parent_sq_c)
                    5)The number of the wave to which it belongs(Wave_num)
                Square is a class to store the above properties of every point on a Wave

            Example for declaration of an object of Square class is given below in the description of __init__

    DATA MEMBERS:   1)row
                    2)col
                    3)parent_sq_row
                    4)parent_sq_col
                    5)Wave_num

    MEMBER FUNCTIONS:

               FUNCTION NAME: __init__

               INPUT:
                   1) self_row: row number of the square
                   2)self_col: column number of the square
                   3) par_row: row number of parent square
                   4) par_col: column number of parent square
                   5) wave_num: corresponding number of the wave to which the square belongs

               OUTPUT : NONE

               LOGIC: __init__ is used to assign the members of the object of square class

               EXAMPLE CALL : This function is called while declaring an object of Square type
                               for example: if A is to be declared as an object of Square class then
                               A = Square(12,1,1,2,3)
    '''


class Square:
    def __init__(self, self_row, self_col, par_row, par_col, wave_num):
            self.row = self_row
            self.col = self_col
            self.parent_sq_row = par_row
            self.parent_sq_col = par_col
            self.Wave_num = wave_num

'''
    CLASS NAME: Wave

    DESCRIPTION:
            Every square in a wave generates children squares, the collection of these children squares is a wave
            Example for declaration of an object of Wave class is given below in the description of __init__

    DATA MEMBERS:
            1)members
            (members is a list to store the member Squares of a give wave)

    MEMBER FUNCTIONS:

                FUNCTION NAME: __init__

                INPUT : NONE(self)

                OUTPUT: NONE

                LOGIC:  members are the children square belonging to the wave
                        __init__ is to assign the members of Wave class

                EXAMPLE CALL : This function gets called when we declare an object of Wave class
                               for example: if A is to be declared as an object of Wave class then
                               A = Wave()

'''

class Wave:
    def __init__(self):
            self.members = []
            # members is a list to stores the Squares which belong to the a given wave

'''
            FUNCTION NAME: around

            INPUT:
                1) row: row number of a given cell of grid_map_2
                2) col: column number of a given cell of grid_map_2
                3) visited: a list to store all the visited cells

            OUTPUT: len(Available_ones): length of the list Available_ones
                    Available_ones:Available_ones is a list which stores index of the neighbouring cells
                    having value '1' around the given cell grid_map_2[r][c]  and were not visited earlier


            LOGIC: A given cell has 8 cells around it, some of these cells are having value '1' and some have value '0'
                   We consider those cells which have value '1' and were not visited earlier and store their index in a list 'Available_ones'


            EXAMPLE CALL : if 1 and 2 are respectively the row and column number of a given cell
                            and n is the number to stores the number of cell having value '1'
                            and m is to store the coordiates of these cells then
                            n,m = around(1,2)
'''

def around(row, col, visited, grid_map_2):
    
    Available_ones = []  
    # Available_ones is a list which stores the coordinates of the available cells having value '1' around the given cell grid_map_2[r][c]  and were not visited earlier
    # in the loop below we consider all the cells around the given cell and if a considered cell is not in visited and has value '1' then we store index in Available_ones
    # and we also append that cell in visited
    # Range of expected number elements in Available_ones : 0 to 7
    
    # two loops to access the cells around a given cell grid_map_2[row][col]
    for a in range(0, 3, 1):
        for b in range(0, 3, 1):
            if not (a == 1 and b == 1):
                cell_visited = False
                # cell_visited is for knowing that the cell under consideration is visited or not, if it is isited then flag is '1' , otherwise '0'
                # Expected values True(if visited) and False(if not visited)

                # loop to access each element of visited
                for i in range(0, len(visited), 1):
                    # checking if the given row and column are in visited, if true then we assign flag to '1'
                    if (row + a - 1, col + b - 1) == visited[i]:
                        cell_visited = True

                if cell_visited is False:
                    if grid_map_2[row + a][col + b] == 1:
                        # if the row and column both are not in visited then we append it to the list Available_ones
                        Available_ones.append((row + a - 1, col + b - 1))
                        # if the row and column both are not in visited then we append it to the list visited
                        visited.append((row + a - 1, col + b - 1))

    return len(Available_ones), Available_ones

'''
            FUNCTION NAME: Trace_path

            INPUT:
                1) Waves: the list waves which stores the waves generated
                2) Wave_num: the number of the wave to which the Sqaure(defined above) belongs
                3) par_row: row number of parent Square
                4) par_col: column number of parent Square
                5) Shortest_path: the shortest path to be found

            OUTPUT:
                :return: NONE

            LOGIC: In Trace_path function we consider the end point which is reached on the ending line and find its parent Square and append its index to shortest path
                    Then we consider the parent Square and find its parent
                    We keep doing this until we reach the starting point

            EXAMPLE CALL : if the number of the wave is 4, row number of parent square is 4, column number of parent Square is 3 then,
                            Trace_path(Waves,4,4,3)
'''


def Trace_path(Waves, Wave_num, par_row, par_col, Shortest_path):
        # We run the loop from the last wave till the first wave is encountered
        while Wave_num > 0:
            # we append the index of parent Square in Shortest_path
            Shortest_path.append((par_col+1, par_row+1))
            # here we consider wave which was generated before the wave we are considering now
            for i in range(0, len(Waves[Wave_num - 1].members)):
                # the parent of the square under consideration belong to this wave
                # we find the parent Square and replace it with the parent Square of the parent Square under consideration
                if Waves[Wave_num - 1].members[i].row == par_row and Waves[Wave_num - 1].members[i].col == par_col:
                    par_row = Waves[Wave_num - 1].members[i].parent_sq_row
                    par_col = Waves[Wave_num - 1].members[i].parent_sq_col
            Wave_num -= 1

'''
            FUNCTION NAME: Concurrent()

            INPUT:
                    1) Wave_num: The serial number of the wave in which we are Working
                    2) starting_point: Column number of starting point
                    ( NOTE: we don't require row number of starting point as it is fixed and is equal to 13)
                    3) grid_map_2: grid_map wrapped with zeros(see code above)
                    4) Waves:a list to store the waves thus formed
                    5) visited:a list to store teh visited points
                    6) Shortest_path:a list to store the shortest path

            OUTPUT:
                    :return: Shortest_path: is the shortest path found for a given starting point

            LOGIC:  Self calling funtion to create a box from previous box.
     	            This requires data which is provided by around function.
        	        Initiation also happens within this funtion(for starting point).
    		        The moment when any square of a box reaches the top trace_path is called
                    and all the necessary stePs have been taken to break from this finction
    		        after we are done with tracing it back.
                   The self calling ALSO breaks when there is no change in no of visited
    		        points that means no possible path then it doesnot calls trace_path

            EXAMPLE CALL:
                    if wave_num is 4, starting_point is 3
                    and "path" is the path o be found
                    then,
                        path = Concurrent(4,3,grid_map_2,Waves,visited,Shortest_path)




'''


def Concurrent(Wave_num, starting_point, grid_map_2, Waves, visited, Shortest_path):

        Low_row = 13
        # A wave consists of Squares, these Squares have their own row and column number
        # Low_row is the minimum value of row number of a Square in a given wave
        # Low_row is 0 for the starting wave
        # We keep checking Low_row for each wave we form
        # Range of expected values: Low row decreases form 13(Starting line) to 0(Ending line)

        # if wave number is zero then we append starting point to visited

        Num_visited = len(visited)
        # Num_visited is the number of visited cells till now
        # Range of expected values: 0 to 80

        Destination_line_encountered = False
        # Destination_line_encountered  is a boolean variable to check if the destination line is encountered or not
        # Range of expected values: True(if destination line is encountered) and False(if destination line is not encountered yet)

        # If the wave_num i.e. the number of waves is '0' then we are on the Starting point(Starting_square)
        # We consider the starting point itself as a wave (Starting_Wave)
        # and append the Starting Wave in the list Waves
        if Wave_num == 0:
            st_point = [13, starting_point]
            visited.append(st_point)
            # Starting_square will have row number =13, col number = starting_point,
            # row number of parent as 0, col number of parent as 0 and wave number 0
            Starting_square = Square(13, starting_point, 0, 0, 0)

            Starting_Wave = Wave()
            # Starting_Wave is the first wave formed

            # Starting wave has Starting_square as its member
            Starting_Wave.members.append(Starting_square)
            # We append the Starting Wave to Waves
            Waves.append(Starting_Wave)

        Next_Wave = Wave()
        # Next_Wave is the next wave which we are going to form

        # we loop through all the members in the present wave
        # the members will be having children we take these children and form another wave
        Num_visited_present = len(visited)
        for i in range(0, len(Waves[Wave_num].members), 1):
            Num_neighbouring_ones, Neighbouring_ones = around(Waves[Wave_num].members[i].row,
                                                              Waves[Wave_num].members[i].col, visited, grid_map_2)
            # Num_neighbouring_ones is the number of cells around the given cell which have value '1'
            # Neighbouring_ones is the list containing coordinates of those cells

            Num_visited_present = len(visited)
            # Num_visited_present is the present number of visited cells

            # We now loop through all the members of the Neighbouring_ones and find their children
            for j in range(0, Num_neighbouring_ones):
                Member_Square = Square(Neighbouring_ones[j][0], Neighbouring_ones[j][1], Waves[Wave_num].members[i].row,
                                       Waves[Wave_num].members[i].col, i)
                # Member_Square is a variable to store the properties of the Square

                # We check if the Number of neighbouring ones is greater than 0 or not i.e. we check if there are any neighbours present
                if Num_neighbouring_ones > 0:
                    # if present then we append the Member_Square to Next Wave
                    Next_Wave.members.append(Member_Square)

                    # We now check if the Row number of any of the Neighbouring_ones is less than Low_row
                    if Low_row > Neighbouring_ones[j][0]:
                        # if true then we overwrite Low_row with column number of Neighbouring_ones[j]
                        Low_row = Neighbouring_ones[j][0]

                    # we check if Low_row is 0 i.e. the destination line is encountered or not
                    if Low_row == 0:
                        # if true then We have reached the destination line
                        # we then call trace back function to find the shortest path
                        Waves.append(Next_Wave)
                        Shortest_path.append((Neighbouring_ones[j][1]+1, Neighbouring_ones[j][0]+1))
                        Trace_path(Waves, Wave_num + 1, Waves[Wave_num].members[i].row, Waves[Wave_num].members[i].col,
                                   Shortest_path)
                        Destination_line_encountered = True
                        break

            #if at any point of execution the destination line was encountered we break out of the loop
            if Destination_line_encountered is True:
                break

        Waves.append(Next_Wave)

        # if the destination line is not reached then we form another wave
        if Num_visited != Num_visited_present and Destination_line_encountered is not True:
            Wave_num += 1
            if Low_row > 0:
                Concurrent(Wave_num, starting_point, grid_map_2, Waves, visited, Shortest_path)

        return Shortest_path

"""
    FUNCTION NAME: create_grid

    INPUT:
            1) starting_point: column number of starting point
            2) grid_map:

    OUTPUT:
            :return:
                    grid:a 16*16 matrix which is formed by adding two rows ,one at top and other at bottom of grid_map
                        and adding two columns one on left and other on right of grid_map
                        we set all te elements in the starting line of the grid to be zero except the starting point
                        all the elements of the added rows/columns are zero
                        grid is basically grid_map wrapped with zeros
                        an element row,col of grid_map will be row+1,col+1 of grid

    LOGIC:  Each element row,col of grid_map will be row+1, col+1 of grid

    EXAMPLE CALL :
                if starting point is 5 then,
                grid_map_2 = create_grid(5,grid_map)


"""


def create_grid(starting_point, grid_map):
        # Declaring grid
        grid = [[0 for i in range(0, 16)] for j in range(0, 16)]

        # loop to assign elements of grid
        for i in range(0, 14):
            for j in range(0, 14):
                if grid_map[i][j] == 1:
                    grid[i + 1][j + 1] = 1
                if i == 13:
                    grid[i + 1][j + 1] = 0

        #we now assign the cell of the starting point as 1
        grid[14][starting_point + 1] = 1
        return grid


"""
    FUNCTION NAME: solveGrid()

    INPUT: grid_map

    OUTPUT:
        1)route_path
        2)route_length

    LOGIC:
            We take one starting point and make other starting points zero
            Then we call the concurrent function for that point and find the shortest path
            and store it in present_path
            and compare length of present path with route_path if length of route_path is greater
            then we overwrite route_path with present_path
            we apply the same procedure for all the 1's in starting line

    EXAMPLE CALL:
            solveGrid(grid_map)

"""
def solveGrid(grid_map):
    starting_points = []
    #starting_points is an array to store the column number of the available starting points
    route_length = 196
    #we have set route_length to a default value so that we can compare it later
    route_path = []
    #route_path is the shortest path found for a particular test image
    present_path = []
    #present_path is a list to store the hortest path for a particulaar starting point

    #we now use a loop to fing the column number of the available starting points and append that in the list starting_points
    for i in range(0, 14):
        if grid_map[13][i] == 1:
            starting_points.append(i)

    for i in range(0, len(starting_points)):
        grid_map_2 = create_grid(starting_points[i], grid_map)
        # a matrix which contains 2 more rows and 2 more columns than grid_map
        # Each element row,col of grid_map will be row+1,col+1 of grid_map_2
        #grid_map_2 is basically grid_map wrapped with zeros around it
        Waves = []  # Waves is a list to store the waves formed during the execution of the program
        visited = []    # a list to stores the coordinates of visited squares

        #we now apply the Concurrent algorithm foe a given starting point
        present_path = Concurrent(0, starting_points[i], grid_map_2,Waves,visited,present_path)

        #if a path was found we compare it with route_path and if the found fath was shorter we overwrite route_path with present_path
        if len(present_path) > 0:

            if (len(present_path) < route_length):
                route_path = present_path
                route_length = len(present_path)
                #14 is the least possible path length
                #so if path length is 14 then we break out of the loop
                if len(route_path) == 14:
                    break

    #the found path was reverse of the path we want
    #so we obtain the required path by reversing route_path
    route_path.reverse()

    #we now return route_path and route_length
    if len(route_path) != 0:
        return route_path, route_length-1
    else:
        #if no path possible
        return route_path, len(route_path)




############################################################################################
