import cv2
import numpy as np




def getMaxContourArea(contours):
    maxArea=0
    maxContour=None
    for contour in contours:
        Xmin = np.min(contour[:,:,0])
        Xmax = np.max(contour[:,:,0])
        Ymin = np.min(contour[:,:,1])
        Ymax = np.max(contour[:,:,1])
        contourArea=(Xmax-Xmin)*(Ymax-Ymin)
        if contourArea>maxArea:
            maxArea=contourArea
            maxContour=contour
            
    return maxArea,maxContour




def getHand(frame):

    
    handBool=False
    humanSkin=getHumanSkin(frame)
    contours = cv2.findContours(humanSkin, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    if   len(contours)>0    :
                maxContourArea,maxContour =getMaxContourArea(contours)
                if maxContourArea > 2500:
                    handBool=True
                    x, y, w1, h1 = cv2.boundingRect(maxContour)
                    humanSkin = humanSkin[y:y + h1, x:x + w1]
        
    return humanSkin,handBool



def getHumanSkin(frame):

    img=np.copy(frame)
    
    img =cv2.bilateralFilter(img,15,75,75)  #blur without losing edges

    #converting from gbr to YCbCr color space
    img_YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    #skin color range for YCbCr color space 
    YCrCb_mask = cv2.inRange(img_YCrCb, (0, 135, 85), (255,180,135)) 
    YCrCb_mask = cv2.morphologyEx(YCrCb_mask, cv2.MORPH_OPEN, np.ones((5,5), np.uint8))
    
    '''try:
        positions = np.nonzero(humanSkin)
        top = positions[0].min()
        bottom = positions[0].max()
        left = positions[1].min()
        right = positions[1].max()
        humanSkin = humanSkin[top:top + bottom, left:left + right]
    except:
        None'''


    
    return YCrCb_mask

