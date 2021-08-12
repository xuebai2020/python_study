'''
if not(i % j):
初学python，看到这行代码有些费解，找到答案后在此分享一下。
在python中false == 0或空，true ==1或非空。
i%j 取余数，当余数是0(能整除)是false，加上not变成true。不能整除相反。
所以这句的意思是如果能整除则进行下面的代码


i = 2
while i < 100: #限制i的范围
    j = 2
    while j <= i/j: #限制j的范围
        if not(i % j): #如果能整除则进行下面的代码
            break #能整除则跳出,直接进行i=i+1，不是素数不打印
        j = j + 1 #不能整除则j+1继续

    if(j > (i/j)): #加到j大于根号i还没有找到可被i整除的数，则应该满足素数的要求，打印
        print(i, " 是素数")
    i = i + 1

print ("Good bye!")



#使用嵌套循环来获取100以内的质数
num = []
i = 2
for i in range (2,100) :
    j = 2
    for j in range (2,i) :
        if(i%j == 0) : break
    else :
         num.append(i)
print(num)

'''

#使用嵌套循环实现*字塔
i = 1
j = 1
while i <= 9 :
    if i <= 5:
        print('*'*i)
    elif i <= 9 and i > 5 :
        j = i-2*(i-5)
        print('*'*j)
    i += 1
else:
    print('')


























