class Ship:
   
    def __init__(self, hp, position, size: int, orientation: int) :
        self.position=position
        self.size = size      
        self.orientation = orientation   # 0 para horizontal, 1 para vertical
        self.hp = hp[size]
