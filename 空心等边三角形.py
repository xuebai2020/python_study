from pip._vendor.distlib.compat import raw_input

print('输出空心等边三角形！')
rows = int(raw_input('请输入行数：'))
for i in range (0,rows) :
    for k in range (0,2*rows-1) :
        if (i != rows-1) and (k == rows-i-1 or k == rows+i-1) :
              print('*' , end = '')
        elif (i == rows-1):
              if (k % 2 == 0) :
                 print('*', end = '')
              else :
                 print(' ', end = '')
        else :
               print(' ', end = '')
    print('\n')