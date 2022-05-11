"""
@ Author: shishaoquan
@ Time:  
@ Project: 


"""

# 创建对象, 给对象发消息
from Object.example01 import Student

# ---> 构造器语法 ---> 类名 (...,...)

stu1 = Student('王大追', 15)
stu2 = Student('石少全', 26)
stu1.watch_tv('你好')
# 调用对象的方法, 给对象发消息
stu1.study('Python程序设计')
# 还是需要继续实战
stu1.eat()
stu2.play('CF')
stu2.watch_tv('BiliBili')










