class A:
    Country='中国'
    def __init__(self,name,age,country):
        self.name=name
        self.age=age

    def pp(self):
        return self.Country


a=A('alex',83,'印度')
b=A('heihei',56,'朝鲜')
print(a.pp())
print(a.Country)
print(a.name)