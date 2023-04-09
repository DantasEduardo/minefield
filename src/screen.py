import pygame
from src.field import Field

pygame.init()
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
GREY = (128,128,128)
FONT = pygame.font.SysFont('arial', 25)

class Screen:
    def __init__(self, width, height, size, bomb):

        self.width = width
        self.height = height
        self.size = size
        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.block_size = 50
        self.interface = [[0 for _ in range(size)] for _ in range(size)]
        self.clicked = [[0 for _ in range(size)] for _ in range(size)]
        self.field = Field(size, bomb)

        pygame.display.set_caption('Minefield')

    def _draw(self):
        self.display.fill(BLACK)

        for i in range(self.size):
            x = i * self.block_size

            for j in range(self.size):
                y = j * self.block_size

                if self.clicked[i][j] == 0:
                    pygame.draw.rect(self.display, WHITE, pygame.Rect(x, y, self.block_size,  self.block_size))
                    pygame.draw.rect(self.display, "black", pygame.Rect(x, y, self.block_size,  self.block_size),2)
                else:
                    pygame.draw.rect(self.display, GREY, pygame.Rect(x, y, self.block_size,  self.block_size))
                    pygame.draw.rect(self.display, "black", pygame.Rect(x, y, self.block_size,  self.block_size),2)

                if self.interface[i][j] == 'P' or self.interface[i][j] > 0:
                    text = FONT.render(str(self.interface[i][j]), 1, BLACK)
                    self.display.blit(text, ((x+(self.block_size/2 - text.get_width()/2), 
                                            y+(self.block_size/2 - text.get_height()/2))))

        pygame.display.flip()

    def _check_victory(self):
        if sum([self.clicked[i].count(1) for i in range(len(self.clicked))]) == self.size * self.size:
            print("YOU WIN!!!")
            pygame.quit()
            quit()  


    def play(self):
        while True:
            self._draw()
            for event in pygame.event.get():    
                if event.type == pygame.QUIT:
                    print("QUIT")
                    pygame.quit()
                    quit()
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_presses = pygame.mouse.get_pressed()
                    if mouse_presses[0]:
                        mx, my = pygame.mouse.get_pos()
                        
                        xp = mx//self.block_size
                        yp = my//self.block_size

                        value = self.field.get_value(xp,yp)
                        self._check_victory()
                        if self.interface[xp][yp] != "P":
                            if value == -1:
                                print("GAME OVER!!!")
                                pygame.quit()
                                quit()  

                            # self.clicked, self.interface = self.field.undercover(board=self.clicked,
                            #                                                      interface=self.interface,
                            #                                                      x=xp, y=yp)

                            self.clicked, self.interface = self.field.reveal_squares(xp, yp, 
                                                                                     self.clicked, self.interface)

                    elif mouse_presses[2]:
                        mx, my = pygame.mouse.get_pos()
                        
                        xp = mx//self.block_size
                        yp = my//self.block_size
                        self._check_victory()
                        if self.interface[xp][yp] == 0:
                            self.interface[xp][yp] = 'P'
                            self.clicked[xp][yp] = 1

                        elif self.interface[xp][yp] == 'P':
                            self.interface[xp][yp] = 0
                            self.clicked[xp][yp] = 0
            
            self.clock.tick(30)
