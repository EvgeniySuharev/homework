class Vehicle:
    vehicle_type = None


class Car:
    price = 1000000

    def __init__(self, h_powers):
        self.h_powers = h_powers

    def horse_powers(self):
        print(self.h_powers)


class Nissan(Car, Vehicle):
    price = 900000
    vehicle_type = 'Minivan'

    def __init__(self, h_powers):
        super().__init__(h_powers)


nissan = Nissan(600)
print(nissan.vehicle_type)
print(nissan.price)
nissan.horse_powers()
