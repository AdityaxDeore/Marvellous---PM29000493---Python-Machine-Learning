
class Demo:
    value1 = 10

    def __init__(self,x,y):
        self.value2 = 20


    def fun(self):
        print("Inside fun")
        print(self.value2)
        print(Demo.value1)

    @classmethod
    def gun(cls):
        print("Inside gun")
        print(cls.value1)



obj1 = Demo(11 , 21)
obj2 = Demo(51 , 101)

obj2.fun()
obj1.gun()
obj2.gun()
