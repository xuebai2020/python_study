class Animal:
    def __init__(self,name):
        self.names=name
    def show_info(self):
        return '动物：{}'.format(self.names)
    def move(self):
        print('动一动...')

class Cat(Animal):
    def __init__(self,name,age):
        super().__init__(name)
        self.ages=age

cat=Cat('tongtong',2)
print(cat.show_info())
cat.move()