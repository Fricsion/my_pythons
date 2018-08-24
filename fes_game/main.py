#_*_coding:utf-8_*_
import sys
import random
import pygame
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (400, 300)

screen = pygame.display.set_mode(WINDOW_SIZE)

#player_layer = pygame.display.set_mode((20, 20))

pygame.display.set_caption("DarkSouls")
 
def load_image(filename, width, height):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image

   
class Player:
    def __init__(self, filename, x, y):
        
        self.my_combat = load_image(filename, 20, 20)
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


class Barrage:
    def __init__(self, filename, x, y, width, height):
        
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.barrage = load_image(filename, width, height) 

        self.rect = Rect(x, y, width, height)

    def update(self):

        direct = random.randint(0, 3)

        if direct == 0:
            self.rect.move_ip(-5, 0)
        if direct == 1:
            self.rect.move_ip(5, 0)
        if direct == 2:
            self.rect.move_ip(0, -5)
        if direct == 3:
            self.rect.move_ip(0, 5)



#    def draw(self, screen):
#
#        screen.blit(self.barrage, self.rect)

class Button:
    def __init__(self, filename, x, y, width, height):
        
        self.button = load_image(filename, width, height)

        self.rect = Rect(x, y, width, height)



    def draw(self):

        self.blit(self.button, self.rect)

        
def main():

    game_status = 0
    # ステータス、０：タイトル。
    
    player = Player("images/heart.png", 200, 150)

    bar1 = Barrage("images/asteroid1.png", 20, 75, 50, 50) 
    bar2 = Barrage("images/asteroid2.png", 380, 75, 50, 50) 
    bars = pygame.sprite.RenderUpdates()
    Barrage.containers = bars
   

    while True:

        # 処理関連 ----------------
 
        player.move()
#        bar1.move()
#        bar2.move()
        bars.update()

        # 描画関連 ----------------


        screen.fill((0, 0, 0))

        player.draw(screen)
#        bar1.draw(screen)
#        bar2.draw(screen)
        bars.draw(screen)

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

