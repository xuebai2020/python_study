dict1 = {102:'张',103:'李',104:'王',105:'周'}
print('遍历键')
for key in dict1.keys():
    print('学号：'+str(key))

print('遍历值')
for value in dict1.values():
    print('姓名：'+value)

print('遍历字典')
for key,value in dict1.items():
    print('学号：{0}-姓名：{1}'.format(key,value))