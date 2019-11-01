import cv2
import numpy as np


def getHumanSkin(frame):

    img=np.copy(frame)
    
    img =cv2.bilateralFilter(img,15,75,75)




    #converting from gbr to YCbCr color space
    img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    #skin color range for YCbCr color space 
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
    

    


    

    humanSkin=np.copy(YCrCb_mask)

    try:
        positions = np.nonzero(humanSkin)
        top = positions[0].min()
        bottom = positions[0].max()
        left = positions[1].min()
        right = positions[1].max()
        humanSkin = humanSkin[top:top + bottom, left:left + right]
    except:
        None



    #show results
    cv2.imshow("humanSkin",humanSkin)
    
    return humanSkin

