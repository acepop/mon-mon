from class_data_class.py import data_class
from class_spicies.py import species
#  "name", number, ["element"], health_iv, health, damage_iv, damang_sp, damage, resist_iv, resist_sp, resist, speed_iv, speed_sp, speed, bond, personality,[evolve level,another mon number], level track
class mon:
    def __init__(self, number, mon_o_pidea):
        # the vars one instance of a mon needs
        # set for the mon as internal values used for battling
        self.nickname = ""
        self.species = species # number, attack, health, resist, speed, name, moves[], element[], bond_modifyer, level_up[], level_track[]
        self.level = [] # level, xp, next_level
        self.personality = [] # bond, nature, obsession,
        self.iv = {} # attack, health, resist, speed, crouption, pride, lust, gluttney
        self.current_stats = {} # attack, health, resist, speed, crouption, pride, lust, gluttney 


    def add_exp(self, exp_add):
        self.xp =+ exp_add
        while self.xp >= self.xp_cap:
            self.level =+ 1
            self.xp =- self.xp_cap
            self.xp_cap =+ 10