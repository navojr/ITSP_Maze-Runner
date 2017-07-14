import cv2
import numpy as np

def fn():
    print("Not executed")

#if __name__ == "__main__":
def getRegion(img):
#    img = cv2.imread('path1.jpg',1)
#    cv2.imshow('im color', img)
#    cv2.waitKey(2000)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)
    print("vmin:", np.amin(v), "vmax", np.amax(v))

    lower_color = np.array([0, 90, 30])
    upper_color = np.array([20, 255, 255])

    lower_color1 = np.array([155,90, 30])
    upper_color1 = np.array([180, 255, 255])
    mask1 = cv2.inRange(hsv, lower_color, upper_color)
    mask2 = cv2.inRange(hsv, lower_color1, upper_color1)
    mask = cv2.bitwise_or(mask1, mask2)
#    cv2.imshow('hhhhhhh', s)
    return(mask)

def applyMorpho(img, mode, l, rev = False):
    """Mode is 0 to get vertical 1 to get horiontal and 2 for both"""
    x = y = l #width of the path
    if mode == 0:
        x = 3
    elif mode == 1:
        y = 3
    else:
        pass
    kernel = np.ones((y,x), np.uint8)
    if (not rev):
        erosion = cv2.erode(img, kernel, iterations = 1)
        dilation = cv2.dilate(erosion, kernel, iterations = 1)
#        cv2.imshow('dilation', dilation)
        return dilation
    if rev:
        dilation = cv2.dilate(img, kernel, iterations = 1)
        erosion = cv2.erode(dilation, kernel, iterations = 1)
#        cv2.imshow('erosion', erosion)
        return erosion
#    return erosion

def contourDetect(img):
    size = 480, 720
    im = np.zeros(size, dtype = np.uint8)
    _, contours, hierarchy = cv2.findContours(img, mode=cv2.RETR_LIST, method=cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(im, contours, -1, (255, 255, 255),1)
#    cv2.imshow("imageCont", im)
    return contours

def rectDetect(contours):
    rectList = []
    size = 480, 720
    im = np.zeros(size, dtype = np.uint8)
    for cont in contours:
        rect = cv2.minAreaRect(cont)
        rectList.append(rect)
    for rec in rectList:
#        box = cv2.cv.BoxPoints(rec)
        box = cv2.boxPoints(rec) # for opencv3
        box = np.int0(box)
        cv2.drawContours(im,[box], 0, (255, 255, 255),1)
#    cv2.imshow("imageRect", im)
    rectList.sort(key = lambda r: r[1][0] * r[1][1], reverse = True)
    return rectList

if __name__ == "__main__":
    img = cv2.imread('path1.jpg',1)
    mask = getRegion(img)
    final1 = applyMorpho(mask.copy(), 7, 20, True)
    final = applyMorpho(final1.copy(), 1, 141)
    cnt = contourDetect(final.copy())
    recList = rectDetect(cnt)
    print (len(recList))
    cv2.imshow('image', final)
    cv2.imshow('ima', mask)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()

