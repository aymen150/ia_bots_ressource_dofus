import cv2
import pytesseract
import time
import numpy as np
from PIL import Image, ImageDraw
import pyautogui
import py.variable as v
import py.Map as m
import py.dofus_action as da
import socket
import sys
from pathlib import Path
import models.predict as predict

#print( '\r',f"i : {i}",end='', flush=True)

#pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
#sys.path.append(Path("D:/Users/Document D/project_dofus/my_bot"))
#model_all_r = "models/model_r_800/model.pb"
#label_all_r = "models/model_r_800/labels.txt"

#model_poisson = "models/model_poisson/model.pb"
#label_poisson = "models/model_poisson/labels.txt"
#model_bois = "models/model_bois_i3/model.pb"
#label_bois = "models/model_bois_i3/labels.txt"
#model_poisson = "models/model_poisson_i15/model.pb"
#label_poisson = "models/model_poisson_i15/labels.txt"
#od_model_poisson = predict.load_model(MODEL_FILENAME = model_poisson,LABELS_FILENAME = label_poisson)
#od_model_bois = predict.load_model(MODEL_FILENAME = model_bois, LABELS_FILENAME = label_bois)


model = "models/model_all_i10/model.pb"
label = "models/model_all_i10/labels.txt"

model_monstre9 = "models/model_monster_i10/model.pb"
label_monstre9 = "models/model_monster_i10/labels.txt"
model_fight = "models/model_fight_i6/model.pb"
label_fight = "models/model_fight_i6/labels.txt"

od_model = predict.load_model(MODEL_FILENAME = model, LABELS_FILENAME = label)
od_model_fight = predict.load_model(MODEL_FILENAME = model_fight,LABELS_FILENAME = label_fight)

#choise "Bonta" : "Amakna" : "Sufokia" : "Pandala"
region_banque = "Pandala"

#choise : "amakna sud" : "foret bonta" : "dragoeuf" : "pandala sud" :
region_parcours = "pandala sud"

print(""" 
      ###############################################################
      ##################### S   T   A   R   T   #####################
      ###############################################################y
      """)
time.sleep(5)
pos_joueur = da.coordonnées_joueur((500,500))
a = 0

circuit = m.circuit(region_parcours) 
while True :                                    
    for map in circuit :                       # pour chaque map du parcours
        time.sleep(2)
                                                   #lecture ocr de la map actuelle
        map_actuelle = da.my_map()
        if map_actuelle == "999,999" :
            print("error detecting map")
            map_actuelle = map.map 
        elif not da.eguals_map(map_actuelle, map.map) :                    # verifier que la map actuelle en jeu est bien la map sur laquel on travaille
            da.travel(map.map,da.distance_map(map_actuelle,map.map)*10)     
        list_bounding_click = []
        list_recolte = []
        list_bounding_deja_cliquer = []
        indice = 0
        while len(list_bounding_click) > 0 or indice == 0 :
            indice += 1
            pyautogui.keyDown("y")                         #surbrillance des ressources de la map en cours
            time.sleep(0.15)
            image = pyautogui.screenshot(region=v.region_gameplay)  #screenshot de la region de jeu
            pyautogui.keyUp("y")                            # fin de surbrillance
            w,h = image.size
        
            # detection des IA ressources
            predictions = od_model.predict_image(image)
            # liste des zones boxes des ressources
            list_bounding_click_tmp =  da.predictions_to_click(predictions,w,h,proba_poisson=0.3,proba_plante=0.3,proba_bois=0.5)
            list_bounding_click = [elem for elem in list_bounding_click_tmp if elem[1] not in list_recolte] 
            if len(list_bounding_click) > 0 :
                list_bounding_click_desordonne = da.list_click_filter(list_bounding_click)    # filtre les positions pour eviter un changement de map
                if len(list_bounding_click_desordonne) > 0 :
                    bounding_click = da.minDistance(pos_joueur,list_bounding_click_desordonne)
                    bounding, click = bounding_click
                    list_recolte.append(click)
                    pos_joueur = click
                    print(f"map : {map.map}, ressource : {click}")
                    while da.is_connected == False :
                        time.sleep(30)
                        #da.connexion() 
                    x,y = click
                    if da.click_in_list_bounding((x,y),list_bounding_deja_cliquer) == False : 
                        da.dofus_click(x,y,0.1,3)                 # recolte de la ressources
                        print("click ", x,y)
                        list_bounding_deja_cliquer.append(bounding)
            
            if da.combat_debut() :
                print("debut combat")
                time.sleep(0.5)
                pyautogui.press("f1")
                while da.combat_fini() == False :
                    if da.my_tourn() == True :
                        image_fight = pyautogui.screenshot(region=v.region_gameplay)
                        w_f,h_f = image_fight.size
                        predictions_fight = od_model_fight.predict_image(image_fight)
                        da.combat(predictions_fight,w_f,h_f)
                time.sleep(3)
                da.dofus_press("enter",3)
                print("fin du combat")
        time.sleep(3)
        
        # deplacement du personnage jusqu'a la prochaine map de recolte
        pos = (map.next_map.x, map.next_map.y)
        x,y = pos
        da.dofus_click(x,y,0.3,0)
        pos_joueur = da.coordonnées_joueur(pos)
        da.changement_map(pyautogui.screenshot(region = v.region_map ))
        print("_____________________________________")
    
    # une fois le parcours fini direction la banque amakna déposer les ressources
    #a += 1
    #if (a%1) == 0 :
    da.go_bank(my_pos = map_actuelle , region  = region_banque )
    #da.travel("-1,24",da.distance_map("2,-2","-1,24")) #retour au point de départ du parcours
