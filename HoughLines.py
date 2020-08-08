import numpy as np
import cv2
import math
from numpy.lib import stride_tricks
from matplotlib import pyplot as plt

img=cv2.imread('D:\CV\Tutorials\\sudoku.png')

def HoughTransform (img, threshold):

    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Finding The Edge points
    edge=cv2.Canny(gray,20,100)
    loc1, loc2 = np.where(edge != 0)
    a = np.dstack((np.array(loc1), np.array(loc2)))
    Edge_Coordinates = a[0]

    #Finding Dimensions of the image
    height=edge.shape[0]
    width=edge.shape[1]

    #Finding maximum rho value
    #rho values range from -D to D

    D=math.ceil(math.sqrt((width-1)**2+(height)**2))

    #Creating a hough Accumulator
    ht=np.zeros((2*D+1,182))

    #rho values
    s=np.arange(-D,D+1,+1)

    #theta values range from -90 degrees to 90 degrees
    #thetai is just a variable to store corresponding indices of theta
    theta=np.arange(-90,91,1)
    thetai=np.arange(0,181,1)

    r=0

    rr=0

    for i in Edge_Coordinates:
        y=0

        #Rho values calculated by the formula: rho= x*cos(theta)+y*sin(theta)
        r=(i[1]*np.cos(np.radians(theta))) + np.multiply(i[0], np.sin(np.radians(theta)))
        rr=np.floor(r).astype('int')+D
        #Voting
        ht[rr,thetai]+=1

    #Finding hough peaks based on threshold provided
    r, t = np.where(ht > threshold)

    return ht,r,t,theta,s



def DrawHoughLines(img,r,t,theta,s):

    w=np.dstack((np.array(r),np.array(t)))
    win=w[0]

    for i in win:

        r=i[0]
        t=i[1]
        d=s[r]
        th=math.radians(theta[t])

        a = math.cos(th)
        b = math.sin(th)
        x0 = a * d
        y0 = b * d
        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

    return img


ht,r,t,theta,s=HoughTransform(img,150)
HoughLine=DrawHoughLines(img,r,t,theta,s)

cv2.imshow('g',img)
k=cv2.waitKey(0) & 0xff
cv2.destroyAllWindows()

