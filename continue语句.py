#跳出本次循环
'''
for letter in 'pathon':
    if letter == 'h':
        continue
    print('当前字母：',letter)

var = 10
while var > 0:
    var = var-1
    if var==5:
        continue
    print('当前变量值：',var)
print('goodbye!')

'''
#实例
i = 0
while i < 10:
    i += 1
    if i%2==0:  #如果i是偶数，执行continue
        continue  #continue会直接继续执行下一轮循环，后续print不会执行
    print(i)