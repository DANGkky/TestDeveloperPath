import pytest

'''
运行顺序相关：

运行的优先级：setup_class》setup_method》setup 》用例》teardown》teardown_method》teardown_class
备注：这里setup_method和teardown_method的功能和setup/teardown功能是一样的，一般二者用其中一个即可

setup_module/teardown_module的优先级是最大的
然后函数里面用到的setup_function/teardown_function与类里面的setup_class/teardown_class互不干涉，互相分开执行
'''


def setup_module():
    print("setup_module：整个.py模块只执行一次")
    print("比如：所有用例开始前只打开一次浏览器")


def teardown_module():
    print("teardown_module：整个.py模块只执行一次")
    print("比如：所有用例结束只最后关闭浏览器")


def setup_function():
    print("setup_function：每个用例开始前都会执行")


def teardown_function():
    print("teardown_function：每个用例结束前都会执行")


def test_one():
    print("正在执行----test_one")
    x = "this"
    assert 'h' in x


def test_two():
    print("正在执行----test_two")
    x = "hello"
    assert hasattr(x, 'llo')


class TestCase():

    def setup_class(self):
        print("setup_class：所有用例执行之前")

    def teardown_class(self):
        print("teardown_class：所有用例执行之前")

    def setup(self):
        print("setup:类中单个用例执行之前")

    def teardown_method(self):
        print("teardown_method:类中单个用例执行之后")

    def test_three(self):
        print("正在执行----test_three")
        x = "this"
        assert 'h' in x

    def test_four(self):
        print("正在执行----test_four")
        x = "hello"
        assert hasattr(x, 'check')


if __name__ == "__main__":
    pytest.main(["-s", "test_fixtclass.py"])
