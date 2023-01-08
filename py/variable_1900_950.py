
import string
import pyautogui
import time
from pathlib import Path
from py.Coord import Coord
path_file = Path(__file__)
path_my_bot = path_file.parent.parent
path_circuit_foret_bonta = Path(path_my_bot,"circuit","foret_bonta.txt")
path_circuit_dragoeuf = Path(path_my_bot,"circuit","presqu_ile_dragoeuf.txt")
path_circuit_amakna_sud = Path(path_my_bot,"circuit","amakna_sud.txt")
path_circuit_pandala_sud = Path(path_my_bot,"circuit","pandala_sud.txt")
###############################################
############## ZONE DE JEU  ###################
###############################################
dimension_ecran = (1920,950)

left = 442
right = 1477
top = 52
down = 779 

###############################################
############## BORDURE CARTE  #################
###############################################
region_gameplay = (435, 27, 1046, 776) 

##############################################
#################  TCHAT  #####################
############################################### 
x_tchat, y_tchat = 516,898

###############################################
###################  POS  #####################
###############################################
region_map = (116, 63, 74, 21)
color_pos_dofus = (228,228,226)
color_pos_dofus_p = (255,255,255)
color_pos_dofus_m = (200,200,200)

###############################################
########### DEPLACEMENT PAR CASE  #############
###############################################
dep_N_2pm = (0,-48)
dep_S_2pm = (0,48)
dep_O_2pm = (-72,0)
dep_E_2pm = (72,0)

dep_NE_2pm = (81,-43)
dep_SE_2pm = (82,32)
dep_SO_2pm = (-73,33)
dep_NO_2pm = (-72,-45)

dep_NE_1pm = (42,-27)
dep_SE_1pm = (44,14)
dep_SO_1pm = (-34,12)
dep_NO_1pm = (-35,-25)
distance_1PO = 50
distance_3PO = 150
distance_6PO = 300
distance_12PO = 600

             
             
###############################################
################  EN COMBAT  ##################
###############################################
color_bouton_pret = (48,48,36)
color_tour_de_jeu = (252,200,0)
color_PA_PM = (255,255,255)

region_bouton_pret= (1314,838,44,16)

region_bouton_fin_de_tour = (1295,829,87,31)

## region barre de temps de jeu restant
region_tour_de_jeu = (853,888,411,13)

region_PA = (769,877,24,24)

region_PM = (815,877,14,23)

pos_hors_zone_combat = (1639,502)

x_sort_1, y_sort_1 = 868,833

x_sort_2, y_sort_2 = 868,868

x_ennemi_1, y_ennemi_1   = 1735,707

x_ennemi_2, y_ennemi_2   = 1676,694

### coffre Banque : variables communes � toutes les banques
x_consulter_banque, y_consulter_banque   = 918,664   #clic consulter sa banque

x_menu_transfert_banque, y_menu_transfert_banque    = 1227,132   #clic transfert avanc�

x_menu_transfert_banque, y_menu_transfert_banque    = 1373,149   #clic tout transferer

x_fermer_banque_banque, y_fermer_banque_banque    = 1486,99   #clic fermer banque

### coffre Guilde : variables communes � toutes les banques
x_coffre_guilde_onglet_ressource, y_coffre_guilde_onglet_ressource   = 1399,132   

x_coffre_guilde_ressource, y_coffre_guilde_ressource    = 1241,203   #clic fermer banque

x_coffre_guilde_onglet_potion, y_coffre_guilde_onglet_potion  = 1354,135   #clic fermer banque

x_coffre_guilde_fermer, y_coffre_guilde_fermer  = 1485 ,  103   #clic fermer banque

################  amakna  ##################
pos_banque_amakna = "2,-2"
x_entre_banque_amakna,y_entre_banque_amakna   = 949,283   #entrer banque

x_hibou_banque_amakna, y_hibou_banque_amakna   = 1060,416   #parler au conseiller

x_coffre_guilde_amakna_ouvrir, y_coffre_guilde_amakna_ouvrir   = 689,395  #ouvrir le coffre deguilde

x_sortie_banque_amakna, y_sortie_banque_amakna  = 788,596   #sortie de la banque

################  sufokia  ##################
pos_banque_sufokia = "14,25"
x_entre_banque_sufokia,y_entre_banque_sufokia  = 1097,461   #entrer banque

x_hibou_banque_sufokia, y_hibou_banque_sufokia  = 1066,467   #parler au conseiller

x_coffre_guilde_sufokia_ouvrir, y_coffre_guilde_sufokia_ouvrir  = 809,406  #ouvrir le coffre deguilde

x_sortie_banque_sufokia, y_sortie_banque_sufokia  = 785,711   #sortie de la banque

################  bonta  ##################
pos_banque_bonta = "-31,-57"
x_entre_banque_bonta, y_entre_banque_bonta   = 965,628   #entrer banque

x_hibou_banque_bonta, y_hibou_banque_bonta = 1131,391   #parler au conseiller

x_coffre_guilde_bonta_ouvrir, y_coffre_guilde_bonta_ouvrir   = 579,441  #ouvrir le coffre deguilde

x_sortie_banque_bonta, y_sortie_banque_bonta = 517,712   #sortie de la banque

################  pandala  ##################
pos_banque_pandala = "-20,30"
x_entre_banque_pandala,y_entre_banque_pandala  = 1099,384   #entrer banque

x_hibou_banque_pandala, y_hibou_banque_pandala = 1108,383   #parler au conseiller

x_coffre_guilde_pandala_ouvrir, y_coffre_guilde_pandala_ouvrir  = 682,372  #ouvrir le coffre deguilde

x_sortie_banque_pandala, y_sortie_banque_pandala = 708,594   #sortie de la banque

             
             
###############################################
##############   DEPLACEMENT V2 #################
###############################################
dep_gauche_haut = Coord(380,76)

dep_gauche_milieu = Coord(338,418)

dep_gauche_bas = Coord(388,729)

dep_droite_haut = Coord(1524,120)

dep_droite_milieu = Coord(1594,438)

dep_droite_bas = Coord(1539,763)

dep_haut_droite = Coord(1366,28)

dep_haut_milieu = Coord(1010,25)

dep_haut_gauche  = Coord(533,30)

dep_bas_droite = Coord(1313,800)

dep_bas_milieu = Coord(877,799)

dep_bas_gauche = Coord(463,798)
