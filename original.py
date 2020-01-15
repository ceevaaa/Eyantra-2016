'''
MOVES:
        w = go straight
        q = turn left,diagonal
        e = turn right, diagonal
        b = turn 180 degree
        l = diagonal drop
        r = straight drop
c = cavity
o = obstacle
'''
Bridge_1 = [[1, 1], [1, 1], ['o', 'c'], [1, 1], ['c', 'o'], [1, 1], ['o', 1]]
Bridge2 = [[0 for i in range(0,2,1)] for j in range(0,7,1)]
Bridge_rev = [[0 for i in range(0,2,1)] for j in range(0,7,1)]
def rev_bridge(Bridge):
    for i in range(0,len(Bridge),1):
        for j in range(0,2,1):
            if Bridge[i][j] == 'c':
                Bridge_rev[i][j] = 1
            else:
                Bridge_rev[i][j] = Bridge[i][j]

    for j in range(0, len(Bridge_rev) / 2, 1):
        temp = Bridge_rev[j]
        Bridge_rev[j] = Bridge_rev[len(Bridge_rev) - 1 - j]
        Bridge_rev[len(Bridge_rev) - 1 - j] = temp
        # Bridge_rev[j].reverse()
        # Bridge_rev[len(Bridge_rev) - 1 - j].reverse()
    return Bridge_rev


def ch_bridge(Bridge):
    for i in range(0, len(Bridge), 1):
        for j in range(0, 2, 1):
            if Bridge[i][j] == 'c':
                Bridge2[i][j] = 1
            else:
                Bridge2[i][j] = Bridge[i][j]

