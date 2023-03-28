# coding:utf-8
import sys
import pygame
import random

pygame.init()                       # 初始化pygame
size = width, height = 640, 480     # 设置窗口大小
screen = pygame.display.set_mode(size)  # 显示窗口

color = (0, 0, 0)  # 设置颜色
ball = pygame.image.load('ball.png')  # 加载图片
ballrect = ball.get_rect()  # 获取矩形区域

clock = pygame.time.Clock()  # 设置时钟

while True:  # 死循环确保窗口一直显示
    clock.tick(1) # 每秒执行次数
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    speed = [x, y]  # 设置移动的X轴、Y轴
    print(speed)
    for event in pygame.event.get():  # 遍历所有事件
        if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
            sys.exit()
    ballrect = ballrect.move(speed)
    if ballrect.left > 0 or ballrect.right < width:
        speed[0] = -speed[0]
    if ballrect.top > 0 or ballrect.bottom < width:
        speed[1] = -speed[1]
    screen.fill(color)  # 填充颜色(设置为0，执不执行这行代码都一样)
    screen.blit(ball, ballrect)  # 将图片画到窗口上
    pygame.display.flip()  # 更新全部显示

pygame.quit()  # 退出pygame
