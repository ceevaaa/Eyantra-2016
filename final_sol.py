"""
* Team Id : eYRC-CC#4227
* Author List : Ruturaj Ramchandra Shitole, Anurag Pandey, Shiva Pundir
* Filename: Final_3.py
* Theme: Cross A Crater
* Functions: choose_bridge(),find_sum(),pick_up_path(),Boulder_pick(),Bridge_1_cross(),go_back()
            come_again(),Bridge_2_cross(), rev_bridge(), ch_bridge(), find_shortest(), come_again()
             go_back(), solver(), send_data()
* Global Variables: SUM, ser, path
"""

import cv2
import numpy as np
import serial
import sys

SUM = int(sys.argv[1])
ser = serial.Serial('COM5', 9600)


def choose_bridge():
    '''
    Function Name: choose_bridge()
    Input : None
    Output: Bridge_1_, Bridge_2_, bridge, r
    Logic :
    Example Call : B = choose_bridge()
    '''
    flag = 1  # black
    upper_row = 0
    lower_row = 0
    left_col = 0
    right_col = 0
    lsi = []
    obs = []
    cav_1 = []
    cav_2 = []
    num_sorted = []
    num_pickups = 0
    some = SUM
    bridge = 1
    grid_1 = [1 for i in range(0, 7)]
    grid_2 = [[1 for i in range(0, 7)] for j in range(0, 2)]
    img = cv2.imread("Arena/capture_39.jpg")
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = [cv2.imread("templates/0.jpg", 0), cv2.imread("templates/1.jpg", 0),
                cv2.imread("templates/2.jpg", 0), cv2.imread("templates/3.jpg", 0),
                cv2.imread("templates/4.jpg", 0), cv2.imread("templates/5.jpg", 0),
                cv2.imread("templates/6.jpg", 0), cv2.imread("templates/7.jpg", 0),
                cv2.imread("templates/8.jpg", 0), cv2.imread("templates/9.jpg", 0)]
    # Reading Templates from 0 to 9
    temp = [cv2.imread("templates/cavity.jpg", 0), cv2.imread("templates/obstacle.jpg", 0)]
    # Reading templates for cavity and obstacle
    # Croping the region inside of black borders
    # for cropping the region we first calculate the
    for i in range(0, len(img_gray)):
        summ = 0
        for j in range(0, len(img_gray[1])):
            summ += img_gray[i][j]
        avg = summ / 640
        if flag == 0 and avg >= 100:
            upper_row = i
            break
        if avg < 100:
            flag = 0
        else:
            flag = 1
    flag = 1
    for i in range(len(img_gray) - 1, -1, -1):
        summ = 0
        for j in range(0, len(img_gray[1])):
            summ += img_gray[i][j]
        avg = summ / 640
        if flag == 0 and avg >= 100:
            lower_row = i
            break
        if avg < 100:
            flag = 0
        else:
            flag = 1
    flag = 1
    for i in range(0, len(img_gray[1])):
        summ = 0
        for j in range(0, len(img_gray)):
            summ += img_gray[j][i]
        avg = summ / 640
        if flag == 0 and avg >= 100:
            left_col = i
            break
        if avg < 100:
            flag = 0
        else:
            flag = 1
    flag = 1
    for i in range(len(img_gray[1]) - 1, 0, -1):
        summ = 0
        for j in range(0, len(img_gray)):
            summ += img_gray[j][i]
        avg = summ / 640
        if flag == 0 and avg >= 100:
            right_col = i
            break
        if avg < 100:
            flag = 0
        else:
            flag = 1
    img2 = img[upper_row:lower_row, left_col:right_col]
    b1 = img2[0:(30 * len(img2) / 92), (25 * len(img[1]) / 160):(95 * len(img2[1]) / 160)]
    b2 = img2[(52 * len(img2) / 92):(len(img2) - 1), (25 * len(img[1]) / 160):(95 * len(img2[1]) / 160)]
    big = img2[0:(len(img2) - 1), (95 * len(img2[1]) / 160):(len(img2[1]) - 1)]
    b1_gray = cv2.cvtColor(b1, cv2.COLOR_BGR2GRAY)
    b2_gray = cv2.cvtColor(b2, cv2.COLOR_BGR2GRAY)
    big_gray = cv2.cvtColor(big, cv2.COLOR_BGR2GRAY)

    # DETECTING THE NOS ON THE TOP OF BOULDERS.
    for q in range(0, len(template), 1):
        res = cv2.matchTemplate(big_gray, template[q], cv2.TM_CCOEFF_NORMED)
        threshold = 0.80
        i = 0
        x = []
        y = []
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            flag = 0
            for i in range(0, len(x)):
                if (pt[0] > (x[i] - 20)) and (pt[0] < (x[i] + 20)):
                    flag = -1
            for i in range(0, len(y)):
                if (pt[1] > (y[i] - 30)) and (pt[1] < (y[i] + 30)):
                    if flag == -1:
                        flag = 1
            if not flag == 1:
                x.append(pt[0])
                y.append(pt[1])
                lsi.append([q, pt[0], pt[1]])

    # COLLECTING DATA OF BRIDGE 2
    for w in range(0, len(temp), 1):
        res = cv2.matchTemplate(b2_gray, temp[w], cv2.TM_CCOEFF_NORMED)
        threshold = 0.80
        i = 0
        x = []
        y = []
        loc = np.where(res >= threshold)
        for pt in zip(*loc[::-1]):
            flag = 0
            for i in range(0, len(x)):
                if (pt[0] > (x[i] - 40)) and (pt[0] < (x[i] + 40)):
                    flag = -1
            for i in range(0, len(y)):
                if (pt[1] > (y[i] - 40)) and (pt[1] < (y[i] + 40)):
                    if flag == -1:
                        flag = 1
            if not flag == 1:
                x.append(pt[0])
                y.append(pt[1])
                #    print pt[0],pt[1]
                if w == 1:
                    obs.append([pt[0], pt[1]])
                if w == 0:
                    cav_2.append([pt[0], pt[1]])

    # COLLECTING DATA OF BRIDGE 1
    res = cv2.matchTemplate(b1_gray, temp[0], cv2.TM_CCOEFF_NORMED)
    threshold = 0.80
    x = []
    y = []
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        flag = 0
        for i in range(0, len(x)):
            if (pt[0] > (x[i] - 40)) and (pt[0] < (x[i] + 40)):
                flag = -1
        for i in range(0, len(y)):
            if (pt[1] > (y[i] - 40)) and (pt[1] < (y[i] + 40)):
                if flag == -1:
                    flag = 1
        if not flag == 1:
            x.append(pt[0])
            y.append(pt[1])
            cav_1.append([pt[0], pt[1]])

    # CHOOSING THE BRIDGE
    if (len(cav_2) * 2 + len(obs)) > (len(cav_1) * 2 + 1):
        bridge = 2

    lsi.sort(key=lambda x: (x[1] + x[2]))
    for i in range(0, 1):
        temp = lsi[1]
        lsi[1] = lsi[2]
        lsi[2] = temp

    # CREATING THE ARRAY CONTAINING NOS ON THE BOULDER
    for i in range(0, len(lsi)):
        num_sorted.append(lsi[i][0])

    ra1 = len(b1[1]) / 7
    ra20 = len(b2[1]) / 7
    ra21 = len(b2) / 2

    # CREATING REPRESENTATION OF BRIDGE 1
    for i in range(0, len(cav_1)):
        x = (int)(((cav_1[i][0] + 20) / ra1))
        grid_1[x] = 'c'

    # CREATING REPRESENTATION OF BRIDGE 1
    for i in range(0, len(cav_2)):
        x = (int)(((cav_2[i][0] + 20) / ra20))
        y = 1
        if (obs[i][1] + 20) < ra21:
            y = 0
        grid_2[y][x] = 'c'
    for i in range(0, len(obs)):
        x = (int)(((obs[i][0] + 20) / ra20))
        y = 1
        if (obs[i][1] + 20) < ra21:
            y = 0
        grid_2[y][x] = 'o'

    if bridge == 1:
        num_pickups = len(cav_1)
    if bridge == 2:
        num_pickups = len(cav_2)

    def find_sum(list_num, summ):
        data = []
        flag = 0
        for i in range(0, 4):
            if list_num[i] == summ:
                data.append([1, i])
                break

        for i in range(0, 3):
            for j in range(i + 1, 4):
                if list_num[i] + list_num[j] == summ:
                    data.append([2, i, j])
                    flag = 1
                    break
            if flag == 1:
                break

        for i in range(3, (-1), -1):
            if list_num[0] + list_num[1] + list_num[2] + list_num[3] - list_num[i] == summ:
                data.append([3, i])
                break
        for i in range(0, 1):
            if list_num[0] + list_num[1] + list_num[2] + list_num[3] == summ:
                data.append([4])
        return data

    data_cone = find_sum(num_sorted, some)

    def pick_up_path(num, data):
        paths = []

        for i in range(0, len(data)):
            if data[i][0] == num:

                if data[i][0] == 1:
                    paths.append(data[i][1])
                    return paths
                if data[i][0] == 2:
                    paths.extend((data[i][1], data[i][2]))
                    return paths
                if data[i][0] == 3:
                    temp = []
                    for j in range(0, 4):
                        if not j == data[i][1]:
                            temp.append(j)
                    paths.extend(temp)
                    return paths
                if data[i][0] == 4:
                    paths.extend((0, 1, 2, 3))
                    return paths
                break
        return paths

    r = pick_up_path(num_pickups, data_cone)
    if len(r) == 0:
        if bridge == 1:
            bridge = 2
            num_pickups = len(cav_2)
            r = pick_up_path(num_pickups, data_cone)
        elif bridge == 2:
            bridge = 1
            num_pickups = len(cav_1)
            r = pick_up_path(num_pickups, data_cone)

    Bridge_2_ = [[0 for i in range(0, 2, 1)] for j in range(0, 7, 1)]
    for i in range(0, 7, 1):
        Bridge_2_[i][0] = grid_2[0][i]
        Bridge_2_[i][1] = grid_2[1][i]

    Bridge_1_ = grid_1
    Bridge_1_.reverse()
    print num_sorted
    num_on_boulders = []
    for i in range(0, len(r),1):
        NUM = str(num_sorted[r[i]])
        num_on_boulders.append(NUM)
    # num_on_boulders.reverse()
    return Bridge_1_, Bridge_2_, bridge, r, num_on_boulders


