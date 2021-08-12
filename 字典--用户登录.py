'''
输入N/n，可新建用户；输入E/e，可登录；输入Q/q退出
|— 新建用户：N/n —|
|— 登录账号：E/e —|
|— 退出登录：Q/q —|
'''

print("""
|--- 新建用户：N/n ---|
|--- 登录账号：E/e ---|
|--- 退出登录：Q/q ---|
""")

message = {}
flag = 1
while flag:
    order = input("请输入指令代码：")
    if order == 'N' or order == 'n':
        name = input("请输入用户名：")
        while 1:
            # 如果有此人的信息
            if name in message:
                name = input("此用户已被使用，请重新输入：")

            # 没有此人的信息
            if name not in message:
                pw = input("请输入密码：")
                message[name] = [pw]
                break

    elif order == 'E' or order == 'e':
        name = input("请输入用户名：")
        while 1:
            # 输入的用户不存在
            if name not in message:
                name = input("输入的用户名不存在，请重新输入：")

            # 存在此用户
            if name in message:
                pw = input("请输入密码：")
                while 1:
                    pw = [pw]
                    if message[name] == pw:
                        print('欢迎欢迎，热烈欢迎！')
                        break
                    else:
                        pw = input("密码错误重新输入：")
                break

    elif order == 'Q' or order == 'q':
        print("程序退出了，再见~")
        flag = 0

    else:
        print("指令错误，请重新输入吧！")
    print()   # 主要目的是换行，让最后的显示好看一点n