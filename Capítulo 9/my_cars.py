from car import Car
from electric_car_2 import EletricCar
my_beetle = Car('volkswagen', 'beetle', 2016)
#my_beetle = car.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())
my_tesla = EletricCar('tesla', 'roadster', 2016)
#my_tesla = car.EletricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())