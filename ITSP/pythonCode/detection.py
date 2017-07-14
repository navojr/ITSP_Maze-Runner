import cv2
import numpy as np
from ip import *
import math
from picamera import PiCamera
#camera = PiCamera()

def captureImg():
    camera = PiCamera()
    camera.capture('orig.jpg')
    img = cv2.imread('orig.jpg',1)
    cv2.imshow("orig",img)
    return img

def getAngle(img):
    mask = getRegion(img)
    final1 = applyMorpho(mask.copy(), 7, 20, True)
    final = applyMorpho(final1.copy(), 0, 301)
    cnt = contourDetect(final.copy())
    recList = rectDetect(cnt)
    if len(recList) > 0:
        ang = recList[0][2]
        if ang < -45:
            return (90 + recList[0][2]) #The rectangles should be sorted
        else:
            return ang
    else:
        return 0

def getOffset(img):
    mask = getRegion(img)
    final1 = applyMorpho(mask.copy(), 7, 20, True)
    final = applyMorpho(final1.copy(), 0, 301)
    cnt = contourDetect(final.copy())
    recList = rectDetect(cnt)
    if len(recList) > 0:
        return (recList[0][0][0] - 360) #The rectangles should be sorted
    else:
        return 0

def getJunction(img):
    """
    -1 no path
    0 st path
    1 left turn
    2 right turn
    3 left T
    4 right T
    5 down T
    6 plus
    """
#    cv2.imshow("what", img)
#    cv2.waitKey(1000)
    near = 120
    mask = getRegion(img.copy())
#    cv2.imshow("mask", mask)
    final1 = applyMorpho(mask.copy(), 7, 20, True)
    cv2.imshow("final1", final1)
    verFinal = applyMorpho(final1.copy(), 0, 301)
    cv2.imshow("verfin1", verFinal)
    cv2.waitKey(2000)
    verCnt = contourDetect(verFinal.copy())
    verRecList = rectDetect(verCnt)
    horFinal = applyMorpho(final1.copy(), 1, 301)
#    cv2.imshow("horfin1", horFinal)
    horCnt = contourDetect(horFinal.copy())
    horRecList = rectDetect(horCnt)
    if len(verRecList) == 0:
        return (-1, (0, 0))
    elif len(horRecList) == 0:
        return (0, (0, 0))
    else:
        verHeight = max(verRecList[0][1][0], verRecList[0][1][1])
        verWidth = min(verRecList[0][1][0], verRecList[0][1][1])
        horHeight = min(horRecList[0][1][0], horRecList[0][1][1])
        horWidth = max(horRecList[0][1][0], horRecList[0][1][1])
        print("hor center y", horRecList[0][0][1])
        print(horRecList)
        print("ver",verRecList)
        print("ver top y",verRecList[0][0][1] - verRecList[0][1][1]/2)
        print("ver center y",verRecList[0][0][1])
        print("ver height",verRecList[0][1][1], verHeight)
        print("ver width",verRecList[0][1][0], verWidth)
        if (math.fabs((horRecList[0][0][0] - horWidth/2) - verRecList[0][0][0]) > near) and (math.fabs((horRecList[0][0][0] + horWidth/2) - verRecList[0][0][0]) > near):
            if math.fabs((verRecList[0][0][1] - verHeight/2) - horRecList[0][0][1]) < near:
                return (5, pictureFrame(verRecList[0][0][0], horRecList[0][0][1])) #down T
            else:
                return (6, pictureFrame(verRecList[0][0][0], horRecList[0][0][1])) #plus
        elif horRecList[0][0][0] > verRecList[0][0][0]:
            print(math.fabs((verRecList[0][0][1] - verHeight/2) - horRecList[0][0][1]))
            if math.fabs((verRecList[0][0][1] - verHeight/2) - horRecList[0][0][1]) < near:
                return (2, pictureFrame(verRecList[0][0][0], horRecList[0][0][1])) #right Turn
            else:
                return (4, pictureFrame(verRecList[0][0][0], horRecList[0][0][1])) #right T
        else:
            print(math.fabs((verRecList[0][0][1] - verHeight/2) - horRecList[0][0][1]))
            if math.fabs((verRecList[0][0][1] - verHeight/2) - horRecList[0][0][1]) < near:
                return (1, pictureFrame(verRecList[0][0][0], horRecList[0][0][1])) #left Turn
            else:
                return (3, pictureFrame(verRecList[0][0][0], horRecList[0][0][1])) #left T

def pictureFrame(x, y):
    return (x - 360, y - 240)

if __name__ == "__main__":
#    img = cv2.imread('path1.jpg',1)
    img = captureImg()
    xJ = getJunction(img.copy())
    print(xJ)
    cv2.waitKey(8000)
    cv2.destroyAllWindows()
