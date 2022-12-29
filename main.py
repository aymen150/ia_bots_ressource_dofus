import cv2
import pytesseract
import time
import numpy as np
from PIL import Image, ImageDraw
import pyautogui
import py.variable as v
import py.map as m
import py.dofus_action as da
import socket
import sys
from pathlib import Path
import models.predict as predict
#pytesseract.pytesseract.tesseract_cmd=r'C:/Program Files/Tesseract-OCR/tesseract.exe'
#sys.path.append(Path("D:/Users/Document D/project_dofus/my_bot"))
#model_all_r = "models/model_r_800/model.pb"
#label_all_r = "models/model_r_800/labels.txt"

#model_poisson = "models/model_poisson/model.pb"
#label_poisson = "models/model_poisson/labels.txt"
model_bois = "models/model_bois_i3/model.pb"
label_bois = "models/model_bois_i3/labels.txt"
model_poisson = "models/model_poisson_i15/model.pb"
label_poisson = "models/model_poisson_i15/labels.txt"
od_model_poisson = predict.load_model(MODEL_FILENAME = model_poisson,LABELS_FILENAME = label_poisson)
od_model_bois = predict.load_model(MODEL_FILENAME = model_bois, LABELS_FILENAME = label_bois)

print("ca va commencer")
time.sleep(5)
pos_joueur = da.coordonnées_joueur((500,500))
a = 0

circuit_dragoeuf = m.circuit_dragoeuf()       
circuit_porco = m.circuit_porco()   # charge le parcours
circuit = circuit_dragoeuf +  circuit_porco 
while True :                                    
    for map in circuit :                       # pour chaque map du parcours
        time.sleep(2)
        if da.magasin_open() == True :                  # verifier que l'interface magasin est fermé
            da.magasin_close()
        try :                                           #lecture ocr de la map actuelle
            map_actuelle = da.my_map()
        except :
            print("error detecting map")
            map_actuelle = map.map
            da.travel(map.map,10) 
        if not da.eguals_map(map_actuelle, map.map) :                    # verifier que la map actuelle en jeu est bien la map sur laquel on travaille
            da.travel(map.map,da.distance_map(map_actuelle,map.map)*10)     
 
        pyautogui.keyDown("y")                          #surbrillance des ressources de la map en cours
        image = pyautogui.screenshot(region=v.region_gameplay)  #screenshot de la region de jeu
        time.sleep(1)
        pyautogui.keyUp("y")                            # fin de surbrillance
        w,h = image.size
        
        # detection des IA ressources
        predictions_bois = od_model_bois.predict_image(image)
        predictions_poisson = od_model_poisson.predict_image(image)
        
        # liste des zones boxes des ressources
        boudingBoxes_poisson = da.list_predictions_boundingBox(predictions_poisson,0.3) # liste des zones boxes des ressources
        boudingBoxes_bois = da.list_predictions_boundingBox(predictions_bois,0.4)
        
        #save map for retrain  od_model
        #da.save_map(image,"bois",predictions_bois)
        #da.save_map(image,"poisson",predictions_poisson)
        
        #list position click x,y ressource 
        list_click_bois = da.list_click_bois(boudingBoxes_bois, w,h)
        list_click_poisson = da.list_click_poisson(boudingBoxes_poisson, w,h)
        
        
        list_click_desordonne = da.list_click_filter(list_click_bois + list_click_poisson)    # filtre les positions pour eviter un changement de map
        list_click = da.order_click(pos_joueur,list_click_desordonne)
        print(f"map : {map.map}, ressource : {len(list_click)}, {list_click}")
        for click in list_click :                       # liste des ressources a recolter
            #if da.is_connected() == False :             # verification de la connexion internet = actif
                   # da.deconnexion()
            while da.is_connected == False :
                time.sleep(30)
                #da.connexion()
        
            x,y = click
            da.dofus_click(x,y,0.3,5.5)                 # recolte de la ressources
            if da.combat_debut() :
                print("debut combat")
                time.sleep(0.5)
                pyautogui.press("f1")
                da.combat_attaque()
                print("fin du combat")
        time.sleep(7)
        
        for pos in map.next_map :                               # deplacement du personnage jusqu'a la prochaine map de recolte
            x,y = pos
            da.dofus_click(x,y,0.3,0)
            pos_joueur = da.coordonnées_joueur(pos)
            da.changement_map(pyautogui.screenshot(region = v.region_map ))
        print("_____________________________________")
    
    # une fois le parcours fini direction la banque amakna déposer les ressources
    a += 1
    if (a%2) == 0 :
        da.go_bank_amakna(map.map)
        da.travel("-1,24",da.distance_map("2,-2","-1,24")) #retour au point de départ du parcours
