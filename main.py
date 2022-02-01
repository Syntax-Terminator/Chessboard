import pygame, sys
from _chessboard import CREATE_CHESSBOARD

pygame.init()

WIDTH = HEIGHT = 700
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

def mainloop():

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        CREATE_CHESSBOARD(WIDTH, HEIGHT, WINDOW)

        pygame.display.update()

mainloop()
