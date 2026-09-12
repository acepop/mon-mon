from .class_species import species

class data_class:
    def __init__(self, species_file_path, move_file_path):
        self.move_file = str(move_file_path)
        self.species_file = str(species_file_path)
        self.moves_list = {}
        self.species_list = {}

        try:
            with open(str(self.move_file),"r") as move_file:
                move_content = move_file.read()
            with open(str(self.species_file),"r") as species_file:
                species_content = species_file.read()
        except OSError as e:
            print(e)

        for move in move_content:
            self.moves[move[0]] = move

        for s_list in species_content:
            self.species_list[s_list[0]] = species(s_list)
    def get_species(self,number): return self.species[number]
    def get_move(self,number): return self.moves[number]