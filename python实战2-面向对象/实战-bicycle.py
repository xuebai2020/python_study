'''
写一个bicycle（自行车）类，有run（骑行）方法，调用时显示骑行里程数km（骑行里程为传入的数字）
再写一个电动自行车ebicycle继承bicycle，添加电池电量battery_level属性通过参数传入，同时有两个方法：
    1.fill_charge(vol)用来充电，vol为电量
    2.run（km）方法用于骑行，每骑行10km消耗电量1度，当电量耗尽时调用bicycle的run方法骑行
通过传入的骑行里程数，显示骑行结果（就是当电量耗尽，需要你真正骑的里程数）
'''
import yaml

class Bycycle():
    def run(self,km):
        print(f"骑行的里程数:{km}km")

class EBycycle(Bycycle):
    # 在init中初始化的实例变量，self.battery_level为属性
    def __init__(self,battery_level):
        self.battery_level = battery_level

    def fill_charge(self,vol):
        print(f"充电:{vol}")

    def run(self,km):
        #每骑行10km消耗电量1度,有10度电，最多骑行10*10=100km
        max_mile = self.battery_level * 10    #用电骑行最多的里程数
        leave_mile = km - max_mile            #电量耗尽，自己骑行的里程数

        if leave_mile > 0:
            print(f"已经使用电量骑行的里程数：{max_mile}km")
            super().run(leave_mile)
        else:
            print(f"骑行的里程数：{km}")

if __name__ == "__main__":

    with open("实战-bicycle-yaml.yml") as f:
        datas = yaml.safe_load(f)

    print(datas)

    my = datas['default']
    my_battery = my['battery_level']
    my_km = my['km']

    mybycycle = EBycycle(my_battery)
    mybycycle.run(my_km)

    # mybycycle1 = EBycycle(10)
    # mybycycle1.run(19)