def Boulder_pick(Boulder_num):
    '''
    Function Name : Boulder_pick(a)
    Input : Boulder_num
    Output : It returns the command to pick the bouder number
            (C for Boulder 0
            G for Boulder 1
            K for Boulder 2
            J for Boulder 3)
    Logic : We take the Boulder_num as the input and return the corresponding command for the robot
    Example call : Boulder_pick(0)
                    [ this will return the value 'C' as 'C' corresponds
                      to the command to pick the boulder number 0]
    '''
    if Boulder_num == 0:
        return 'C'
    elif Boulder_num == 1:
        return 'G'
    elif Boulder_num == 2:
        return 'K'
    elif Boulder_num == 3:
        return 'J'


def Bridge_1_cross(Bridge_one, Boulders_to_be_picked, No_on_boulders):
    '''
    Function Name: Bridge_1_cross()
    Input : Bridge_one, Boulders_to_be_picked
    Output: route [ which is the rote to be followed by the robot ]
    Logic : We take the data of bridge 1 and the boulders to be picked, we consider the next row and store the moves
            according to that
    Example Call : B = Bridge_2_cross(Bridge1, Boulders)

    '''
    No_of_Boulders = len(Boulders_to_be_picked)
    # A variable to store the n
    # umber of boulders to be picked
    print Boulders_to_be_picked
    def go_back(row):
        '''
        Function Name: go_back()
        Input: row
        Output: path
        Logic: we take the row number on which the robot is present facing backwards from this row we take the robot to
                the zeroth row
        Example Call: C = go_back(2)
        '''
        row_num = row
        # we assign the row to a variable row_num

        back_path = []
        # back_path is a variable to store the path for the robot to move
        while row_num != 0:
            back_path.append('w')
            # 'w' is a command to go straight
            #  here we keep on subtracting 1 from row_num till it becomes zero
            #  [ i.e. till the robot reaches the starting point ]
            row_num -= 1
        # we now return the path for the robot to go back
        return back_path

    def come_again(row):
        '''
        Function Name: come_again()
        Input: row()
        Output: come_again_path
        Logic: From the zeroth row we make te rbot come forward to one row ahead of where it was before going back
                for this we append 'w' to the come_again_path till we reach the required row
        Example Call: D = come_again(3)
        '''
        row_num = row + 1
        # we assign row+1 to row_num as we have to reach one row ahead of what we were initially
        come_again_path = []
        # come_again_path is a list to store the moves for the robot to come again to initial point
        while row_num != 0:
            come_again_path.append('w')
            # 'w' is a command to go straight
            row_num -= 1
        # we now return the come_again_path
        return come_again_path

    route = []
    # route is a list to store the path for the robot to cross bridge 1

    route.append(Boulder_pick(Boulders_to_be_picked[len(Boulders_to_be_picked) - 1]))
    # we append the last element of the list Boulders_to_be picked to route so that firstly the robot picks a boulder
    # and then goes to the bridge

    #  a loop to loop to loop through all the rows of the bridge and store the corresponding moves in the lit route
    for i in range(0, 7, 1):
        if i < 6:
            Next = Bridge_one[i]
            # Next is a variable to store the value of the Next row of the row which we are currently on
            if Next == 1:
                route.append('w')
            #     if the next row is available to move then we move forward
            elif Next == 'c':
                # i.e. if the next row contains a cavity
                route.append('r')
                # 'r' is for straight drop
                No_of_Boulders -= 1

                # if the No_of_Boulders to be picked is 0 [ i.e. there is no boulder left to be picked ]
                if No_of_Boulders != 0:
                    # if the No_of_Boulders to be picked is not zero
                    route.append('b')
                    # turn the robot 180 degree

                    route.extend(go_back(i - 1))
                    # we extend the path to go back for the robot to route

                    route.extend(Boulder_pick(Boulders_to_be_picked[No_of_Boulders - 1]))
                    # we extend the command for the robot to pick the required Boulder

                    route.extend(come_again(i))
                    # we extend the come again path to route

        elif i == 6:
            route.append('w')
    route.extend(No_on_boulders)
    route.extend(str(len(No_on_boulders)))
    route.extend('1')
    return route


