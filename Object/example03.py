"""
@ Author: shishaoquan
@ Time:  
@ Project: 


"""

# 面向对象编程范式
# 2 个 对象, 一个小，一个大
# 定义 圆 这个类
# 用 面向对象编程思想解决问题
# initialize ---> 初始化
# 前后有两个下划线
# 写好了吗？
import math


class Circle:
    # 数据抽象
    def __init__(self, radius):
        self.radius = radius

    # 行为抽象
    def perimeter(self):
        """
        周长
        :return:
        """
        return 2 * math.pi * self.radius

    def area(self):
        """
        面积
        :return:
        """
        return math.pi * self.radius ** 2


if __name__ == '__main__':
    r = float(input('请输入游泳池的半径：'))
    c1 = Circle(r)
    c2 = Circle(r + 3)

    fence_price = c2.perimeter() * 38.5
    aisle_price = (c2.area() - c1.area()) * 58.5

    print(f'围墙的造价： {fence_price:.2f} 元')
    print(f'过道的造价: {aisle_price:.2f} 元')
    print(f'总计：{fence_price + aisle_price:.2f} 元')





