class species:
    def __init__ (self, input_species):
        # 1,"crustatamon",["normal"],{"attack":10,"resist":5,"speed":15,"health":10},[[0,0,0,0],[0,0,0,0],[2,1,3,3],[1,1,3,2],[3,2,3,3]],{"4":2,"crouption":3},[1,2,3,4]
        self.number = input_species["number"]     
        self.name = input_species["name"] 
        self.element = input_species["elements"]  # normal, fire, grass, water
        self.base_stats = input_species["base_stats"]  # attack, resist, speed, health
        self.level_track = input_species["level_track"]  # [[0,0,0,0],[0,0,0,0],[2,1,3,3],[1,1,3,2],[3,2,3,3]]
        self.evolves_track = input_species["evolves_track"]  # {"4":2,"crouption":3}
        self.move_table = input_species["move_table"]  # [move0,move1,move2,move3]
        self.nurture = ["obsessive","hatefull","wrath"]
        self.nature = ["anxious","inquisitive","stupid","brave","strudy","obeadent","hyper"]
    
    def get_species_number (self): return self.number
    def get_species_name (self): return self.name
    def get_species_element (self): return self.element
    def get_species_base_stats (self): return self.base_stats
    def get_species_level_track (self): return self.level_track
    def get_species_evolves_track (self): return self.evolves_track
    def get_species_move_table (self): return self.move_table
    def get_species_nurture (self): return self.nurture
    def get_species_nature (self): return self.nature



        