def Bridge_2_cross(bridge_two, Boulders_to_be_picked, No_on_Boulders):
    '''
    MOVES:
            w = go straight
            q = turn left,diagonal
            e = turn right, diagonal
            b = turn 180 degree
            l = diagonal drop
            r = straight drop
            n = align left
            m = align right
            W = diagonal straight
            c = cavity
            o = obstacle
    '''


    print Boulders_to_be_picked

    Bridge2 = [[0 for i in range(0, 2, 1)] for j in range(0, 7, 1)]
    Bridge_rev = [[0 for i in range(0, 2, 1)] for j in range(0, 7, 1)]


    def rev_bridge(Bridge):
        '''
        Function Name: rev_bridge()
        Input: Bridge
        Output: Bridge_rev
        Logic: First we set all the 'c' [ which stands for cavity ] in the input Bridge to 1
                then we reverse the bridge in such a way that the Bridge_rev formed as observed from the the end of the
                arena
        Example Call: Y = rev_bridge(Bridge1)
        '''

        # we loop through all the elements of the bridge and if there is a cavity present then we make it 1
        for i in range(0, len(Bridge), 1):
            for j in range(0, 2, 1):
                if Bridge[i][j] == 'c':
                    Bridge_rev[i][j] = 1
                else:
                    Bridge_rev[i][j] = Bridge[i][j]
        # we now reverse the bridge in such a way that the Bridge_rev is the view of the Bridge2 as seen
        # from the other end
        for j in range(0, len(Bridge_rev) / 2, 1):
            row_bridge = Bridge_rev[j]
            Bridge_rev[j] = Bridge_rev[len(Bridge_rev) - 1 - j]
            Bridge_rev[len(Bridge_rev) - 1 - j] = row_bridge

        return Bridge_rev

    def ch_bridge(Bridge):
        '''
        Function Name: ch_bridge()
        Input: Bridge
        Output: None
        Logic: We loop through all the elements of the Bridge 2 and set all the 'c' to 1
        Example Call: ch_bridge(Bridge1)
        '''
        for i in range(0, len(Bridge), 1):
            for j in range(0, 2, 1):
                if Bridge[i][j] == 'c':
                    Bridge2[i][j] = 1
                else:
                    Bridge2[i][j] = Bridge[i][j]

    def find_shortest(Bridge, path, col, row_end, row_start, No_of_Boulders):
        '''
        Function Name: find_shortest()
        Input: Bridge, path, col, row_end, sow_start, No_of_Boulders
        Output: path [ i.e. the path to be followed by the robot]
        Logic: This function returns the path for the robot from one row to another
                we take the start row, the end row and the column as the input
                and then analyze the next row every time and accordingly store the moves for the robot to
                cross the bridge
        Example Call: ideal_route = find_shortest(Bridge2, ideal_rt, 0, row_end = row_end + 1,
                                                    row_start = row_start, No_of_Boulders=0)

        '''

        # a for loop to loop from start row to the end row
        for i in range(row_start, row_end - 1, 1):
            Now = Bridge[i]
            # Now stores the value of the row on which the robot is present

            Next = Bridge[i + 1]
            # Next stores the value of the row next to the current row

            if i == 0:

                # if the zeroth row has both its elements as 1 then we have set 'n' as the default value for the robot
                # to move
                if Now[0] == 1 and Now[1] == 1:
                    path.append('n')  # allign left
                    col = 0


                elif Now[0] == 'o':
                    # i.e. if the zeroth col of the zeroth row has an obstacle
                    path.append('m') # align right
                    col = 1 # change the column to 1

                elif Now[1] == 'o':
                    # i.e. if the first row of the zeroth row contains an obstacle
                    path.append('n') # allig right
                    col = 0 # change the column to 1

                # elif Now[0] == 'c':
                #     path.append('m')  # allign right
                #     path.append('a')  # left
                #     path.append('r')  # straight drop
                #     path.append('d')
                #     No_of_Boulders -= 1
                #     if No_of_Boulders != 0:
                #         path.append('b')
                #         bck = go_back(6 - i, 7, col)
                #         again = come_again(i + 1, 0)
                #         # for c in range(0, len(bck), 1):
                #         #     path.append(bck[c])
                #         # for u in range(0, len(again), 1):
                #         #     path.append(again[u])
                #         # go_back_and_come(len(path)-1)
                #         path.extend(bck)
                #         path.extend(Boulder_pick(Boulders_to_be_picked[No_of_Boulders - 1]))
                #         path.extend(again)
                #
                #     col = 1
                #     Bridge[0] = 1
                #
                # elif Now[1] == 'c':
                #
                #     path.append('n')  # allign left
                #     path.append('d')  # right
                #     path.append('r')  # straight drop
                #     path.append('a')
                #     col = 0
                #     Bridge[1] = 1
                #
                #     # print "after: " + "i= " + str(i) + "  col= " + str(col)

            if Next[0] == 1:
                # if the zeroth col of the Next row is 1

                if Next[1] == 1:
                    # if the first column is also 1
                    path.append('w')  # go straight, col remains same

                elif Next[1] == 'o':
                    # i.e. if the Next row is [1,'o']

                    if col == 0:
                        # if the col is zero the the robot can go straight
                        path.append('w')

                    elif col == 1:
                        # if the col is 1 then the robot has to first travel diagonally left
                        path.append('q')
                        path.append('W')
                        path.append('e')
                        col = 0

                elif Next[1] == 'c':
                    # i.e. Next row is [1, 'c']

                    if col == 1:
                        # if the col 1 of the Next row is a cavity
                        #  and the robot is also present on first col
                        path.append('r') #straight drop

                        No_of_Boulders -= 1
                        # we subtract 1 from the number of boulders

                        if No_of_Boulders != 0:
                            # if the Number of boulders to be picked is not equal to zero then we go back and pick the
                            # required boulder
                            path.append('b')
                            #  to turn the robot 180 degrees

                            bck = go_back(6 - i, 7, col)
                            # to store the path for the robot to travel to row zero

                            again = come_again(i + 1, 0)
                            # to store the path or the robot to travel from the row zero to the initial row

                            path.extend(bck)
                            # to add the path for the robot to travel back to row zero

                            path.extend(Boulder_pick(Boulders_to_be_picked[No_of_Boulders - 1]))
                            # to add the Boulder Number to picked

                            path.extend(again)
                            # to add the path for the robot to travel from the zeroth

                        if No_of_Boulders == 0:
                            # if the number of boulders left to pick is zero then we simply go straight
                            path.append('w')


                    elif col == 0:
                        # i.e. if the the robot is present on the zeroth column and the cavity is on the first column
                        path.append('e')
                        # to turn left diagonally
                        path.append('l')
                        # to drop diagonally
                        path.append('q')
                        # to turn right diagonally

                        No_of_Boulders -= 1
                        # subtract 1 from No_of_Boulders

                        if No_of_Boulders != 0:
                            # if the No_of_Boulder is Not equal to zero
                            #  [ i.e. there are still boulders left to pick

                            path.append('b')
                            # turn 180 degree

                            bck = go_back(6 - i, 7, col)
                            # Go back to the zeroth row

                            again = come_again(i + 1, 0)
                            # Come again to the initial row

                            path.extend(bck)
                            # Go to the starting point

                            path.extend(Boulder_pick(Boulders_to_be_picked[No_of_Boulders - 1]))
                            # Pick the required boulder

                            path.extend(again)
                            # Come back to the starting point

                        if No_of_Boulders == 0:
                            # if the number of boulders left to pick is zero then don't go back

                            path.append('e')
                            # turn right diagonally

                            path.append('W')
                            #  go straight diagonally

                            path.append('q')
                            #   turn left diagonally

                    Bridge[i + 1][1] = 1
                    # after putting the boulder the 'c' on the Bridge becomes 1

            elif Next[0] == 'o':
                #  if the zeroth column of the next row contains an obstacle

                if Next[1] == 'c':
                    # if the first column of the next row contains a cavity
                    # i.e. the next row is ['o','c']

                    if col == 0:
                        #  if the robot is on zeroth column

                        path.append('e')
                        # turn right diagonally

                        path.append('l')
                        # diagonal drop

                        path.append('q')
                        # turn left diagonally

                        No_of_Boulders -= 1

                        if No_of_Boulders != 0:
                            path.append('b')
                            # turn 180 degrees

                            bck = go_back(6 - i, 7, col)
                            # go back to the starting row

                            again = come_again(i + 1, 0)
                            # come back to the initial row

                            path.extend(bck)
                            path.extend(Boulder_pick(Boulders_to_be_picked[No_of_Boulders - 1]))
                            path.extend(again)

                        if No_of_Boulders == 0:
                            path.append('e')
                            #  turn right diagonally
                            path.append('W')
                            # go straighy diagonally

                            path.append('q')
                            # turn left diagonally

                        col = 1

                    elif col == 1:
                        path.append('r')
                        # straight drop

                        No_of_Boulders -= 1
                        if No_of_Boulders != 0:

                            path.append('b')
                            # turn 180 degrees

                            bck = go_back(6 - i, 7, col)
                            # go back to the zeroth row

                            again = come_again(i + 1, 0)
                            # come back to the initial row

                            path.extend(bck)
                            path.extend(Boulder_pick(Boulders_to_be_picked[No_of_Boulders - 1]))
                            path.extend(again)

                        if No_of_Boulders == 0:
                            path.append('w')
                            # go straight as no boulder left to pick

                    Bridge[i + 1][1] = 1

                elif Next[1] == 1:
                    # i.e. the next row is ['o',1]

                    if col == 0:

                        path.append('e')
                        # turn right diagonally

                        path.append('W')
                        # go straight diagonally

                        path.append('q')
                        # turn left diagonally

                        col = 1

                    elif col == 1:
                        path.append('w')
                        # go straight

            elif Next[0] == 'c':
                # if the zeroth column of the next row is 'c'

                if col == 0:
                    path.append('r')
                    # straigt drop

                    No_of_Boulders -= 1

                    if No_of_Boulders != 0:
                        path.append('b')
                        #  turn 180 degrees

                        bck = go_back(6 - i, 7, col)
                        #  go back to the the zeroth row

                        again = come_again(i + 1, 0)
                        # come again to the initial row

                        path.extend(bck)

                        path.extend(Boulder_pick(Boulders_to_be_picked[No_of_Boulders - 1]))
                        #  pick the required boulder

                        path.extend(again)

                    if No_of_Boulders == 0:
                        path.append('w')
                        # if no boulder left to pick then go straight

                else :
                    path.append('q')
                    # turn left diagonally

                    path.append('l')
                    # diagonal drop

                    path.append('e')
                    # turn right diagonally

                    No_of_Boulders -= 1

                    if No_of_Boulders != 0:
                        path.append('b')
                        # turn 180 degrees

                        bck = go_back(6 - i, 7, col)
                        # go back to the starting point

                        again = come_again(i + 1, 0)
                        # come back to the initial point

                        path.extend(bck)
                        path.extend(Boulder_pick(Boulders_to_be_picked[No_of_Boulders - 1]))
                        #  pick the required boulder
                        path.extend(again)

                    if No_of_Boulders == 0:
                        path.append('q')
                        # turn left diagonally

                        path.append('W')
                        # go straight diagonally

                        path.append('e')
                        # turn right diagonally

                    col = 0

                Bridge[i + 1][0] = 1

            if i == 5:

                if col == 1:
                    path.append('n')
                    # align left
                else:
                    path.append('m')
                    # align right

        return path

    def come_again(row_end, row_start):
        '''
        Function Name: come_again()
        Input: row_end, row_start
        Output: comeagain_rt
        Logic: we find the route for the robot to come back to the initial point by passing the start row and the
                end row to the function find_shortest , here we find the route in Bridge2 as it contains no cavities
        Example Call: come_again(4,0)
        '''

        comeagain_rt = []
        comeagain_rt = find_shortest(Bridge2, comeagain_rt, 0, row_end = row_end + 1, row_start = row_start, No_of_Boulders=0)
        return comeagain_rt

    def go_back(start_row, end_row, column):
        '''
        Function Name: go_back()
        Input: start_row, end_row, column
        Output: back
        Logic: We find the route for the robot to go back to the zeroth row by passing row number from where we want to
                go back to the zeroth row and 0 to the function find_shortest() here we operate on Bridge_rev as this
                Bridge is the view as observed by the robot facing towards the starting point
        Example Call: go_back(3,0,1)
        '''
        back = []
        back = find_shortest(Bridge_rev, back, column, end_row, start_row, 0)
        return back

    ch_bridge(bridge_two)
    # set all the 'c' in Bridge1 to 1
    rev_bridge(bridge_two)
    # reverse bridge_two

    ROUTE = []
    rt = []

    ROUTE.append(Boulder_pick(Boulders_to_be_picked[len(Boulders_to_be_picked) - 1]))
    # command for the first boulder to be picked

    rt = find_shortest(bridge_two, rt, 0, 7, 0, len(Boulders_to_be_picked))
    ROUTE.extend(rt)
    # A = str( Boulders_to_be_picked.reverse())
    # ROUTE.extend(A)
    # ROUTE.extend(len(Boulders_to_be_picked))
    ROUTE.extend(No_on_Boulders)
    ROUTE.extend(str(len(No_on_Boulders)))
    ROUTE.extend('2')

    return ROUTE


