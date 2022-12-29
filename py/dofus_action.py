
import sys
from pathlib import Path
import cv2
import pytesseract
import time
import numpy as np
from PIL import Image
import pyautogui
import py.variable as v
import py.map as m
import socket
from math import sqrt
from random import randint


#######################################################################################################
#######################################################################################################
##################################    O     U   T   I   L   S   #######################################
#######################################################################################################
####################################################################################################### 

def Sqr(a):
    return a*a
 
def Distance(pos1, pos2):
    x1,y1 = pos1[0],pos1[1]
    x2,y2 = pos2[0],pos2[1]
    return sqrt(Sqr(y2-y1)+Sqr(x2-x1))

def minDistance(pos,l) :
    if len(l) > 0 :
        mini = Distance(pos,l[0])
        mini_pos = l[0]
        for p in l : 
            mini_tmp = Distance(pos,p)
            if mini_tmp < mini :
                mini = mini_tmp
                mini_pos = p
        return mini_pos

def order_click(pos,list_click):
    new_list = []
    min_pos = pos
    for i in range(0,len(list_click)) :
        min_pos = minDistance(min_pos,list_click)
        new_list.append(min_pos)
        list_click.remove(min_pos)
    return new_list

def dofus_click(x,y,d,t):
    """
    Clique à la position x et y

    Args:
        x (int): coordonnée x du clique
        y (int): coordonnée y du clique
        d (float): durée en seconde du déplacement de la souris juqu'au point x,y
        t (float): temps d'attente en seconde apres le click
    """
    pyautogui.click(x,y,duration=d)
    time.sleep(t)

def click_in_list(click, list) :
    x,y = click
    
    for l in list :
        x_l,y_l = l
        if x_l - 10 < x and x < x_l + 10 and y_l - 10 < y and y < y_l + 10 :
            return True
    return False

def list_click(boundingBox, w_size, h_size, hauteur=1) :
    """
    Args:
        boundingBox (list[[boxes],..]): list contenant les coordonnées des boxes proportielle à l'image entré dans le model
        w_size (int): longueur du screenshoot en pixel entré dans le model
        h_size (int): largeur du screenshoot en pixel entré dans le model
        hateur (float): permet de pointer vers le haut(<1) ou le bas (>1) de la boxes, 1 = centre
        
    fnct:
        v.region_gameplay[0] (int): decalage du x screenshoot par rapport au bord gauche de l'ecran
        v.region_gameplay[1] (int): decalage du y screenshoot par rapport au bord haut de l'ecran
    Returns:
        list[(x,y), ..]: renvoi une liste de position (x,y) (en pixel) à l'echelle de l'écran des ressources detecté par le model
    """
    x1, y1 = w_size * boundingBox[0], h_size * boundingBox[1]
    x2, y2 = x1 + (w_size * boundingBox[2]) , y1 + (h_size * boundingBox[3]* hauteur) # *1.5 selectionne le bas de la boxes
    x3 = ((x1 + x2) / 2 ) + v.region_gameplay[0]
    y3 = ((y1 + y2) / 2 ) + v.region_gameplay[1]
    return (round(x3,1),round(y3,1))

def list_click_filter(liste_click) :
    return list(filter(lambda pos: pos[0] >= v.left and pos[0] <= v.right and pos[1] >= v.top and pos[1] <= v.down , liste_click))


def dofus_press(cmd,t) : 
    """
    Effectue un raccourci clavier
    Args:
        cmd (str or list[str]): raccourci clavier
        t (flaot): temps d'attente en seconde apres le raccourci clavier
    """
    pyautogui.press(cmd)
    time.sleep(t)

def is_connected():
    """
    Vérifie que la connexion internet est fonctionnelle

    Returns:
        boolean: True, la connexion internet est fonctionnelle sinon False
    """
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        socket.create_connection(("1.1.1.1", 443))
        return True
    except OSError:
        pass
    return False

def ajustement_decran(imageSize) :
    x,y = imageSize
    return x + v.region_gameplay[0], y + v.region_gameplay[1]

