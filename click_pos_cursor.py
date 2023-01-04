
import win32api
import time
import pyautogui
time.sleep(3)

while True :
    x,y = pyautogui.position()
    if win32api.GetKeyState(0x01)<0 :
        print("x : ", x,"y :", y)
        time.sleep(0.3)
