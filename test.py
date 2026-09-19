import json
# relitive paths




pre_path = (str(__file__)).replace("test.py","")
species_file = f"{pre_path}{r"data/species.json"}"
move_file = f"{pre_path}{r"data/move.json"}"

with open(species_file, "r") as f: # opens the file in read mode
    mon_list = json.load(f)  # reads all of the data to a list of ditc

with open(move_file) as f: # opens the file in read mode
    move_list =  json.load(f)  # reads all of the data to a list of ditc

for mon in mon_list:
    self.mon_dict[mon["number"]] = species(mon)

for move in move_list:
    self.move_dict[move["number"]] = move