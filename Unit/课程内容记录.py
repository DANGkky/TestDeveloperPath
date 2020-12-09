
'''
https://docs.python.org/3/library/unittest.html
test fixture
test case
test suite
test runner
'''


'''
使用allure生成报告的方法
先用命令生成一个报告
(venv) D:\TestDeveloperLearn\TestDeveloper>pytest --alluredir=.\Unit\allure_results
再allure serve把报告在浏览器中打开
(venv) D:\TestDeveloperLearn\TestDeveloper>allure serve Unit\allure_results
'''

'''

使用allure生成index.html的报告，并且通过python临时搭建服务器的方法
在PYCHARM里：
(venv) D:\TestDeveloperLearn\TestDeveloper>cd Unit
(venv) D:\TestDeveloperLearn\TestDeveloper\Unit>allure generate allure_results -o allure
(venv) D:\TestDeveloperLearn\TestDeveloper\Unit>cd allure
(venv) D:\TestDeveloperLearn\TestDeveloper\Unit\allure>python -m http.server
打开127.0.0.1:8000即可打开。

从桌面CMD进入时：
cd到对应的目录 比如 
D:\Users\80230531>cd D:\TestDeveloperLearn\TestDeveloper\Unit
D:\TestDeveloperLearn\TestDeveloper\Unit>allure generate allure_results -o allure
D:\TestDeveloperLearn\TestDeveloper\Unit>cd allure
D:\TestDeveloperLearn\TestDeveloper\Unit\allure>python -m http.server
打开127.0.0.1:8000即可打开。
【注意，打开地址的目录，需要和allure文件夹一样】
'''

