message = {}


def new():
    temp = "请输入用户名："
    while 1:
        name = input(temp)
        # 如果有此人的信息
        if name in message:
            temp = "此用户已被使用，请重新输入："
            continue
        # 没有此人的信息
        if name not in message:
            break

    pw = input("请输入密码：")
    message[name] = pw
    print("注册成功，登陆试试吧")


def old():
    temp = "请输入姓名："
    while 1:
        name = input(temp)
        if name not in message:
            temp = "此用户不存在，请重新输入："
            continue

        else:
            break

    pw = input("请输入密码：")
    password = message.get(name)
    if pw == password:
        print("欢迎您`")
    else:
        print("密码错误！")


def menu():
    print("""
    |--- 新建用户：N/n ---|
    |--- 登录账号：E/e ---|
    |--- 退出登录：Q/q ---|
    """)

    while True:
        chose = 0
        while not chose:
            print('\n')
            order = input("请输入指令：")
            if order not in 'QqNnEe':
                print("指令输入有误！请重新输入")
            else:
                chose = 1

        if order == 'N' or order == 'n':
            new()
        if order == 'E' or order == 'e':
            old()
        if order == 'Q' or order == 'q':
            break

menu()
