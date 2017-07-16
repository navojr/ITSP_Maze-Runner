import cv2
import numpy as np
from stateHelper import *
import math
import copy

class solver:
    def __init__(self, Map_):
        self.Map = Map_
    def getDis(self, x, y):
        pos1 = list(self.Map.lis[x].cordi)
        pos2 = list(self.Map.lis[y].cordi)
        print("the coordinates of the parent", pos1)
        print("the coordinates of the child", pos2)
        if (pos1[0] == pos2[0]) or (pos1[1] == pos2[1]):
            return math.fabs(pos1[0] - pos2[0]) + math.fabs(pos1[1] - pos2[1])
        else:
            print("Error in getDis")
            return 50000
    def update(self, x, xChildIndex):
        if (xChildIndex in x[0]):
            return None
        else:
            di = self.getDis(x[0][-1], xChildIndex)
            x[0].append(xChildIndex)
            x[1] += di
            return x

    def debugPrint(self, path):
        for i in range(len(path)):
            print("")
            print("")
            for j in range(len(path[i][0])):
                print("the j ", j, path[i][0][j])
            print("lenght", path[i][1])

    def findShortest(self, ini, fin):
        """ returns -2 when path is not possible """
        path = [[[ini], 0]]
        pos = -1
        nPath = []
        while True:
            nPath = []
            i = 0
            for i in range(len(path)):
                print("The list of neighbours of i =", i, self.Map.lis[path[i][0][-1]].connect)
                for neigh in self.Map.lis[path[i][0][-1]].connect:
                    print("Value of i and neigh", i, neigh)
                    if neigh == fin:
                        pos = len(nPath)
                    else:
                        pass
                    New = self.update(copy.deepcopy(path[i]),neigh)
                    if New != None:
                        nPath.append(copy.deepcopy(New))
                        print("The values in nPath")
                        self.debugPrint(copy.deepcopy(nPath))
                    else:
                        pass
            if pos != -1:
                print("break because of pos =", pos)
                path = copy.deepcopy(nPath)
                break
            if len(nPath) == 0:
                print("break because nPath is empty")
                break
            path = copy.deepcopy(nPath)
            self.debugPrint(copy.deepcopy(path))
        if len(nPath) == 0:
            print("The npath is 0")
            return -2
        elif pos == -1:
            print("pos is -1")
            return -2
        else:
            MaxLen = path[pos][1]
            while True:
                flagModified = False
                nPath = []
                i = 0
                for i in range(len(path)):
                    if path[i][0][-1] == fin:
                        nPath.append(path[i])
                    else:
                        for neigh in self.Map.lis[path[i][0][-1]].connect:
                            if neigh == fin:
                                New = self.update(copy.deepcopy(path[i]),neigh)
                                nPath.append(copy.deepcopy(New))
                            else:
                                New = self.update(copy.deepcopy(path[i]),neigh)
                                if New != None and New[1] < MaxLen:
                                    nPath.append(copy.deepcopy(New))
                                    flagModified = True
                                else:
                                    pass
                path = copy.deepcopy(nPath)
                if not flagModified:
                    break
            MinIndex = 0
            MinLen = path[0][1]
            i = 0
            for i in range(len(path)):
                if path[i][1] < MinLen:
                    MinLen = path[i][1]
                    MinIndex = i
                else:
                    pass
            print("completed finding the path")
            return path[MinIndex][0]
    def moveShortest(self, ini, fin):
        route = copy.deepcopy(self.findShortest(ini, fin))
        if route == -2:
            print("No path possible")
        else:
            i = 1
            for i in range(1, len(route)):
                self.Map.moveNeighbour(route[i-1],route[i])
