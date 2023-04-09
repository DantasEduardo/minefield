import random


class Field:
    def __init__(self, size, bomb):
        self.field = [[0 for _ in range(size)] for _ in range(size)]
        self.size = len(self.field)
        self.mines = []
        self._generate_bombs(bomb)
        self._generate_neighbors()

    def _generate_bombs(self, bomb):
        size = len(self.field)

        while len(self.mines) < bomb:
            row = random.randint(0, size - 1)
            col = random.randint(0, size - 1)
            if (row, col) not in self.mines:
                self.mines.append((row, col))
                self.field[row][col] = -1


    def _generate_neighbors(self):
        width = self.size
        height = self.size

        for x in range(width):
            for y in range(height):
                if self.field[x][y] != -1:
                    sum = 0
                    if x != 0 and y != 0:
                        if self.field[x-1][y-1] == -1:
                            sum+=1

                    if x != 0:
                        if self.field[x-1][y] == -1:
                            sum+=1
                    
                    if x != 0 and y != width-1:
                        if self.field[x-1][y+1] == -1:
                            sum+=1
                        
                    if y != 0:
                        if self.field[x][y-1] == -1:
                            sum+=1
                        
                    if y != width-1:
                        if self.field[x][y+1] == -1:
                            sum+=1

                    if x != height-1 and y != 0:
                        if self.field[x+1][y-1] == -1:
                            sum+=1
                        
                    if x != height-1:
                        if self.field[x+1][y] == -1:
                            sum+=1
                        
                    if x != height-1 and y != width-1:
                        if self.field[x+1][y+1] == -1:
                            sum+=1 

                    self.field[x][y] = sum               
        
    def get_value(self, x, y):
        return self.field[x][y]
        

    def reveal_squares(self, row, col, clicked, interface):
        rows = self.size
        cols = self.size 
        to_check = [(row, col)]
        while to_check:
            row, col = to_check.pop()
            if not (0 <= row < rows and 0 <= col < cols) or clicked[row][col] == 1:
                continue
            clicked[row][col] = 1
            interface[row][col] = self.field[row][col]
            if interface[row][col] == 0:
                to_check += [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]

        return clicked, interface
    