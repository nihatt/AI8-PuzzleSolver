from array import *
from numpy import *
import ast
import sys
import time

xofzero = 0
yofzero = 0
wrongcount = 0
maxlengfth = 1
arr1 = [[1, 2, 5], [3, 4, 0], [6, 7, 8]]
arrgoal = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
newxtobemoved = [[0, 0], [0, 0], [0, 0], [0, 0]]
newytobemoved = [[0, 0], [0, 0], [0, 0], [0, 0]]
oppurtunities = [[[0, 1, 2], [3, 6, 4], [7, 8, 5]], [[0, 1, 2], [3, 6, 4], [7, 8, 5]],
                 [[0, 1, 2], [3, 6, 4], [7, 8, 5]], [[0, 1, 2], [3, 6, 4], [7, 8, 5]]]
graph = {}
fringe = [arr1]
final = False
headnodes = [[1, 2, 5], [3, 4, 0], [6, 7, 8], [[0, 1, 2], [3, 6, 4], [7, 8, 5]],
             [[0, 1, 2], [3, 6, 4], [7, 8, 5]], [[0, 1, 2], [3, 6, 4], [7, 8, 5]]]
start_time = time.time()


# Nihat Pamukcu
# 1306190035
# IU-C 2021-2022 Autumn AI Homework




# find the index of zero in a given array
def findzero(arr1):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr1[i][j] == 0:
                findzero.xofzero = i
                findzero.yofzero = j


# swapping to indexes in a given array
def swapnumber(a, b, i, j):
    global arr1
    global firstarray
    global oppurtunities
    arr1[a][b], arr1[i][j] = arr1[i][j], arr1[a][b]
    liste = arr1.copy()
    listasim = list()
    listasim.append([row[:] for row in arr1])
    oppurtunities.append([row[:] for row in arr1])
    arr1[a][b], arr1[i][j] = arr1[i][j], arr1[a][b]
    return listasim


# printing the table anytime we want
def printtable(arr1):
    print(arr1[0])
    print(arr1[1])
    print(arr1[2])


# checking how many wrong numbers do we have (not necessary just added for myself to try another algorithm)
def checkwrong(arr1):
    checkwrong.wrongcount = 0
    if (arr1[0][0]) != 0:
        checkwrong.wrongcount += 1
    if (arr1[0][1]) != 1:
        checkwrong.wrongcount += 1
    if (arr1[0][2]) != 2:
        checkwrong.wrongcount += 1
    if (arr1[1][0]) != 3:
        checkwrong.wrongcount += 1
    if (arr1[1][1]) != 4:
        checkwrong.wrongcount += 1
    if (arr1[1][2]) != 5:
        checkwrong.wrongcount += 1
    if (arr1[2][0]) != 6:
        checkwrong.wrongcount += 1
    if (arr1[2][1]) != 7:
        checkwrong.wrongcount += 1
    if (arr1[2][2]) != 8:
        checkwrong.wrongcount += 1


