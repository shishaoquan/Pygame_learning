"""
@ Author: shishaoquan
@ Time: $ 
@ Project: $


"""


# 1 主程序
import pygame.display


class MainGame():
    # 2 创建关数，得分，剩余分数等
    shaoguan = 1
    score = 0
    remain_score = 100
    money = 200
    # 3 存储所有地图坐标点
    map_points_list = []
    # 3 存储所有的地图块
    map_list = []
    # 4 存储所有的植物列表
    plants_list = []
    # 7 存储所有豌豆子弹的列表
    peabullet_list = []
    # 9 新增存储所有僵尸的列表
    zombie_list = []
    count_zombie = 0
    produce_zombie = 100


    # 1 加载游戏窗口
    def init_window(self):
        pygame.display.init()
        # 1 创建窗口
        # 还是没看懂
        MainGame.window = pygame.display.set_mode([screen_width,
                                                   screen_height])

    # 2 文本绘制
    def draw_text(self, content, size, color):
        pygame.font.init()
        font = pygame.font.SysFont('kaiti', size)
        text = font.render(content, True, color)
        return text

    # 2 加载帮助提示
    def load_help_text(self):
        text1 = self.draw_text('1. 鼠标左键'
                               '创建向日葵'
                               '2. 鼠标右键创建豌豆射手')
        MainGame.window.blit(text1, (5, 5))
        # 待续













