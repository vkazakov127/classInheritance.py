class Car:
    price = 1000000

    def horse_powers(self):
        return 300


class Nissan(Car):
    price = 2000000

    def horse_powers(self):
        return 600


class Kia(Car):
    price = 1500000

    def horse_powers(self):
        return 200


car1 = Car()
print(f'class {car1.__class__.__name__}: price = {car1.price}; horse_powers = {car1.horse_powers()}')
car2 = Nissan()
print(f'class {car2.__class__.__name__}: price = {car2.price}; horse_powers = {car2.horse_powers()}')
car3 = Kia()
print(f'class {car3.__class__.__name__}: price = {car3.price}; horse_powers = {car3.horse_powers()}')
