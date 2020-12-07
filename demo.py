# print('py','thon')
# print('hello')
from TestDeveloper.sdet.Student import Student


def x(a, b=1, *c, **d):
    '''
    函数传参数 函数拆箱
    '''
    print(f"a={a}")
    print(f"b={b}")
    print(f"c={c}")
    print(f"d={d}")


x(2)
x(2,3)
x(2,3,4)
x(2,3,4,5)
x(2,3,4,5,'a')
x(2,3,4,5,'a',x=1,y=2)


# def num(a,b=1):
#     x=a+1+b
#     print(x)
#
# num(2)
# num(2,3)


class Dog:
    kind = 'habagou'

    def __init__(self, name, *dogsize):
        self.name = name
        self.size = dogsize


Student().gotoschool('PE class')

#check check