def solver():
    '''
     Function Name : solver()
     Input : None
     Output : returns the path for the robot to follow
                ( i.e. the variable PATH)
     Logic: solver() calls the function choose_bridge() which returns the contents of bridge 1 and bridge 2,
            the choosen bridge and the boulders to be picked
            then according to the chosen bridge we call the crossing functions for the respective bridge
            and store the returned path in the variable PATH and the variable PATH is returned
     Example call: A = solver()
                  [ Here solver() will return the path for the robot to follow ]
     '''

    BRIDGE_1, BRIDGE_2, chosen_bridge, Boulders_to_be_picked, NUM_on_Boulders = choose_bridge()
    '''
    choose_bridge returns:
                            1. Bridge_1 [ a 1-D array which contains the positions of cavities on the bridge]
                            2. Bridge_2 [ a 2-D array which contains the positions of obstacles and cavities on the bridge]
                            3. chosen_bridge [ an integer which stores the value of the chosen bridge
                            4. Boulders_to_picked [ a 1-D array which contains the boulder number to be picked]
    we store these variables respectively in BRIDGE_1, BRIDGE_2, chosen_bridge and Boulders_to_be_picked and then according to

    the value of chosen_bridge we call the respective crossing function of the chosen Bridge
    '''
    PATH = []

    if chosen_bridge == 1:
        PATH = Bridge_1_cross(BRIDGE_1, Boulders_to_be_picked, NUM_on_Boulders)

    #     if chosen bi=ridge is 1 then we call bridge_1_cross()
    #     Bridge_1_cross() returns the path to be followed by the robot to cross bridge 1
    #     we store the returned path in a variable PATH

    elif chosen_bridge == 2:
        PATH = Bridge_2_cross(BRIDGE_2, Boulders_to_be_picked, NUM_on_Boulders)

    #     if chosen bridge is 2 then we call Bridge_2_cross()
    #     Bridge_1_cross() returns the path to be followed by the robot to cross bridge 1
    #     we store the returned path in a variable PATH

    # we now return PATH
    PATH.append('*')
    return PATH


def send_data(data):

    '''
    Function Name: send_data()
    Input: data
    Output: None
    Logic: we take the data to be sent as an input and then send it one by one to the robot
    Example Call: send_data(B)
                 where B is the path for the robot to follow
    '''

    for i in range(0,len(data), 1):
        ser.write(data[i])
        print i
        ser.read()



path = solver()
print path
print len(path)
send_data(path)
ser.close()
cv2.destroyAllWindows()