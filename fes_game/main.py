#_*_coding:utf-8_*_
import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption("DarkSouls")


def main():
    
    while True:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

                sys.exit
    
        pygame.display.update()

if __name__ == '__main__':
    main()

