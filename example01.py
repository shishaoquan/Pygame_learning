"""
@ Author: shishaoquan
@ Time:  
@ Project: 


"""


# pygame 入门训练
# 系统的仿真功能
# 游戏开发引擎
# 非常好的

import pygame, sys

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Pygame游戏之旅')
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    pygame.display.update()





