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