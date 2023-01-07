
import win32api
import time
import pyautogui
import jaro

time.sleep(3)

def append_write(fichier, text) :
    with open(fichier, 'a') as f :
        f.write(text)

def get_click():
    while True :
        x,y = pyautogui.position()
        if win32api.GetKeyState(0x01)<0 :
            return x,y

taille_ecran = pyautogui.screenshot().size

a = input("voulez-vous creer un nouveau fichier de variable ? O/n")

if a == "n" : 
    exit()
    
path_f = f"variable_{taille_ecran[0]}_{taille_ecran[1]}.py"
file = open(path_f, "w")
file.write(f"""
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

dimension_ecran = ({taille_ecran[0]},{taille_ecran[1]})

""")
file.close()
#####################################################################################
print("""
###############################################
############## ZONE DE JEU  ###################
###############################################""")
print("CLIQUER SUR << ENTER >> A QUE FOIS QUE VOUS ETES PRET")
input("""
      bord d'une map hors zone de changement de map
      -> ENTER : cliquer sur x1,y1 :""")
#bord d'une map hors zone de changement de map
left, top = get_click()
input("""
      bord d'une map hors zone de changement de map
      -> ENTER : cliquer sur x2,y2 :""")


right, down = get_click()

append_write(path_f, f"""
left = {left}
right = {right}
top = {top}
down = {down} 
""")

#############################################################""""""
print("""
###############################################
############## BORDURE CARTE  ###################
###############################################
      """)
input("""
      zone de jeu avec zone de changement de map
      -> ENTER : cliquer sur x1,y1 :""")
#bord d'une map hors zone de changement de map
x1, y1 = get_click()
input("""
      zone de jeu avec zone de changement de map
      -> ENTER : cliquer sur x2,y2 :""")
x2, y2 = get_click()

x2 = x2 - x1
y2 = y2 - y1

append_write(path_f, f"""
###############################################
############## BORDURE CARTE  #################
###############################################

region_gameplay = ({x1}, {y1}, {x2}, {y2}) 
""")
#############################################################""""""
print("""
###############################################
#################  TCHAT  #####################
###############################################
""")
input("""
      -> ENTER : cliquer sur x1,y1 :""")

x_tchat, y_tchat = get_click()

append_write(path_f, f"""
##############################################
#################  TCHAT  #####################
############################################### 

x_tchat, y_tchat = {x_tchat},{y_tchat}
""")
#############################################################""""""
print("""
###############################################
###################  POS  #####################
###############################################
""")

input("""
      zone OCR pour changement de map ( !!! Attention prendre map -xx,-xx pour référence)
      -> ENTER : cliquer sur x1,y1 :""")
x1,y1 = get_click()

input("""
      -> ENTER : cliquer sur x2,y2 :""")
x2,y2 = get_click()

x2 = x2 - x1
y2 = y2 - y1

append_write(path_f,f"""
###############################################
###################  POS  #####################
###############################################

region_map = ({x1}, {y1}, {x2}, {y2})
color_pos_dofus = (228,228,226)
color_pos_dofus_p = (255,255,255)
color_pos_dofus_m = (200,200,200)
""")
##################################################################################
print("""
###############################################
########### DEPLACEMENT PAR CASE  #############
###############################################
""")

input("""
      Calcul des pixels de déplacement PM
      -> ENTER : cliquer sur la position centrale x1,y1 :""")
xc,yc = get_click()

input("""
      -> ENTER : cliquer sur la position NORD 2pm x,y :""")
xN2,yN2 = get_click()

input("""
      Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position SUD 2pm x,y :""")
xS2, yS2 = get_click()
input("""
      Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position OUEST 2pm x,y :""")
xO2, yO2 = get_click()
input("""
      Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position EST 2pm x,y :""")
xE2, yE2 = get_click()


input("""
      Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position NORD-EST 2pm x,y :""")
xNE2,yNE2 = get_click()

input("""
      Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position SUD-EST 2pm x,y :""")
xSE2, ySE2 = get_click()
input("""
      Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position SUD-OUEST 2pm x,y :""")
xSO2, ySO2 = get_click()
input("""
      Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position NORD-OUEST 2pm x,y :""")
xNO2, yNO2 = get_click()

input("""
      Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position NORD-EST 1pm x,y :""")
xNE1,yNE1 = get_click()

input("""Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position SUD-EST 1pm x,y :""")
xSE1, ySE1 = get_click()
input("""Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position SUD-OUEST 1pm x,y :""")
xSO1, ySO1 = get_click()
input("""Retourner sur la position centrale x1,y1
      -> ENTER : cliquer sur la position NORD-OUEST 1pm x,y :""")
