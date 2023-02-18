import time
import numpy as np
from PIL import Image
import pyautogui
import py.variable as v
from random import randint
from pathlib import Path


while True:
            time.sleep(3)
           # pyautogui.keyDown("y")                         #surbrillance des ressources de la map en cours
          #  time.sleep(0.15)
            image = pyautogui.screenshot(region=(370, 194, 310, 606))  #screenshot de la region de jeu
            pyautogui.keyUp("y")
            p = Path(r"D:\Users\Document D\project_dofus\dataset\inventaire", f"{randint(1000,1000000)}.png")   
            image.save(p)     