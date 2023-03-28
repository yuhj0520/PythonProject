# coding:utf-8
class Setting:
    """设置类"""

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船移动速度
        self.ship_speed = 1.5

        # 子弹的设置
        self.bullet_speed = 1
        self.bullet_width = 3
        self.bullet_hight = 15
        self.bullet_color = (60, 60, 60)
