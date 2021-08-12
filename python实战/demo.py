name = 'bob'
a = 1
print(id(a))    #打印出a值的内存地址

def fun():
    print(f"名字是{name}")
fun()

def func():
    global a  #将a变成全局变量,使外部变量在方法内对它修改
    a = 3   #方法中的局部变量,只能在函数中使用
    print(f"a = {a}")
print(a)
func()