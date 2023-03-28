# coding:utf-8
import pygame.image


class Ship:
    """管理飞船的类"""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # 加载飞船图像并获取其外界矩形坐标
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于新飞船，初始化屏幕底部中央
        self.rect.midbottom = self.screen_rect.midbottom

        # 左右移动属性
        self.move_right = False
        self.move_left = False
        self.move_up = False
        self.move_down = False

        # 移动速度
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        elif self.move_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        elif self.move_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        self.rect.x = self.x
        self.rect.y = self.y

    def blitme(self):
        """在指定位置绘制飞船surface"""
        self.screen.blit(self.image, self.rect)
