import cv2

cap = cv2.VideoCapture("ml_laptop.mp4")
currentFrame = 1

while(True):
    ret, frame = cap.read()
    if currentFrame%5000==0 :
        cv2.imwrite('./images/frame' + str(currentFrame/5000) + '.jpg', frame)
    currentFrame+=1
           
cap.release()
cv2.destroyAllWindows()            
            
        
        
        
        
"""
Spyder Editor

This is a temporary script file.
"""