def deconnexion() : 
    """
    ferme la page actif de jeu
    """
    time.sleep(4)
    pyautogui.keyDown("alt")#fermetuer de la fenetre dofus
    pyautogui.press("f4")
    pyautogui.keyUp("alt")
    
def connexion():
    """
    connecte un comte en jeu
    """
    time.sleep(30)  
    dofus_click(v.x_launcher, v.y_launcher,0.7,20) # open launcher
    dofus_click(v.x_scroller_multi_compte,v.y_scroller_multi_compte,0.7,2) # open scroller multi compte
    dofus_click(v.x_select_roublar, v.y_select_roublar,0.5,60) # connec to roublar compte 
    pyautogui.press("enter")

def magasin_open():
    txt = pytesseract.image_to_string(pyautogui.screenshot(region = v.region_magasin))
    if txt == "":
        return False 
    else :
        return True

def magasin_close():
    dofus_click(v.x_close_magasin,v.y_close_magasin,0.3,1)
    
    
 


#######################################################################################################
#######################################################################################################
##################  C   H   A   N   G   E   M   E   N   T       M   A   P     #########################
#######################################################################################################
#######################################################################################################  
     
def filtre_my_map(map : str ) -> str :
    characters = "-0123456789,"
    string = ''.join( x for x in map if x in characters)
    if string.count(',') == 1 :
        m = string.split(",")
    if string.count(',') == 2 :
        m = string.split(",")[:-1]
    return f"{m[0]},{m[1]}"

def eguals_map(map_1,map_2):
    number = "0123456789"
    map_1f = ''.join( x for x in map_1 if x in number)
    map_2f = ''.join( x for x in map_2 if x in number)
    return (map_1f == map_2f)

def my_map()  :
    """
    Effectue un screenshot de la region v.region_map
    modification des couleurs du screen ==> meilleur performance de l'ocr
    tentative de lecture ocr de l'image

    Returns:
        str: retourne la map actuelle du joueur
    """
    data = np.array(pyautogui.screenshot(region = v.region_map ))   # "data" is a height x width x 4 numpy array
    red, green, blue  = data.T # Temporarily unpack the bands for readability
    ecriture_noir = ((red < v.color_pos_dofus_p[0]) & (red > v.color_pos_dofus_m[0])) & ((green < v.color_pos_dofus_p[1] ) & (green > v.color_pos_dofus_m[1] )) & ((blue < v.color_pos_dofus_p[2] ) &  (blue > v.color_pos_dofus_m[2] ))
    fond_blanc = (ecriture_noir == False)
    data[..., :][fond_blanc.T] = (255,255,255) # Transpose back needed
    data[..., :][ecriture_noir.T] = (0,0,0) # Transpose back needed
    return filtre_my_map(pytesseract.image_to_string(Image.fromarray(data)))
    
def changement_map(image):
    while image == pyautogui.screenshot(region = v.region_map ) :
        time.sleep(1)

def distance_map(pos_d :str, pos_a : str): 
    """_summary_

    Args:
        pos_d (str): map actuelle
        pos_a (str): map d'arrivée

    Returns:
        int : compte le nombre de map entre la map actuelle et la map de destination
    """
    x_pos_d, y_pos_d = pos_d.split(',')
    x_pos_a, y_pos_a = pos_a.split(',')
    x = abs(int(x_pos_a) - int(x_pos_d))
    y = abs(int(y_pos_a) - int(y_pos_d))
    return abs(x + y)

def travel(pos : str,t:float) : # effectue un voyage jusqu'a la map pos, t -> durée du voyage en s
    """Effectue un voyage autopilité en dragodinde jusqu'a une map de destination

    Args:
        pos (str): map de destination
        t (float): durée en seconde du voyage
    """
    time.sleep(3)
    travel = "/travel" + " " + pos
    pyautogui.click(v.x_tchat,v.y_tchat,duration=0.3)
    pyautogui.press('left', presses = 20)
    pyautogui.press('delete', presses = 30)
    pyautogui.write(travel,interval =0.1)
    dofus_press("enter",1.5)
    dofus_press("enter",t-1)
    pyautogui.click(v.x_tchat,v.y_tchat-30)
    time.sleep(1)

