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