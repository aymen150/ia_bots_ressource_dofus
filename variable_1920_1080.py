
import string
import pyautogui
import time
from pathlib import Path
from py.Coord import Coord
path_file = Path(__file__)
path_my_bot = path_file.parent.parent
path_circuit_foret_bonta = Path(path_my_bot,"circuit","foret_bonta.txt")
path_circuit_dragoeuf = Path(path_my_bot,"circuit","presqu_ile_dragoeuf.txt")
path_circuit_porco = Path(path_my_bot,"circuit","amakna_sud.txt")
path_circuit_pandala_sud = Path(path_my_bot,"circuit","pandala_sud.txt")
###############################################
############## ZONE DE JEU  ###################
###############################################
dimension_ecran = (1920,1080)
