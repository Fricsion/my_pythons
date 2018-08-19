#_*_coding:utf-8_*_
import sys
import pygame
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (400, 300)

screen = pygame.display.set_mode(WINDOW_SIZE)

#player_layer = pygame.display.set_mode((20, 20))

pygame.display.set_caption("DarkSouls")
    
class Player:
    def __init__(self, filename, x, y):
        
        self.my_combat = pygame.image.load(filename).convert_alpha()
        width = self.my_combat.get_width()
        height = self.my_combat.get_height()
        self.rect = Rect(x, y, width, height)

    def draw(self, screen):

        screen.blit(self.my_combat, self.rect)

    def move(self):

        pressed_key = pygame.key.get_pressed()
        if pressed_key[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_key[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if pressed_key[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_key[K_DOWN]:
            self.rect.move_ip(0, 5)




        

def main():
    
    player = Player("images/heart.png", 20, 20)



    while True:

        # 処理関連 ----------------
 
        player.move()


        # 描画関連 ----------------


        screen.fill((0, 0, 0))

        player.draw(screen)

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

