class species:
    def __init__ (self, input_species):
        # 1,"crustatamon",["normal"],{"attack":10,"resist":5,"speed":15,"health":10},[[0,0,0,0],[0,0,0,0],[2,1,3,3],[1,1,3,2],[3,2,3,3]],{"4":2,"crouption":3},[1,2,3,4]
        self.number = input_species[0]     
        self.name = input_species[1] 
        self.element = input_species[2]  # normal, fire, grass, water
        self.base_stats = input_species[3]  # attack, resist, speed, health
        self.level_track = input_species[4]  # [[0,0,0,0],[0,0,0,0],[2,1,3,3],[1,1,3,2],[3,2,3,3]]
        self.evolves_to = input_species[5]  # {"4":2,"crouption":3}
        self.move_table = input_species[6]  # [move0,move1,move2,move3]
        self.nurture = ["obsessive","hatefull","rathfull"]
        self.nature = ["anxious","inquisitive","stupid","brave","strudy","obeadent","hyper"]