# lets the programme see where can the 0 (blank dot) move
def wherecanmove(arr1):
    newxtobemoved.clear()
    newytobemoved.clear()
    oppurtunities.clear()
    liste = list()
    listxx = arr1.copy()

    headnodes.append(listxx.copy())
    findzero(arr1)
    if (findzero.xofzero) == 0:
        # newxtobemoved.append([1, findzero.yofzero])
        tmp = list()
        for i in range(len(arr1)):
            tmp.append(list())
            for j in range(len(arr1)):
                tmp[i].append(arr1[i][j])
        tmp[findzero.xofzero][findzero.yofzero], tmp[1][findzero.yofzero] = tmp[1][findzero.yofzero], 0
        liste.append(tmp)
    if (findzero.xofzero) == 1:
        # newxtobemoved.append([0, findzero.yofzero])
        tmp = list()
        for i in range(len(arr1)):
            tmp.append(list())
            for j in range(len(arr1)):
                tmp[i].append(arr1[i][j])
        tmp[findzero.xofzero][findzero.yofzero], tmp[0][findzero.yofzero] = tmp[0][findzero.yofzero], 0
        liste.append(tmp)
        # newxtobemoved.append([2, findzero.yofzero])
        tmp = list()
        for i in range(len(arr1)):
            tmp.append(list())
            for j in range(len(arr1)):
                tmp[i].append(arr1[i][j])
        tmp[findzero.xofzero][findzero.yofzero], tmp[2][findzero.yofzero] = tmp[2][findzero.yofzero], 0
        liste.append(tmp)
    if (findzero.xofzero) == 2:
        # newxtobemoved.append([1, findzero.yofzero])
        tmp = list()
        for i in range(len(arr1)):
            tmp.append(list())
            for j in range(len(arr1)):
                tmp[i].append(arr1[i][j])
        tmp[findzero.xofzero][findzero.yofzero], tmp[1][findzero.yofzero] = tmp[1][findzero.yofzero], 0
        liste.append(tmp)

    if (findzero.yofzero) == 0:
        # newytobemoved.append([findzero.xofzero, 1])
        tmp = list()
        for i in range(len(arr1)):
            tmp.append(list())
            for j in range(len(arr1)):
                tmp[i].append(arr1[i][j])
        tmp[findzero.xofzero][findzero.yofzero], tmp[findzero.xofzero][1] = tmp[findzero.xofzero][1], 0
        liste.append(tmp)
    if (findzero.yofzero) == 1:
        # newytobemoved.append([findzero.xofzero, 0])
        tmp = list()
        for i in range(len(arr1)):
            tmp.append(list())
            for j in range(len(arr1)):
                tmp[i].append(arr1[i][j])
        tmp[findzero.xofzero][findzero.yofzero], tmp[findzero.xofzero][0] = tmp[findzero.xofzero][0], 0
        liste.append(tmp)
        # newytobemoved.append([findzero.xofzero, 2])
        tmp = list()
        for i in range(len(arr1)):
            tmp.append(list())
            for j in range(len(arr1)):
                tmp[i].append(arr1[i][j])
        tmp[findzero.xofzero][findzero.yofzero], tmp[findzero.xofzero][2] = tmp[findzero.xofzero][2], 0
        liste.append(tmp)
    if (findzero.yofzero) == 2:
        tmp = list()
        for i in range(len(arr1)):
            tmp.append(list())
            for j in range(len(arr1)):
                tmp[i].append(arr1[i][j])
        tmp[findzero.xofzero][findzero.yofzero], tmp[findzero.xofzero][1] = tmp[findzero.xofzero][1], 0
        liste.append(tmp)
        # newytobemoved.append([findzero.xofzero, 1])

    return liste


# moves the blank (0) tile to positions which found before
def move():
    global final
    listniyo = list()
    global oppurtunities
    global arr1
    global firstarray
    n = 0
    for i in range(int(len(newxtobemoved))):
        swapnumber(newxtobemoved[i][0], newxtobemoved[i][1], findzero.xofzero, findzero.yofzero)
        listniyo.append(swapnumber(newxtobemoved[i][0], newxtobemoved[i][1], findzero.xofzero, findzero.yofzero))
    for i in range(int(len(newytobemoved))):
        swapnumber(newytobemoved[i][0], newytobemoved[i][1], findzero.xofzero, findzero.yofzero)
        listniyo.append(swapnumber(newytobemoved[i][0], newytobemoved[i][1], findzero.xofzero, findzero.yofzero))
    return listniyo


# gives me the father of any node when i want
def getfather(graph, value):
    for i in graph:
        if (value in graph[i]):
            return i
    return "yok"


# lets me control if there is any-same other from the node
def control(array1, checkvalue):
    for i in array1:
        if (checkvalue in headnodes):
            return checkvalue
    return 0


