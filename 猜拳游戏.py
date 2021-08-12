import random

from pip._vendor.distlib.compat import raw_input

while 1 :
    s = int (random.randint(1,3))
    if s == 1 :
        ind = '石头'
    elif s == 2 :
        ind = '剪刀'
    elif s == 3 :
        ind = '布'
    m = raw_input ('输入石头、剪刀、布，输入"end"退出游戏!\n')
    blist = ['石头','剪刀','布']
    if (m not in blist) and (m != 'end') :
        print('输入错误，请重新输入！')
    elif (m not in blist) and (m == 'end') :
        print('\n退出游戏！')
    elif m == ind :
        print('电脑出了：' + ind + ',平局！')
    elif (m == '石头' and ind == '剪刀') or (m == '剪刀' and ind == '布') or (m == '布' and ind == '石头') :
        print('电脑出了：' + ind + ',你赢了！')
    elif (m == '石头' and ind == '布') or (m == '剪刀' and ind == '石头') or (m == '布' and ind == '剪刀'):
        print('电脑出了：' + ind + ',你输了！')

