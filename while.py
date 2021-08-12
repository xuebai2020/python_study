'''
numbers = [12, 37, 5, 42, 8, 3]
evev = []
odd = []
while len(numbers) > 0 :
    number = numbers.pop()
    if (number % 2 == 0) :
        evev.append(number)
    else :
        odd.append(number)
print('evev为' , evev)
print('odd为' , odd)
'''
from Tools.scripts.treesync import raw_input

'''
count = 0
while count < 9 :
    count = count + 1
    print('The count is : ' , count)
print('Good bye!')
'''
'''
#continue和break
i = 1
while i < 10 :
    i += 1
    if i % 2 > 0 :
        continue
    print(i)

j = 1
while 1 :
    j += 1
    if j > 10 :
      break
    print(j)
'''
'''
#无限循环
var = 1
while var == 1 :
    num = raw_input("Enter a number :")
    print("You entered :", num)
print("Good bye!")
'''
count = 0
while count < 5 :
    count += 1
    print(count,"is less than 5")
else :
    print(count,"is not less than 5")