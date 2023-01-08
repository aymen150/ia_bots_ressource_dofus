
import sys
from pathlib import Path
import cv2
import pytesseract
import time
import numpy as np
from PIL import Image
import pyautogui
import py as v
import py.map as m
import socket
import random as rand
from math import sqrt
from random import randint
import jaro

#######################################################################################################
#######################################################################################################
################    T   R   A   I   T   E   M   E   N   T       I   M   A   G   E   ###################
#######################################################################################################
#######################################################################################################

def traitement_image_map(image) : 
    data = np.array(image)   # "data" is a height x width x 4 numpy array
    red, green, blue  = data.T # Temporarily unpack the bands for readability
    ecriture_noir = ((red < v.color_pos_dofus_p[0]) & (red > v.color_pos_dofus_m[0])) & ((green < v.color_pos_dofus_p[1] ) & (green > v.color_pos_dofus_m[1] )) & ((blue < v.color_pos_dofus_p[2] ) &  (blue > v.color_pos_dofus_m[2] ))
    fond_blanc = (ecriture_noir == False)
    data[..., :][fond_blanc.T] = (255,255,255) # Transpose back needed
    data[..., :][ecriture_noir.T] = (0,0,0) # Transpose back needed
    return Image.fromarray(data)


def traitement_image_bouton_pret(image) :
    data = np.array(image)   # "data" is a height x width x 4 numpy array
    red, green, blue  = data.T # Temporarily unpack the bands for readability
    ecriture_noir = ((red < v.color_bouton_pret[0] + 50)  & (green < v.color_bouton_pret[1] + 50) & (blue < v.color_bouton_pret[2] + 50))
    fond_blanc = (ecriture_noir == False)
    data[..., :][fond_blanc.T] = (255,255,255) # Transpose back needed
    data[..., :][ecriture_noir.T] = (0,0,0) # Transpose back needed
    return Image.fromarray(data)

def traitement_image_PA_PM(image) :
    data = np.array(image) 
    red, green, blue = data.T 
    areas_PA = ( red > v.color_PA_PM[0] - 100 ) & (green > v.color_PA_PM[0] - 100 ) & (blue > v.color_PA_PM[0] - 100) 
    areas_background = (areas_PA == False) 
    data[..., :][areas_background.T] = (255,255,255) # Transpose back needed
    data[..., :][areas_PA.T] = (0,0,0)
    return Image.fromarray(data)


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

def minDistance_combat(pos,l) :
    if len(l) > 0 :
        mini = Distance(pos,l[0])
        mini_pos = l[0]
        for p in l : 
            mini_tmp = Distance(pos,p)
            if mini_tmp < mini :
                mini = mini_tmp
                mini_pos = p
        return mini_pos
"""
def order_click(pos,list_click):
    new_list = []
    min_pos = pos
    for i in range(0,len(list_click)) :
        min_pos = minDistance(min_pos,list_click)
        new_list.append(min_pos)
        list_click.remove(min_pos)
    return new_list
"""
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

def click_in_list_bounding(click, list) :
    x,y = click
    
    for l in list :
        x1_l,y1_l,x2_l,y2_l  = l
        if x1_l < x and x < x2_l and y1_l < y and y < y2_l :
            return True
    return False

def list_click_filter(liste_click) :
    return list(filter(lambda pos: pos[1][0] >= v.left and pos[1][0] <= v.right and pos[1][1] >= v.top and pos[1][1] <= v.down , liste_click))


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




#######################################################################################################
#######################################################################################################
##################  C   H   A   N   G   E   M   E   N   T       M   A   P     #########################
#######################################################################################################
#######################################################################################################  
     
def filtre_my_map(map : str ) -> str :
    map = map.replace(".",",")
    characters = "-0123456789,"
    string = ''.join( x for x in map if x in characters)
    m = []
    if string.count(',') == 1 :
        m = string.split(",")
    if string.count(',') == 2 :
        m = string.split(",")[:-1]
    
    if len(m) == 2 :
        return f"{m[0]},{m[1]}"
    else :
        return None

def eguals_map(map_1,map_2):
    number = "0123456789"
    map_1f = ''.join( x for x in map_1 if x in number)
    map_2f = ''.join( x for x in map_2 if x in number)
    return (map_1f == map_2f)


