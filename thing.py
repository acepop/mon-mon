def main():
    mon_o_pidea = mon_apidia(r".\mon.csv",r".\move.csv")
    mon1 = mon(0)




    print("hellow world")

    
    





class move:
    def __init__(self, name, element, valu, abilit):
        self.name = str(name)
        self.element = str(element) 
        self.valu = str(valu)
        self.abilit = str(abilit)
    def use(self):
        match self.abilit:
            case "attack":
                return {
                    "target" : "opponent",
                    "name" : self.name,
                    "effect" : ["dmg",self.valu,self.element],
                    "text" : f" used {self.name}"
                }
            case "heal":
                return{
                    "target" : "self",
                    "name" : self.name,
                    "effect" : ["heal",self.valu],
                    "text" : f" healed using {self.name} "
                }

#  "spices name", ["element"], iv, health, damage, resist, speed
class mon:
    def __init__(self, number):
        self.number = int(number)
        self.mondata = []

        if self.number:
            self.mondata = mon_o_pidea.get_mon(self.number)
            self.spices = mondata[0]
            self.total_health = 10
            self.total_damage = 10
            self.total_resistance = 10
            self.total_speed = 10 
            self.element = ["normal"]
        else:
            raise RuntimeError("no number or save was passed for mon data")

   
        self.xp = 0
        self.level = 1
        self.xp_cap = 10 
        self.health = self.total_health
        self.damage = self.total_damage
        self.resistance = self.total_resistance
        self.speed = self.total_speed      

    def __str__(self):
        print(
            "nothing string"
        )
    def get_name(self): return self.name
    def get_element(self): return self.element
    def get_health(self): return self.health
    def get_damage(self): return self.damage
    def get_resistance(self): return self.resistance
    def get_speed(self): return self.speed
    def get_level(self): return self.level
    def get_xp(self): return self.xp
    def get_moves(self): return self.moves
    def add_exp(self, exp_add):
        self.xp =+ exp_add
        while self.xp >= self.xp_cap:
            self.level =+ 1
            self.xp =- self.xp_cap
            self.xp_cap =+ 10




class mon_apidia:
    def __init__(self, mon_file_path, move_file_path):
        self.move_file = str(move_file_path)
        self.mon_file = str(mon_file_path)
        self.moves = {}
        self.mons = {}

        try:
            with open(str(self.move_file),"r") as move_file:
                move_content = move_file.read()
            with open(str(self.mon_file),"r") as mon_file:
                mon_content = mon_file.read()
        except OSError as e:
            print(e)

        for move in move_content:
            self.moves[move[0]] = move

        for mon in mon_content:
            self.mons[mon[0]] = mon
    def get_mon(self,number): return self.mons[number]
    def get_move(self,number): return self.moves[number]

        









if __name__ == "__main__":
    main()