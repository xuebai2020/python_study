class DefException(Exception):
    def __init__(self,message):
        super().__init__(message)

i=input('请输入数字：')
n=8888
try:
    result=n/int(i)
    print(result)
    print('{0}除以{1}等于{2}'.format(n,i,result))

except ZeroDivisionError as e:
    print('不能除以0，异常：{}'.format(e))

except ValueError as e:
    #print('输入的是无效数字，异常：{0}'.format(e))
    raise DefException('输入的是无效数字')

except:
    print('异常')

finally:
    print('释放资源')