import datetime


class Car:
    def __init__(self, car_make: str, manufacturer: str, fuel_consumption: float, release_year: int = 2002,
                 mileage: int = 0):
        self._release_year = release_year
        self.manufacturer = manufacturer
        self.car_make = car_make
        self.fuel_consumption = fuel_consumption
        self.__mileage = mileage

    def __str__(self):
        return f'Car Make: {self.car_make}, Manufacturer: {self.manufacturer}, Fuel Consumption:' \
               f' {self.fuel_consumption} l/100km, ' \
               f'Release Year: {self._release_year}, Car age: {self.age} years, Mileage: {self.__mileage}'

    @property
    def age(self):
        car_age = datetime.datetime.today().year - self._release_year
        return car_age


car1 = Car('Mercedes-Benz GLC 300 Base', 'Mercedes-Benz', 11.3, 2021)
car2 = Car('Toyota Crown Limited', 'Toyota', 5.7, 2023)
car3 = Car('Nissan Maxima 3.5 SV', 'Nissan', 9.3, 2020)

print(car1)
print(car2)
print(car3)
