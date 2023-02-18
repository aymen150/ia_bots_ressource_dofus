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
path_circuit_koalak = Path(path_my_bot,"circuit","koalak.txt")

path_dataset = "D:/Users/Document D/project_dofus/my_bot/dataset/"
###############################################
############## ZONE DE JEU  ###################
###############################################

dimension_ecran = (1920, 1080)
#bord d'une map hors zone de changement de map
left = 370
right = 1550
top = 50
down = 890


###############################################
############## ZONE DE JEU  ###################
###############################################

region_gameplay = (290,30, 1240, 890) 

###############################################
#################  TCHAT  #####################
###############################################

x_tchat, y_tchat = 118,1010

###############################################
################# MAGASIN  ####################
###############################################

region_magasin = (505,102,100,30) 
x_close_magasin , y_close_magasin = 730,117

###############################################
###################  POS  #####################
###############################################

region_map = (15,71,85,35)
color_pos_dofus = (228,228,226)
color_pos_dofus_p = (255,255,255)
color_pos_dofus_m = (200,200,200)

###############################################
###############   CONNEXION  ##################
###############################################

region_deconnexion = (905,360, 150,50)
x_launcher, y_launcher =  584,1050 # open launcher
x_scroller_multi_compte , y_scroller_multi_compte = 613,522 # open scroller multi compte
x_select_roublar,y_select_roublar = 667,717 # connec to roublar compte 

###############################################
################   COMBAT  ####################
###############################################
distance_1PO = 50
distance_3PO = 150
distance_6PO = 300
distance_12PO = 600
dep_O_2pm = (-85,0)
dep_E_2pm = (85,0)
dep_N_2pm = (0,-45)
dep_S_2pm = (0,45)

dep_NE_2pm = (90,-50)
dep_SE_2pm = (80,40)
dep_SO_2pm = (-90,50)
dep_NO_2pm = (-80,-40)

dep_NE_1pm = (45,-25)
dep_SE_1pm = (40,20)
dep_SO_1pm = (-45,25)
dep_NO_1pm = (-40,-20)

pos_hors_zone_combat = (1600,480)

color_bouton_pret = (48,48,36)
region_bouton_pret = (1310,945, 50, 30)
region_bouton_fin_de_tour = (1280,940, 110, 50)

## region barre de temps de jeu restant
region_tour_de_jeu = (786,1004,464,17)

region_PA = (700,990,35,35)
color_PA_PM = (255,255,255)
region_PM = (744, 995, 25,25)

color_tour_de_jeu = (252,200,0)
x_sort_1, y_sort_1 = 815,944
x_sort_2, y_sort_2 = 815,988
x_ennemi_1, y_ennemi_1      = 1710, 833
x_ennemi_2, y_ennemi_2      = 1773, 833

###############################################
################   BANQUE  ####################
###############################################

### coffre Banque : variables communes à toutes les banques
region_onglet_ressource = (1246 , 198 , 305 ,600)
x_consulter_banque, y_consulter_banque = 850,750 #clic consulter sa banque
x_menu_transfert_banque, y_menu_transfert_banque = 1264,152 #clic transfert avancé
x_all_transfert_banque, y_all_transfert_banque = 1400,165 #clic tout transferer
x_fermer_banque_banque, y_fermer_banque_banque = 680,118 #clic fermer banque

### coffre Guilde : variables communes à toutes les banques
x_coffre_guilde_onglet_ressource, y_coffre_guilde_onglet_ressource = 1458, 156
x_coffre_guilde_ressource, y_coffre_guilde_ressource = 1280, 243
x_coffre_guilde_potion, y_coffre_guilde_potion = 1398, 235
x_coffre_guilde_onglet_potion, y_coffre_guilde_onglet_potion =  1404, 156
x_coffre_guilde_fermer, y_coffre_guilde_fermer =  1554, 116

################  amakna  ##################
pos_banque_amakna = "2,-2"
x_entre_banque_amakna,y_entre_banque_amakna =   930,315 # click entrer dans la banque
x_sortie_banque_amakna, y_sortie_banque_amakna = 760,670 #clic quitter la banque
#coffre bank
x_hibou_banque_amakna, y_hibou_banque_amakna = 1080,475 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_amakna_ouvrir, y_coffre_guilde_amakna_ouvrir = 662, 446

################  sufokia  ##################
pos_banque_sufokia = "14,25"
x_entre_banque_sufokia,y_entre_banque_sufokia =  1104, 527  # click entrer dans la banque
x_sortie_banque_sufokia, y_sortie_banque_sufokia =  734, 790 #clic quitter la banque
#coffre bank
x_hibou_banque_sufokia, y_hibou_banque_sufokia = 1071, 517 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_sufokia_ouvrir, y_coffre_guilde_sufokia_ouvrir = 798, 463

################  bonta  ##################
pos_banque_bonta = "-31,-57"
x_entre_banque_bonta,y_entre_banque_bonta =  1086, 791 # click entrer dans la banque
x_sortie_banque_bonta, y_sortie_banque_bonta =   382, 813 #clic quitter la banque
#coffre bank
x_hibou_banque_bonta, y_hibou_banque_bonta = 1148, 433 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_bonta_ouvrir, y_coffre_guilde_bonta_ouvrir = 786, 267

################  pandala  ##################
pos_banque_pandala = "-20,30"
x_entre_banque_pandala,y_entre_banque_pandala =  1104, 442 # click entrer dans la banque
x_sortie_banque_pandala, y_sortie_banque_pandala =   693, 680 #clic quitter la banque
#coffre bank
x_hibou_banque_pandala, y_hibou_banque_pandala = 1119, 423 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_pandala_ouvrir, y_coffre_guilde_pandala_ouvrir = 652, 428

################  koalak  ##################
pos_banque_koalak = "-16,4"
x_entre_banque_koalak,y_entre_banque_koalak =  1101 , 485 # click entrer dans la banque
x_sortie_banque_koalak, y_sortie_banque_koalak =  806 , 698 #clic quitter la banque
#coffre bank
x_hibou_banque_koalak, y_hibou_banque_koalak = 1085 , 475 # clique parler à l hibou
# Cofre de guilde #
x_coffre_guilde_koalak_ouvrir, y_coffre_guilde_koalak_ouvrir = 740 , 439


###############################################
##############   DEPLACEMENT V2 #################
###############################################

dep_gauche_haut = Coord(300,130)
dep_gauche_milieu = Coord(300,480)
dep_gauche_bas = Coord(300,850)


dep_droite_haut = Coord(1600,130)
dep_droite_milieu = Coord(1600,480)
dep_droite_bas = Coord(1600,850)


dep_haut_droite = Coord(1500,35)
dep_haut_milieu = Coord(1000,35)
dep_haut_gauche = Coord(500,35)

dep_bas_droite = Coord(1500,910)
dep_bas_milieu = Coord(1000,910)
dep_bas_gauche = Coord(500,910)