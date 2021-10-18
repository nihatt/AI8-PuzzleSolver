from array import *
from numpy import *
import ast
import sys
import time

xofzero = 0
yofzero = 0
wrongcount = 0
arr1 = [[7, 2, 4], [5, 0, 6], [8, 3, 1]]
firstarray = [[1, 3, 8], [4, 0, 6], [2, 5, 7]]
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


# find the index of zero
def findzero(arr1):
    for i in range(len(arr1)):
        for j in range(len(arr1[i])):
            if arr1[i][j] == 0:
                findzero.xofzero = i
                findzero.yofzero = j


# swapping to indexes
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


# checking how many wrong numbers do we have
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


def getfather(graph, value):
    for i in graph:
        if (value in graph[i]):
            return i
    return "yok"


def control(array1, checkvalue):
    for i in array1:
        if (checkvalue in headnodes):
            return checkvalue
    return 0


maxlengfth = 1


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
                print(("Fringe : " + len(fringe).__str__()))
                print("Nodes expanded : " + expand.__str__())
                print("Starting situation was " + arr1.__str__())
                print(temp)
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
                print(("Fringe : " + len(fringe).__str__()))
                print("Nodes expanded : " + expand.__str__())
                print("Starting situation was " + arr1.__str__())
                print(temp)
                return True
            else:

                cocuklar = wherecanmove(temp)
                expand += 1

                if (getfather(graph, temp) != "yok"):
                    sikilcek = ast.literal_eval(str(getfather(graph, temp)))
                    cocuklar.remove(sikilcek)
                fringe = fringe + cocuklar.copy()
                graph[repr(temp)] = cocuklar.copy()
                print(expand.__str__() + " node is searched")


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

    '''
        if (getfather(graph, arr1)) != "yok":
        oppurtunities.remove(ast.literal_eval(getfather(graph, arr1)))
    headnodes.append(arr1.copy())

    for s in range(len(oppurtunities)):
        if (oppurtunities[s] in headnodes):
            oppurtunities.remove(oppurtunities[s])
            break

    graph[repr(arr1)] = oppurtunities
    print(arr1)
    arr1.clear()
    arr1 = oppurtunities.copy()[0]
    n += 1

    if (arr1 == arrgoal):
        print(graph)
        print("sonuc bulundu")
        final = True
        quit()

    '''


dfs()
# dfs
