"""
创建一个person类
    属性：姓名、年龄、性别、存款金额
    方法：吃、睡、跑、赚钱

创建FunnyMan类（喜剧演员）
    继承父类person所有属性和方法
    新增一个方法fun（）搞笑

创建singerman类（歌手演员）
    继承父类persom的所有属性和方法
    覆写方法、赚钱、传参（monkey）
"""

class Person():
    name:str = "default"
    gender:str = "default"
    age:int = 20
    __money:float = 1000     #属性前加__，属性将变成私有属性，不能被子类继承，不能被访问

    '''
    def set_name(self,name):   #set_name方法，传入一个name
       self.name = name        #self.name则代表类变量的name（name：str），类变量也可以通过实例变量来调用
    '''
    @classmethod  #类方法
    def classmethod(cls):
        pass

    def __init__(self,name,gender,age,money):   #在init方法中实例化
        print("start init")
        self.name = name
        self.gender = gender
        self.age = age
        self.__money = money
        print("end init")

    def get_money(self):
        print(f"获取私有属性的值{self.__money}")
        return self.__money

    def eat(self):
        print(f"{self.name} is eating!")

    def sleep(self):
        print(f"{self.name} is sleeping!")

    def run(self):
        print(f"{self.name} is running!")

    '''
    def __make_money(self):    #私有方法
        print(f"{self.name} could make money!")
    '''

    def make_money(self):
        print(f"{self.name} could make money!")

#继承person类
class FunnyMan(Person):
    def fun(self):
        print(f"{self.name} is very funny!")

class singerMan(Person):
    def make_money(self,moneynum:str=None):
        print(f"{self.name} could make money {moneynum}")

class chengxuyuan(Person):
    def write_code(self):
        print(f"{self.name} could write code!")

    @classmethod
    def zhengshu(cls):
        print("我有证书")

    @staticmethod
    def jingtai():
        print("这是一个静态方法")

'''
#实例化一个具体的人
p = Person("lily","女",14,12222)
print(p.name)
p.eat()
p.get_money()
print(dir(p))    #当前实例有哪些可调用的方法
#p._Person__make_money()
print(p._Person__money)
#p.__monkey()       父类也不能访问到
#p.set_name("tom")
'''

'''
funnyman = FunnyMan("沈腾","男",23,2222)
print(funnyman.name)
funnyman.eat()
funnyman.fun()
'''

'''
singer = singerMan("jjj","男",33,188888)
singer.make_money(108888888)
'''

gezishan = chengxuyuan("jerry","男",44,999999)
gezishan.write_code()
chengxuyuan.zhengshu()
chengxuyuan.jingtai()