def go_bank_amakna(my_pos:str):
    """
    Args:
        my_pos (str): ma map actuelle dans le jeu
    
    déplace le personnage jusqu'à la banque d'amakna et transfert tout les élements du personnage en banque
    """
    travel("2,-2",distance_map("2,-2",my_pos)*10) # voyage jusqu'a la banque (compte le nb de map * 10 secondes )
    dofus_click(v.x_entre_banque_amakna,v.y_entre_banque_amakna,0.5,7) # click entrer dans la banque
    dofus_click(v.x_hibou_banque_amakna, v.y_hibou_banque_amakna,0.5,5) # clique parler à l hibou
    dofus_click(v.x_consulter_banque_amakna, v.y_consulter_banque_amakna,0.5,3) #clic consulter sa banque
    dofus_click(v.x_menu_transfert_banque_amakna, v.y_menu_transfert_banque_amakna,1,1) #clic transfert avancé
    dofus_click(v.x_all_transfert_banque_amakna, v.y_all_transfert_banque_amakna,0.5,3) #clic tout transferer
    dofus_click(v.x_fermer_banque_banque_amakna, v.y_fermer_banque_banque_amakna,0.5,2) #clic fermer banque
    dofus_click(v.x_sortie_banque_amakna, v.y_sortie_banque_amakna,0.5,2) #clic quitter la banque

def coordonnées_joueur(pos) :
    if   pos ==  v.dep_gauche_haut :
        return v.dep_droite_haut
    elif pos ==  v.dep_gauche_milieu:
        return v.dep_droite_milieu
    
    elif pos == v.dep_gauche_bas   :
        return v.dep_droite_bas
    
    elif pos == v.dep_droite_haut  :
        return v.dep_gauche_haut
    
    elif pos == v.dep_droite_milieu:
        return v.dep_gauche_milieu
    
    elif pos == v.dep_droite_bas   :
        return v.dep_gauche_bas
    
    elif pos ==  v.dep_haut_droite :
        return v.dep_bas_droite
    
    elif pos ==  v.dep_haut_milieu :
        return v.dep_bas_milieu
    
    elif pos == v.dep_haut_gauche  :
        return v.dep_bas_gauche
    
    elif pos == v.dep_bas_droite   : 
        return v.dep_haut_droite
    
    elif pos == v.dep_bas_milieu   :
        return v.dep_haut_milieu
    
    elif pos == v.dep_bas_gauche   :
        return v.dep_haut_gauche
    else :
        return (500,500)



#######################################################################################################
#######################################################################################################
##################################    C   O   M   B   A   T     #######################################
#######################################################################################################
####################################################################################################### 

def nombre_PA() : 
    img = pyautogui.screenshot( region = v.region_PA ).resize((300,300))
    data = np.array(img) 
    red, green, blue = data.T 
    areas_PA = ( red > v.color_PA[0] - 20 ) & (green > v.color_PA[0] - 20 ) & (blue > v.color_PA[0] - 20) 
    areas_background = (areas_PA == False) 
    data[..., :][areas_background.T] = (255,255,255) # Transpose back needed
    data[..., :][areas_PA.T] = (0,0,0)
    return pytesseract.image_to_string(Image.fromarray(data))

def combat_debut() : 
    """ 
    Effectue un screenshot de l'ecran à la position v.region_bouton_pret
    Tentative d'ocr sur le screenshot
    Si du text est reconnue:
        (ex: "pret" ou "terminé son tour") ==> combat en cours
    Sinon :
        aucun combat en cours

    Returns:
        boolean : true si un combat est en cours, sinon false
    """
    txt = pytesseract.image_to_string(pyautogui.screenshot( region = v.region_bouton_pret  ))
    fight_debut = False 
    if txt != "":
        fight_debut = True 
    else :
        fight_debut = False
    return fight_debut

