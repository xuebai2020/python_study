class Horse:
    def __init__(self,name):
        self.names=name

    def show_info(self):
        return '马的名字是{}'.format(self.names)

    def run(self):
        print('马在跑。。。')

class Donkey:
    def __init__(self,name):
        self.names=name

    def show_info(self):
        return '驴的名字是{}'.format(self.names)

    def run(self):
        print('驴在跑。。。')

    def roll(self):
        print('打滚儿。。。')

class Mule(Horse,Donkey):
    def __init__(self,name,age):
        super().__init__(name)
        self.ages=age
    #重写show_info方法
    def show_info(self):
        return '骡的名字是{},年龄是{}'.format(self.names,self.ages)

m=Mule('tian',2)
m.run()
m.roll()
print(m.show_info())  #调用的是子类Mule中的show_info方法

