from class_mon_apidia.py import mon_apidia
#  "name", number, ["element"], health_iv, health, damage_iv, damang_sp, damage, resist_iv, resist_sp, resist, speed_iv, speed_sp, speed, bond, personality,[evolve level,another mon number], level track
class mon:
    def __init__(self, number, mon_o_pidea):
        # initaly set by the mons number
        self.name = ""
        self.number = 0
        self.element = []
        self.health_iv = 0
        self.health_sp = 0
        self.health = 0
        self.damage_iv = 0
        self.damage_sp = 0
        self.damage = 0
        self.resist_iv = 0
        self.resist_sp = 0
        self.resist = 0
        self.speed_iv = 0
        self.speed_sp = 0
        self.speed = 0
        self.bond_modifyer = 0
        self.personality = ""
        self.level_evolve = []
        self.level_track = ""

        # set for the mon as internal values used for battling
        self.bond = 0
        self.nickname = ""
        self.xp = 0
        self.level = 0
        self.xp_cap = 0
        self.current_health = 0
        self.current_damage = 0
        self.current_resiste = 0
        self.current_speed = 0    


    def add_exp(self, exp_add):
        self.xp =+ exp_add
        while self.xp >= self.xp_cap:
            self.level =+ 1
            self.xp =- self.xp_cap
            self.xp_cap =+ 10