
have_girl = False   #定义变量have_girl

def send():
    print("发女朋友！")
    global have_girl    #使其变成全局变量，使得外部变量在函数也可以修改
    have_girl = True
    print(f"have_girl = {have_girl}")

def show():
    if have_girl == True:
        print("有女朋友，好开心！")
    else:
        print("单身贵族！")
    return have_girl

#print(__name__)

if __name__ == '__main__':
    send()
    print(show())
