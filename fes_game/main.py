#_*_coding:utf-8_*_
import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption("DarkSouls")

img = pygame.image.load("images/earth.png")

pos = [10, 10]


def main():
    
    while True:

        # Processor ----------------
        rect = img.get_rect()
        rect.center = pos

        pygame.transform.scale(img, (20, 20))


        # Rendering ----------------


        screen.fill((0, 0, 0))

        screen.blit(img, rect)
        pygame.display.update()


        # Relating input ----------------

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

                sys.exit
    
if __name__ == '__main__':
    main()

