import girl    #它是导入girl.py模块，导入的是模块里的变量的内存地址，直接修改内存地址
#from girl import have_gril   导入girl.py里面的have_girl这个变量，复制了一份，修改的是本地中的copy变量

def send():
    print("发女朋友！")
    girl.have_girl = True
    #have_girl = True