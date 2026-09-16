import json
# relitive paths
pre_path = (str(__file__)).replace("test.py","")

species_file = f"{pre_path}{r"data/species.json"}"
move_file = f"{pre_path}{r"data/move.json"}"






with open(species_file, "r") as f: # with the listed file
    data = json.load(f)  # reads all of the data to a string
    dic = data[0]
    for key, value in dic.items():
        print(f"{key} : {value}")

# trys to import file values as move_content and species_content
with open(move_file) as f: # with the listed file
    data =  json.load(f)  # reads all of the data to a string
    dic = data[0]
    for key, value in dic.items():
        print(f"{key} : {value}")

def import_formater(atxt_file_import): 
    # changes the imported data into usibal data
    out_list = [] # this is what will get retruned
    # data in the atxt fils are specifyed with #s=data # is the deliminator
    # s is the string data type, = is another dleminator, there are no "" or 





    return out_list 

formated_move_content = import_formater(move_content)
for m in formated_move_content:
    print(f"{m} ##")
    for i in m:
        print(f"{i} ==")
    #self.moves_list[move[0]] = move

for s_list in species_content:
    self.species_list[s_list[0]] = species(s_list)