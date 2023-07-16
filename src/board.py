import random
from src.block import Block

class Board:
    def __init__(self, size:int, qtd_bomb:float)->None:
        """Construct and manipulation of the board"""
        self.size = size
        self.won = False
        self.lost = False
        self.board = []

        for row in range(size[0]):
            row = []
            for col in range(size[1]):
                bomb = random.random() < qtd_bomb
                block = Block(bomb)
                row.append(block)
            self.board.append(row)
        
        self.set_neighbors()
        self.set_num_around()

    def get_board(self)->object:
        """Return the board object"""
        return self.board

    def get_size(self)->int:
        """Return the size"""
        return self.size
    
    def get_block(self, index)->Block:
        """Return the block in the position"""
        return self.board[index[0]][index[1]]  

    def get_won(self)->bool:
        """Return if won the game"""
        return self.won

    def get_lost(self)->bool:
        """Return if lost the game"""
        return self.lost  
    
    def add_neighbors_list(self, neighbors, row, col)->None:
        """Add neighboors of the block in the position"""
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                ###refatorar esse if
                if r == row and c == col:
                    continue
                if r < 0 or r >= self.size[0] or c < 0 or c >= self.size[1]:
                    continue
                neighbors.append(self.board[r][c])

    
    def set_neighbors(self)->None:
        """Set the neighbors of the blocks"""
        for row in range(len(self.board)):
            for col in range(len(self.board[0])):
                block = self.board[row][col]
                neighbors = []
                self.add_neighbors_list(neighbors, row, col)
                block.set_neighbors(neighbors)

    def set_num_around(self)->None:
        """Set the amount of bombs arround the block"""
        for row in self.board:
            for block in row:
                block.set_num_around()
    
    def check_won(self)->bool:
        """Check if the player won the game"""
        for row in self.board:
            for block in row:
                if not block.get_has_bomb() and not block.get_clicked():
                    return False
        return True

    def handle_click(self, block:Block, flag:tuple)->None:
        """"""
        if block.get_clicked() or (block.get_flagged() and not flag):
            return 
        if flag:
            block.toggle_flag()
            return
        
        block.handle_click()

        if block.get_num_around() == 0:
            for neighbor in block.get_neighbors():
                self.handle_click(neighbor, False)
        if block.get_has_bomb():
            self.lost = True
        else:
            self.won = self.check_won()
