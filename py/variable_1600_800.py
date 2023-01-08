
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

path_dataset = "D:/Users/Document D/project_dofus/my_bot/dataset/"
###############################################
############## ZONE DE JEU  ###################
###############################################

dimension_ecran = (1600, 1200)
#bord d'une map hors zone de changement de map
left = 150
right = 1450
top = 65
down = 985


###############################################
############## ZONE DE JEU  ###################
###############################################

region_gameplay = (140,35, 1320, 975) 

###############################################
#################  TCHAT  #####################
###############################################

x_tchat, y_tchat = 148 , 1136



###############################################
###################  POS  #####################
###############################################

region_map = (11,79,111,30)
color_pos_dofus = (228,228,226)
color_pos_dofus_p = (255,255,255)
color_pos_dofus_m = (200,200,200)


###############################################
################   COMBAT  ####################
###############################################
distance_1PO = 50
distance_3PO = 150
distance_6PO = 300
distance_12PO = 600
dep_O_2pm = (-94,0)
dep_E_2pm = (94,0)
dep_N_2pm = (0,-50)
dep_S_2pm = (0,50)

dep_NE_2pm = (95,-50)
dep_SE_2pm = (95,50)
dep_SO_2pm = (-95,50)
dep_NO_2pm = (-95,-50)

dep_NE_1pm = (50,-20)
dep_SE_1pm = (50,20)
dep_SO_1pm = (-50,20)
dep_NO_1pm = (-50,-20)

pos_hors_zone_combat = (1537 , 582)

color_bouton_pret = (48,48,36)
region_bouton_pret = (1246 , 1059, 61, 25)
region_bouton_fin_de_tour = (1219 , 1048, 116, 42)

## region barre de temps de jeu restant
region_tour_de_jeu = ( 658 , 1122 , 532, 22)

region_PA = (556 , 1108 , 35, 34)
color_PA_PM = (255,255,255)
region_PM = (615 , 1110, 23, 32)

color_tour_de_jeu = (252,200,0)
x_sort_1, y_sort_1 = 687 , 1053
x_sort_2, y_sort_2 = 685 , 1099
x_ennemi_1, y_ennemi_1      = 1490 , 888
x_ennemi_2, y_ennemi_2      = 1426 , 891

###############################################
################   BANQUE  ####################
###############################################

### coffre Banque : variables communes à toutes les banques
x_consulter_banque, y_consulter_banque = 779 , 840 #clic consulter sa banque
x_menu_transfert_banque, y_menu_transfert_banque = 1136 , 167 #clic transfert avancé
x_all_transfert_banque, y_all_transfert_banque = 1295 , 184  #clic tout transferer
x_fermer_banque_banque, y_fermer_banque_banque = 463 , 133 #clic fermer banque

### coffre Guilde : variables communes à toutes les banques
x_coffre_guilde_onglet_ressource, y_coffre_guilde_onglet_ressource = 1357 , 169
x_coffre_guilde_ressource, y_coffre_guilde_ressource = 1158 , 258
x_coffre_guilde_onglet_potion, y_coffre_guilde_onglet_potion =  1404, 156
x_coffre_guilde_fermer, y_coffre_guilde_fermer =  1464 , 127

################  amakna  ##################
pos_banque_amakna = "2,-2"
x_entre_banque_amakna,y_entre_banque_amakna =   802 , 370 # click entrer dans la banque
x_sortie_banque_amakna, y_sortie_banque_amakna = 574 , 748 #clic quitter la banque
#coffre bank
x_hibou_banque_amakna, y_hibou_banque_amakna = 930 , 521 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_amakna_ouvrir, y_coffre_guilde_amakna_ouvrir = 458 , 485

################  sufokia  ##################
pos_banque_sufokia = "14,25"
x_entre_banque_sufokia,y_entre_banque_sufokia =  950 , 582  # click entrer dans la banque
x_sortie_banque_sufokia, y_sortie_banque_sufokia =  538 , 878 #clic quitter la banque
#coffre bank
x_hibou_banque_sufokia, y_hibou_banque_sufokia = 932 , 581 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_sufokia_ouvrir, y_coffre_guilde_sufokia_ouvrir = 616 , 514

################  bonta  ##################
pos_banque_bonta = "-31,-57"
x_entre_banque_bonta,y_entre_banque_bonta =   940 , 863 # click entrer dans la banque
x_sortie_banque_bonta, y_sortie_banque_bonta =   192 , 875 #clic quitter la banque
#coffre bank
x_hibou_banque_bonta, y_hibou_banque_bonta = 584 , 638 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_bonta_ouvrir, y_coffre_guilde_bonta_ouvrir = 614 , 305

################  pandala  ##################
pos_banque_pandala = "-20,30"
x_entre_banque_pandala,y_entre_banque_pandala =  946 , 486 # click entrer dans la banque
x_sortie_banque_pandala, y_sortie_banque_pandala =   481 , 754 #clic quitter la banque
#coffre bank
x_hibou_banque_pandala, y_hibou_banque_pandala = 965 , 468 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_pandala_ouvrir, y_coffre_guilde_pandala_ouvrir = 441 , 472


###############################################
##############   DEPLACEMENT V2 #################
###############################################

dep_gauche_haut = Coord(70,140)
dep_gauche_milieu = Coord(70,600)
dep_gauche_bas = Coord(70,940)


dep_droite_haut = Coord(1540,130)
dep_droite_milieu = Coord(1540,600)
dep_droite_bas = Coord(1540,940)


dep_haut_droite = Coord(1310,40)
dep_haut_milieu = Coord(800,40)
dep_haut_gauche = Coord(265,40)

dep_bas_droite = Coord(1310,1010)
dep_bas_milieu = Coord(800,1010)
dep_bas_gauche = Coord(265,1010)