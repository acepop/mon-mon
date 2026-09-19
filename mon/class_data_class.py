from .class_species import species
from .class_move import move
import json

class data_class:
    def __init__(self, species_file_path, move_file_path):
        self.move_file = move_file_path
        self.species_file = species_file_path
        self.moves_dict = {}
        self.species_dict = {}

        # grabs list of dictinarys from the json files before adding mons and moves
        # to a soarted ditc refrenced by number of move and mons
        # 
        with open(species_file_path, "r") as f: # opens the file in read mode
            mon_list = json.load(f)  # reads all of the data to a list of ditc

        with open(move_file_path) as f: # opens the file in read mode
            move_list =  json.load(f)  # reads all of the data to a list of ditc

        for mon in mon_list: # dict of mons class refrenced by there number
            self.species_dict[mon["number"]] = species(mon)
            print(mon["number"])

        for m in move_list: # dict of move vlass refrenced by there numbers
            self.moves_dict[m["number"]] = move(m["number"], m["name"], m["element"], m["value"], m["abilit"])


    def get_species(self,number): return self.species_dict[number]
    def get_move(self,number): return self.moves_dict[number]