def my_map() :
    resize_definition = [(100,25),(300,80),(300,60),(300,100),(400,80)]
    option = ['--psm 10 --oem 3 ','--psm 6 --oem 3 ','--psm 6',None]
    for config in option :
        for resize in resize_definition :
            map = my_map_dofus(resize, config)
            if map_valide(map) == True :
                return map
    print("Map non detécté : map(999,999) renvoyé")
    return "999,999"

def map_valide(map):
    if map == None :
        return False
    else :
        try :
            x,y = [int(pos) for pos in map.split(",")]
            if x > -100 and x <100 and y <100 and y > -100 :
                return True
            else :
                return False
        except :
            return False

def my_map_dofus(resize, config : str )  :
    """
    Effectue un screenshot de la region v.region_map
    modification des couleurs du screen ==> meilleur performance de l'ocr
    tentative de lecture ocr de l'image

    Returns:
        str: retourne la map actuelle du joueur
    """
    map = ""
    image = pyautogui.screenshot(region = v.region_map ).resize(resize)   # "data" is a height x width x 4 numpy array
    image = traitement_image_map(image)
    map = pytesseract.image_to_string(image, lang="eng", config=config)
    
    return filtre_my_map(map)
    
def changement_map(image, x,y):
    a = 0
    while image == pyautogui.screenshot(region = v.region_map ) :
        print("changement de map")
        time.sleep(1)
        if (a % 4) == 0 :
            dofus_click(x,y,0.3,0)
        a +=1
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
    dofus_press("enter",3)
    dofus_press("enter",t-1)
    pyautogui.click(v.x_tchat,v.y_tchat-30)
    time.sleep(1)

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
##################################   B   A   N   Q   U   E     ########################################
#######################################################################################################
#######################################################################################################  

def go_bank(my_pos:str ,region:str = "Amakna") :
    match region :
        case "Amakna" :
            pos_banque = v.pos_banque_amakna
            x_entre_banque, y_entre_banque = v.x_entre_banque_amakna, v.y_entre_banque_amakna
            x_sortie_banque, y_sortie_banque = v.x_sortie_banque_amakna, v.y_sortie_banque_amakna
            x_coffre_guilde_ouvrir, y_coffre_guilde_ouvrir = v.x_coffre_guilde_amakna_ouvrir, v.y_coffre_guilde_amakna_ouvrir
        case "Sufokia" :
            pos_banque = v.pos_banque_sufokia
            x_entre_banque, y_entre_banque = v.x_entre_banque_sufokia, v.y_entre_banque_sufokia
            x_sortie_banque, y_sortie_banque = v.x_sortie_banque_sufokia, v.y_sortie_banque_sufokia
            x_coffre_guilde_ouvrir, y_coffre_guilde_ouvrir = v.x_coffre_guilde_sufokia_ouvrir, v.y_coffre_guilde_sufokia_ouvrir
        case "Bonta" :
            pos_banque = v.pos_banque_bonta
            x_entre_banque, y_entre_banque = v.x_entre_banque_bonta, v.y_entre_banque_bonta
            x_sortie_banque, y_sortie_banque = v.x_sortie_banque_bonta, v.y_sortie_banque_bonta
            x_coffre_guilde_ouvrir, y_coffre_guilde_ouvrir = v.x_coffre_guilde_bonta_ouvrir, v.y_coffre_guilde_bonta_ouvrir  
        case "Pandala" : 
            pos_banque = v.pos_banque_pandala
            x_entre_banque, y_entre_banque = v.x_entre_banque_pandala, v.y_entre_banque_pandala
            x_sortie_banque, y_sortie_banque = v.x_sortie_banque_pandala, v.y_sortie_banque_pandala
            x_coffre_guilde_ouvrir, y_coffre_guilde_ouvrir = v.x_coffre_guilde_pandala_ouvrir, v.y_coffre_guilde_pandala_ouvrir  

    enter_bank(my_pos, pos_banque, x_entre_banque ,y_entre_banque )
    ouvrir_coffre_guilde(x_coffre_guilde_ouvrir, y_coffre_guilde_ouvrir)
    transfert_coffre_ressource("ressource",30)
    transfert_coffre_ressource("potion",10)
    fermer_coffre_guilde()
    out_bank(x_sortie_banque, y_sortie_banque)       
            
