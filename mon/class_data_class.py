from .class_species import species
from .class_move import move

class data_class:
    def __init__(self, species_file_path, move_file_path):
        self.move_file = move_file_path
        self.species_file = species_file_path
        self.moves_list = {}
        self.species_list = {}


    def get_species(self,number): return self.species[number]
    def get_move(self,number): return self.moves[number]


