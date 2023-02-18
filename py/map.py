from py.Coord import Coord
import py.Coord as coord
import py.variable as v
import pandas as pd
from py.variable import dep_gauche_haut, dep_gauche_milieu,dep_gauche_bas,\
                        dep_droite_haut,dep_droite_milieu,dep_droite_bas,\
                        dep_haut_droite,dep_haut_milieu,dep_haut_gauche,\
                        dep_bas_droite,dep_bas_milieu,dep_bas_gauche
class Map :
    def __init__(self, move_prec_map : Coord , pos : str , move_next_map : Coord )  :
        self.prec_map = move_prec_map
        self.map = pos
        self.next_map = move_next_map


def str_to_map(str) :
    map = eval(str)
    map.prec_map = eval(map.prec_map)
    map.next_map = eval(map.next_map)
    return map

def circuit(parcours = "amakna sud") :
    match parcours :
        case "amakna sud" :
            return circuit_amakna_sud()
        case "foret bonta" :
            return circuit_foret_bonta()
        case "dragoeuf" :
            return circuit_dragoeuf()
        case "pandala sud" :
            return circuit_pandala_sud()
        case "koalak" :
            return circuit_koalak()
        case _ :
            print("Error selection circuit")

def circuit_foret_bonta():
    fichier = pd.read_csv (v.path_circuit_foret_bonta, sep=";", header=None, encoding = "UTF-8")
    return [ str_to_map(map) for map in  fichier[0].values.tolist()]

def circuit_dragoeuf():
    fichier = pd.read_csv (v.path_circuit_dragoeuf, sep=";", header=None, encoding = "UTF-8")
    return [ str_to_map(map) for map in  fichier[0].values.tolist()]

def circuit_amakna_sud():
    fichier = pd.read_csv (v.path_circuit_amakna_sud, sep=";", header=None, encoding = "UTF-8")
    return [ str_to_map(map) for map in  fichier[0].values.tolist()]

def circuit_pandala_sud():
    fichier = pd.read_csv (v.path_circuit_pandala_sud, sep=";", header=None, encoding = "UTF-8")
    return [ str_to_map(map) for map in  fichier[0].values.tolist()]


def circuit_koalak():
    fichier = pd.read_csv (v.path_circuit_koalak, sep=";", header=None, encoding = "UTF-8")
    return [ str_to_map(map) for map in  fichier[0].values.tolist()]