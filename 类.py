class car:
    '''一次汽车的简单模拟尝试'''
    def __init__(self, make, model, year):
        '''初始化汽车的属性'''
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def read_odometer(self):
        '''打印一条指出汽车里程的消息'''
        print(f"This car has {self.odometer_reading} on it")
    def update_odometer(self, mileage):
        '''将里程表读数改为特定的值
           禁止将里程表读数回调'''
        if mileage>=self.odometer_reading:
            self.odometer_reading=mileage
        else:
            print("you can't roll back an odometer!")
  
    def get_descriptive_name(self):
        '''返回整洁的描述性信息'''
        long_name=f"{self.year} {self.make} {self.model}"
        return long_name.title()
    def increment_odometer(self, miles):
        '''将里程表读数增加指定的量'''
        self.odometer_reading+=miles
        
my_new_car=car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading=2
my_new_car.read_odometer()
my_new_car.update_odometer(56)
my_new_car.read_odometer()
my_new_car.update_odometer(15)
my_new_car.increment_odometer(59)
my_new_car.read_odometer()

