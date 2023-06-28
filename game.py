from PIL import ImageGrab
import cv2
import numpy as np
import pyautogui
temp_dir = "/home/sachin/Personal/Projects/Python/audo_dino/screenshots/"
ctr = 0
while True:
    pic = ImageGrab.grab(bbox=(182, 332, 280, 490)) # Change it according to the screen dimension and position of browser window
    image = cv2.cvtColor(np.array(pic),
                         cv2.COLOR_RGB2BGR)
    ret,thresh1 = cv2.threshold(image,127,255,cv2.THRESH_BINARY) # entire section
    thresh1,_,_ = cv2.split(thresh1)
    upper = thresh1[0:80,0:98]
    lower = thresh1[80:,0:98]
    if np.sum(lower == 255) > 500:
        pyautogui.press("space")
    if np.sum(upper == 255) > 200:
        pyautogui.press("down")
    cv2.imshow("Upper", upper)
    cv2.imshow("Lower", lower)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
