
#字典创建 while开关  字典添加 字典寻找
from Tools.scripts.treesync import raw_input

dictionary = {}
flag = 'a'
page = 'a'
off = 'a'
word = 'a'
defintion = 'a'

while flag == 'a' or 'c':
    flag = raw_input("添加或查找字典？（a/c)")
    if flag == "a":
        word = raw_input("输入单词（key）：")
        defintion = raw_input("输入定义值（value）：")
        dictionary[str(word)] = str(defintion)
        print("添加成功！")

        if page == 'a' :
            print(dictionary)
        else :
            continue
    elif flag == "c" :
        check_word = raw_input("要查找的单词：")
        for key in sorted(dictionary.keys()):
            if str(check_word) == key :
                print("该单词存在！",key ,dictionary[key])
                break
            else :
                off = 'b'
        if off == 'b' :
            print("抱歉，该值不存在！")
    else:
        print("error type")
        break