def combat_fini() : 
    """ 
    Effectue un screenshot de l'ecran à la position v.region_bouton_pret
    Tentative d'ocr sur le screenshot
    Si du text est reconnue:
        (ex: "pret" ou "terminé son tour") ==> combat en cours
    Sinon :
        aucun combat en cours

    Returns:
        boolean : false si un combat est en cours, sinon true
    """
    txt = pytesseract.image_to_string(pyautogui.screenshot( region = v.region_bouton_pret ))
    fight_finish = False 
    if txt != "" :
        fight_finish = False 
    else :
        fight_finish = True
    return fight_finish 

def attaque(x_sort,y_sort,x_ennemi,y_ennemi,t=1) :
    """ Attaque un ennemi à partir d'un sort et de sa position dans l'infobulle

    Args:
        x_sort (_type_): cordonnnée x d'un sort de mon personnage
        y_sort (_type_): coordonnée y d'un sort de mon personnage
        x_ennemi (_type_): coordonnée x de mon ennemi dans l'infobulle
        y_ennemi (_type_): cordonnée y de mon ennemi dans l'infobulle
    """
    dofus_click(x_sort,y_sort,0.5,0.3)
    dofus_click(x_ennemi,y_ennemi,0.3,0.2)
    pyautogui.moveTo( v.dep_droite_milieu, duration=0.5)
    time.sleep(t)
    
def my_tourn():
    """ 
    Screen la time line du joueur en combat.
    Returns:
        boolean: True si c'est a notre joueur de jouer, sinon False
    """
    screen = pyautogui.screenshot(region = (786,1004,464,17))
    red, green, blue  = np.array(screen).T # Temporarily unpack the bands for readability
    my_tourn = ((red == v.color_tour_de_jeu[0]) & (green == v.color_tour_de_jeu[1]) & (blue == v.color_tour_de_jeu[2]))
    return True in my_tourn

def add_deplacement(perso, deplacement) :
    perso_x , perso_y = perso
    deplacement_x , deplacement_y = deplacement
    return ((float(perso_x) + float(deplacement_x)),(float(perso_y) + float(deplacement_y)))
            
def direction_ennemi(mon_perso,ennemi) : 
    perso_x , perso_y  = [float(pos) for pos in mon_perso]
    ennemi_x ,ennemi_y = [ float(dep) for dep in ennemi]
    
    if ((perso_y - 7) <= ennemi_y ) and (ennemi_y <= (perso_y +7)) :
        if  ennemi_x < perso_x :
            print("O")
            return "O"
        else :
            print("E")
            return "E"
    elif ((perso_x - 7 ) <= ennemi_x) and ( ennemi_x <= (perso_x+7)) :
        if ennemi_y < perso_y:
            print("N")
            return "N"
        else :
            print("S")
            return "S"
    elif (ennemi_y <= (perso_y - 7)) and (ennemi_x <= (perso_x -7)) :
        print("NO")
        return "NO"
    elif (ennemi_y >= (perso_y + 7)) and (ennemi_x <= (perso_x -7)) :
        print("SO")
        return "SO"
    elif (ennemi_y <= (perso_y - 7)) and (ennemi_x >= (perso_x +7)) :
        print("NE")
        return "NE"
    elif (ennemi_y >= (perso_y + 7)) and (ennemi_x >= (perso_x +7)) :
        print("SE")
        return "SE"

def deplacer_mon_perso(perso, ennemi, pm) :
    if pm == 0 :
        return perso
    while pm >= 2 and Distance(perso, ennemi) > 140 : 
        direction = direction_ennemi(perso, ennemi)
        match direction :
            case "N" : 
                perso = add_deplacement(perso, v.dep_N_2pm)
                pm -= 2
            case "O" :
                perso = add_deplacement(perso, v.dep_O_2pm)
                pm -= 2
            case "S" :
                perso = add_deplacement(perso, v.dep_S_2pm)
            case "E" :
                perso = add_deplacement(perso, v.dep_E_2pm)
                pm -= 2
            case "NE" :
                perso = add_deplacement(perso, v.dep_NE_2pm)
                pm -= 2
            case "NO" :
                perso = add_deplacement(perso, v.dep_NO_2pm)
                pm -= 2
            case "SO" :
                perso = add_deplacement(perso, v.dep_SO_2pm)
                pm -= 2
            case "SE" :
                perso = add_deplacement(perso, v.dep_SE_2pm)
                pm -= 2
    return perso
 