def find_shortest(Bridge,path,col,row,row_start,No_of_obs):
    for i in range(row_start, row-1, 1):
        Now = Bridge[i]
        Next = Bridge[i+1]

        if i == 0:
            # print "before: "+ "i= "+str(i) + "  col= "+str(col)
            if Now[0] == 1 and Now[1] == 1:
                path.append('n') #  allign left
                col = 0

            elif Now[0] == 'o':
                path.append('m')
                col = 1

            elif Now[1] == 'o':
                path.append('n')
                col = 0

            elif Now[0] == 'c':
                path.append('m') # allign right
                path.append('a') # left
                path.append('r') # straight drop
                path.append('d')
                No_of_obs -=  1
                if No_of_obs != 0:
                    path.append('b')
                    bck = go_back(6 - i, 7, col)
                    again = come_again(i + 1, 0)
                    for c in range(0, len(bck), 1):
                        path.append(bck[c])
                    for u in range(0, len(again), 1):
                        path.append(again[u])
                    # go_back_and_come(len(path)-1)

                col = 1
                Bridge[0] = 1

            elif Now[1] == 'c':

                path.append('n')  # allign left
                path.append('d')  # right
                path.append('r')  # straight drop
                path.append('a')
                col = 0
                Bridge[1] = 1

            # print "after: " + "i= " + str(i) + "  col= " + str(col)


        if Next[0] == 1:

            # print "before: " + "i= " + str(i) + "  col= " + str(col)
            if Next[1] == 1:
                path.append('w')    # go straight, col remains same
                # print "idhar pe: "+ str(col) + " i = "+ str(i)

            elif Next[1] == 'o':

                if col == 0:
                    path.append('w')

                elif col == 1:
                    path.append('q')
                    path.append('w')
                    path.append('e')
                    col = 0

            elif Next[1] == 'c':
                if col == 1:
                    path.append('r')
                    No_of_obs -= 1
                    if No_of_obs != 0:
                        path.append('b')
                        bck = go_back(6 - i, 7, col)
                        again = come_again(i + 1, 0)
                        for c in range(0, len(bck), 1):
                            path.append(bck[c])
                        for u in range(0, len(again), 1):
                            path.append(again[u])
                    if No_of_obs == 0:
                        path.append('w')
                        # go_back_and_come(len(path) - 1)

                elif col == 0:
                    path.append('e')
                    path.append('l')
                    path.append('q')
                    No_of_obs -= 1
                    if No_of_obs != 0:
                        path.append('b')
                        bck = go_back(6 - i, 7, col)
                        again = come_again(i + 1, 0)
                        for c in range(0, len(bck), 1):
                            path.append(bck[c])
                        for u in range(0, len(again), 1):
                            path.append(again[u])
                            # go_back_and_come(len(path) - 1)
                    if No_of_obs == 0:
                        path.append('e')
                        path.append('w')
                        path.append('q')
                Bridge[i + 1][1] = 1

            # print "after: " + "i= " + str(i) + "  col= " + str(col)

        elif Next[0] == 'o':
            # print "before: " + "i= " + str(i) + "  col= " + str(col)
            if Next[1] == 'c':
                    if col == 0:
                        path.append('e')
                        path.append('l')
                        path.append('q')
                        No_of_obs -= 1
                        if No_of_obs != 0:
                            path.append('b')
                            bck = go_back(6 - i, 7, col)
                            again = come_again(i + 1, 0)
                            for c in range(0, len(bck), 1):
                                path.append(bck[c])
                            for u in range(0, len(again), 1):
                                path.append(again[u])
                        if No_of_obs == 0:
                            path.append('e')
                            path.append('w')
                            path.append('q')
                        # go_back_and_come(len(path) - 1)
                        col = 1

                    elif col == 1:
                        path.append('r')
                        No_of_obs -= 1
                        if No_of_obs != 0:
                            path.append('b')
                            bck = go_back(6 - i, 7, col)
                            again = come_again(i + 1, 0)
                            for c in range(0, len(bck), 1):
                                path.append(bck[c])
                            for u in range(0, len(again), 1):
                                path.append(again[u])
                        # go_back_and_come(len(path) - 1
                        if No_of_obs == 0:
                            path.append('w')
                    Bridge[i+1][1] = 1

            elif Next[1] == 1:
                if col == 0:
                    path.append('e')
                    path.append('w')
                    path.append('q')
                    col = 1
                elif col == 1:
                    path.append('w')
            # print "after: " + "i= " + str(i) + "  col= " + str(col)

        elif Next[0] == 'c':
            # print "before: " + "i= " + str(i) + "  col= " + str(col)
            if col == 0:
                path.append('r')
                No_of_obs -= 1
                if No_of_obs != 0:
                    path.append('b')
                    bck = go_back(6 - i, 7, col)
                    again = come_again(i + 1, 0)
                    for c in range(0, len(bck), 1):
                        path.append(bck[c])
                    for u in range(0, len(again), 1):
                        path.append(again[u])
                if No_of_obs == 0:
                    path.append('w')

                    # go_back_and_come(len(path) - 1)

            else:
                path.append('q')
                path.append('l')
                path.append('e')
                No_of_obs -= 1
                if No_of_obs != 0:
                    path.append('b')
                    bck = go_back(6 - i, 7, col)
                    again = come_again(i + 1, 0)
                    for c in range(0, len(bck), 1):
                        path.append(bck[c])
                    for u in range(0, len(again), 1):
                        path.append(again[u])
                if No_of_obs == 0:
                    path.append('q')
                    path.append('w')
                    path.append('e')
                # go_back_and_come(len(path) - 1)
                col = 0

            Bridge[i+1][0] = 1
            # print "after: " + "i= " + str(i) + "  col= " + str(col)
        if i == 5:
            if col == 1:
                path.append('n')
            else:
                path.append('m')
    return path


def come_again(row_end,row_start):
    ideal_rt = []
    ideal_route = find_shortest(Bridge2,ideal_rt,0,row = row_end+1, row_start=row_start,No_of_obs=0)
    return ideal_route

def go_back(start_row,end_row,column):
    bk = []
    back = find_shortest(Bridge_rev,bk,column,end_row,start_row,0)
    return back

ch_bridge(Bridge_1)
rev_bridge(Bridge_1)
A = []
A = find_shortest(Bridge_1,A,0,7,0,2)
print A
