#_*_coding:utf-8_*_
import sys
import pygame
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (400, 300)

screen = pygame.display.set_mode(WINDOW_SIZE)

#player_layer = pygame.display.set_mode((20, 20))

pygame.display.set_caption("DarkSouls")

class Player(pygame.sprite.Sprite):

    def __init__(self, radius, pos):


        self.radius = radius
        self.pos = pos
        

        
    def move(self):
 
        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            self.pos[0] -= 5
#            self.mine.move_ip(-5, 0)        
        if pressed_key[K_RIGHT]:
            self.pos[0] += 5
#            self.mine.move_ip(5, 0)
        if pressed_key[K_UP]:
            self.pos[1] -= 5
#            self.mine.move_ip(0, -5)
        if pressed_key[K_DOWN]:
            self.pos[1] += 5
#            self.mine.move_ip(0, 5)


    
    def draw(self):
        
        pygame.draw.circle(screen, (255, 255, 255), (self.pos[0], self.pos[1]), self.radius)
#        player_layer.fill((0, 0, 0))





def main():
    
    player = Player(10, [200, 150])



    while True:

        # 処理関連 ----------------

        player.move()
        player.draw()

          


        # 描画関連 ----------------


        screen.fill((0, 0, 0))



        pygame.display.update()



        # イベント関連 ----------------

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

