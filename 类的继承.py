class car:
  def __init__(self, make, model, year):
    self.make=make
    self.model=model
    self.year=year
    self.odometer=0

  def read_odometer(self):
     print(f"this car's odometer is {self.odometer}")

  def get_descriptive_name(self):
     long_name=f"{self.year} {self.model} {self.make}"
     print(long_name.title())   
  
  def increment_odometer(self, miles):
     self.odometer+=miles

  def update_odometer(self, mileage):
     if self.odometer>=mileage:
        self.odometer=mileage
     else:
        print("you can't roll back an odometer!")    

class battery:
	def __init__(self, battery_size=75):
		self.battery_size=battery_size
	def describe_battery(self):
	    print(f"this car has a {self.battery_size}-kwh battery")
	def get_range(self):
		if self.battery_size==75:
			range=260
		elif self.battery_size==100:
			range=315
		print(f"this car can go about {range} miles on a full charge")


class electriccar(car):
	def __init__(self, make, model, year):
		super().__init__(make, model, year)
		self.battery=battery()

	#def describe_battery(self):
		#print(f"this car has a {self.battery_size}-kwh battery")



my_tesla=electriccar('tesla','model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()














