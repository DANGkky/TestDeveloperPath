
'''
运行顺序相关：

运行的优先级：setup_class》setup_method》setup 》用例》teardown》teardown_method》teardown_class
备注：这里setup_method和teardown_method的功能和setup/teardown功能是一样的，一般二者用其中一个即可
'''


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5
