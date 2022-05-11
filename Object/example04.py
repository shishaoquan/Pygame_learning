"""
@ Author: shishaoquan
@ Time:  
@ Project: 


"""


# 创建时钟对象
import os
import time


class Clock:

    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second

    # 行为抽象
    def show(self):
        """显示时间"""
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.second:0>2d}'

    def run(self):
        """走字"""
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
            if self.minute == 60:
                self.minute = 0
                self.hour += 1
                if self.hour == 24:
                    self.hour = 0


if __name__ == '__main__':
    clock = Clock(23, 59, 58)
    while True:
        os.system('cls')
        print(clock.show())
        time.sleep(1)
        clock.run()









