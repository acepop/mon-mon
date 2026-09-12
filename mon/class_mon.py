from class_data_class.py import data_class
from class_spicies.py import species
import random 
#  "name", number, ["element"], health_iv, health, damage_iv, damang_sp, damage, resist_iv, resist_sp, resist, speed_iv, speed_sp, speed, bond, personality,[evolve level,another mon number], level track
class mon:
    def __init__(self, mon_species):
        # the vars one instance of a mon needs
        # set for the mon as internal values used for battling
        self.nickname = ""
        self.species = mon_species # number, bace_stats, name, move_table[], element[], level_track[]
        self.level = {} # level, xp, next_level
        self.personality = {} # bond, nature, nurture,
        #self.iv = {} # attack, health, resist, speed, crouption, pride, lust, gluttney
        self.current_stats = {} # attack, health, resist, speed, crouption, pride, lust, gluttney

        self.type_nurture = ["obsessive","hatefull","rathfull"]
        self.type_nature = ["anxious","inquisitive","stupid","brave","strudy","obeadent","hyper"]

    def setup(self):
        self.level = {"level":1,"xp":0,"next_level":100} # bace levelup stuff
        self.personality = {"bond":10, "nature":(random.choice(self.type_nature)), "nurture":(random.choice(self.type_nurture))} #
        self.current_stats = {"attack":self.species.bace_stats["attack"],"health":self.species.bace_stats["health"],
                            "resist":self.species.bace_stats["resist"],"speed":self.species.bace_stats["speed"],
                            "crouption":0,"pride":0,"lust":0,"gluttney":0 }
        self.move_table = [(random.choice(self.species.move_table)),(random.choice(self.species.move_table))]
    def set_nickname(self,nickname): self.nickname = nickname




    def apply_attack(self, user, value, target): target.apply_danmage(value *(100 /(self.current_stats["attack"])))
    def apply_health(self,user, value, target): self.current_stats["health"] = (self.current_stats["health"] + value)
    def apply_speed(self, user, value, target): self.current_stats["speed"] = (self.current_stats["speed"] + value)
    def apply_resist(self, user, value, target): self.current_stats["resist"] = (self.current_stats["resist"] + value)
    def apply_crouption(self, user, value, target): self.current_stats["crouption"] = (self.current_stats["crouption"] + value)
    def apply_pride(self, user, value, target): self.current_stats["pride"] = (self.current_stats["pride"] + value)
    def apply_lust(self, user, value, target): self.current_stats["lust"] = (self.current_stats["lust"] + value)
    def apply_gluttney(self, user, value, target): self.current_stats["gluttney"] = (self.current_stats["gluttney"] + value)

    def add_exp(self, exp_add):
        self.xp =+ exp_add
        while self.xp >= self.xp_cap:
            self.level =+ 1
            self.xp =- self.xp_cap
            self.xp_cap =+ 10