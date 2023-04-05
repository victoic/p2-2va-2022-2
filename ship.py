class Ship:
   
    def __init__(self, position=int[2],size=int,orientation=int,hp=bool) :
        self.position=position
        self.size = size      
        self.orientation = orientation   # 0 para horizontal, 1 para vertical
        self.hp = hp[size]

