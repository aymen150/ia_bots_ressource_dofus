import py.dofus_action as da
import time
import time
from pathlib import Path


"""
ce script note dans nom_parcours le chemin que vous etes en train de parcourir dans dofus
"""
path_file = Path(__file__).parent
def generator_circuit(nom_parcours, mode = "w" ) :
    path_parcours = Path(path_file,"circuit",f"{nom_parcours}.txt")
    if mode == "w" :
        fichier = open(path_parcours, "w") 
        fichier.close()
    x_old = 0
    y_old = 0
    dep_old = ""
    dep = ""
    circuit = ""
    en_cours = True
    map_old = ""
    time.sleep(3)
    while en_cours :
        time.sleep(2)
        map = da.my_map()
        if map != "999,999" :
            x,y = [int(pos) for pos in map.split(",")]
            try : 
                if x != x_old or y != y_old :
                    dep_old = dep
                    if x > x_old and y == y_old: 
                        dep = "dep_droite_milieu"
                    elif x < x_old and y == y_old: 
                        dep = "dep_gauche_milieu"
                    elif y < y_old and x == x_old : 
                        dep = "dep_haut_milieu"
                    elif y > y_old and x == x_old : 
                        dep = "dep_bas_milieu"
                    msg = f"""Map("{dep_old}","{map_old}","{dep}")\n"""
                    circuit += map
                    with open(path_parcours, "a") as fichier:
                        fichier.write(msg)
                    print(msg, end="")
                    x_old = x
                    y_old = y
                    map_old = map
            except :
                en_cours = False

        
if __name__ == "__main__" :
    name_file = "koalak"
    generator_circuit(name_file)