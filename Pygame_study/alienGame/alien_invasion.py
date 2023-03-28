# coding:utf-8
import sys

import pygame

from alienGame.ship import Ship
from alienGame.setting import *


class AlienInvasion:
    """管理游戏资源和行为动作的类"""

    def __init__(self):
        """初始化游戏并创建游戏资源"""
        pygame.init()  # 初始化背景及设置
        self.settings = Setting()

        # self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # 全屏游戏，需要重新设置游戏窗口大小，start
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        # 全屏游戏，end
        pygame.display.set_caption('Alien Invasion')

        self.ship = Ship(self)

    def run_game(self):
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        """事件监听"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _update_screen(self):
        """更新屏幕图像"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        pygame.display.flip()

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            # 右移属性为true
            self.ship.move_right = True
        if event.key == pygame.K_LEFT:
            # 左移属性为true
            self.ship.move_left = True
        if event.key == pygame.K_UP:
            self.ship.move_up = True
        if event.key == pygame.K_DOWN:
            self.ship.move_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            # 右移属性为false
            self.ship.move_right = False
        if event.key == pygame.K_LEFT:
            # 左移属性为false
            self.ship.move_left = False
        if event.key == pygame.K_UP:
            self.ship.move_up = False
        if event.key == pygame.K_DOWN:
            self.ship.move_down = False


if __name__ == '__main__':
    # 创建游戏实例并运行游戏
    ai = AlienInvasion()
    ai.run_game()