def enter_bank(my_pos:str, pos_bank : str, entre_bank_x, entre_bank_y):
    """
    Args:
        my_pos (str): ma map actuelle dans le jeu
    
    déplace le personnage jusqu'à la banque d'amakna et transfert tout les élements du personnage en banque
    """
    travel(pos_bank,distance_map(pos_bank,my_pos)*10) # voyage jusqu'a la banque (compte le nb de map * 10 secondes )
    dofus_click(entre_bank_x, entre_bank_y,0.5,12) # click entrer dans la banque
   
def out_bank(sortie_banque_x, sortie_banque_y):
    dofus_click(sortie_banque_x, sortie_banque_y ,0.5,3) #clic quitter la banque

def ouvrir_coffre_guilde(coffre_guilde_x, coffre_guilde_y):
    dofus_click(coffre_guilde_x,coffre_guilde_y,0.5,7)
    
def fermer_coffre_guilde():
    dofus_click(v.x_coffre_guilde_fermer,v.y_coffre_guilde_fermer,0.5,4)

def transfert_coffre_ressource(onglet_inventaire, nb_ressource) :
    match onglet_inventaire :
        case "ressource" :
            dofus_click(v.x_coffre_guilde_onglet_ressource, v.y_coffre_guilde_onglet_ressource,0.5,4)
        case "potion" :
            dofus_click(v.x_coffre_guilde_onglet_potion, v.y_coffre_guilde_onglet_potion, 0.5,2)
    pyautogui.keyDown("ctrl")#fermetuer de la fenetre dofus
    for i in range(nb_ressource) : 
        pyautogui.doubleClick(x = v.x_coffre_guilde_ressource, y= v.y_coffre_guilde_ressource)
        time.sleep(rand.uniform(0.9,1.9))
    pyautogui.keyUp("ctrl")
    time.sleep(5)
    
def transfert_bank_all(hibou_banque_x, hibou_banque_y):
    dofus_click(hibou_banque_x, hibou_banque_y,0.5,3) # clique parler à l hibou
    dofus_click(v.x_consulter_banque, v.y_consulter_banque,0.5,5) #clic consulter sa banque
    dofus_click(v.x_menu_transfert_banque, v.y_menu_transfert_banque,1,1) #clic transfert avancé
    dofus_click(v.x_all_transfert_banque, v.y_all_transfert_banque,0.5,3) #clic tout transferer
    dofus_click(v.x_fermer_banque_banque, v.y_fermer_banque_banque,0.5,2) #clic fermer banque
 


#######################################################################################################
#######################################################################################################
##################################    C   O   M   B   A   T     #######################################
#######################################################################################################
####################################################################################################### 

