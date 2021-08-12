'''
x = 10
def print_value():
#    global x
    x = 20
    print('局部变量：{0}'.format(x))

print_value()
print('全局变量：{0}'.format(x))
'''

data1 = [12,13,23,33,45,56,67,88]
filtered=filter(lambda x:(x>40),data1)
maped=map(lambda y:(y*2),data1)
data2 = list(filtered)
data3 = list(maped)
print('大于40的数为{0}'.format(data2))
print('以上的数乘2后为{0}'.format(data3))