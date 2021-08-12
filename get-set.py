class Dog:
    def __init__(self,name,age):
        self.names=name
        self.__ages=age
    def run(self):
        print('{}在跑！'.format(self.names))
    def get_age(self):
        return self.__ages
    def set_age(self,age):
        self.__ages=age
    @property
    def age(self):
        return self.__ages
    @age.setter
    def age(self,age):
        self.__ages=age
dog1=Dog('tongtong',1)
print('{}的年龄是{}'.format(dog1.names,dog1.get_age()))
dog1.set_age(3)
print('{}两年后的年龄是{}'.format(dog1.names,dog1.get_age()))

dog2=Dog('yueue',2)
print('{}的年龄是{}'.format(dog2.names,dog2.age))
dog2.age=3
print('{}一年后的年龄是{}'.format(dog2.names,dog2.age))