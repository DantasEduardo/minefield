import pygame
import os
from src.board import Board


class Screen:
    def __init__(self, width:int, heigth:int, size:int, bomb:float)->object:
        """Initialize Screen and set the board"""
        self.board = Board(size, bomb)
        self.images = {}
        self.sizeScreen = width, heigth
        self.blockSize = (self.sizeScreen[0] / size[1], self.sizeScreen[1] / size[0]) 
        
        pygame.init()
        self.screen = pygame.display.set_mode(self.sizeScreen)
        self.__load_pictures()

    def __load_pictures(self)->None:
        """Load the pictures to use in the board"""
        imagesDirectory = "./src/imgs"
        for fileName in os.listdir(imagesDirectory): 
            img = pygame.image.load(f"{imagesDirectory}/{fileName}")
            img = img.convert()
            img = pygame.transform.scale(img, (int(self.blockSize[0]), int(self.blockSize[1])))
            self.images[fileName.split(".")[0]] = img

    def __get_img_name(self, block:object)->str:
        """Returns the image name according to block type"""
        if block.get_clicked():
            return str(block.get_num_around()) if not block.get_has_bomb() else 'bomb-at-clicked-block'
        if self.board.get_lost():
            if block.get_has_bomb():
                return 'unclicked-bomb'
            else:
                return 'wrong-flag' if block.get_flagged() else 'empty-block'
        else:
            return 'flag' if block.get_flagged() else 'empty-block'
    
    def __handle_click(self, position:tuple, flag:tuple):
        index = tuple(int(pos // size) for pos, size in zip(position, self.blockSize))[::-1] 
        self.board.handle_click(self.board.get_block(index), flag)
    
    def __draw(self)->None:
        """Draw the board in the screen"""
        topLeft = (0, 0)
        for row in self.board.get_board():
            for block in row:
                rect = pygame.Rect(topLeft, self.blockSize)
                image = self.images[self.__get_img_name(block)]
                self.screen.blit(image, topLeft) 
                topLeft = topLeft[0] + self.blockSize[0], topLeft[1]
            topLeft = (0, topLeft[1] + self.blockSize[1])

    def run(self)->None:
        """Run the game"""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN and not (self.board.get_won() or self.board.get_lost()):
                    rightClick = pygame.mouse.get_pressed(num_buttons=3)[2]
                    self.__handle_click(pygame.mouse.get_pos(), rightClick)
                
            self.screen.fill((0, 0, 0))
            self.__draw()
            pygame.display.flip()
            
            if self.board.get_won():
                print("YOU WIN!!!!")
                running = False
            if self.board.get_lost():
                print("YOU LOSE!!!!")
                running = False

        pygame.quit()