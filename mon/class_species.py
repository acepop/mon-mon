class species:
    def __init__ (self):
        self.number = 0        
        self.name = ""
        self.element = [] # normal, fire, grass, water
        self.base_stats = {} # attack, resist, speed, health
        self.level_track = [] # [[0,0,0,0],[0,0,0,0],[2,1,3,3],[1,1,3,2],[3,2,3,3]]
        self.evolves_to = {} # {"4":2,"crouption":3}
        self.move_table = [] # [move0,move1,move2,move3]