xNO1, yNO1 = get_click()

y_move_vertical2 = abs(yc - yN2)
x_move_horizontal2 = abs(xc - xO2)
 
append_write(path_f,f"""
###############################################
########### DEPLACEMENT PAR CASE  #############
###############################################

dep_N_2pm = (0,-{y_move_vertical2})
dep_S_2pm = (0,{y_move_vertical2})
dep_O_2pm = (-{x_move_horizontal2},0)
dep_E_2pm = ({x_move_horizontal2},0)


dep_NE_2pm = ({xc-xNE2},{yc-yNE2})
dep_SE_2pm = ({xc-xSE2},{yc-ySE2})
dep_SO_2pm = ({xc-xSO2},{yc-ySO2})
dep_NO_2pm = ({xc-xNO2},-{yc-yNO2})

dep_NE_1pm = ({xc-xNE1},{yc-yNE1})
dep_SE_1pm = ({xc-xSE1},{yc-ySE1})
dep_SO_1pm = ({xc-xSO1},{yc-ySO1})
dep_NO_1pm = ({xc-xNO1},{yc-yNO1})

distance_1PO = 50
distance_3PO = 150
distance_6PO = 300
distance_12PO = 600

""")
######################################################################################
print("""
###############################################
################  EN COMBAT  ##################
###############################################
""")

append_write(path_f,f"""
             
             
###############################################
################  EN COMBAT  ##################
###############################################

color_bouton_pret = (48,48,36)
color_tour_de_jeu = (252,200,0)
color_PA_PM = (255,255,255)
""")


input("""
      zone OCR Bouton PRET : Faire un minimun de marge
      -> ENTER : cliquer sur x1,y1 :""")
x1,y1 = get_click()

input("""
      -> ENTER : cliquer sur x2,y2 :""")
x2,y2 = get_click()

x2 = x2 - x1
y2 = y2 - y1

append_write(path_f,f"""
region_bouton_pret= ({x1},{y1},{x2},{y2})
""")

input("""
      zone OCR Bouton FIN TOUR DE JEU : Faire un minimun de marge
      -> ENTER : cliquer sur x1,y1 :""")
x1,y1 = get_click()

input("""
      -> ENTER : cliquer sur x2,y2 :""")
x2,y2 = get_click()

x2 = x2 - x1
y2 = y2 - y1

append_write(path_f,f"""
region_bouton_fin_de_tour = ({x1},{y1},{x2},{y2})
""")

input("""
      zone reconnaissance couleur : barre du temps de jeu restant 
      -> ENTER : cliquer sur x1,y1 :""")
x1,y1 = get_click()

input("""
      -> ENTER : cliquer sur x2,y2 :""")
x2,y2 = get_click()

x2 = x2 - x1
y2 = y2 - y1

append_write(path_f,f"""
## region barre de temps de jeu restant
region_tour_de_jeu = ({x1},{y1},{x2},{y2})
""")


input("""
      zone OCR Bouton PA : Faire un minimun de marge
      -> ENTER : cliquer sur x1,y1 :""")
x1,y1 = get_click()

input("""
      -> ENTER : cliquer sur x2,y2 :""")
x2,y2 = get_click()

x2 = x2 - x1
y2 = y2 - y1

append_write(path_f,f"""
region_PA = ({x1},{y1},{x2},{y2})
""")

input("""
      zone OCR Bouton PM : Faire un minimun de marge
      -> ENTER : cliquer sur x1,y1 :""")
x1,y1 = get_click()

input("""
      -> ENTER : cliquer sur x2,y2 :""")
x2,y2 = get_click()

x2 = x2 - x1
y2 = y2 - y1

append_write(path_f,f"""
region_PM = ({x1},{y1},{x2},{y2})
""")




input(""" pos_hors_zone_combat 
      -> ENTER : cliquer sur x,y :""")
x,y = get_click()
append_write(path_f,f"""
pos_hors_zone_combat = ({x},{y})
""")

input(""" pos_hors_zone_combat 
      -> ENTER : cliquer sur x,y :""")
x,y = get_click()
append_write(path_f,f"""
pos_hors_zone_combat = ({x},{y})
""")

input("""
      sort à lancer pos 1 
      -> ENTER : cliquer sur x,y :""")
x,y = get_click()
append_write(path_f,f"""
x_sort_1, y_sort_1 = {x},{y}
""")

input(""" 
      sort à lancer pos 2 
      -> ENTER : cliquer sur x,y :""")
x,y = get_click()
append_write(path_f,f"""
x_sort_2, y_sort_2 = {x},{y}
""")

input("""
      ennemi 1 ( dans ordre tour de jeu)
      -> ENTER : cliquer sur x,y :""")
