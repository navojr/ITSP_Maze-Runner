import cv2
import numpy as np
from detection import *
from ex2 import *
import math
from lineFollower import *
from stateHelper import *
from solver import *
"""
stepLen = 532

class junction:
    """""" pass jType_ as -2 and parent as -1 if it is origin
        jType:
        -1 for origin
        0 for dead end
        1 to 4 L : 1 1st quadrant ....
        5 to 8 T : 5 -> Right 6 -> Up 7 -> Left 8 -> Down
        9 + """"""
    def __init__(self, jType_, angle, cordi, parent_):
        self.jType = self.findJuncGlobal(jType_, angle)
        self.cordi = [cordi[0], cordi[1]]
        self.parent = parent_
        self.connect = []
        self.addNeigh(parent_)
        self.maxConnect = -1
        self.calcConnect()
    def calcConnect(self):
        if self.jType ==  0 or self.jType == -1:
            self.maxConnect = 1
        elif self.jType <= 4:
            self.maxConnect = 2
        elif self.jType <= 8:
            self.maxConnect = 3
        else:
            self.maxConnect = 4
    def helpFindJ(self, ang):
        if ang == 0:
            return 0
        elif ang == 90:
            return 1
        elif ang == 180:
            return 2
        else:
            return 3
    def findJuncGlobal(self, junc, ang = 0):
        if junc == -2:
            return -1
        elif junc == -1:
            return 0
        elif junc == 1 or junc == 2:
            A = 0
            if junc == 1:
                A = ang + 90
            else:
                A = ang + 180
            return 1 + self.helpFindJ(A % 360)
        elif junc == 6:
            return 9
        else:
            A = 0
            if junc == 5:
                A = ang + 180
            elif junc == 3:
                A = ang + 90
            else:
                A = ang - 90
            return 5 + self.helpFindJ(A % 360)
    def addNeigh(self, n):
        if n == -1:
            self.parent = n
        else:
            if len(self.connect) == 0:
                self.parent = n
            else:
                pass
            self.connect.append(n)


def moveTillJunc():
    count_ = 0
    while True:
        im_ = captureImg()
        ang_ = getAngle(im_.copy())
        print("angle", ang_)
        while math.fabs(ang_) > 6:
            correctAngle(ang_)
            print("angle", ang_)
            im_ = captureImg()
            ang_ = getAngle(im_.copy())

 #       im = captureImg()
        off_ = getOffset(im_.copy())
        print("off", off_)

        while math.fabs(off_) > 170:
            correctOffset(off_)
            print("off", off_)
            im_ = captureImg()
            ang_ = getAngle(im_.copy())
            print("angle", ang_)

            while math.fabs(ang_) > 6:
                correctAngle(ang_)
                print("angle", ang_)
                im_ = captureImg()
                ang_ = getAngle(im_.copy())
            off_ = getOffset(im_.copy())
        xJ_ = getJunction(im_.copy())
        print("xjxjxj", xJ_)
        junc_ = xJ_[0]
        if junc_ == 0:
            moveForward(stepLen / 2)
            count_ += 1
        else:
            print("junc", xJ_)
            if xJ_[1][1] < -100:
                moveForward(120) #to be tuned
            else:
                return [int(count_ / 2), xJ_]

class MaP:
    def __init__(self):
        j = junction(-2, 0, [0, 0], -1)
        self.presCordi = [0, 0]
        self.lis = [j]
        self.nJunc = 0
        self.prev = 0
        self.angle = 90
    def calcGlobalAngle(self, ini, final):
        if ini[0] == final[0]:
            if ini[1] > final[1]:
                return 270
            else:
                return 90
        else:
            if ini[0] > final[0]:
                return 180
            else:
                return 0
    def moveParent(self, n):
        if self.lis[n].parent == -1:
            return -1
        else:
            dest = self.lis[n].parent
            self.moveNeighbour(n, dest)
            self.prev = dest
            return 0

    def updateCordi(self, dis):
        print("In update cordi dis and ang", dis, self.angle)
        if self.angle == 0:
            self.presCordi[0] += dis
        elif self.angle == 90:
            self.presCordi[1] += dis
        elif self.angle == 180:
            self.presCordi[0] -= dis
        elif self.angle == 270:
            self.presCordi[1] -= dis
        else:
            print("ANGLE OUT RANGE")
        print("Final codi in updateCordi", self.presCordi)

    def moveNeighbour(self, ini, fin):
#        if self.lis[n].parent == -1
#            return -1
#        else:
#            dest = self.lis[self.lis[n].parent]
#            self.prev = dest
        AnG = self.calcGlobalAngle(self.lis[ini].cordi, self.lis[fin].cordi)
        turnAnG = AnG - self.angle
        turnAnG %= 360
        if turnAnG == 0:
            moveForward(stepLen)
        elif turnAnG == 90:
            moveForward(stepLen)
            cv2.waitKey(500)
            turnleft_90()
            self.angle += 90
            self.angle %= 360
#            moveForward()
        elif turnAnG == 180:
            turn_180() # TODO offset to be tuned
            self.angle += 180
            self.angle %= 360
        elif turnAnG == 270:
            moveForward()
            cv2.waitKey(500)
#            moveForward()
            turnright_90()
            self.angle -= 90
            self.angle %= 360
#            moveForward()

        mParent = moveTillJunc()
        self.updateCordi(mParent[0] + 1)

    def explore(self, n):
        """ """
        returns 7 when completely explored
        returns 1 in case loop anf returns to the same junc
        returns -7 dead end
        returns 0 for origin or common node
        """ """
        jType = self.lis[n].jType
        print("jType in explore", jType)
        print("lis", self.lis)
        if self.lis[n].maxConnect == len(self.lis[n].connect):
            return 7
        else:
            if jType == -1:
                print("Origin being explored")
                newJ = moveTillJunc()
                print("Output of move till junction", newJ)
                self.updateCordi(newJ[0] + 1)
                NewJunction = junction(newJ[1][0], self.angle, self.presCordi, n)
                self.lis.append(NewJunction)
                self.nJunc += 1
                self.lis[n].addNeigh(self.nJunc)
                self.prev = self.nJunc
                return 0

            elif jType == 0:
                return -7
            else:
                self.prev == n
                Pang = self.calcGlobalAngle(self.lis[n].cordi, self.lis[self.lis[n].parent].cordi)
                print("Parent index", self.lis[n].parent)
                print("Parent cordi", self.lis[self.lis[n].parent].cordi)
                print("Junc cordi", self.lis[n].cordi)
                print("Pang in explore", Pang)
                if jType < 5: #L turns
                    if Pang == (jType - 1) * 90:
#                        Ang = Pang + 90
                        Ang = jType * 90
                        Ang %= 360
                    else:
                        Ang = (jType - 1) * 90
                    turnAng = Ang - self.angle
                elif jType < 9:
                    print("n = ", n)
                    print("connect length", len(self.lis[n].connect))
                    if len(self.lis[n].connect) == 1:
                        TryAng = ((jType - 6) * 90) % 360
                        if TryAng == Pang:
                            TryAng += 90
                            TryAng %= 360
                    else:
                        neighAng = self.calcGlobalAngle(self.lis[n].cordi, self.lis[self.lis[n].connect[1]].cordi)
                        TryAng = ((jType - 6) * 90) % 360
                        if (TryAng == Pang) or (TryAng == neighAng):
                            TryAng += 90
                            TryAng %= 360
                            if (TryAng == Pang) or (TryAng == neighAng):
                                TryAng += 90
                                TryAng %= 360
                    print("Final value of TryAng", TryAng)
                    turnAng = TryAng - self.angle
                else:
                    angArray = []
                    for neighs in self.lis[n].connect:
                        angang = self.calcGlobalAngle(self.lis[n].cordi, self.lis[neighs].cordi)
                        angArray.append(angang)
                    TryAng = 0
                    while True:
                        if (TryAng in angArray):
                            TryAng += 90
                            print("Adding 90", TryAng)
                        else:
                            break
                    print("Final value of TryAng", TryAng)
                    turnAng = TryAng - self.angle
                turnAng %= 360
#                moveForward()
                moveForward(stepLen)
                print("Final value of turnAng", turnAng)
                cv2.waitKey(500)
                if turnAng == 90:
                    turnleft_90()
                    self.angle += 90
                elif turnAng == 270:
                    turnright_90()
                    self.angle -= 90
                elif turnAng == 180:
                    turn_180()
                    self.angle += 180
                else:
                    print("turning 0 degrees")
                self.angle %= 360
#                moveForward()
                newJ = moveTillJunc()
                self.updateCordi(newJ[0] + 1)
                NewJunction = junction(newJ[1][0], self.angle, self.presCordi, n)
                cordiList = map(lambda x: x.cordi, self.lis)
#                if NewJunction.cordi == (0,0):
#                if (NewJunction in self.lis):
                print("Cordi list", cordiList)
                print("NewJuncionCordi", NewJunction.cordi)
                if (NewJunction.cordi in cordiList):
                    encPos = 0
#                    for pos, NewJu in enumerate(self.lis):
                    for pos, NewJu in enumerate(cordiList):
#                        if NewJu == NewJunction:
                        if NewJu == NewJunction.codi:
                            encPos = Pos
                            break
                        else:
                            pass
                    self.lis[encPos].addNeigh(n)
                    self.lis[n].addNeigh(encPos)
                    moveForward(stepLen)
                    turn_180()
                    self.angle += 180
                    self.angle %= 360
                    oldJ = moveTillJunc()
                    self.presCordi = self.lis[n].cordi
                    return 1 #for loop
                else:
                    self.lis.append(NewJunction)
                    self.nJunc += 1
                    self.lis[n].addNeigh(self.nJunc)
                    self.prev = self.nJunc
                    return 0
        print("lis when comming out of explore", self.lis)
"""
if __name__ == "__main__":
    startCam()
    MapObject = MaP()
    print("Parent of Origin", MapObject.lis[0].parent)
    while True:
        print("Entering loop in main")
        exOut = MapObject.explore(MapObject.prev)
        print("After calling explore in main angle", MapObject.angle)
        print("Parent of Origin", MapObject.lis[0].parent)
        if exOut == 7 or exOut == -7:
            print('a dead end or a node with all explored paths encountered and prev is ====', MapObject.prev)
            pare = MapObject.moveParent(MapObject.prev)
            print('Index of parent from main', pare)
            if pare == -1:
                break
            else:
                pass
        else:
            pass
    solverObject = solver(MapObject)
    solverObject.moveShortest(0,13)
    stopCam()
