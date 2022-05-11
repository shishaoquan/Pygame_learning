"""
@ Author: shishaoquan
@ Time: $ 
@ Project: $


"""


# 静态方法：
# 类中的方法：他们是函数，是对象可以接收的消息
# 基本上都是
# 但是有些消息并不是发给对象的消息
# 但有的时候，消息并不想发送给对象，而是希望发送给这个类
# 对象的四大特色，这个时候，可以使用静态方法和类方法
# 知不知道，必须要说明
# 接收


class Triangle:

    def __init__(self, a, b, c):
        if not Triangle.is_valid(a, b, c):
            raise ValueError('无效的边长')
        self.a = a
        self.b = b
        self.c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        half = self.perimeter() / 2
        return (half * (half - self.a) * (half - self.b) * (half - self.c)) ** 0.5


if __name__ == '__main__':
    t = Triangle(1, 2, 3)
    print(t.perimeter())
    print(t.area())