x,y = get_click()
append_write(path_f,f"""
x_ennemi_1, y_ennemi_1   = {x},{y}
""")

input("""
      ennemi 2 ( dans ordre tour de jeu)
      -> ENTER : cliquer sur x,y :""")
x,y = get_click()
append_write(path_f,f"""
x_ennemi_2, y_ennemi_2   = {x},{y}
""")


###############################################################################################

print("""
###############################################
################   BANQUE  ####################
###############################################

- CLIQUE COMMUNE A TOUTES LES BANQUES

commencez par :
==> Entrée dans une banque
==> cliquer sur le conseiller de banque (hibou)
      """)

input("""
      -> ENTER : cliquer sur "consulter banque" :""")
x,y = get_click()
append_write(path_f,f"""
### coffre Banque : variables communes à toutes les banques
x_consulter_banque, y_consulter_banque   = {x},{y}   #clic consulter sa banque
""")

input("""
      -> ENTER : cliquer sur le menu avancé : """)
x,y = get_click()
append_write(path_f,f"""
x_menu_transfert_banque, y_menu_transfert_banque    = {x},{y}   #clic transfert avancé
""")

input("""
      -> ENTER : cliquer sur "tout transférer" : """)
x,y = get_click()
append_write(path_f,f"""
x_menu_transfert_banque, y_menu_transfert_banque    = {x},{y}   #clic tout transferer
""")

input("""
      -> ENTER : cliquer sur "fermer banque" : """)
x,y = get_click()
append_write(path_f,f"""
x_fermer_banque_banque, y_fermer_banque_banque    = {x},{y}   #clic fermer banque
""")

input("""
      commencez par :
    ==> Entrée dans une banque
    ==> ouvrir le coffre de guilde
    -> ENTER : cliquer sur onglet ressource : """)
x,y = get_click()
append_write(path_f,f"""
### coffre Guilde : variables communes à toutes les banques
x_coffre_guilde_onglet_ressource, y_coffre_guilde_onglet_ressource   = {x},{y}   
""")

input("""
      -> ENTER : cliquer sur une ressource : """)
x,y = get_click()
append_write(path_f,f"""
x_coffre_guilde_ressource, y_coffre_guilde_ressource    = {x},{y}   #clic fermer banque
""")

input("""
      -> ENTER : cliquer sur onglet consommable : """)
x,y = get_click()
append_write(path_f,f"""
x_coffre_guilde_onglet_potion, y_coffre_guilde_onglet_potion  = {x},{y}   #clic fermer banque
""")

input("""
      -> ENTER : cliquer sur onglet consommable : """)
x,y = get_click()
append_write(path_f,f"""
x_coffre_guilde_fermer, y_coffre_guilde_fermer  = {x},{y}   #clic fermer banque
""")

print("""
###############################################
################   BANQUE  ####################
###############################################

- CLIQUE SPECIFIQUE A CHAQUE BANQUES

commencez par :
==> Ce rendre map banque Amakna
""")

input("""
      -> ENTER : cliquer sur entrer dans la banque : """)
x,y = get_click()
append_write(path_f,f"""
################  amakna  ##################
pos_banque_amakna = "2,-2"
x_entre_banque_amakna,y_entre_banque_amakna   = {x},{y}   #entrer banque
""")

input("""
      -> ENTER : cliquer sur le conseiller (hibou) : """)
x,y = get_click()
append_write(path_f,f"""
x_hibou_banque_amakna, y_hibou_banque_amakna   = {x},{y}   #parler au conseiller
""")

input("""
      -> ENTER : cliquer sur le coffre de guilde : """)
x,y = get_click()
append_write(path_f,f"""
x_coffre_guilde_amakna_ouvrir, y_coffre_guilde_amakna_ouvrir   = {x},{y}  #ouvrir le coffre deguilde
""")

input("""
      -> ENTER : cliquer sur sortie banque : """)
x,y = get_click()
append_write(path_f,f"""
x_sortie_banque_amakna, y_sortie_banque_amakna  = {x},{y}   #sortie de la banque
""")
#####
print("""
commencez par :
==> Ce rendre map banque Sufokia
""")

input("""
      -> ENTER : cliquer sur entrer dans la banque : """)
x,y = get_click()
append_write(path_f,f"""
################  sufokia  ##################
pos_banque_sufokia = "14,25"
x_entre_banque_sufokia,y_entre_banque_sufokia  = {x},{y}   #entrer banque
""")

input("""
      -> ENTER : cliquer sur le conseiller (hibou) : """)
