class Block:
    def __init__(self, has_bomb:bool)->None:
        """Initialize Block"""
        self.has_bomb = has_bomb
        self.around = 0
        self.clicked = False
        self.flagged = False
        self.neighbors = []

    def get_num_around(self)->int:
        """Return the number of bombs arround"""
        return self.around

    def get_has_bomb(self)->bool:
        """Return if the block is a bomb"""
        return self.has_bomb

    def get_clicked(self)->bool:
        """Return if the block is alredy clicked"""
        return self.clicked

    def get_flagged(self)->bool:
        """Return if the block recive a flag"""
        return self.flagged

    def set_num_around(self)->None:
        """Check the amount of bombs arround the block"""
        num = 0
        for neighbor in self.neighbors:
            if neighbor.get_has_bomb():
                num += 1
        self.around = num

    def set_neighbors(self, neighbors:object)->None:
        """Set the neighbors of the block"""
        self.neighbors = neighbors
        
    def get_neighbors(self)->None:
        """Return the neighbors of the block"""
        return self.neighbors
        
    def toggle_flag(self)->None:
        """Set or remove a flag from the block"""
        self.flagged = not self.flagged

    def handle_click(self)->None:
        """Set the block is clicked"""
        self.clicked = True
