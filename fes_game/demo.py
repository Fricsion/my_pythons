#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame
from pygame.locals import *
import sys

SCR_RECT = Rect(0, 0, 640, 480)

def load_image(filename, width, height):
    image = pygame.image.load(filename).convert_alpha()
    image = pygame.transform.scale(image, (width, height))
    return image

class Barrage(pygame.sprite.Sprite):
    def __init__(self, filename, x, y, vx, vy, width, height):
        # デフォルトグループをセット
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = load_image(filename, width, height)
        width = self.image.get_width()
        height = self.image.get_height()
        self.rect = Rect(x, y, width, height)
        self.vx = vx
        self.vy = vy
    
    def update(self):
        self.rect.move_ip(self.vx, self.vy)
        # 壁にぶつかったら跳ね返る
        if self.rect.left < 0 or self.rect.right > SCR_RECT.width:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > SCR_RECT.height:
            self.vy = -self.vy
        # 画面からはみ出ないようにする
        self.rect = self.rect.clamp(SCR_RECT)

def main():
    pygame.init()
    screen = pygame.display.set_mode(SCR_RECT.size)
    pygame.display.set_caption(u"Undertale")
    
    # スプライトグループを作成してスプライトクラスに割り当て
    group = pygame.sprite.RenderUpdates()
    Barrage.containers = group
    
    # スプライトを作成
    bar1 = Barrage("images/asteroid1.png", 0, 0, 2, 2, 30, 30)
    bar2 = Barrage("images/asteroid2.png", 10, 10, 5, 5, 30, 30)
    bar3 = Barrage("images/asteroid3.png", 320, 240, -2, 3, 30, 30)
    
    clock = pygame.time.Clock()
    
    while True:
        clock.tick(60)  # 60fps
        screen.fill((0,0,0))
        # スプライトグループを更新
        group.update()
        # スプライトグループを描画
        group.draw(screen)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()