x,y = get_click()
append_write(path_f,f"""
x_hibou_banque_sufokia, y_hibou_banque_sufokia  = {x},{y}   #parler au conseiller
""")

input("""
      -> ENTER : cliquer sur le coffre de guilde : """)
x,y = get_click()
append_write(path_f,f"""
x_coffre_guilde_sufokia_ouvrir, y_coffre_guilde_sufokia_ouvrir  = {x},{y}  #ouvrir le coffre deguilde
""")

input("""
      -> ENTER : cliquer sur sortie banque : """)
x,y = get_click()
append_write(path_f,f"""
x_sortie_banque_sufokia, y_sortie_banque_sufokia  = {x},{y}   #sortie de la banque
""")
############################
print("""
commencez par :
==> Ce rendre map banque Bonta
""")

input("""
      -> ENTER : cliquer sur entrer dans la banque : """)
x,y = get_click()
append_write(path_f,f"""
################  bonta  ##################
pos_banque_bonta = "-31,-57"
x_entre_banque_bonta, y_entre_banque_bonta   = {x},{y}   #entrer banque
""")

input("""
      -> ENTER : cliquer sur le conseiller (hibou) : """)
x,y = get_click()
append_write(path_f,f"""
x_hibou_banque_bonta, y_hibou_banque_bonta = {x},{y}   #parler au conseiller
""")

input("""
      -> ENTER : cliquer sur le coffre de guilde : """)
x,y = get_click()
append_write(path_f,f"""
x_coffre_guilde_bonta_ouvrir, y_coffre_guilde_bonta_ouvrir   = {x},{y}  #ouvrir le coffre deguilde
""")

input("""
      -> ENTER : cliquer sur sortie banque : """)
x,y = get_click()
append_write(path_f,f"""
x_sortie_banque_bonta, y_sortie_banque_bonta = {x},{y}   #sortie de la banque
""")
####
print("""
commencez par :
==> Ce rendre map banque Bonta
""")

input("""
      -> ENTER : cliquer sur entrer dans la banque : """)
x,y = get_click()
append_write(path_f,f"""
################  pandala  ##################
pos_banque_pandala = "-20,30"
x_entre_banque_pandala,y_entre_banque_pandala  = {x},{y}   #entrer banque
""")

input("""
      -> ENTER : cliquer sur le conseiller (hibou) : """)
x,y = get_click()
append_write(path_f,f"""
x_hibou_banque_pandala, y_hibou_banque_pandala = {x},{y}   #parler au conseiller
""")

input("""
      -> ENTER : cliquer sur le coffre de guilde : """)
x,y = get_click()
append_write(path_f,f"""
x_coffre_guilde_pandala_ouvrir, y_coffre_guilde_pandala_ouvrir  = {x},{y}  #ouvrir le coffre deguilde
""")

input("""
      -> ENTER : cliquer sur sortie banque : """)
x,y = get_click()
append_write(path_f,f"""
x_sortie_banque_pandala, y_sortie_banque_pandala = {x},{y}   #sortie de la banque
""")

################################################################################################

print("""
###############################################
##############   DEPLACEMENT V2 #################
###############################################

""")

input("""
      -> ENTER : deplacement gauche haut : """)
x,y = get_click()
append_write(path_f,f"""
             
             
###############################################
##############   DEPLACEMENT V2 #################
###############################################
dep_gauche_haut = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement gauche milieu : """)
x,y = get_click()
append_write(path_f,f"""
dep_gauche_milieu = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement gauche bas : """)
x,y = get_click()
append_write(path_f,f"""
dep_gauche_bas = Coord({x},{y})
""")


input("""
      -> ENTER : deplacement droite haut : """)
x,y = get_click()
append_write(path_f,f"""
dep_droite_haut = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement droite milieu : """)
x,y = get_click()
append_write(path_f,f"""
dep_droite_milieu = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement droite bas : """)
x,y = get_click()
append_write(path_f,f"""
dep_droite_bas = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement haut droite : """)
x,y = get_click()
append_write(path_f,f"""
dep_haut_droite = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement haut milieu : """)
x,y = get_click()
append_write(path_f,f"""
dep_haut_milieu = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement haut gauche : """)
x,y = get_click()
append_write(path_f,f"""
dep_haut_gauche  = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement bas droite : """)
x,y = get_click()
append_write(path_f,f"""
dep_bas_droite = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement bas milieu : """)
x,y = get_click()
append_write(path_f,f"""
dep_bas_milieu = Coord({x},{y})
""")

input("""
      -> ENTER : deplacement bas gauche : """)
x,y = get_click()
append_write(path_f,f"""
dep_bas_gauche = Coord({x},{y})
""")




