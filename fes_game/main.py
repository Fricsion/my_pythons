#_*_coding:utf-8_*_
import sys
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption("DarkSouls")

pos = [20, 20]

def main():
    
    while True:

        # Processor ----------------
        
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            pos[0] -= 5
        if pressed_key[K_RIGHT]:
            pos[0] += 5
        if pressed_key[K_UP]:
            pos[1] -= 5
        if pressed_key[K_DOWN]:
            pos[1] += 5

   


        # Rendering ----------------


        screen.fill((0, 0, 0))

        pygame.draw.circle(screen, (255, 255, 255), (pos[0], pos[1]), 10)


        pygame.display.update()



        # Relating input ----------------

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

                sys.exit

            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
#                if event.key == K_LEFT:
#                    pos[0] -= 5
#                elif event.key == K_RIGHT:
#                    pos[0] += 5
#                elif event.key == K_UP:
#                    pos[1] -= 5
#                elif event.key == K_DOWN:
#                    pos[1] += 5


    
if __name__ == '__main__':
    main()