def nombre_PA() : 
    image = pyautogui.screenshot( region = v.region_PA ).resize((300,300))
    image = traitement_image_PA_PM(image) 
    return pytesseract.image_to_string(image, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')


def nombre_PM() :
    pm_bool = True
    resize_definition = [(300,300),(60,60),(100,50),(300,100),(50,20)]
    image = pyautogui.screenshot( region = v.region_PM )
    image = traitement_image_PA_PM(image)
    pm = pytesseract.image_to_string(image, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
    if pm != "" :
            pm = int(pm)
            return pm
    else :
        for size in resize_definition :
            image = pyautogui.screenshot( region = v.region_PM ).resize(size)
            image = traitement_image_PA_PM(image)
            pm = pytesseract.image_to_string(image, lang='eng', config='--psm 10 --oem 3 -c tessedit_char_whitelist=0123456789')
            if pm != "" :
                pm = int(pm)
                return pm
    return 0
    
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
    image = pyautogui.screenshot( region = v.region_bouton_pret ).resize((300,200))
    txt = pytesseract.image_to_string(image)
    score = jaro.jaro_metric("PRET",txt)
    fight_debut = False 
    if score > 0.5:
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
    txt_1 = pytesseract.image_to_string(pyautogui.screenshot( region = v.region_bouton_fin_de_tour ).resize((300,200)))
    txt_2 = pytesseract.image_to_string(pyautogui.screenshot( region = v.region_bouton_pret  ).resize((300,200)))
    score_pret = jaro.jaro_metric("PRET", txt_1)
    score_tour = jaro.jaro_metric("TERMINER SON TOUR", txt_2)
    fight_finish = False 
    if score_pret > 0 or score_tour > 0.3 :
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
    pyautogui.moveTo( v.pos_hors_zone_combat, duration=0.5)
    time.sleep(t)
    
def my_tourn():
    """ 
    Screen la time line du joueur en combat.
    Returns:
        boolean: True si c'est a notre joueur de jouer, sinon False
    """
    screen = pyautogui.screenshot(region = v.region_tour_de_jeu)
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

def direction_deplacement_clique(perso, direction):
    match direction :
            case "N" : 
                deplacement = add_deplacement(perso, v.dep_N_2pm)
                i = 0
            case "NO" :
                deplacement = add_deplacement(perso, v.dep_NO_2pm)
                i = 1
            case "O" :
                deplacement = add_deplacement(perso, v.dep_O_2pm)
                i = 2
            case "SO" :
                deplacement = add_deplacement(perso, v.dep_SO_2pm)
                i = 3
            case "S" :
                deplacement = add_deplacement(perso, v.dep_S_2pm)
                i = 4
            case "SE" :
                deplacement = add_deplacement(perso, v.dep_SE_2pm)
                i = 5
            case "E" :
                deplacement = add_deplacement(perso, v.dep_E_2pm)
                i = 6
            case "NE" :
                deplacement = add_deplacement(perso, v.dep_NE_2pm)
                i = 7
    return deplacement, i

def deplacer_mon_perso_2pm(perso, ennemi, PM : int) :
    liste_direction = ["N","NO","O","SO","S","SE","E","NE"]
    direction = direction_ennemi(perso, ennemi)
    indice_direction = liste_direction.index(direction)
    a  = 0
    while PM == int(nombre_PM()) :
        if a > 1 :
            print("new : ", liste_direction[indice_direction] )
        deplacement_clique, i = direction_deplacement_clique(perso, liste_direction[indice_direction])
        dofus_click(deplacement_clique[0],deplacement_clique[1],0.5,1.5)
        indice_direction = (i-1) 
        if indice_direction == -1 :
            indice_direction = 7
        a+=1
    return deplacement_clique

def deplacer_mon_perso(perso,ennemi) :
    distance_ennemi = Distance(perso, ennemi)
    PM = int(nombre_PM())
    while distance_ennemi > v.distance_3PO and PM > 1:
        perso = deplacer_mon_perso_2pm(perso,ennemi, PM)
        distance_ennemi = Distance(perso, ennemi)
        PM = int(nombre_PM())
    return perso
        
def combat_attaque() :
    """
    Tant que le combat est en cours :
        Attaque un ennemi à partir d'un sort et de sa position dans l'infobulle 
        puis passe son tour.
    
    ferme le résumé du combat    
    """
    attaque(v.x_sort_1,v.y_sort_1,v.x_ennemi_1,v.y_ennemi_1,1)
    if combat_fini() == False : 
        attaque(v.x_sort_1,v.y_sort_1,v.x_ennemi_2,v.y_ennemi_2,1)
    if  combat_fini() == False : 
        attaque(v.x_sort_1,v.y_sort_1,v.x_ennemi_1,v.y_ennemi_1,1)
    if combat_fini() == False : 
        attaque(v.x_sort_1,v.y_sort_1,v.x_ennemi_2,v.y_ennemi_2,1)
            
    dofus_press("f1",1) 
    time.sleep(1)
    

def combat(predictions,w,h) :
    """
    Tant que le combat est en cours :
        Attaque un ennemi à partir d'un sort et de sa position dans l'infobulle 
        puis passe son tour.
    
    ferme le résumé du combat    
    """

    list_ennemis = [list_click(x["boundingBox"],w, h,1) for x in predictions if  ((x["tagName"] == "ennemi") and (x["probability"]) > 0.4)] 
    list_allie = [list_click(x["boundingBox"],w, h,1) for x in predictions if  ((x["tagName"] == "allie") and (x["probability"]) > 0.1)] 
    #print(list_ennemis, list_allie)
    if len(list_ennemis) == 0 or len(list_allie) == 0 :
        print(predictions)
        combat_attaque()
    else :
        mon_perso = list_allie[0]
        plus_proche_ennemi = minDistance_combat(mon_perso, list_ennemis)
        x_ennemi,y_ennemi = plus_proche_ennemi
        mon_perso = deplacer_mon_perso(mon_perso,  plus_proche_ennemi)
        distance_ennemi = Distance(mon_perso,plus_proche_ennemi)
        if distance_ennemi <= v.distance_12PO + 10 : 
            attaque(v.x_sort_1,v.y_sort_1,x_ennemi,y_ennemi,1)
            if combat_fini() == False : 
                attaque(v.x_sort_1,v.y_sort_1,x_ennemi,y_ennemi,1)
            if  combat_fini() == False : 
                attaque(v.x_sort_2,v.y_sort_2,x_ennemi,y_ennemi,1)        
    dofus_press("f1",1) 






#######################################################################################################
#######################################################################################################
##################################    R     E   C   O   L   T   E     #################################
#######################################################################################################
#######################################################################################################  

def predictions_ressources(predictions, w_size, h_size, proba_poisson = 0.5, proba_bois = 0.5, proba_plante = 0.5) :
    
    list_click_poisson = [x for x in predictions if  ((x["tagName"] == "poisson") and (x["probability"]) > proba_poisson)] 
    list_click_bois =  [x for x in predictions if ((x["tagName"] == "bois") and (x["probability"]) > proba_bois)] 
    list_click_plante =  [x for x in predictions if ((x["tagName"] == "plante") and (x["probability"]) > proba_plante)] 
    return list_click_poisson + list_click_plante + list_click_bois

def predictions_to_click(predictions, w_size, h_size, proba_poisson = 0.5, proba_bois = 0.5, proba_plante = 0.5) :
    """
    Args:
        predictions (_type_): _description_
        w_size (_type_): _description_
        h_size (_type_): _description_
        proba_poisson (float, optional): _description_. Defaults to 0.5.
        proba_bois (float, optional): _description_. Defaults to 0.5.
        proba_plante (float, optional): _description_. Defaults to 0.5.

    Returns:
        _type_: Return a list : [(BoundingBox, pos_click),...]
    """
    list_click_poisson = [pos_bounding_click(x["boundingBox"],w_size, h_size,1) for x in predictions if  ((x["tagName"] == "poisson") and (x["probability"]) > proba_poisson)] 
    list_click_bois =  [pos_bounding_click(x["boundingBox"],w_size, h_size,0.8) for x in predictions if ((x["tagName"] == "bois") and (x["probability"]) > proba_bois)] 
    list_click_plante =  [pos_bounding_click(x["boundingBox"],w_size, h_size,1) for x in predictions if ((x["tagName"] == "plante") and (x["probability"]) > proba_plante)] 
    return list_click_poisson + list_click_plante + list_click_bois


def pos_bounding_click(boundingBox, w_size, h_size, hauteur=1) :
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
    
    return ((x1 + v.region_gameplay[0] ,
             y1 + v.region_gameplay[1],
             x2 + v.region_gameplay[0],
             y2 + v.region_gameplay[1]),(round(x3,1),round(y3,1)))

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
    
    return ((round(x3,1),round(y3,1)))


def minDistance(pos,list_bounding_click):
    if len(list_bounding_click) > 0 :
        min_bounding_click = list_bounding_click[0]
        min_distance = Distance(pos, min_bounding_click[1])
        for bounding_click in list_bounding_click :
            distance_tmp = Distance(pos, bounding_click[1])
            if min_distance > distance_tmp :
                min_distance = distance_tmp
                min_bounding_click = bounding_click
        return min_bounding_click
            




"""      
def click_in_ennemi(x,y,w,h,boudingBoxes_monster) :
    for boxes in boudingBoxes_monster : 
        x1,y1 = boxes[0] * w ,boxes[1] * h,
        x2,y2 = x1 + boxes[2] * w , y1 + boxes[3] * h
        if (x1 <= x and x <= x2) and (y1 <= y and y <= y2) :
            return True
    return False 
"""     