def combat_attaque() :
    """
    Tant que le combat est en cours :
        Attaque un ennemi à partir d'un sort et de sa position dans l'infobulle 
        puis passe son tour.
    
    ferme le résumé du combat    
    """
    attaque(v.x_sort_1,v.y_sort_1,v.x_ennemi_1,v.y_ennemi_1,2)
    if combat_fini() == False : 
        attaque(v.x_sort_1,v.y_sort_1,v.x_ennemi_2,v.y_ennemi_2,2)
    if  combat_fini() == False : 
        attaque(v.x_sort_1,v.y_sort_1,v.x_ennemi_1,v.y_ennemi_1,2)
    if combat_fini() == False : 
        attaque(v.x_sort_1,v.y_sort_1,v.x_ennemi_2,v.y_ennemi_2,2)
            
    dofus_press("f1",1) 
    time.sleep(3)
    

def combat(predictions,w,h,pm) :
    """
    Tant que le combat est en cours :
        Attaque un ennemi à partir d'un sort et de sa position dans l'infobulle 
        puis passe son tour.
    
    ferme le résumé du combat    
    """

    list_ennemis = [list_click(x["boundingBox"],w, h,1) for x in predictions if  ((x["tagName"] == "ennemi") and (x["probability"]) > 0.5)] 
    list_allie = [list_click(x["boundingBox"],w, h,1) for x in predictions if  ((x["tagName"] == "allie") and (x["probability"]) > 0.1)] 
    #print(list_ennemis, list_allie)
    if len(list_ennemis) == 0 or len(list_allie) == 0 :
        print(predictions)
        combat_attaque()
    else :
        mon_perso = list_allie[0]
        plus_proche_ennemi = minDistance(mon_perso, list_ennemis)
        x_ennemi,y_ennemi = plus_proche_ennemi
        distance_ennemi = Distance(mon_perso,plus_proche_ennemi)
        
        if  distance_ennemi > v.distance_3PO :
                deplacement = deplacer_mon_perso(mon_perso,plus_proche_ennemi,pm)
                dofus_click(deplacement[0],deplacement[1],1,1)
                distance_ennemi = Distance(deplacement,plus_proche_ennemi)
                
        if distance_ennemi <= v.distance_12PO + 10 : 
            attaque(v.x_sort_1,v.y_sort_1,x_ennemi,y_ennemi,2)
            if combat_fini() == False : 
                attaque(v.x_sort_1,v.y_sort_1,x_ennemi,y_ennemi,2)
            if  combat_fini() == False : 
                attaque(v.x_sort_2,v.y_sort_2,x_ennemi,y_ennemi,2)        
    dofus_press("f1",1) 






#######################################################################################################
#######################################################################################################
##################################    R     E   C   O   L   T   E     #################################
#######################################################################################################
#######################################################################################################  

def predictions_to_click(predictions, w_size, h_size, proba_poisson = 0.5, proba_bois = 0.5, proba_plante = 0.5) :
    
    list_click_poisson = [list_click(x["boundingBox"],w_size, h_size,1) for x in predictions if  ((x["tagName"] == "poisson") and (x["probability"]) > proba_poisson)] 
    list_click_bois =  [list_click(x["boundingBox"],w_size, h_size,1) for x in predictions if ((x["tagName"] == "bois") and (x["probability"]) > proba_bois)] 
    list_click_plante =  [list_click(x["boundingBox"],w_size, h_size,1) for x in predictions if ((x["tagName"] == "plante") and (x["probability"]) > proba_plante)] 
    return list_click_poisson + list_click_plante + list_click_bois









"""      
def click_in_ennemi(x,y,w,h,boudingBoxes_monster) :
    for boxes in boudingBoxes_monster : 
        x1,y1 = boxes[0] * w ,boxes[1] * h,
        x2,y2 = x1 + boxes[2] * w , y1 + boxes[3] * h
        if (x1 <= x and x <= x2) and (y1 <= y and y <= y2) :
            return True
    return False 
"""     