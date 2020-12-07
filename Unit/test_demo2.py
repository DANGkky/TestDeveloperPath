import unittest


class TestDemo(unittest.TestCase):
    # unittest要求测试的类里需要继承上面的unittest.TestCase方法

    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")

    def setUp(self) -> None:
        print("\nsetup\n")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def tearDown(self) -> None:
        print("\nteardown\n")

    def test_sum(self):
        print("test_sum")
        x = 1 + 2
        print(x)
        self.assertEqual(3, x, f'x={x} expection=3')

    def test_demo(self):
        print("test_demo")
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()
