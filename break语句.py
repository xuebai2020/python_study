'''
第一个实例
for letter in 'pathon':
    if letter == 'a':
        break
    print('当前字母：',letter)


第二个实例
'''
#break终止循环，嵌套循环中break将停止执行最深层的循环，并开始执行下一行代码
var = 10
while var > 0 :
    print('当前变量值：',var)
    var = var-1
    if var==5:     #当变量var等于5时退出循环
        break
print('goodbye！')


