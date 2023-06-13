from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, make: str, tank_volume: float, remaining_fuel: float, speed: float, mileage: float):
        self.make = make
        self.tank_volume = tank_volume
        self.remaining_fuel = remaining_fuel
        self.speed = speed
        self.mileage = mileage

    def refuel(self, additional_fuel_volume: float):
        tank_space_available = self.tank_volume - self.remaining_fuel
        if additional_fuel_volume <= tank_space_available:
            tank_refilled = self.remaining_fuel + additional_fuel_volume
            self.remaining_fuel = tank_refilled
            return self.remaining_fuel
        else:
            self.remaining_fuel = self.tank_volume
            return self.remaining_fuel

    def transfer_fuel(self, other, amount: float):
        if amount <= self.remaining_fuel:
            available_space = other.tank_volume - other.remaining_fuel
            if amount <= available_space:
                transferred_amount = amount
            else:
                transferred_amount = available_space
            self.remaining_fuel -= transferred_amount
            other.remaining_fuel += transferred_amount
        else:
            return 'Lack of fuel in the source vehicle.'

    @abstractmethod
    def __str__(self):
        pass


class Car(Vehicle):
    def __init__(self, passengers_number: int, airbag_available: bool, make: str, tank_volume: float,
                 remaining_fuel: float, speed: float, mileage: float):
        super().__init__(make, tank_volume, remaining_fuel, speed, mileage)
        self.passengers_number = passengers_number
        self.airbag_available = airbag_available

    def __str__(self):
        return f'That is a car. Its make is {self.make}. There are {self.passengers_number} passengers. Airbag is ' \
               f'availble:{self.airbag_available}. Its tank volume is {self.tank_volume}. Its remaining fuel volume ' \
               f'is {self.remaining_fuel}. Its speed is {self.speed}. Its mileage is {self.mileage} km'


class Motorcycle(Vehicle):
    def __init__(self, sidecar_available: bool, make: str, tank_volume: float, remaining_fuel: float, speed: float,
                 mileage: float):
        super().__init__(make, tank_volume, remaining_fuel, speed, mileage)
        self.sidecar_available = sidecar_available

    def __str__(self):
        return f'That is a motorcycle. Its make is {self.make} passengers. Its tank volume is {self.tank_volume}.Its ' \
               f'remaining fuel volume is {self.remaining_fuel}. Its speed is {self.speed}. Its mile' \
               f'age is {self.mileage} km'


car1 = Car(passengers_number=5, airbag_available=True, make='Toyota', tank_volume=5.2, remaining_fuel=3.8, speed=150,
           mileage=10000)

motorcycle1 = Motorcycle(sidecar_available=True, make='Harley', tank_volume=6, mileage=50000, remaining_fuel=3,
                         speed=300)

car1.refuel(1)
car1.refuel(8)
car1.transfer_fuel(motorcycle1, 2)
