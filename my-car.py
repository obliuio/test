from super_car import car

my_new_car=car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.odometer=23
my_new_car.read_odometer()