# function to search the given sequence with Depth-first
def dfs():
    global maxlengfth
    global fringe
    expand = 0
    while True:

        if (len(fringe) == 0):
            return False
        else:
            temp = fringe.pop(0)

            if (temp == arrgoal):
                print("--- %s seconds have passed and solution has been found---" % (time.time() - start_time))
                print("Solution has been found with Depth-first Search")
                print(("Fringe : " + len(fringe).__str__()))
                print("Nodes expanded : " + len(cocuklar).__str__())
                print("Starting situation was ")
                printtable(arr1)
                print("=================")
                printtable(temp)
                return True
            else:

                cocuklar = wherecanmove(temp)
                expand += 1

                if (getfather(graph, temp) != "yok"):
                    silincek = ast.literal_eval(str(getfather(graph, temp)))
                    cocuklar.remove(silincek)
                fringe = cocuklar.copy() + fringe

                graph[repr(temp)] = cocuklar.copy()
                print(expand.__str__() + " node is searched")


# function to search the given sequence with Breadth-first
def bfs():
    global fringe
    expand = 0
    while True:

        if (len(fringe) == 0):
            return False
        else:
            temp = fringe.pop(0)

            if (temp == arrgoal):

                print("--- %s seconds have passed and solution has been found---" % (time.time() - start_time))
                print("Solution has been found with Breadth-first Search")
                print(("Fringe : " + len(fringe).__str__()))
                print("Nodes expanded : " + len(cocuklar).__str__())
                print("Starting situation was ")
                printtable(arr1)
                print("=================")
                printtable(temp)
                return True
            else:

                cocuklar = wherecanmove(temp)
                expand += 1

                if (getfather(graph, temp) != "yok"):
                    silincek = ast.literal_eval(str(getfather(graph, temp)))
                    cocuklar.remove(silincek)
                fringe = fringe + cocuklar.copy()
                graph[repr(temp)] = cocuklar.copy()
                print(expand.__str__() + " node is searched")


# function to search the given sequence with Depth limited Search
def dls(depthlimit, dls):
    global fringe
    expand = 0
    depths = dict()
    depths[repr(fringe[0])] = 0
    paths = [fringe]
    while True:
        if (len(fringe) == 0):
            return False
        else:
            temp = fringe[0].copy()
            fringe.remove(temp)

            if temp == arrgoal and dls == False:
                print("--- %s seconds have passed and solution has been found---" % (time.time() - start_time))
                print("Solution has been found with Depth limited Search")
                print(("Fringe : " + len(fringe).__str__()))
                print("Nodes expanded : " + len(cocuklar).__str__())
                print("Starting situation was ")
                printtable(arr1)
                print("=================")
                printtable(temp)
                return True
            elif temp == arrgoal and dls == True:
                print("--- %s seconds have passed and solution has been found---" % (time.time() - start_time))
                print("Solution has been found with Iterative deepening Search")
                print(("Fringe : " + len(fringe).__str__()))
                print("Nodes expanded : " + len(cocuklar).__str__())
                print("Starting situation was ")
                printtable(arr1)
                print("=================")
                printtable(temp)
                return True

            else:
                expand += 1
                if depths[repr(temp)] < depthlimit:

                    cocuklar = wherecanmove(temp)
                    removes = list()
                    for i in cocuklar:

                        if i not in paths:
                            paths.append(i)
                            depths[repr(i)] = depths[repr(temp)] + 1
                        else:
                            removes.append(i)
                    for i in removes:
                        cocuklar.remove(i)

                    fringe = cocuklar.copy() + fringe
                    graph[repr(temp)] = cocuklar.copy()
                else:
                    graph[repr(temp)] = []


# function to search the given sequence with Iterative deepening Search
def ids():
    global arr1
    global fringe
    depth = 1
    while True:
        durum = dls(depth,True)
        if durum == True:
            break
        else:
            fringe = [arr1]
            depth += 1


# write here the algorithm that you want to search with
dls(3,False)

