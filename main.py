from mon.class_mon import mon
from mon.class_move import move
from mon.class_species import species
from mon.class_data_class import data_class
import os

def main():

    # relitive paths
    species_file_path_rel = r"/data/species.csv"
    move_file_path_rel = r"/data/move.csv"
    # converts to full paths
    species_file_path_full = os.path.join(f"{os.path.dirname(__file__)}{species_file_path_rel}")
    moves_file_path_full = os.path.join(f"{os.path.dirname(__file__)}{move_file_path_rel}")
    # passes pathes to data sequincer/reader to be indexed 
    pokeydex = data_class(species_file_path_full ,moves_file_path_full)

    # testing
    mon1 = mon()
    mon1.set_species(pokeydex.get_species["1"])
    print(mon1.get_attack)





    print("hellow world")

    



if __name__ == "__main__":
    main()


'''
def apply_heal(user, target, value):   target.current_hp += value
def apply_damage(user, target, value): target.current_hp -= value

EFFECTS = {"heal": apply_heal, "damage": apply_damage, "corrupt": apply_corrupt}

def use_move(move, user, target):
    EFFECTS[move.ability](user, target, move.value)
'''